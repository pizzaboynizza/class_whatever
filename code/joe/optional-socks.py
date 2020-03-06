# Lab : Sock Sorter
# Author : Joe

from random import choice

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']
sock_varis = []

for c in sock_colors:
    for t in sock_types:
        sock_varis.append((c, t))

all_socks = []

for i in range(100):
    all_socks.append((choice(sock_colors) , choice(sock_types)))

sorter = {v : 0 for v in sock_varis}
colors = {c : 0 for c in sock_colors}
types = {t : 0 for t in sock_types}

for n in all_socks:
    sorter[n] += 1
    colors[n[0]] += 1
    types[n[1]] += 1

print("Colors:")

for n in sock_colors:
    if colors[n] % 2 == 1:
        print(f"{n}\t has {colors[n] // 2} pairs with one left over.")
    else:
        print(f"{n}\t has {colors[n] // 2} pairs")

print("Types:")

for n in sock_types:
    if types[n] % 2 == 1:
        print(f"{n}\t has {types[n] // 2} pairs with one left over.")
    else:
        print(f"{n}\t has {types[n] // 2} pairs")

print("All Socks:")

for m in sock_colors:
    for n in sock_types:
        if sorter[(m, n)] % 2 == 1:
            print(f"{(m, n)}\thas {sorter[(m, n)] // 2} pairs with one left over.")
        else:
            print(f"{(m, n)}\thas {sorter[(m, n)] // 2} pairs ")