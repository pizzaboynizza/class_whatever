name = "Michael"
job = "instructor"
#concatanation 
print("Hello " + name + "!\nYou are a " + job + "!")
# C-Style
print("Hello %s!\nYou are a %s!" %(name, job))
# python version
print("Hello {}!\nYou are a {}!".format(name, job))
#fstring
print(f"Hello {name}!\nYou are a {job}!")  