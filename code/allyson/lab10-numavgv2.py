nums=[]
import time
total=0
# for x in nums:
#     total += x
# len_nums=len(nums)
# ans=total/len_nums

print('Add a number or type "exit" to close.')

while True:
    n=input('Add a number?   ')
    nums.append(int(n))
    print(nums)
    n2=input('done (y/n)?')
    if n2 == 'y':
        print('Calculating....')
        for x in nums:
            total += x
            len_nums=len(nums)
            ans=total/len_nums
        time.sleep(2)
        print('Thinking....')
        time.sleep(2)
        print('Calling SkyNet....')
        time.sleep(2)
        print('Hanging up on Skynet...')
        time.sleep(1)
        print('Regretting calling Skynet...  TT__TT ')
        time.sleep(2)
        print(f'Results!  =', ans)
        break
    
# if n == 'exit':
#     print('Goodbye')
# else:
#    print('Invalid Input')

#  print(f'Averaging...', nums)