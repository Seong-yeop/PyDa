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
    m, n = height + 1 - kernel_size, width + 1 - kernel_size
    conv_out = np.zeros((int((height-kernel_size)/ stride)+1, int((width-kernel_size) / stride)+1))
    k = 0
    for i in range(0, m, stride):
        l = 0
        for j in range(0, n, stride):
            conv_out[k][l] = np.sum(x[i:i + kernel_size, j:j + kernel_size] * kernel)
            l = l + 1
        k = k + 1
    # =========================================================================
    return conv_out


if __name__ == '__main__':
    x = np.array([[1,0,0,0], [1,1,1,1], [0,1,0,0], [1,1,0,1]])
    kernel = np.array([[1,0,0], [0,1,1], [1,1,1]])

    x_ = np.array([[1,1,0,1,1], [0,1,0,0,1], [1,1,0,1,0], [0,0,1,1,1], [1,1,1,1,1]])
    kernel_ = np.array([[1,0,1], [1,1,1], [0,1,0]])

    y = convolution2d(x_,kernel_,stride=2)
    print(y)