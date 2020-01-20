import numpy as np
from answer import evaluation_test


label = np.array([0, 1, 1, 1, 1, 0, 0, 1, 1, 0])
pred  = np.array([0, 1, 0, 0, 1, 1, 1, 0, 0, 1])

result = evaluation_test(label, pred)

real_result = {}
real_result['Accuracy '] = 0.300000
real_result['Precision'] = 0.400000
real_result['Recall   '] = 0.333333
real_result['F_measure'] = 0.363636

for key in result.keys():
    print('your: ', key, '\t:\t %.6f' % result[key], '\tanswer: ', '\t:\t %.6f' % real_result[key])
