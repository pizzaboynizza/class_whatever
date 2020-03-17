from recipe_scrapers import scrape_me
import string
import copy
import re

def get_just_ing(recipe_list):
    '''Takes a list of list of strings recipe_list and returns a new recipe
    list where the strings have been cleaned to remove words in 
    boring_word_listand unit_word_list and characters in replace_char'''
    stopwords = boring_word_list + unit_word_list
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
            just_ing = just_ing.strip()
            recipe_list[i][j] = just_ing
    return recipe_list

def get_ing_set(recipe_list):
    '''This takes a list of lists of strings recipe_list and returns a set
    ing_set with all the ingredients.'''
    stopwords = boring_word_list + unit_word_list
    joined_ing_list = ''
    for recipe in recipe_list:
        for ing in recipe:
            ing_list = ing.split()
            for word in ing_list:
                joined_ing_list += ' ' + word.lower()

    joined_ing_list = joined_ing_list.split()
    for k, word in enumerate(joined_ing_list):
        if stopwords.count(word) > 0:
            joined_ing_list[k] = ''
    joined_ing_list = ' '.join(joined_ing_list)
    joined_ing_list = joined_ing_list.strip()
    ing_list = joined_ing_list.split() 
    ing_set = set(ing_list)
    return ing_set

def dict_merge_subsets(org_dict):
    '''Takes a dictionary org_dict if any of the tuple keys are a subset of
    another their integer value is added to the superset and the subset is
    removed.'''
    keys = list(org_dict.keys())
    new_dict = org_dict.copy()
    for i, key in enumerate(keys):
        break_flag = False
        for j, other_key in enumerate(keys):
            if set(key) <= set(other_key) and i != j:
                num = new_dict[key]
                new_dict.pop(key)
                new_dict[other_key] += num
                break_flag = True
                break
        if break_flag:
            break
    return new_dict

def intersecting_tuples(org_list):
    '''Takes a list of tupules and returns True if two of them intersect.'''
    for i, tup in enumerate(org_list):
        for j, other_tup in enumerate(org_list):
            if set(tup) & set(other_tup) and i != j:
                return True
    return False

def remove_infrequent_intersections(org_dict):
    #akes a dictionaries with tuple:num as the pairs and removes pairs where the value num = 1 and the key tuple intersects with two of the other keys tuple that don't intersect
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
    '''Takes a dictionary org_dict and adds the integer values if the
    tuple keys intersect.'''
    keys = list(org_dict.keys())
    new_dict = org_dict.copy()
    while intersecting_tuples(keys):
        break_flag = False
        for i, key in enumerate(keys):
            for j, other_key in enumerate(keys):
                if set(key) & set(other_key) and i != j:
                    num = new_dict[key] + new_dict[other_key]
                    new_dict.pop(key)
                    new_dict.pop(other_key)
                    new_dict[tuple(set(key).union(set(other_key)))] = num
                    break_flag = True
                    break
            if break_flag:
                break
        keys = list(new_dict.keys())
    return new_dict

def get_duplicate_ing(recipe_list, ing_set):
    '''Takes a list of lists of strings called recipe_list and a set 
    ing_set if there are more than two ingredients a tuple is created: 
    (ing1, ing2, ...). These tuples are stored as keys in a dictionary with
    they values as the number of occurances in recipe_list.'''
    ing_dict = {}
    for recipe in recipe_list:
        for ing in recipe:
            ing_temp = ing
            for char in replace_chars:
                ing_temp = ing_temp.replace(char, ' ').lower()
            ing_temp = ' ' + ing_temp + ' '#this formats it so the string begins and ends in a space, which is important later when comparing to ing_set
            ing_in_current = []
            for ing_from_set in ing_set:
                if ing_temp.count(' ' + ing_from_set + ' ') > 0 and ing_in_current.count(ing_from_set) == 0:
                    ing_in_current.append(ing_from_set)
            if len(ing_in_current) > 0:
                ing_in_current_tuple = tuple(ing_in_current)
                ing_keys = list(ing_dict.keys())
                if ing_keys.count(ing_in_current_tuple) > 0:
                    ing_dict[ing_in_current_tuple] += 1
                else:
                    ing_dict[ing_in_current_tuple] = 1
    return ing_dict

