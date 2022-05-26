#Sigmoid Function 
 
import numpy as np 
import matplotlib.pyplot as plt 
import numpy as np 
plt.style.use('seaborn') 
plt.figure(figsize=(8,4)) 
def SigmoidBinary(t): 
	return 1/(1+np.exp(-t)) 
t = np.linspace(-5, 5) 
plt.plot(t, SigmoidBinary(t)) 
plt.title('Binary Sigmoid Activation Function') 
plt.show()


#ReLu Function:
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')
plt.figure(figsize=(8,4))
def RectifiedLinearUnit(t):
    lst=[]
    for i in t:
        if i>=0:
            lst.append(i)
        else:
            lst.append(0)
    return lst
arr = np.linspace(-5, 5)
plt.plot(arr, RectifiedLinearUnit(arr))
plt.title('Rectified Linear Unit Activation Function')
plt.show()

#Softmax Functions:	
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')
plt.figure(figsize=(8,4))
def softmax(t):
    return np.exp(t) / np.sum(np.exp(t))
t = np.linspace(-5, 5)
plt.plot(t, softmax(t))
plt.title('Softmax Activation Function')
plt.show()
