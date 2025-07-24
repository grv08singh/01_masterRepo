# Open jupyter notebook at a specified path:
# Type in Anaconda Prompt
# jupyter notebook --notebook-dir="specified_path"
# jupyter notebook --notebook-dir="D:\04 Intellipaat - EPGC\02 EPGC - Python\06 Python - Mandatory Assignments\05 - Data Visualization Assignment"
# jupyter notebook --notebook-dir="C:\Users\Grv\00 DS Python\00-grv-DS PythonPractice"
# jupyter notebook --notebook-dir="D:\04 Intellipaat - EPGC\03 EPGC - ML\2025.07.20 - EPGC - RF HandsOn"



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_scoreimport warnings
warnings.filterwarnings('ignore')








# 1. EDA :: Exploratory Data Analysis

# 1.1 Cleaning

# 1.2 Checking Datatype Inconsistency 
#### (when column is supposed to be float/int, but it is object type due to a space or unknown value maybe)
####
#### for col in df.columns:
####     if df[col].dtype == 'object':
####        print(f"{col}: {df[col].unique()}")
####        print()
####
#### 'unknown' values count
#### for col in [col1, col3, col6, col9]:
####    if df[col].dtype == 'object':
####        print(f"{col}: {df[col].value_counts()['unknown']}")
####
#### replacing 'unknown' value with Null
#### for col in ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan']:
####   if df[col].dtype=='object':
####     df[col].replace('unknown',np.NAN)

# 1.3 Remove Null Values (if Null < 10% of data, [dropna], else if Null < 40% of data, [fillna] with median/mode, else [drop feature/col])
#### for col in df.columns:
####     if(df[col].dtype in ('int64', 'float64'):
####         df[col] = df[col].fillna(df[col].median())
####     else:
####         df[col] = df[col].fillna(df[col].mode()[0])
####
#### drop Null rows from specific columns -->
#### df = df.dropna(subset=[col1, col2, col3, col4])

# 1.4 Remove Duplicates
#### df.drop_duplicates()

# 1.5 Outliers - 
#### Check for outliers
#### 
#### for col in df.columns:
####     if(df[col].dtype in ('int64', 'float64'):
####         sns.boxplot(data = df, y = col)
####         plt.show()

#### Remove outliers
####
#### initial_size = df.shape[0]
#### for col in df.columns:
####     if(df[col].dtype in ('int64', 'float64')):
####         Q1 = df[col].quantile(0.25)
####         Q3 = df[col].quantile(0.75)
####         IQR = Q3-Q1
####         LB = Q1 - 1.5 * (IQR)
####         UB = Q3 + 1.5 * (IQR)
####         df = df[ (df[col] >= LB) & (df[col] <= UB) ]
#### final_size = df.shape[0]
#### print(f"rows removed: {initial_size - final_size}")

# 1.6 Label Encoding
#### Label encoding on all the non-numeric columns
####
#### from sklearn.preprocessing import LabelEncoder
#### LE = LabelEncoder()
#### for col in df.columns:
####    if(df[col].dtype == 'object'):
####        df[col] = LE.fit_transform(df[col])
####        print(LE.classes())


# 2. Statistics



# 3. Machine Learning - Model Building
# IMPORT LIBRARY
#### from sklearn.linear_model import LinearRegression
#### from sklearn.model_selection import train_test_split
#### from sklearn.metrics import *
#### 
# x-y SPLIT
#### x = df.drop(columns = [out_col])
#### y = df[out_col]
####
# TRAIN-TEST SPLIT
#### x_train, x_test, y_train, y_test = train_test_split(x, y, train_size= 0.7, random_state = 42)
####
# TRAINING
#### my_model = LinearRegression()
#### my_model.fit(x_train,y_train)
####
# TESTING
#### y_pred = my_model.predict(x_test)
####
# EVALUATION
#### r2_score(y_test,y_pred)                                            #r-squared value
#### mean_absolute_error(y_test,y_pred)
#### mean_squared_error(y_test,y_pred)
#### np.sqrt(mse)                                                       #root-mean-squared error (rmse)
#### sns.regplot(x = y_pred, y =y_test,line_kws={'color':'red'})