def identify_ingredients(recipe_list, distinct_ing_list):
    '''Takes a list of lists of strings recipe_list and a list of tuples 
    distinct_ing_list and counts the occurances of any tuple element
    from distinct_ing_list for each element of recipe_list. Returns a list
    of lists ing_identifiers, which is the same size as recipe_list, where
    each element is the most frequently occuring tuple, ('garnish',) (if it
    contains anything in garnish_indicator_list) or ('unknown',) if it's 
    doesn't match anything in distinct_ing_list'''
    just_ing = get_just_ing(recipe_list)
    ing_identifiers = []
    for recipe in just_ing:
        cur_ing_identifier = []
        for ing in recipe:
            occurances_dict = {}
            for distinct_ing in distinct_ing_list:
                occurances_dict[distinct_ing] = 0
                for id_string in distinct_ing:
                    occurances_dict[distinct_ing] += ing.count(id_string)
            occurances = list(occurances_dict.items())
            occurances.sort(key=lambda tup: tup[1], reverse=True)
            ing_list = ing.split()
            garnish = False
            for ing in ing_list:
                if len(set(ing_list) & set(garnish_indicator_list)) > 0: 
                    garnish = True
            if garnish:
                cur_ing_identifier.append(('garnish',))
            elif occurances[0][1] == 0:
                cur_ing_identifier.append(('unknown',))
            else:
                cur_ing_identifier.append(occurances[0][0])
        ing_identifiers.append(cur_ing_identifier)
    return ing_identifiers

def remove_garnish_dict(org_dict):
    '''Takes a dictionary and returns a copy with items removed if their
    key tuples contain elements that are also in the list 
    garnish_indicator_list'''
    keys = org_dict.keys()
    new_dict = org_dict.copy()
    for key in keys:
        if len(set(key) & set(garnish_indicator_list)) > 0:
            new_dict.pop(key)
    return new_dict

def get_amounts(recipe_list_org):
    '''Takes a list of lists of strings recipe_list_org that contains the
    raw data (not just ingredients) and returns a list of lists of that is
    the same size as recipe_list_org where each element is the amount in 
    milliliters'''
    amount_exp_list = []
    for recipe in recipe_list_org:
        cur_recipe = []
        for ing in recipe:
            ing_copy = ing
            ing = ing.lower()
            ing_list = ing.split()
            if len(set(ing_list) & set(garnish_indicator_list)) > 0:
                ing = 'garnish'
            else:
                ing = ing.replace('1¾', ' 1.75 ')
                ing = ing.replace('1¼', ' 1.25 ')
                ing = ing.replace('1½', ' 1.5 ')
                ing = ing.replace('¾', ' 0.75 ')
                ing = ing.replace('1 1/2', ' 1.5 ')
                ing = ing.replace('1 1/4', ' 1.25 ')
                ing = ing.replace('1/2', ' 0.5 ')
                ing = ing.replace('1/4', ' 0.25 ')
                ing = ing.replace('/', ' ')
                fluid_ounce_phrase = ['fluid ounces', 'fluid ounce', 'fl oz.', 'fl oz', 'ounces', 'ounce', 'oz.', 'oz']
                ing = replace_phrase_once(ing, fluid_ounce_phrase, ' FLOZ ')
                teaspoon_phrase = ['teaspoons', 'teaspoon', 'tsp', 'tsp.']
                ing = replace_phrase_once(ing, teaspoon_phrase, 'TSP')
                tablespoon_phrase = ['tablespoons', 'tablespoon', 'tbsp', 'tbsp.']
                ing = replace_phrase_once(ing, tablespoon_phrase, 'TBSP')
            pattern = '([+\-])?((?:\d+\/|(?:\d+|^|\s)\.)?\d+)\s*([^\s\d+\-.,:;^\/]+(?:\^\d+(?:$|(?=[\s:;\/])))?(?:\/[^\s\d+\-.,:;^\/]+(?:\^\d+(?:$|(?=[\s:;\/])))?)*)?'
            result = re.findall(pattern, ing)
            supported_units = ['ml', 'TBSP', 'FLOZ', 'cup', 'TSP']
            amount_in_ml = 0
            for amount_tuple in result:
                if len(amount_tuple) > 0 and supported_units.count(amount_tuple[2]) > 0:
                    amount = float(amount_tuple[1])
                    units = amount_tuple[2]
                    amount_in_ml = convert_vol_to_ml(amount, units)
            cur_recipe.append(amount_in_ml)
        amount_exp_list.append(cur_recipe)
    return amount_exp_list

