## one shot encoding
import numpy as np

# ========== EDIT HERE ==========
alphabet = 'abcdefghijklmnopqrstuvwxyz ' # <- 빈칸이 있어야 빈칸도 처리 가능
# ===============================

def encoding(data):
    ######################################
    # TODO :  encoding 함수를 구현하시오.  
    #         [Input]
    #         - data : (type : string)  
    #  
    #         [output]
    #         - encoded : (type : array, size of [len(data), len(alphabet)]) encoding result.  
    # ========== EDIT HERE ==========

    char_to_int = dict((c,i) for i,c in enumerate(alphabet))
    encoded = np.zeros([len(data), len(alphabet)], dtype = int)
    for i,j in enumerate(data):
        encoded[i, char_to_int[j]] = 1

    # ===============================
    return encoded

def decoding(data):
    ######################################
    # TODO :  decoding 함수를 구현하시오.  
    #         [Input]
    #         - data : (type : array, size : [len(data), len(alphabet)])  
    #  
    #         [output]
    #         - decoded : (type : string) decoding result.  
    # ========== EDIT HERE ==========
    int_to_char = dict((i,c) for i,c in enumerate(alphabet))
    decoded = ''
    for v in data:
        decoded += int_to_char[np.argmax(v)]
    # ===============================
    
    return decoded
    
if __name__ == '__main__':
    data = 'data scientist'
    
    encoded = encoding(data)
    decoded = decoding(encoded)

    print(encoded)