# 10-different models for same data
#### r_sq = []
#### rmse = []
#### for i in range(10):
####     x_train, x_test, y_train, y_test = train_test_split(x, y, train_size= 0.7)
####     my_model = LinearRegression()
####     my_model.fit(x_train,y_train)
####     y_pred = my_model.predict(x_test)
####     r2_score(y_test,y_pred)
####     mean_absolute_error(y_test,y_pred)
####     mse = mean_squared_error(y_test,y_pred)
####     rmse.append(np.sqrt(mse))
#### 
#### print(r_sq)
#### print(rmse)












# numpy - Everything

# list = []

# import numpy as np

# np.ceil(arr)                                                      #returns an array of integers lower than orig numbers
# np.floor(arr)                                                     #returns an array of integers greater than orig numbers
# np.rint(arr)                                                      #returns an array of integers closest to orig numbers

# np.array(list)
# np.ones((rows, columns))
# np.zeros((rows, columns))
# np.full((rows, columns), n)                                       #an array of rows x columns filled with n

# np.linspace(start, end+1, number_of_points)
# np.arange(start, end+1, space_between_numbers)

# np.identity(3)                                                    #identity Matrix
# np.eye(3,4,k=1)                                                   #diagonal(1) shifted right Matrix
# np.eye(4,3,k=-1)                                                  #diagonal(1) shifted left Matrix
# arr.flatten()                                                     #array flattened to 1-D
# np.diag(arr)                                                      #diagonal of a Matrix
# np.fliplr(arr)                                                    #flipping an array from left to right
# np.rot90(arr)                                                     #rotating an array by 90 degrees anticlock-wise

# np.random.random()                                                #random whole number between 0 and 1 - uniform distribution
# np.random.rand()                                                  #random whole number between 0 and 1 - uniform distribution
# np.random.randn()                                                 #random number - normal distribution
# np.random.randint(start, end)                                     #for random integer

# np.random.random(2)                                               #1-D array of 2 random whole numbers between 0 and 1 from uniform distribution
# np.random.rand(4)                                                 #1-D array of 4 random whole numbers between 0 and 1 from uniform distribution
# np.random.randn(3)                                                #1-D array of 3 random numbers from normal distribution

# np.random.random((3,4))                                           #2-D array of 12 random whole numbers between 0 and 1 from uniform distribution
# np.random.rand(3,4)                                               #2-D array of 12 random whole numbers between 0 and 1 from uniform distribution
# np.random.randn(2,3)                                              #2-D array of 6 random numbers from normal distribution

# np.random.random((2,3,4))                                         #3-D array of 24 random whole numbers between 0 and 1 from uniform distribution
# np.random.rand(2,3,4)                                             #3-D array of 24 random whole numbers between 0 and 1 from uniform distribution
# np.random.randn(2,3,4)                                            #3-D array of 24 random numbers from normal distribution

# np.random.seed(101)                                               #Fix the random numbers all at ones using a particular number in seed

# np.size(array)                                                    #total number of elements in an array
# array.size                                                        #total number of elements in an array
# np.ndim(array)                                                    #dimension of array
# array.ndim                                                        #dimension of array
# np.shape(array)                                                   #shape of the array (n,m) format
# array.shape                                                       #shape of the array (n,m) format
# array.dtype

# array.reshape(num_of_rows, num_of_columns)                        #shows the changed shape but doesn't change the original shape.
# array.resize(num_of_rows, num_of_columns)                         #changes the original shape of array

# arr2 = np.append(arr1, n)                                         #append element n at the end of an array
# arr3 = np.insert(arr1, i, n)                                      #insert element n at index i
# arr4 = np.delete(arr1, i)                                         #delete element at index i
# for i,v in enumerate(arr4):                                       #loop through arr4, v=value at i=index
# np.where(arr4 == 50)                                              #in arr4, find index of element value=50
# sorted(arr4)                                                      #sort arr4 and print without saving permanently
# np.sort(arr4)                                                     #sort arr4 and print without saving permanently
# arr4.sort()                                                       #sort arr4 ascending and save the values in arr4

# np.equal(arr1, arr2)                                              #element-by-element comparison, returns an array of true/false
# np.array_equal(arr1, arr2)                                        #array as a whole comparison, returns either true or false

# np.sum(array)                                                     #sum of all the elements of an array - returns a scalar
# np.sum(array,axis=0)                                              #sum of all elements from 1st axis
# np.sum(array,axis=1)                                              #sum of all elements from 2nd axis
# np.sum([arr1, arr2])                                              #sum of all elements from both the arrays - returns a scalar
# np.sum((arr1, arr2))                                              #sum of all elements from both the arrays - returns a scalar