def convert_vol_to_ml(volume_units_org, units_org):
    '''Takes a float volume_units_org and a string units_org and returns a
    float volume_ml which represents a volume in milliliters equal to the
    input volume.'''
    volume_ml = float(volume_units_org)
    if units_org == 'TBSP':
        volume_ml *= 14.79
    elif units_org == 'FLOZ':
        volume_ml *= 29.57
    elif units_org == 'cup':
        volume_ml *= 236.6
    elif units_org == 'TSP':
        volume_ml *= 4.929
    return volume_ml

def replace_phrase_once(str_to_replace, phrase_list_old, new_phrase):
    '''Takes a string str_to_replace a list of strings phrase_list_old and
    a string new_phrase and returns a string str_to_replace_new in which 
    one occurance of a phrase from phrase_list_old has been replaced with 
    the string new_phrase. The string that is replaced is the first element 
    in phrase_list_old that str_to_replace contains. If str_to_replace 
    doesn't contain anything in phrase_list_old it returns 
    str_to_replace.'''
    phrase_flag = False
    for phrase in phrase_list_old:
        if str_to_replace.count(phrase) > 0:
            phrase_flag = True
            break
    i = 0
    str_to_replace_new = str_to_replace
    while str_to_replace == str_to_replace_new and phrase_flag:
        str_to_replace_new = str_to_replace.replace(phrase_list_old[i], new_phrase)
        i += 1
    return str_to_replace_new

def analyze_recipes(recipe_list_org, amounts, ing_duplicate_dict, ing_id):
    ml_tequila_in_recipe = []
    amount_normalize_tequila = []
    ratios = []
    for i, recipe in enumerate(recipe_list_org):
        amount_normalize_tequila_single_recipe = []
        #Getting amount of tequila in each recipe
        for j in range(len(recipe)):
            if ing_id[i][j].count('tequila') > 0:
                ml_tequila_in_recipe.append(amounts[i][j])
                break
        
        #Dividing each ingredient volume by volume of tequila
        for j in range(len(recipe)):
            amount_normalize_tequila_single_recipe.append(amounts[i][j]/ml_tequila_in_recipe[i])
        amount_normalize_tequila.append(amount_normalize_tequila_single_recipe)
        ratios_single_recipe = []
        for j in range(len(recipe)):
            for ing_tuple in list(ing_duplicate_dict.keys()):
                if ing_id[i][j] == ing_tuple:
                    ratios_single_recipe.append((ing_tuple, amount_normalize_tequila[i][j]), )
                    break
        ratios.append(ratios_single_recipe)
    for ing_tuple in list(ing_duplicate_dict.keys()):
        avg_recipe = 0
        num_ing = 0
        for recipe in ratios:
            for ing_from_recipe in recipe:
                ing, amount = ing_from_recipe
                if ing_tuple == ing:
                    avg_recipe += amount
                    num_ing += 1
        print(ing_tuple, 'Average: %1.2f'%(avg_recipe/num_ing), 'Number: ' + str(num_ing))

