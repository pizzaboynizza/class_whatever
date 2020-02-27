#
def compute_ARI():

    with open('Gettysburg.txt', 'r', encoding = 'utf-8') as f:
        contents = f.read()

        characters = (len(contents))

        words = len(contents.split(" "))

        sentences = len(contents.split("."))

        result1 = (characters/words)

        result2 = (words/sentences)

        result3 = (4.71 * result1)
        result4 = (0.5 * result2)


        ARI = result3 + result4 - 21.43

        print(ARI)

compute_ARI()