# arr1 + arr2                                                       #element-wise sum - returns an array
# np.add(arr1, arr2)                                                #element-wise sum - returns an array

# arr1 - arr2                                                       #element-wise difference - returns an array
# np.subtract(arr1, arr2)                                           #element-wise difference - returns an array

# arr1 / arr2                                                       #element-wise division - returns an array of float
# np.divide(arr1, arr2)                                             #element-wise division - returns an array of float

# arr1 // arr2                                                      #element-wise division - returns an array of integers
# np.floor_divide(arr1, arr2)                                       #element-wise division - returns an array of integers

# arr1 * arr2                                                       #element-wise (Hadamard or Schur) product - returns an array
# np.multiply(arr1, arr2)                                           #element-wise (Hadamard or Schur) product - returns an array

# arr1 @ arr2                                                       #Matrix (dot) product - returns an array
# np.dot(arr1, arr2)                                                #Matrix (dot) product - returns an array
# np.matmul(arr1, arr2)                                             #Matrix (dot) product - returns an array

# np.inner(arr1, arr2)                                              #inner product of two arrays, returns a scalar
# np.outer(arr1, arr2)                                              #outer product of two arrays, returns an array

# np.cross(v1, v2)                                                  #Vector (cross) product - returns an array

# arr1 % arr2                                                       #element-wise modulus - returns an array
# np.mod(arr1, arr2)                                                #element-wise modulus - returns an array

# arr1 ** arr2                                                      #element-wise power - returns an array
# np.power(arr1, arr2)                                              #element-wise power - returns an array

# np.sqrt(num)
# np.pi

# np.min(array)
# np.argmin(array)                                                  #index/position of minimum
# np.max(array)
# np.argmax(array)                                                  #index/position of maximum

# np.mean(array)
# np.median(array)
# np.median(array)
# np.std(array)

# np.sin(num)
# np.sin(array)
# np.cos(num)
# np.cos(array)
# np.tan(num)
# np.tan(array)

# np.log(num)
# np.log(array)
# np.exp(num)
# np.exp(array)

# np.corrcoef(array)

# np.concatenate((arr1, arr2))                                      #concat two arrays one after another
# np.hstack((arr1, arr2))                                           #
# np.vstack((arr1, arr2))                                           #concat two arrays one below another
# np.column_stack((arr1, arr2))                                     #Transposed of vstack result
            
# np.hsplit(array,2)                                                #split into 2 horizontal parts
# np.hsplit(array,np.array([3]))                                    #split into one part of 3 cols and another part of remaining cols
# np.vsplit(array,3)                                                #split into 3 vertical parts

# np.clip(arr, a_min=10, a_max=30)                                  #replace all values below 10 with 10 and greater than 30 with 30 in arr
# np.where(arr < 10, 10, np.where(arr > 30, 30, arr))               #replace all values below 10 with 10 and greater than 30 with 30 in arr



# M1 * M2                                                           #element-by-element multiplication of matrix
# M1 @ M2                                                           #matrix multiplication
# np.matmul(M1, M2)                                                 #matrix multiplication
# np.dot(M1, M2)                                                    #matrix multiplication

# M.T                                                               #Transpose numpy array without changing the original array
# np.transpose(M)                                                   #Transpose numpy array without changing the original array
# np.linalg.det(M)                                                  #determinant of matrix
# np.linalg.inv(M)                                                  #inverse of a matrix
# np.linalg.matrix_rank(M)                                          #rank of a matrix
# np.linalg.eig(M)                                                  #(eig_val, eig_vector) of matrix

# np.cross(V1, V2)                                                  #cross product of vectors
# np.dot(V1, V2)                                                    #dot product of vectors
# np.linalg.norm(V1)                                                #magnitude of vector


















# pandas - Everything

# import pandas as pd
# my_list = []
# labels = []

############# Series
# pd.Series(my_list, index=labels)                                  #list to pd.Series
# pd.Series(my_dictionary)                                          #dictionary to pd.Series
# pd.Series(list(my_set))                                           #set to list to pd.Series
# pd.Series(my_array, index=labels)                                 #np.array to pd.Series
            
# list(series_1)                                                    #pd.Series to list
# tuple(series_1)                                                   #pd.Series to tuple
# series_1.to_dict()                                                #pd.Series to dictionary
# set(series_1)                                                     #pd.Series to set
            
# series_1 + series_2                                               #gives union of both the series
            
