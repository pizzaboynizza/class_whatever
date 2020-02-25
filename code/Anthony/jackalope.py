mylist = [1,1]
n = len(mylist)
while len(mylist) < 1000:
    for age in mylist:
        if 4 <= age <= 8:
    
            mylist.insert(age, age+1)
            # mylist.append(0)
            print(mylist)
        else:
            mylist.insert(age, age+1)
            print(mylist)
            # if age == 10:
                # mylist.remove(age)
print(mylist)





