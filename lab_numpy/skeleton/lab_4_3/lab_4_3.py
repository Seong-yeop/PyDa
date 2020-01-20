## 알파벳 소문자와 빈칸만 iuput으로 주어진다 가정합니다.
import numpy as np

# ========== EDIT HERE ==========
# TODO : 인코딩, 디코딩 할때 쓸 자료형

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
  
    # ===============================
    
    return decoded
    
if __name__ == '__main__':
    data = 'data scientist'
    
    encoded = encoding(data)
    decoded = decoding(encoded)

    print(encoded)

