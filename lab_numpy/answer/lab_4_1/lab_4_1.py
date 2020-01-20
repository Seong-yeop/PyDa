import numpy as np
import matplotlib.pyplot as plt

def Activation(func, x):
    if(func == 'Relu'):
        return Relu(x)
    else :
        return Sigmoid(x)
        
def Relu(x):
     ######################################
    # TODO :  Relu 함수를 구현하시오.  
    #         [Input]
    #         - x : (list or np.array) 
    #  
    #         [output]
    #         - y : (list or np.array) 함수의 결과
    # ========== EDIT HERE ==========
    y = np.maximum(0,x)
    
    # ===============================
    return y

def Sigmoid(x):
    ######################################
       # TODO :  Relu 함수를 구현하시오.  
    #         [Input]
    #         - x : (list or np.array) 
    #  
    #         [output]
    #         - y : (list or np.array) 함수의 결과
    # ========== EDIT HERE ==========
    
    y = (1/(1+np.exp(-x)))
    # ===============================
    return y

# ========== You can setting ==========
FUNCTION_NAME = 'Sigmoid'
# =====================================

assert FUNCTION_NAME in ['Sigmoid', 'Relu',]
if __name__ == '__main__':
    x = np.array([i for i in range(-6,7)])
    y = Activation(FUNCTION_NAME,x)
	
	#plt.plot(x,y)
	#plt.show()