# series_1.loc[2]                                                   #returns data from row index 2
# series_1.loc[0:3]                                                 #returns data from row index 0 to 3
# series_1.loc[[2,3,6]]                                             #returns data from row index 2,3,6
            
# series_1.iloc[2]                                                  #returns data from row index 2
# series_1.iloc[0:3]                                                #returns data from row index 0 to 2
# series_1.iloc[[2,3,6]]                                            #returns data from row index 2,3,6
# series_1.drop(2)                                                  #remove row at index 2
            
# series_1.append(5)                                                #append element=5 at the end of series_1
# #### series_1.insert()                                            #pandas series don't have insert method, so, convert to dataframe first
# pd.concat([s[:5], pd.Series([50], index=[5]), s[5:]])             #use concat to insert at index 5 in pandas series
# series_1.reset_index(drop = True)                                 #reset index without making previous index a column
# series_1.reset_index()                                            #reset index making previous index a column
            
            
            
            
############# DataFrame df          
# df = pd.DataFrame(my_list, columns =['x','y'])                    #create DataFrame from list
# df = pd.DataFrame(my_dict, columns =['x','y'])                    #create DataFrame from dictionary

# df = pd.read_csv('my_csv.csv')                                    #read data from csv file into df
# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# df.head()                                                         #show first 5 rows of df
# df.tail()                                                         #show last 2 rows of df
            
# df.columns                                                        #show all the columns in df
# df.shape                                                          #returns a tuple of size (#rows(length), #columns(width))
# df.info()                                                         #returns column-wise non-null counts and data-types
# df.describe()                                                     #returns count,mean,std,min,25%,median,75%,max for each numeric column
# df.transpose()                                                    #transpose all the data of df
# df.index                                                          #range of index
            
# df.min()                                                          #returns a minimum value for each column
# df.max()                                                          #returns a maximum value for each column
# df.mean()                                                         #returns mean for every numeric column
# df.median()                                                       #returns median for every numeric column
# df.std()                                                          #returns standard deviation for every numeric column
# df.count()                                                        #returns count for every numeric column
# df.describe()                                                     #returns count,mean,std,min,25%,median,75%,max for each numeric column
# df.describe(include = 'O')                                        #returns count,unique,frequency,top (Statistics) for non-numeric column
# df.describe(include = 'all')                                      #returns Statistics for all numeric column

# df.duplicated().sum()                                             #row-wise count of duplicates
# df.drop_duplicates()                                              #drop duplicate rows
# df['col_1'].astype(float)                                         #change col_1 data type to float
# df.drop(columns = [col_1,col_2], inplace=True)                    #drop col_1 and col_2

# df['col_1'].mean()                                                #returns mean for col_1
# df['col_1'].median()                                              #returns median for col_1
# df['col_1'].std()                                                 #returns standard deviation for col_1
# df['col_1'].count()                                               #returns count for col_1
# df['col_1'].value_counts()                                        #group by col_1 and show its count
# df.groupby('col_1')['col_2'].size()                               #group by col_1, count of col_2
            
# df.values.tolist()                                                #All DataFrame values to list
# df.to_dict()                                                      #DataFrame to a dictionary
# df['col_1'].astype(int)                                           #convert data type to integer
# pd.to_numeric(df['col_1'], errors='coerce')                       #convert col_1 values to numbers, if there is space then make it null
# df.corr(numeric_only = True)                                      #correlation coefficient for each value with respect to every other value
            
# df['col_1'].fillna(value=df['col_1'].mean())                      #fill all the null values in col_1 with avg of it
# df['col_1'].replace(' ', np.nan)                                  #replace all the space values with null
# df.dropna()                                                       #drop all the rows with null in any column
# df.dropna(axis=0)                                                 #drop all the rows with null in any column
# df.dropna(axis=1)                                                 #drop all the columns with null in any row
# df.dropna(thresh=2)                                               #drop all the rows with values above 2
# df.fillna(value='abc')                                            #fill all the null values with 'abc'
            
# pd.concat([df_1, df_2])                                           #append df_2 at the end of df_1
# pd.concat([df_1, df_2], axis=0)                                   #append df_2 at the end of df_1
# pd.concat([df_1, df_2], axis=1)                                   #append df_2 at the end and right of df_1
# pd.merge(df_1,df_2,how='inner',on='col_3')                        #SQL INNER JOIN on col_3
# pd.merge(df_1,df_2,how='outer',on=['col_3','col_5'])              #SQL OUTER JOIN on col_3 and col_5
# pd.merge(df_1,df_2,how='left',on='col_5')                         #SQL LEFT JOIN on col_5
            
