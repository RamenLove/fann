def perceptronx(x):
	if x>0:
		return 1
	return 0
def AndLogic(i,j,b):
	for x,y in zip(i,j):
		sum1 = 0
		sum1 = x + y + b
		print(perceptronx(sum1))
		
i = [0,0,1,1]
j = [0,1,0,1]
print("Output for AND")
AndLogic(i,j,-1)

def perceptron1(y):
	if y >= 0:
		return 1
	return 0

def OrLogic(i,j,b):
	for x,y in zip(i,j):
		sum1 = 0
		sum1 = x + y + b
		print(perceptron1(sum1))

i = [0,0,1,1]
j = [0,1,0,1]

print("Output for OR")
OrLogic(i,j,-1)
