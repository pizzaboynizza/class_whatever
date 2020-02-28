# Lab 22
# Author : Joe
import math

filename = input("Enter filename to analyze (enter nothing for the default file): ")
if filename == "":
    filename = "data/gettysburg-address.txt"
elif len(filename.split("/")) < 2:
    filename = "data/" + filename

with open(filename, encoding="utf-8") as f:
    whole = f.read()

# Sentences
whole = whole.split(".")
sentences = []
for n in whole:
    sentences.append(n.strip())
num_sen = len(sentences)

# Words
words = []
for n in sentences:
    for m in n.split(" "):
        words.append(m)
    
for m in words:
    good_word = False
    for c in m: #Check that a word is actually a word
        if c.isalnum():
            good_word = True
            break
    if not good_word:
        words.remove(m) #If word isn't actually a word, remove it

num_words = len(words)

# Characters
num_chars = 0
for n in words:
    for c in n:
        if c.isalnum():
            num_chars += 1

# Test
# print(num_chars)
# print(num_words)
# print(num_sen)

# Result
ari_scale = {
    1: {"ages":   "5-6", "grade_level": "Kindergarten"},
    2: {"ages":   "6-7", "grade_level":    "1st Grade"},
    3: {"ages":   "7-8", "grade_level":    "2nd Grade"},
    4: {"ages":   "8-9", "grade_level":    "3rd Grade"},
    5: {"ages":  "9-10", "grade_level":    "4th Grade"},
    6: {"ages": "10-11", "grade_level":    "5th Grade"},
    7: {"ages": "11-12", "grade_level":    "6th Grade"},
    8: {"ages": "12-13", "grade_level":    "7th Grade"},
    9: {"ages": "13-14", "grade_level":    "8th Grade"},
    10: {"ages": "14-15", "grade_level":    "9th Grade"},
    11: {"ages": "15-16", "grade_level":   "10th Grade"},
    12: {"ages": "16-17", "grade_level":   "11th Grade"},
    13: {"ages": "17-18", "grade_level":   "12th Grade"},
    14: {"ages": "18-22", "grade_level":      "College"} }
ari = math.ceil(4.71 * (num_chars / num_words) + 0.5 * (num_words / num_sen) - 21.43)
print(f"{'-'*40}\n")
print(f"The ARI for {filename.split('/')[-1]} is {ari}")
print(f"This corrisponds to a {ari_scale[ari]['grade_level']} of difficulty")
print(f"that is suitable for an average person {ari_scale[ari]['ages']} years old.")
print(f"\n{'-'*40}")

