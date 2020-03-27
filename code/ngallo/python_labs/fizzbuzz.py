for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
    if i % 3 == 0:
        print("fizz")
    if i % 5 == 0:
        print("buzz")
    else:
        print(i)