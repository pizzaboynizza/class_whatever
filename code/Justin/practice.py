#def add(a, b):
#    return a + b

#print(add(1,2))

# #def is_even(a):
#     #if a%2 == 0:
#      #   print("true")
#
#     else:
#         print("false")
#
# is_even(5)

# def near_100(num):
#     if num - 10 == 100:
#         print ("True")
#
#     elif num + 10 == 100:
#         print("True")
#     else:
#         print("False")
#
# near_100(89)

#
def compute_ARI():

    with open('Gettysburg.txt', 'r', encoding = 'utf-8') as f:
        contents = f.read()

        characters = (len(contents))

        words = len(contents.split(" "))

        sentences = len(contents.split("."))

        result1 = (characters/words)

        result2 = (words/sentences)

        ARI = result1/result2

        print(ARI)



print(ans)



compute_ARI()