# df_left.join(df_right)                                            #SQL INNER JOIN based on row_index
# df_left.join(df_right,how='left')                                 #SQL LEFT JOIN based on row_index
            
# pd.reset_index(drop = True)                                       #reset index making previous index a column
# pd.set_index('col_3', inplace=True)                               #to set col_3 as indexs
            
# np.array_split(df, 2)                                             #split df into 2 np arrays of almost equal rows
# np.array_split(df, 2, axis=0)                                     #split df into 2 np arrays of almost equal rows
# np.array_split(df, 2, axis=1)                                     #split df into 2 np arrays of almost equal columns
            
# df['col_1']                                                       #returns data of col_1
# df.col_1                                                          #returns data of col_1
            
# df['col_1'][0]                                                    #returns data of col_1 @ row index 0
# df.col_1'[0]                                                      #returns data of col_1 @ row index 0
            
# df.loc[0:3, 'col_1':'col_4']                                      #returns data from row 0 to 2 & col_1 to col_4
# df.loc[0:5,'col_0':'col_2']                                       #returns data from row 0 to 4, col_0 to col_2
# df.loc[[2,3,6],['col_1','col_3']]                                 #returns data from row 2,3,6 & col 1,3
            
# df.iloc[0:3, 1:4]                                                 #returns data from row 0 to 2 & col_1 to col_4
# df.iloc[0:5,0:3]                                                  #returns data from row 0 to 4, col 0 to 2
# df.iloc[[2,3,6],[5,2]]                                            #returns data from row 2,3,6 & col 5,2
            
# df['col_1'].unique()                                              #Unique values from col_1
# df['col_1'].nunique()                                             #The number of unique values from col_1
# df['col_1'].value_counts()                                        #group by col_1 and show its count
            
# df.isnull.sum()                                                   #column-wise count of null values
# df.notnull.sum()                                                  #column-wise count of non-null values
# del df['col_1']                                                   #permanently remove col_1
# df.fillna({'col_1':x}, inplace=True)                              #fill null values in col_1 with x
            
# Sorting of DataFrame          
# df.sort_values(by = 'col_1')                                      #sort ascending based on col_1
# df.sort_values(by = 'col_1', ascending = False)                   #sort descending based on col_1
            
# Filtering DataFrame           
# df['col_1']>5]                                                    #returns True/False based on the condition >5
# df[df['col_1']>5]                                                 #returns DataFrame where condition is true
# df[df['col_1']>5 & df['col_2']<10]                                #returns DataFrame where both the conditions meet
            
# df.groupby('col_1')['col_2'].sum()                                #group by col_1, sum of col_2
# df.groupby('col_1')['col_2'].count()                              #group by col_1, count of col_2
# df.groupby('col_1')['col_2'].mean()                               #group by col_1, mean of col_2
# df.groupby('col_1')['col_2'].std()                                #group by col_1, standard deviation of col_2
# df.groupby('col_1')['col_2'].max()                                #group by col_1, maximum of col_2
# df.groupby('col_1')['col_2'].min()                                #group by col_1, minimum of col_2

# df.pivot_table(values='col_4',index=['col_1', 'col_2'],columns=['col_3'])
                                                                    #summarize col_4 on combination of col_1, col_2 on rows and col_3 on columns
# df['date'] = pd.to_datetime(df['date'])


# pd.Timestamp.now()
# pd.Timestamp.now().year

















# matplotlib - Everything

# import matplotlib.pyplot as plt

#univariate     (1-axis)    ::  countplot,histogram,box
#bivariate      (2-axes)    ::  bar,scatter,line
#multivariate   (>1-axes)   ::  heatmap,pairplot

#relation plots             ::  scatter,line
#distribution plots         ::  histogram,kde plot,pie chart,countplot
#categorical plots          ::  barplot,countplot,box plot,violin plot


# Udemy
# Regular Plotting
# x = np.linspace(0,5,21)
# y = x**2
# plt.plot(x,y)
# 
# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.subplot(1,2,2)
# plt.plot(y,x)

