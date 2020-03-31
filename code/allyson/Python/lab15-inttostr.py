(##  Convert Numbers to Phrase (Level 1) ##

num=input('Type Number Here  -->')
num=str(num)

def wordSpliter(word):
      return [char for char in word]



sin = {
      1:"One", 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 0:'Zero'
}
teen ={
      10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen',19:'Nineteen'
}
dou ={
      2:'Twenty', 3:'Thirty', 4:'Fourty',5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'
}
tri={
      '':'Hundred'
}
count=[]
wordArray=[]
l=len
print(count)
count=wordSpliter(num)

chk=len(count)

for i in range(len(count)):
      if chk == 1:
            wordArray.append(sin[int(count[i])])
      elif chk == 2:
            if int(num) < 20: 
                  wordArray.append(teen[int(num)])
      break
      
      else:
            if i == 0:
                  wordArray.append(dou[int(count[i])])
            elif i == 1:
                  wordArray.append(sin[int(count[i])])
      if chk == 3:
            wordArray.append(tri[int(count[i])])

finalWordNumberString = ''.join(wordArray)
print('Entered Number is: ' + finalWordNumberString)

if chk == 0:
      print('Zero')
if chk == 1:
      print('One Digit')
if chk == 2:
      print('Two Digits')  
