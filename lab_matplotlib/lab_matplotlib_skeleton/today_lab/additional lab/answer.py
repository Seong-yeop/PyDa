########################################################################################
#   Accuracy, Precision, Recall, F_measure 를 구하는 함수를 구현한다.                         
#   함수에서 넘겨주는 변수 label은 정답이고, pred는 예측값이다.  
#   label, pred에서 1은 positive이고, 0은 negative이다.
#
#   EDIT HERE 부분만 작성하시면 됩니다.
#   원하는 출력은 아래와 같습니다. 
#   your:  Accuracy         :        0.300000       answer:         :        0.300000
#   your:  Precision        :        0.400000       answer:         :        0.400000
#   your:  Recall           :        0.333333       answer:         :        0.333333
#   your:  F_measure        :        0.363636       answer:         :        0.363636
########################################################################################
import numpy as np

def Accuracy(label, pred):
    ########################################################################################
    # TODO :  accuracy 를 구하는 함수를 구현하시오.  
    #         [Input]
    #         - label : (N, ), Correct label with 0 (negative) or 1 (positive)
    #  
    #         [output]
    #         - Acc : (scalar, float), Computed accuracy score
    # ========================= EDIT HERE =========================
    

    # =============================================================
    return Acc

def Precision(label, pred):
    ########################################################################################
    # TODO :  precision 을 구하는 함수를 구현하시오.
    #         (단, 0으로 나눌 경우에는 1을 반환한다.) 
    #         [Input]
    #         - label : (N, ), Correct label with 0 (negative) or 1 (positive)
    #       
    #         [output]
    #         - precision : (scalar, float), Computed precision score
    # ========================= EDIT HERE =========================
    
    
    # =============================================================
    return precision

def Recall(label, pred):
    ########################################################################################
    # TODO : recall을 구하는 함수를 구현하시오.
    #        (단, 0으로 나눌 경우에는 1을 반환한다.)
    #         [Input]
    #         - label : (N, ), Correct label with 0 (negative) or 1 (positive)
    #        
    #         [output]
    #         - recall : (scalar, float), Computed recall score
    # ========================= EDIT HERE =========================



    # =============================================================
    return recall

def F_measure(label, pred):
    ########################################################################################
    # TODO : F-measure을 구하는 함수를 구현하시오.
    #        (단, 0으로 나눌경우에는 1을 반환한다.)
    #         [Input]
    #         - label : (N, ), Correct label with 0 (negative) or 1 (positive)
    #         [output]
    #         - F_score : (scalar, float), Computed F-score score
    # ========================= EDIT HERE =========================
 
 
 
 
    # =============================================================
    return F_score

def evaluation_test(label, pred):
    result = {}

    result['Accuracy '] = Accuracy(label, pred)
    result['Precision'] = Precision(label, pred)
    result['Recall   '] = Recall(label, pred)
    result['F_measure'] = F_measure(label, pred)

    return result
