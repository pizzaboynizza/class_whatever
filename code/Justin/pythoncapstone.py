

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
The_Beatles_Rank = 1

b2 = Musical_Artist("Elvis Presley", 2, 3, 100, 2, 8)
Elvis_Presley = [2, 3, 100, 2, 8]
Elvis_Presley_Rank = 23

b3 = Musical_Artist("James Brown", 3, 7, 100, 100, 6)
James_Brown = [3, 7, 100, 100, 6] 
James_Brown_Rank = 43.2

b4 = Musical_Artist("Bob Dylan", 4, 2, 5, 18, 5)
Bob_Dylan = [4, 2, 5, 18, 5]
Bob_Dylan_Rank = 6.8

b5 = Musical_Artist("The Rolling Stones", 5, 4, 2, 3, 2)
The_Rolling_Stones = [5, 4, 2, 3, 2]
The_Rolling_Stones_Rank = 3.2

b6 = Musical_Artist("Stevie Wonder", 6, 15, 100, 27, 11)
Stevie_Wonder = [6, 15, 100, 27, 11]
Stevie_Wonder_Rank = 31.8

b7 = Musical_Artist("Chuck Berry", 7, 5, 100, 100, 26)
Chuck_Berry = [7, 5, 100, 100, 26]
Chuck_Berry_Rank = 47.6

b8 = Musical_Artist("The Who", 8, 29, 12, 39, 9)
The_Who = [8, 29, 12, 39, 9]
The_Who_Rank =  19.4

b9 = Musical_Artist("Led Zeppelin", 9, 14, 3, 5, 4)
Led_Zeppelin = [9, 14, 3, 5, 4]
Led_Zeppelin_Rank = 7

b10 = Musical_Artist("Ray Charles", 10, 10, 100, 100, 12)
Ray_Charles = [10, 10, 100, 100, 12]
Ray_Charles_Rank = 46.4

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

plt.plot(The_Who)
plt.ylabel('The Who')
plt.show()

plt.plot(Led_Zeppelin)
plt.ylabel('Led Zeppelin')
plt.show()

plt.plot(Ray_Charles)
plt.ylabel('Ray Charles')
plt.show()



