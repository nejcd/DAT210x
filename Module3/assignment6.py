import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv('Datasets/wheat.data')
print df.head()
print df.dtypes



#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
# .. your code here ..
df = df.drop(axis=1,labels ='id')
#df = df.drop(axis=1,labels ='area')
#df = df.drop(axis=1,labels ='perimeter')
print df.head()

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
corr = df.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow(corr, cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()


