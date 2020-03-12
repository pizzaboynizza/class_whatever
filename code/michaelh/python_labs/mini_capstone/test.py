from recipe_scrapers import scrape_me
import string

def ingredient_in_recipe(recipe_str, ing_list):
    for ing in ing_list:
        if recipe_str.count(ing) > 0:
            return True
    return False

def get_just_ing(recipe_list):
    stopwords = boring_word_list + unit_word_list
    recipe_list_temp = recipe_list.copy()
    for i, recipe in enumerate(recipe_list):
        for j, ing in enumerate(recipe):
            just_ing = ing.lower()
            for char in replace_chars:
                just_ing = just_ing.replace(char, ' ')
            just_ing = just_ing.split()
            for k, word in enumerate(just_ing):
                if stopwords.count(word) > 0:
                    just_ing[k] = ''
            just_ing = ' '.join(just_ing)
            # for word in unit_word_list:
            #     just_ing = just_ing.replace(' ' + word + ' ', ' ')
            # for word in boring_word_list:
            #     just_ing = just_ing.replace(' ' + word + ' ', ' ')
            just_ing = just_ing.strip()
            recipe_list_temp[i][j] = just_ing
    return recipe_list_temp

def get_ing_list(recipe_list):
    joined_ing_list = ''
    for recipe in recipe_list:
        for ing in recipe:
            ing_cur = []
            ing_list = ing.split()
            for word in ing_list:
                joined_ing_list += ' ' + word.lower()

    for char in replace_chars:
        joined_ing_list = joined_ing_list.replace(char, ' ')
    for word in unit_word_list:
        joined_ing_list = joined_ing_list.replace(' ' + word + ' ', ' ')
    for word in boring_word_list:
        joined_ing_list = joined_ing_list.replace(' ' + word + ' ', ' ')
    # print(joined_ing_list)
    ing_list = joined_ing_list.split() 
    ing_list = set(ing_list)
    return ing_list

def dict_merge_subsets(org_dict):
    keys = list(org_dict.keys())
    new_dict = org_dict.copy()
    for i, key in enumerate(keys):
        for j, other_key in enumerate(keys):
            if set(key) <= set(other_key) and i != j:
                num = new_dict[key]
                new_dict.pop(key)
                new_dict[other_key] += num
                break
    return new_dict

#takes a list of tupules and returns True if two of them intersect
def intersecting_tuples(org_list):
    for i, tup in enumerate(org_list):
        for j, other_tup in enumerate(org_list):
            if set(tup) & set(other_tup) and i != j:
                return True
    return False

#takes a dictionaries with tuple:num as the pairs and removes pairs where the value num = 1 and the key tuple intersects with two of the other keys tuple that don't intersect
def remove_infrequent_intersections(org_dict):
    #gets the keys that intersect with each key and puts them as the values for intersection_dict, a list of tuples
    keys = list(org_dict.keys())
    intersection_dict = {}
    org_dict_temp = org_dict.copy()
    for key_tup in keys:
        intersection_dict[key_tup] = []
        for other_key_tup in keys:
            if key_tup != other_key_tup and len(set(key_tup) & set(other_key_tup)) > 0:
                intersection_dict[key_tup].append(other_key_tup)

    #loops through the intersecting_dict and figures out if there's some wierd sort of intersection (where two of the tuples it intersects with do not intersect with one another)
    weird_intersection_dict = {}
    for key_tup in keys:
        intersection_list = intersection_dict[key_tup]
        weird_intersection_dict[key_tup] = False
        for i, tup_val in enumerate(intersection_list):
            for j, other_tup_val in enumerate(intersection_list):
                if i != j:
                    if len(set(tup_val) & set(other_tup_val)) == 0:
                        weird_intersection_dict[key_tup] = True

    #this removes the item if it is a wierd intersection and infrequent (only occurs once)
    for key_tup in keys:
        if weird_intersection_dict[key_tup] and org_dict[key_tup] == 1:
            org_dict_temp.pop(key_tup)
    # print(set(org_dict) - set(org_dict_temp))
    return org_dict_temp


def dict_merge_intersecting(org_dict):
    keys = list(org_dict.keys())
    new_dict = org_dict.copy()
    # print(new_dict)
    while intersecting_tuples(keys):
        break_flag = False
        for i, key in enumerate(keys):
            for j, other_key in enumerate(keys):
                if set(key) & set(other_key) and i != j:
                    # print(new_dict.keys())
                    num = new_dict[key] + new_dict[other_key]
                    new_dict.pop(key)
                    new_dict.pop(other_key)
                    new_dict[tuple(set(key).union(set(other_key)))] = num
                    # print(new_dict)
                    break_flag = True
                    break
            if break_flag:
                break
        keys = list(new_dict.keys())
    return new_dict

def get_duplicate_ing(recipe_list, ing_list):
    ing_dict = {}
    for recipe in recipe_list:
        for ing in recipe:
            ing_temp = ing
            for char in replace_chars:
                ing_temp = ing_temp.replace(char, ' ').lower()
            # print(ing_temp)
            ing_temp = ' ' + ing_temp + ' '
            ing_in_current = []
            for ing_from_list in ing_list:
                if ing_temp.count(' ' + ing_from_list + ' ') > 0 and ing_in_current.count(ing_from_list) == 0:
                    ing_in_current.append(ing_from_list)
            if len(ing_in_current) > 1:
                ing_in_current_tuple = tuple(ing_in_current)
                ing_keys = list(ing_dict.keys())
                if ing_keys.count(ing_in_current_tuple) > 0:
                    ing_dict[ing_in_current_tuple] += 1
                else:
                    ing_dict[ing_in_current_tuple] = 1
    return ing_dict

