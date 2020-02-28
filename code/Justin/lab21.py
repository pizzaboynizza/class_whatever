
def count_words():

    with open('gutenbergproject.txt', 'r', encoding='utf-8') as f:
        contents = f.read()
        contents_lower = contents.lower()

        import string


        translator = str.maketrans('', '', string.punctuation)
        string_without_punct = contents_lower.translate(translator)

        sentence = string_without_punct
        words = sentence.split()

        output = {}

        for word in words:
                 if word not in output.keys():
                     output[word] = 0
                 output[word] += 1

        words2 = list(output.items())
        words2.sort(key=lambda tup: tup[1], reverse=True)
        for i in range(min(10, len(words2))):
            print(words2[i])

count_words()