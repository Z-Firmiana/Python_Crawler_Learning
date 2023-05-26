import numpy as np
import pandas as pd

def Excel_Load_to_Array(address):
    pd.set_option('display.notebook_repr_html',False)
# 读取xls（绝对路径）
    data = pd.read_excel(io=address)
    print(data)
    Data_Array = np.array(data)
    return Data_Array
# Data_List = Data_Array.tolist()

# data1 = int(Data_Array[1][2])
# print(data1)
# print(type(data1))
#
# for i in range(34):
#     print(i)