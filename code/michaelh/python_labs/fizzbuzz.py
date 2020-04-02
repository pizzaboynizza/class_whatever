# for i in range(100):
#     if 3 % 0 = 
old_list=range(1, 101)
# print(old_list[99])
new_list=[]
new_list = [str(old_list[i]) for i in range(0, 100) if old_list[i]%3!=0 and old_list[i]%5!=0]
new_list = ['FizzBuzz' for i in range(0, 100) if old_list[i]%3==0 and old_list[i]%5==0]
new_list = ['Fizz' for i in range(0, 100) if old_list[i]%3==0 and old_list[i]%5!=0]
new_list = ['Buzz' for i in range(0, 100) if old_list[i]%5==0 and old_list[i]%3!=0]
print(new_list)
