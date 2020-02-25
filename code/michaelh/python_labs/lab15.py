'''
# Lab 15: Number to Phrase

Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the one_reps and tens digit.

```python
x = 67
tens_digit = x//10
one_reps_digit = x%10
```
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

## Version 2

Handle numbers from 100-999.

## Version 3 (optional)

Convert a number to roman numerals.

## Version 4 (optional)

Convert a time given in hours and minutes to a phrase.
'''
while True:
    org_num = input('Enter a number with up to two digits: ')
    if org_num == 'done_rep':
        break
    
    org_num = int(org_num)
    one_rep = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tenth_rep = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    irregular = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    hundredth_rep = [digit + '-hundred' if digit != '' else '' for digit in one_rep]
    # print(hundredth_rep)
    one_place = org_num % 10
    tenth_place = (org_num % 100) // 10
    hundredth_place = org_num // 100
    print(hundredth_place, tenth_place, one_place)
    print(hundredth_rep[hundredth_place], tenth_rep[tenth_place], one_rep[one_place])
    eng_rep = ''
    
    if tenth_place == 1:
        eng_rep += irregular[one_place]
    elif one_place == 0:
        eng_rep += tenth_rep[tenth_place] 
    elif tenth_place == 0:
        eng_rep += one_rep[one_place]
    else: 
        eng_rep += tenth_rep[tenth_place] + '-' + one_rep[one_place]
    
    if org_num > 99:
        if tenth_place == 0 and one_place == 0:
            hundredth_rep[hundredth_place]
        else:
            eng_rep = hundredth_rep[hundredth_place] + ' and ' + eng_rep
        
    print(eng_rep)