# Object Oriented Plotting (OOP) - Manual Method of creating figure and axes separately
# fig = plt.figure()
# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# ax.plot(x,y)
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.set_title('title')
# ax.set_xlim([4,7])                                                #set lower and upper limit on x-axis
# ax.set_ylim([15,50])
# 
# fig = plt.figure()
# ax0 = fig.add_axes([0,0,1,1])
# ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
# ax2 = fig.add_axes([0.2,0.5,0.4,0.3])
# ax1.plot(x,y)
# ax2.plot(y,x)


# Object Oriented Plotting (OOP) - Automatic Method of creating figure and axes simultaneously
# fig,axes = plt.subplot(nrows=1,ncols=2)                           #automatic execution of [fig = plt.figure()] & [ax = fig.add_axes()]
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.tight_layout()                                                #remove the issue of overlapping plots


# fig = plt.figure(figsize=(3,2),dpi=200)
# fig,axes = plt.subplots(figsize=(3,2))
# axes.plot(x,y)

# fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(8,3))
# axes[0].plot(x,y)
# axes[1].plot(y,x)

# fig.savefig('x-y sq plot.png', dpi=200)

# ax.plot(x, x**2, label='x-squared')
# ax.plot(x, x**3, label='x-cubed')
# ax.legend(loc=0)                                                  #0-best fit location

# arguments of plot() method:           
    # color                                                         #'r','g','b','k','y','c','m'
    # linewidth or lw                                               #for line plot only
    # linestyle or ls                                               #for line plot only
    # alpha                                                         #0 to 1: 0-Transparent, 1-Opaque
    # marker                                                        #'o','*','+','y','^'
    # markersize                                                    #
    # markerfacecolor                                               #
    # markeredgewidth                                               #
    # markeredgecolor                                               #
    # explode                                                       #tuple having values >= 0, to Cut out a sector from pie chart
    # autopct='%1.2f%%'                                             #2-decimal pt. %age in pie chart
    # shadow                                                        #explode in pie chart
    # startangle=90                                                 #only in pie chart
    # radius=1.5                                                    #only in pie chart, to change pie to donut
    # labels                                                        #labels
    # hue='col_2'                                                   #Segregate based on col_2








# Intellipaat
# x = range(32)
# y = df['col_1']

# Single Chart/Plot
# plt.plot(df['col_1'],df['col_2'])                                 #line chart
# plt.bar(df['col_1'],df['col_2'])                                  #vertical bar chart
# plt.barh(df['col_1'],df['col_2'])                                 #horizontal bar chart
# plt.scatter(df['col_1'],df['col_2'])                              #scatter plot
# plt.stackplot(df['col_1'],df['col_2'])                            #Area/stack plot, y can be 2-d array
# plt.pie(df['col_2'])                                              #Pie Chart
# plt.boxplot(df['col_2'])                                          #used to find outlier
# plt.violinplot(df['col_2'])                                       #used to find outlier
# plt.imshow(df['col_2'], cmap='summer')                            #heatmap
# plt.hist(df['col_1'], bins=8, edgecolor="white")                  #histogram with 8 bins
            
# plt.figure(figsize=(4, 10))           
# plt.xlabel('X Axis Title Here')           
# plt.ylabel('Y Axis Title Here')           
# plt.title('title_1')            
# plt.legend('legend_1')            
# plt.grid(True)            
# plt.xticks(rotation=90)            
# plt.show()            

# plt.subplot(2,3,4).plot(df['col_1'],df['col_2'],'g--')            #2 rows, 3 coloumns, 4th plot, g-- green dashed line
# plt.subplot(r,c,sn).plot(df['col_1'],df['col_2'],'y*-')           #y*- yellow line with * marker
            
                
# arguments of pie() method:            
    # labels='col_1'                                                #Pie chart only
    # explode=()                                                    #Pie chart only
    # autopct='%1.2f%%'                                             #Pie chart only
                
# arguments of imshow() method:         
    # cmap = 'autumn', 'summer', 'winter','spring'                  #different color schemes
            
# Multiple Charts/Plots in Grid of 1x3                              # 1-row, 3-columns
# plt.subplot(1,3,1).scatter(x=df['col_1'],y=df['col_2'])           # 1- rows, 3 - col 1 - position
# plt.subplot(1,3,2).scatter(x=df['col_1'],y=df['col_2'])           # 1- rows, 3 - col 2 - position
# plt.subplot(1,3,3).scatter(x=df['col_1'],y=df['col_2'])           # 1- rows, 3 - col 3 - position
# plt.show()




















# Seaborn

# import seaborn as sns