def main_function(recipe_list_org):
    recipe_list = copy.deepcopy(recipe_list_org)
    recipe_list_just_ing = get_just_ing(recipe_list)
    # print(recipe_list_just_ing)#[['salt', 'tequila', 'orange  liqueur   cointreau', 'lime juice', 'ice', 'lime wheel'], ['reposado tequila', 'cointreau', 'lime juice', 'ice', 'lime wedge  garnish'], ['ice', 'tequila reposado', 'lime juice', 'triple sec   cointreau', 'salt', 'lime wedges'], ['ice', 'tequila', 'lime juice', 'cointreau', 'lime'], ['salt', 'lime wheel', 'tequila blanco', 'lime juice', 'syrup'], ['tequila', 'triple sec', 'lime juice', 'powdered sugar', 'frozen  strawberries', 'ice'], ['lime wedge  lime wheels  garnish', 'salt', 'blanco tequila', 'cointreau', 'juice  limes'], ['ice', 'tequila', 'lime juice', 'syrup', 'orange liqueur', 'lime salt sugar', 'sugar', 'water', 'zest   lime', 'salt', 'sugar']]
    ing_set = get_ing_set(recipe_list_just_ing)
    # print(ing_set)#{'frozen', 'syrup', 'tequila', 'wedge', 'wheel', 'salt', 'juice', 'sec', 'wheels', 'reposado', 'limes', 'water', 'zest', 'blanco', 'lime', 'liqueur', 'ice', 'garnish', 'triple', 'orange', 'cointreau', 'wedges', 'sugar', 'powdered', 'strawberries'}
    ing_duplicate_dict = get_duplicate_ing(recipe_list_just_ing, ing_set)
    # print(ing_duplicate_dict)#{('salt',): 5, ('tequila',): 4, ('liqueur', 'orange', 'cointreau'): 1, ('lime', 'juice'): 7, ('ice',): 6, ('lime', 'wheel'): 2, ('reposado', 'tequila'): 2, ('cointreau',): 3, ('lime', 'wedge', 'garnish'): 1, ('sec', 'triple', 'cointreau'): 1, ('lime', 'wedges'): 1, ('lime',): 1, ('blanco', 'tequila'): 2, ('syrup',): 2, ('sec', 'triple'): 1, ('powdered', 'sugar'): 1, ('strawberries', 'frozen'): 1, ('lime', 'wedge', 'wheels', 'garnish'): 1, ('limes', 'juice'): 1, ('liqueur', 'orange'): 1, ('lime', 'sugar', 'salt'): 1, ('sugar',): 2, ('water',): 1, ('lime', 'zest'): 1}
    ing_duplicate_dict = remove_garnish_dict(ing_duplicate_dict)
    # print(ing_duplicate_dict)#{('tequila',): 4, ('cointreau', 'orange', 'liqueur'): 1, ('lime', 'juice'): 7, ('ice',): 6, ('reposado', 'tequila'): 2, ('cointreau',): 3, ('cointreau', 'sec', 'triple'): 1, ('lime',): 1, ('tequila', 'blanco'): 2, ('syrup',): 2, ('sec', 'triple'): 1, ('sugar', 'powdered'): 1, ('strawberries', 'frozen'): 1, ('limes', 'juice'): 1, ('orange', 'liqueur'): 1, ('sugar',): 2, ('water',): 1}
    ing_duplicate_dict = dict_merge_intersecting(ing_duplicate_dict)
    # print(ing_duplicate_dict)#{('ice',): 6, ('syrup',): 2, ('frozen', 'strawberries'): 1, ('water',): 1, ('blanco', 'reposado', 'tequila'): 8, ('sugar', 'powdered'): 3, ('juice', 'lime', 'limes'): 9, ('cointreau', 'liqueur', 'orange', 'triple', 'sec'): 7}
    ing_id = identify_ingredients(recipe_list_just_ing, ing_duplicate_dict.keys())
    # print(ing_id)#[[('garnish',), ('tequila', 'reposado', 'blanco'), ('cointreau', 'triple', 'liqueur', 'sec', 'orange'), ('limes', 'lime', 'juice'), ('ice',), ('garnish',)], [('tequila', 'reposado', 'blanco'), ('cointreau', 'triple', 'liqueur', 'sec', 'orange'), ('limes', 'lime', 'juice'), ('ice',), ('garnish',)], [('ice',), ('tequila', 'reposado', 'blanco'), ('limes', 'lime', 'juice'), ('cointreau', 'triple', 'liqueur', 'sec', 'orange'), ('garnish',), ('garnish',)], [('ice',), ('tequila', 'reposado', 'blanco'), ('limes', 'lime', 'juice'), ('cointreau', 'triple', 'liqueur', 'sec', 'orange'), ('limes', 'lime', 'juice')], [('garnish',), ('garnish',), ('tequila', 'reposado', 'blanco'), ('limes', 'lime', 'juice'), ('syrup',)], [('tequila', 'reposado', 'blanco'), ('cointreau', 'triple', 'liqueur', 'sec', 'orange'), ('limes', 'lime', 'juice'), ('powdered', 'sugar'), ('frozen', 'strawberries'), ('ice',)], [('garnish',), ('garnish',), ('tequila', 'reposado', 'blanco'), ('cointreau', 'triple', 'liqueur', 'sec', 'orange'), ('limes', 'lime', 'juice')], [('ice',), ('tequila', 'reposado', 'blanco'), ('limes', 'lime', 'juice'), ('syrup',), ('cointreau', 'triple', 'liqueur', 'sec', 'orange'), ('garnish',), ('powdered', 'sugar'), ('water',), ('garnish',), ('garnish',), ('powdered', 'sugar')]]
    amounts = get_amounts(recipe_list_org)
    # print(amounts)#[[0, 44.355000000000004, 29.57, 14.785, 236.6, 0], [36.9625, 22.177500000000002, 36.9625, 0, 0], [0, 50.0, 25.0, 20.0, 0, 0], [0, 44.355000000000004, 9.858, 4.929, 0], [0, 0, 59.14, 22.177500000000002, 22.177500000000002], [59.14, 29.57, 59.14, 59.15, 29.58, 236.6], [0, 14.79, 118.28, 59.14, 44.355000000000004], [0, 88.71000000000001, 59.14, 29.57, 4.929, 14.79, 236.6, 236.6, 0, 0, 29.58]]
    analyze_recipes(recipe_list_org, amounts, ing_duplicate_dict, ing_id)

