def perceptronAnd(x):
  if x>0:
    return 1
  return 0

def perceptronOr(x):
  if x>=0:
    return 1
  return 0

def perceptronNot(x):
  if x<0:
    return 1
  return 0  

l1 = []
l2 = []
l3 = []

def NotLogic(i,b):
  sum1 = 0
  for x in i:
    l3.append(perceptronNot(x+b))

def AndLogic(i,j,b):
  sum1 = 0
  for x,y in zip(i,j):
    sum1 = x + y + b
    l1.append(perceptronAnd(sum1))

def AndLogic1(i,j,b):
  sum1 = 0
  for x,y in zip(i,j):
    sum1 = x + y + b
    print(perceptronAnd(sum1))

def OrLogic(i,j,b):
  sum1 = 0
  for x,y in zip(i,j):
    sum1 = x + y + b
    l2.append(perceptronOr(sum1))

i = [0,0,1,1]
j = [0,1,0,1]
b = -1
AndLogic(i,j,b)
OrLogic(i,j,b)
NotLogic(l1,b)
AndLogic1(l3,l2,b)

'''
output
[0, 0, 0, 1]
[0, 1, 1, 1]
0
1
1
0
'''