import numpy as np
from lab_4_1 import *

input_path = './test/input.txt'
output_path = './test/output.txt'
answer_path = './test/answer.txt'
logfile_path = 'log.txt'


with open(input_path) as f:
    inputs = f.readlines()

f_w = open(output_path, 'w')

outputs_relu = [Relu(int(v.strip())) for v in inputs]
outputs_sig = [Sigmoid(int(v.strip())) for v in inputs]

#outputs = [Activation('Relu',list(map(int,v.strip().split(',')))) for v in inputs]



with open(output_path, 'w') as filehandle:
    for listitem in zip(outputs_relu, outputs_sig):
        filehandle.write('%s,%s\n' % listitem)

with open(output_path, 'r') as filehandle:
    outputs = filehandle.readlines()
with open(answer_path, 'r') as filehandle:
    answers = filehandle.readlines()

wrong_cases = []
correct = 0
num = 0

for i, o, a in zip(inputs, outputs, answers):
    if len(o.strip()) > 0 and o == a:
        correct += 1
    else:
        wrong_cases.append((num,i, o, a))

    num += 1

print("Score : " + str(correct) + "/" + str(correct + len(wrong_cases)))

if len(wrong_cases):
    with open(logfile_path, 'w') as f:
        for num, i, o, a in wrong_cases:
            f.write(
                f'Line #{num}\n' +
                f'Input: {i}' +
                f'Expected: {a}' +
                f'But you : {o}\n'
            )
