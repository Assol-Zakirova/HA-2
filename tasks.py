#1) It can hold data of any type,however sets are not recommended
#2)
import pandas as pd
import numpy as np
data = [i for i in range(1,13)]
df = pd.Series(data,index=['January','February','March','April','May','June',
                           'July','August','September','October','November','December'])
print(df)
print()
#3
d={ 'MatMIE':34, 'MatDAIS':36, 'COMSE':40, 'COMSEH':43}
print(pd.Series(d))
print()
#4
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(pd.DataFrame(exam_data,index=labels))
print()
#5
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
res=pd.DataFrame(exam_data,index=labels)
filt_res=res.query('attempts>2')
print('Number of attempts in the examination is greater than 2:\n',filt_res)
