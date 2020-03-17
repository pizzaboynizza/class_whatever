import string

with open('getty.txt', 'r', encoding='utf-8') as file:
    contents_of_getty = file.read()

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
    ari_value = ari_scale[13]
    ari_printed_value = (ari_scale[13]['ages'])
    ari_printed_value_level = (ari_scale[13]['grade_level'])

    def count_sentences(contents_of_getty):
        number_of_sentences = int(contents_of_getty.count("."))
        return number_of_sentences
    var_count_sentences = count_sentences(contents_of_getty)
    
    def func_number_of_words(contents_of_getty):
        translator = str.maketrans('', '', string.punctuation)
        string_without_puncution = contents_of_getty.translate(translator)
        almost_number_of_words = string_without_puncution.split()
        number_of_words = len(almost_number_of_words)
        return number_of_words

    def count_words(contents_of_getty, var_count_sentences):
        translator = str.maketrans('', '', string.punctuation)
        string_without_puncution = contents_of_getty.translate(translator)
        almost_number_of_words = string_without_puncution.split()
        giant_string = string_without_puncution.replace(' ', '')
        giant_string_length = len(giant_string)
        number_of_words = len(almost_number_of_words)
        num_char_minus_num_words = (giant_string_length / number_of_words) * 4.71
        words_divided_by_sentences = .50 * (number_of_words / var_count_sentences) - 21.43
        ari = int(num_char_minus_num_words) + int(words_divided_by_sentences)
        return ari

    print(count_words(contents_of_getty, var_count_sentences))

print(f"There are {count_sentences(contents_of_getty)} sentences.")

print(f"In this text file there are {func_number_of_words(contents_of_getty)} words.")
print(f"The ARI for this file is {count_words(contents_of_getty, var_count_sentences)}.")
print(f"This corresponds to a person that is aged {ari_printed_value} that likely is in {ari_printed_value_level}.")




'''
# Lab 22: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. **If the result is a decimal, always round up.** Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:

```
    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
```

Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

```python
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
```

The output should look something like the following:

    --------------------------------------------------------

    The ARI for gettysburg-address.txt is 12
    This corresponds to a 11th Grade level of difficulty
    that is suitable for an average person 16-17 years old.

    --------------------------------------------------------
    '''