def get_amounts(recipe_list, distinct_ing_list):
    just_ing = get_just_ing(recipe_list)
    for i, recipe in enumerate(just_ing):
        for j, ing in enumerate(recipe):
            occurances_dict = {}
            for distinct_ing in distinct_ing_list:
                occurances_dict[distinct_ing] = 0
                for id_string in distinct_ing:
                    occurances_dict[distinct_ing] += ing.count(id_string)
            print(recipe_list[i][j], occurances_dict)
# filename = 'recipe_urls.txt'
# with open('/home/michael/Desktop/recipe_scrapers/'+filename, 'r') as f:
#     contents = f.read().lower()
# recipe_urls = contents.split('\n')
# recipe_list = []
# for recipe_url in recipe_urls:
#     scraper = scrape_me(recipe_url)
#     recipe_list.append(scraper.ingredients())
# print(recipe_list)

recipe_list = [['1 tablespoon kosher salt', '1 1/2 fluid ounces tequila', '1 fluid ounce orange flavored liqueur (such as Cointreau®)', '1/2 fluid ounce lime juice', '1 cup ice', '1 lime wheel'], ['35ml/1¼fl oz Reposado Tequila', '20ml/¾fl oz Cointreau', '35ml/1¼fl oz fresh lime juice', 'handful ice cubes', 'lime wedge, to garnish'], ['ice', '50ml tequila reposado', '25ml lime juice', '20ml triple sec (we used Cointreau)', 'salt', '2 lime wedges'], ['Ice cubes', '3 tablespoons tequila (1 1/2 oz)', '2 teaspoons lime juice', '1 teaspoon Cointreau', '1 lime slice'], ['Kosher salt (for serving)', '½ thick lime wheel (for serving)', '2 oz. tequila blanco', '¾ oz. fresh lime juice', '¾ oz. simple syrup'], ['2 ounces tequila', '1 ounce triple sec', '2 ounces fresh lime juice', '1/4 cup powdered sugar', '2 tablespoons frozen sweetened strawberries', '1 cup ice'], ['1 lime wedge, plus 2 lime wheels for garnish', '1 tablespoon coarse salt, for glass rims', '4 ounces (120ml) high-quality blanco tequila (see note)', '2 ounces (60ml) Cointreau', '1 1/2 ounces (45ml) fresh juice from 2 limes'], ['Ice cubes', '3 ounces tequila', '2 ounces freshly squeezed lime juice', '1 ounce Simple Syrup, recipe follows', '1/2 to 1 teaspoon orange liqueur', '1 tablespoon Lime-salt-sugar, recipe follows', '1 cup sugar', '1 cup water', 'Zest of one lime', '2 tablespoons kosher salt', '2 tablespoons sugar']]
replace_chars = string.digits + string.punctuation + '®' + '¼' + '¾' + '½'
unit_word_list = ['ounces', 'ounce', 'oz', 'ml', 'fl', 'fluid', 'tbl', 'tbs', 'tbsp', 'tablespoon', 'tablespoons', 'cup', 'cups', 'handful', 'tsps', 'tsp', 'teaspoon', 'teaspoons', 'slice', 'thick']
# boring_word_list = ['follows', 'old', 'fashioned', 'rim', 'rims', 'glass', 'chilled', 'cocktail', 'strain','strains','straining','strained','strainer','note', 'recipe', 'one', 'see', 'seeing', 'saw', 'seen', 'plus', 'use', 'using', 'used', 'serve', 'serves', 'serving', 'served', 'shaker', 'plus', 'follow', 'follows', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
boring_word_list = ['flavored', 'squeezed', 'zest', 'wedge', 'wedges', 'garnish', 'wheel','wheels', 'old', 'fashioned', 'rim', 'rims', 'glass', 'chilled', 'cocktail', 'fresh', 'freshly', 'high', 'quality', 'strain','strains','straining','strained','strainer','note', 'recipe', 'one', 'see', 'seeing', 'saw', 'seen', 'plus', 'use', 'using', 'used', 'serve', 'serves', 'serving', 'served', 'shaker', 'plus', 'follow', 'follows', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

recipe_list_just_ing = get_just_ing(recipe_list)
# print(recipe_list_just_ing)
ing_list = get_ing_list(recipe_list)
ing_duplicate_dict = get_duplicate_ing(recipe_list, ing_list)
# print(ing_duplicate_dict)
# print(list(ing_dict.keysduplicate_()))

print(ing_duplicate_dict)
ing_duplicate_dict = dict_merge_subsets(ing_duplicate_dict)
print(ing_duplicate_dict)
ing_duplicate_dict = remove_infrequent_intersections(ing_duplicate_dict)
print(ing_duplicate_dict)
ing_duplicate_dict = dict_merge_intersecting(ing_duplicate_dict)
print(ing_duplicate_dict)

get_amounts(recipe_list, ing_duplicate_dict.keys())

# keys = list(ing_duplicate_dict.keys())
# if len(ing_in_current) == 1:
#     for key in keys:
#         if key.count(ing_in_current[0]) > 0:
#             ing_duplicate_dict[key] duplicate += 1
#             break
# print(ing_duplicate_dict)

