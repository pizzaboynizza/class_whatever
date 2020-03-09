'''
Nick Barker
Lab22
2/27/2020
'''
import math
import string
import os
#compute the ARI Score
# we do this by taking the total number of characters (total_char)
#and the total number of words (total_words)
#and then multiply the dividend of characters/words by 4.71
#simultaneously, we are taking the total number of words (total_words) and divising that by the total number of sentences (total_sentences), and multiplying this by .5
#THEN (char/words) * 4.71 + (words/sentences) *.5 - 21.43 = ARI!
#if it's a decimal (float) we ALWAYS ROUND UP!


#data = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth."

with open('gettyaddy.txt', 'r', encoding='utf-8') as file:
    contents = file.read()
    #print(contents)
data = contents

file_name = input("Please enter filename: ") 

def character_counter(data):
        #this will return the white spaces, periods, question marks, exclaimation marks
        apples = (len(data))
        print(f'{apples} is the total number of characters in the string')
        zebra = int(data.count(' '))
        print("This is the white space count:", zebra)
        rhino = int(data.count('.'))
        print("this is the amount of periods:", rhino)
        lion = int(data.count('!'))
        print('this is the amount of exclaimation points:', lion)
        tiger = int(data.count('?'))
        print('this is the amount of question marks:', tiger)
        feast = (rhino + lion + tiger)
        print("based on this amount of punctuation, there are most likely about:", (feast), "sentences")
        hyeena = (zebra + rhino + lion + tiger)
        print("The total number of non-critical characters to subtract from the character count is:", hyeena)
        giraffe = (apples - hyeena)
        wordslist=data.split()
        applejax = (len(wordslist))
        #print(wordslist)
        #print(giraffe)
        #print(hyeena)
        return giraffe, applejax, feast, apples, lion, tiger, hyeena, rhino, zebra

giraffe, applejax, feast, apples, lion, tiger, hyeena, rhino, zebra =character_counter(data)
print(giraffe)
print(applejax)
print(feast)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

ari = 4.71*(giraffe/applejax) + .5*(applejax/feast) - 21.43
print("The ARI of this file is:", ari)
ari = math.ceil(ari)
if ari > 14:
    ari = 14

grade_level = ari_scale[ari]['grade_level']
years_old = ari_scale[ari]['ages']

output = '**'*40 + '\n' #I really like the stars!
print(f"The ARI for {file_name} is {ari}")
print(f'Based on this score, this corresponds to a {grade_level} level of difficulty')
print(f"Based on this grade level, it is suitable for an average person {years_old} years old.")
output = '**'*40 + '\n' #I really like the stars!

#Juuuuuuuuuuuuuuuust checking!
# arii = (giraffe/applejax)
# ariii = (applejax/feast)
# ariv = 4.71*arii
# arv = .5*ariii
# the_final_ARI = ariv + arv - 21.43 
# print(the_final_ARI)


