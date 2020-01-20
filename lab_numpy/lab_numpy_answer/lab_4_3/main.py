import numpy as np
from lab_4_3 import *

input_path = './test/input.txt'
output_path = './test/output.txt'
answer_path = './test/answer.txt'
logfile_path = 'log.txt'

alphabet = 'abcdefghijklmnopqrstuvwxyz ' 

def encoding_ans(data):
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

def decoding_ans(data):
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


with open(input_path) as f:
    inputs = f.readlines()

f_w = open(output_path, 'w')
outputs = [encoding(list(v.strip())) for v in inputs]
outputs_ans = [encoding_ans(list(v.strip())) for v in inputs]

outputs2 = [decoding(v) for v in outputs]
outputs2_ans = [decoding_ans(v) for v in outputs_ans]

wrong_cases = []
correct = 0
num = 0


for i, j in zip(outputs, outputs_ans):
    if (i==j).all():
        correct += 1
    else:
        wrong_cases.append((num,i,j))

for i, j in zip(outputs2, outputs2_ans):
    if i==j:
        correct += 1
    else:
        wrong_cases.append((num,i,j))

    num += 1
print("Score : " + str(correct) + "/" + str(correct + len(wrong_cases)))

if len(wrong_cases):
    with open(logfile_path, 'w') as f:
        for num, i, j in wrong_cases:
            f.write(
                f'Line #{num}\n' +
                f'Expected: {j}\n' +
                f'But you : {i}\n'
            )
