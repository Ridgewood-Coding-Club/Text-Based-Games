import random


def randomword():
    words= ["apples", "pampero", "realm", "gasometer", "tortoise",
        "goal", "decree", "aquire", "pandemic"]
    word=words[random.randint(0,8)]
    return word
def RemoveChar(string1,idx1):
  if idx1 != -1:
    return string1[:idx1]+string1[idx1+1:]
  elif idx1 ==-1:
    return string1[0:idx1]       
def randomize(word):
  answer=word
  shown=""
  for i in range(len(word)-1,-1,-1):
    idx=random.randint(0,i)
    shown=shown+ word[idx]
    word=RemoveChar(word,idx)
  return shown,answer
x=True
shown,answer=randomize(randomword())

while x==True:
    print (shown)
    userint=str(input("Guess the word: "))
    if userint==answer:
        print('you win!!!')
        break
    else:
        print("Try again")
