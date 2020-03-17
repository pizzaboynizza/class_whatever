

class Musical_Artist:
    def __init__(self, name, digitaldreamdoor, rolling_stone, ultimateclassic, whenwasitcool, vh1): 
        self.name = name
        self.digitaldreamdoor = digitaldreamdoor
        self.rolling_stone = rolling_stone
        self.ultimateclassic = ultimateclassic
        self.whenwasitcool = whenwasitcool
        self.vh1 = vh1

b1 = Musical_Artist("The Beatles", 1, 1, 1, 1, 1)
The_Beatles = [1, 1, 1, 1, 1]
The_Beatles1 = sum(The_Beatles)
The_Beatles2 = The_Beatles1/5
print(The_Beatles2)

b2 = Musical_Artist("Elvis Presley", 2, 3, 100, 2, 8)
Elvis_Presley = [2, 3, 100, 2, 8]
Elvis_Presley1 = sum(Elvis_Presley)
Elvis_Presley2 = Elvis_Presley1/5

b3 = Musical_Artist("James Brown", 3, 7, 100, 100, 6)
James_Brown = [3, 7, 100, 100, 6]
James_Brown1 = sum(James_Brown)
James_Brown2 = James_Brown1/5

b4 = Musical_Artist("Bob Dylan", 4, 2, 5, 18, 5)
Bob_Dylan = [4, 2, 5, 18, 5]
Bob_Dylan1 = sum(Bob_Dylan)
Bob_Dylan2 = Bob_Dylan1/5

b5 = Musical_Artist("The Rolling Stones", 5, 4, 2, 3, 2)
The_Rolling_Stones = [5, 4, 2, 3, 2]
The_Rolling_Stones1 = sum(The_Rolling_Stones)
The_Rolling_Stones2 = The_Rolling_Stones1/5

b6 = Musical_Artist("Stevie Wonder", 6, 15, 100, 27, 11)
Stevie_Wonder = [6, 15, 100, 27, 11]
Stevie_Wonder1 = sum(Stevie_Wonder)
Stevie_Wonder2 = Stevie_Wonder1/5

b7 = Musical_Artist("Chuck Berry", 7, 5, 100, 100, 26)
Chuck_Berry = [7, 5, 100, 100, 26]
Chuck_Berry1 = sum(Chuck_Berry)
Chuck_Berry2 = Chuck_Berry1/5

b8 = Musical_Artist("The Who", 8, 29, 12, 39, 9)
The_Who = [8, 29, 12, 39, 9]
The_Who1 = sum(The_Who)
The_Who2 = The_Who1/5

b9 = Musical_Artist("Led Zeppelin", 9, 14, 3, 5, 4)
Led_Zeppelin = [9, 14, 3, 5, 4]
Led_Zeppelin1 = sum(Led_Zeppelin)
Led_Zeppelin2 = Led_Zeppelin1/5

b10 = Musical_Artist("Ray Charles", 10, 10, 100, 100, 12)
Ray_Charles = [10, 10, 100, 100, 12]
Ray_Charles1 = sum(Ray_Charles)
Ray_Charles2 = Ray_Charles1/5

Artist_Rank = {'The Beatles': 1, 'Elvis Presley': 23, 'James Brown': 43.2, 'Bob Dylan': 6.8, 'The Rolling Stones': 3.2, 'Stevie Wonder': 31.8, 'Chuck Berry': 47.6, 'The Who': 19.4, 'Led Zeppelin': 7, 'Ray Charles': 46.4}

Artist_Rank_Two = list(Artist_Rank.items())
Artist_Rank_Two.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(Artist_Rank_Two))):
        print(Artist_Rank_Two[i])

import matplotlib.pyplot as plt

plt.plot(The_Beatles)
plt.ylabel('The Beatles')
plt.show()

plt.plot(Elvis_Presley)
plt.ylabel('Elvis Presley')
plt.show()

plt.plot(James_Brown)
plt.ylabel('James Brown')
plt.show()

plt.plot(Bob_Dylan)
plt.ylabel('Bob Dylan')
plt.show()

plt.plot(The_Rolling_Stones)
plt.ylabel('The Rolling Stones')
plt.show()

plt.plot(Stevie_Wonder)
plt.ylabel('Stevie Wonder')
plt.show()

plt.plot(Chuck_Berry)
plt.ylabel('Chuck Berry')
plt.show()

plt.plot(The_Who1)
plt.ylabel('The Who')
plt.show()

plt.plot(Led_Zeppelin)
plt.ylabel('Led Zeppelin')
plt.show()

plt.plot(Ray_Charles)
plt.ylabel('Ray Charles')
plt.show()