# sns.pairplot(data=df)                                             #scatterplot for all the column pairs
# sns.countplot(data=df, x='col_1')                                 #vertical bar chart of col_1 summarized with its count
# sns.countplot(data=df, y='col_1')                                 #horizontal bar chart of col_1 summarized with its count
# sns.boxplot(data=df, y='col_1')                                   #used to find outlier
# sns.scatterplot(data=df, x='col_1', y='col_2')                    #scatter plot
# sns.barplot(data=df, x='col_1', y='col_2')                        #bar chart
# sns.regplot(data=df, x='col_1', y='col_2')                        #regression plot = scatter plot with best fit line
# sns.heatmap(data=df, y=3x3_array)                                 #heat map
# sns.boxplot(data=df, y='col_1', hue='col_2')                      #box plot
# sns.histplot(data=df, x='col_1', hue='col_2')                     #histogram plot
# sns.lineplot(data=df, x='col_1', y='col_2')                       #line plot

# arguments of scatterplot() method:
    # color 'r','g','b','k','y','c','m'
    # palette for multiple colors
    # hue for group by on col_2
    # marker '^','-','--','*','o','+'
    # s for size of the marker
    # edgecolor is for the edge color of the marker
    # alpha is for transparency of the marker

################## Subplots in seaborn
# fig, axis = plt.subplots(nrows=2, ncols=2, figsize=(12,8))
# sns.barplot(data=df, x='col_1', y='col_2', hue='col_3', ax = axis[0,0])













# strings - Everything

# s1 = 'abcdefghij'                                                 #string
# s1[3]                                                             #string indexing
# s1[-1]
# s1[2:]                                                            #string slicing
# s1[:8]
# s1[1:5]
# s1[::2]                                                           #every character from string s with step size 2
# s1[::-1]                                                          #string backwards

# s2 = 'welcome'
# s1 + s2                                                           #concatenation
# char = 'a'
# char * 10                                                         #'aaaaaaaaaa'

# s1.upper()                                                        #upper case
# s1.lower()                                                        #lower case
# s1.capitalize()                                                   #capitalize first character of first word

# s1.replace('d','z')                                               #replace 'd' with 'z' in s1
# s1.strip()                                                        #remove white space before and after s1
# s1.split()                                                        #split the string at space and provide a list of strings
# s1.split('c')                                                     #split the string at 'c'
# " ".join(arr_of_str)                                              #join an array of string with space in between
# len(s1)                                                           #length of string




# list - Everything

# my_list = ['A string',23,100.232,'o']                             #a list can contain anything
# len(my_list)                                                      #number of elements in a list
# my_list[2]                                                        #element at index 2
# my_list[2:]                                                       #elements from index 2 to end
# my_list[:3]                                                       #elements from start to index 2
# my_list[2:5]                                                      #elements at index 2,3,4
# my_list[::2]                                                      #every 2nd element from the list
# my_list[::-1]                                                     #reverse the list
# my_list + ['new item']                                            #concatenate element to the list
# my_list * 2                                                       #repeat the list
# my_list.append('append_me')                                       #append element to the list
# my_list.pop()                                                     #remove last element from the list and return it
# my_list.pop(2)                                                    #remove element at index 2 from the list and return it
# my_list.reverse()                                                 #reverse the list
# my_list.sort()                                                    #sort the list - in place
# sorted(my_list)                                                   #just show the sorted list, not sort original list
# [i**2 for i in my_list if i%2==0]                                 #list comprehension






# dictionary - Everything

# d = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
# d['key3']                                                         #give the value of key3 i.e. ['item0','item1','item2']
# d['key3'][0]                                                      #'item0'
# d['key3'][0].upper()                                              #'ITEM0'
# d.keys()                                                          #all the keys of the dictionary
# d.values()                                                        #all the values of the dictionary
# d.items()                                                         #all the key:value pairs of the dictionary




# tuples - Everything

# t = ('one', 2, 3.1)                                               #initializing a tuple
# len(t)                                                            #number of elements in the tuple
# t[-1]                                                             #last element of the tuple
# t.index('one')                                                    #index of element 'one' in the tuple
# t.count('one')                                                    #count of element 'one' in the tuple



# sets - Everything

# x = set()                                                         #creating a set
# x.add(1)                                                          #adding element to set
# x.add(2)                                                          #adding element to set
# set(my_list)                                                      #convert my_list to set: show any duplicate values only once