filename = 'recipe_urls.txt'
with open('/home/michael/Desktop/recipe_scrapers/'+filename, 'r') as f:
    contents = f.read().lower()
recipe_urls = contents.split('\n')
recipe_list = []
for recipe_url in recipe_urls:
    scraper = scrape_me(recipe_url)
    recipe_list.append(scraper.ingredients())
recipe_list_org = recipe_list
# print(recipe_list_org)# [['1 tablespoon kosher salt', '1 1/2 fluid ounces tequila', '1 fluid ounce orange flavored liqueur (such as Cointreau®)', '1/2 fluid ounce lime juice', '1 cup ice', '1 lime wheel'], ['35ml/1¼fl oz Reposado Tequila', '20ml/¾fl oz Cointreau', '35ml/1¼fl oz fresh lime juice', 'handful ice cubes', 'lime wedge, to garnish'], ['ice', '50ml tequila reposado', '25ml lime juice', '20ml triple sec (we used Cointreau)', 'salt', '2 lime wedges'], ['Ice cubes', '3 tablespoons tequila (1 1/2 oz)', '2 teaspoons lime juice', '1 teaspoon Cointreau', '1 lime slice'], ['Kosher salt (for serving)', '½ thick lime wheel (for serving)', '2 oz. tequila blanco', '¾ oz. fresh lime juice', '¾ oz. simple syrup'], ['2 ounces tequila', '1 ounce triple sec', '2 ounces fresh lime juice', '1/4 cup powdered sugar', '2 tablespoons frozen sweetened strawberries', '1 cup ice'], ['1 lime wedge, plus 2 lime wheels for garnish', '1 tablespoon coarse salt, for glass rims', '4 ounces (120ml) high-quality blanco tequila (see note)', '2 ounces (60ml) Cointreau', '1 1/2 ounces (45ml) fresh juice from 2 limes'], ['Ice cubes', '3 ounces tequila', '2 ounces freshly squeezed lime juice', '1 ounce Simple Syrup, recipe follows', '1/2 to 1 teaspoon orange liqueur', '1 tablespoon Lime-salt-sugar, recipe follows', '1 cup sugar', '1 cup water', 'Zest of one lime', '2 tablespoons kosher salt', '2 tablespoons sugar']]
replace_chars = string.digits + string.punctuation + '®' + '¼' + '¾' + '½'
unit_word_list = ['ounces', 'ounce', 'oz', 'ml', 'fl', 'fluid', 'tbl', 'tbs', 'tbsp', 'tablespoon', 'tablespoons', 'cup', 'cups', 'handful', 'tsps', 'tsp', 'teaspoon', 'teaspoons', 'slice', 'thick']
garnish_indicator_list = ['zest', 'wedge', 'wedges', 'garnish', 'wheel', 'wheels', 'salt']
boring_word_list = ['coarse', 'kosher', 'sweetened', 'simple', 'cubes','sweetened', 'flavored', 'squeezed', 'old', 'fashioned', 'rim', 'rims', 'glass', 'chilled', 'cocktail', 'fresh', 'freshly', 'high', 'quality', 'strain','strains','straining','strained','strainer','note', 'recipe', 'one', 'see', 'seeing', 'saw', 'seen', 'plus', 'use', 'using', 'used', 'serve', 'serves', 'serving', 'served', 'shaker', 'plus', 'follow', 'follows', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

main_function(recipe_list_org)