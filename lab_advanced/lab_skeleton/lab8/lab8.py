import numpy as np

def convolution2d(x, kernel, stride=1):
    """
    Convolution 2D : Do Convolution on 'x' with filter = 'kernel', stride = 'stride'
    입력 x에 대해 'kernel'을 filter로 사용하여 2D Convolution을 수행하시오.
    [Input]
    x: 2D array
    - Shape : (Height, Width)
    kernel : 2D convolution filter
    - Shape : (Kernel size, Kernel size)
    stride : Stride size (default = 1)
    - dtype : int
    [Output]
    conv_out : convolution result
    - Shape : (Conv_Height, Conv_Width)
    - Conv_Height & Conv_Width can be calculated using 'Height', 'Width', 'Kernel size', 'Stride'
    """
    height, width = x.shape
    kernel_size = kernel.shape[0]
    conv_out = None
    # =============================== EDIT HERE ===============================
   
   
   
   
   
   
    # =========================================================================
    return conv_out


if __name__ == '__main__':
    x = np.array([[1,0,0,0], [1,1,1,1], [0,1,0,0], [1,1,0,1]])
    kernel = np.array([[1,0,0], [0,1,1], [1,1,1]])

    x_ = np.array([[1,1,0,1,1], [0,1,0,0,1], [1,1,0,1,0], [0,0,1,1,1], [1,1,1,1,1]])
    kernel_ = np.array([[1,0,1], [1,1,1], [0,1,0]])

    y = convolution2d(x_,kernel_,stride=2)
    print(y)
