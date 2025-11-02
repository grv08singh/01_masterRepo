# AWS
# Acc ID: 676206921654
# Username: grv08singh@gmail.com
# pw: 

# Create Python environment using python
# python -m venv .venv
# .\.venv\Scripts\activate.bat
# 
# pip install -r requirements.txt
# 
# Create Python environment using conda
# conda create -p venv python==3.13 -y
# conda activate venv/
# 
# conda install -r requirements.txt






#Proj_01: use mnist dataset to learn a MBGD,DT,RF,KNN,DL model and create an online app to recognize handwritten digits.
#Proj_02: 





## Open jupyter notebook at a specified path:
## Type in Anaconda Prompt
## jupyter notebook --notebook-dir="specified_path"
## jupyter notebook --notebook-dir="D:\git_repo_DS\02_EPGC_Intellipaat\03 EPGC - Mandatory Assignments\19 EPGC - Py - Data Visualization Assignment Quiz"
## jupyter notebook --notebook-dir="D:\git_repo_DS\02_EPGC_Intellipaat\03 EPGC - Mandatory Assignments\17 EPGC - ML - Decision Tree Quiz"
## jupyter notebook --notebook-dir="D:\Projects\streamlit_startup_dashboard"
## C:\Users\grv06\AppData\Roaming\Code\User\settings.json


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,f1_score,accuracy_score, confusion_matrix,ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV





# Deep Learning Project (Predict handwritten digits):
# 1) Recognizing handwritten digits in training data
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.getcwd() #get the current working directory
os.listdir() #list the items in cwd

from PIL import Image #calling Pillow Library (PIL) and then loading the function/method Image
image_path = r"C:\Users\think\OneDrive\TRAINING\INTELLIPAAT\DEEP LEARNING\09. AI and DL IITR-07Sep2025(M)\number_7.png"
img = Image.open(image_path) #Pillow lib is used to open and load the image
img #print the image
img = img.convert('RGB') #convert the raw image to standard RGB image
img_gray = img.convert('L') #convert the standard RGB image to grayscale. L stands for Luminance
width, height = img_gray.size #it returns a tuple (width, height) of the image in pixels
img_gray_resized = img_gray.resize((28,28)) #Convert this image from (width X height) to (28 X 28)
img_gray_resized_array = np.array(img_gray_resized) # Convert the resized grayscale image into a pixelated np array

### Plotting the `pixelated image` as a 28 by 28 grid
plt.figure(figsize = (4,4))
plt.imshow(img_gray_resized_array, cmap='gray')
plt.colorbar()
plt.show()













# ML Pipeline:
#
## 1) Data Cleaning:
###    Remove Duplicates rows - df.duplicated()
###    Handle Null values - df.dropna() / df.fillna()
###    Check unique values of each column - df['col1'].unique().tolist()
###    Handle Errors - df['col1'].replace('unknown',NaN)
#
#
## 2) Data Pre-Processing (Standardize, Scale, Encode)
###    Inspect Data Types - df.info()
###    Check Missing Values - df.isnull().sum()
###    Statistical Summary - df.describe().T
###    Visualize Outliers in each numerical column using boxplot()
###    Remove Outliers using IQR Method
###    Correlation Analysis to understand the relationship between features & target variable - df.corr()
###    Check if Target Variable is balanced affecting model training and evaluation - plt.pie()
###    X - y Split
###    Feature Scaling:
####      Normalization      - MinMaxScaler().fit_transform(X)
####      Standardization    - StandardScaler().fit_transform(X)
#
#
## 3) Feature Engineering (Feature Selection, Create New or Transform Existing Features)
###    Feature Creation: creating new features using domain knowledge
###    Feature Transformation: 
####      Normalization / Standardization /Scaling
####      Encoding
####      Mathematical Transformation (log, sqrt etc.)
###    Feature Extraction: (PCA Technique) Reduces dimension, Reduces computation cost, Improves model performance, Prevents overfitting
####      Signal Processing
####      Statistical Techniques
####      Transformation Algorithms
###    Feature Selection: Choosing relevant features
####      Filter Methods
####      Wrapper Methods
####      Embedded Methods
###    Feature Scaling: to ensure all the features contribute equally
####      Min-Max Scaling
####      Standard Scaling
#
#
## 4) EDA Types:
###    Univariate Analysis: one variable - mean, median, mode, variance, std, barplot, kdeplot
###    Bivariate A.: relationship b/w two variables - pairplot, scatterplot, correlation cofficient, contingency table, line graph, covariance
###    Multivariate A.: rel. b/w two or more variables - heatmap, PCA, Spatial Analysis (geog. maps), ARIMA (time series Analysis)
#
#
## 5) Model Selection ---> based on: 
### data Complexity
### decision factors like performance, interpretability, scalability
### Experimentation with different models to find the best one
#
#
## 6) Model Training ---> basic features are:
### Iterative Process: Train the model iteratively, adjusting parameters to minimize errors & enhance accuracy
### Optimization: Fine-tune model to optimize its predictive capabilities
### Validation: Rigorously train model to ensure accuracy to new unseen data
#
#
## 7) Model Evaluation & Tuning
### Evaluation Metrics: Accuracy, Precision, Recall, F1 score, Specificity, Type-1-2 error, Confusion Matrix for performance evaluation
### Strengths & Weaknesses: Identify the strengths & weaknesses of the model through rigorous testing
### Iterative Improvement: Initiate model tuning to adjust hyperparameters & enhance predictive accuracy
### Model Robustness: Iterative tuning to achieve desired levels of model robustness & reliability
### Regularization - Lasso, Ridge, Elastic Net Regression - prevents overfitting, fine tuning, stable model, better performance, interpretability
### Bias Variance tradeoff
### Hyperparameter Tuning
### Cross Validation
### AUC-ROC curve
#
#
### 8) Model Deployment









###############################################################################################################
#### 1. EDA :: Exploratory Data Analysis
###############################################################################################################

# 1.1 Cleaning
df.shape
df.columns.tolist()
df.info()
df.describe().T
df.isnull().sum()
df.isnull().sum().sum()
df.duplicated().sum()
df['col1'].count()
df['col1'].sum()
df['col1'].unique()
df['col1'].nunique()
df['col1'].value_counts()
df.groupby('col1')['col2'].size()
df.groupby('col1')[['col2','col3','col4']].mean()
df.rename(columns={'col1' : 'col101','col2' : 'col102'},inplace = True)




# 1.2 Checking Datatype Inconsistency

#### (when column is supposed to be float/int, but it is object type due to a space or unknown value maybe)
for col in df.columns:
    if df[col].dtype == 'object':
       print(f"{col}: {df[col].unique().tolist()}")
       print()
       
#### 'unknown' values count
for col in [col1, col3, col6, col9]:
   if df[col].dtype == 'object':
       print(f"{col}: {df[col].value_counts()['unknown']}")
       
#### replacing 'unknown' value with Null
for col in ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan']:
  if df[col].dtype=='object':
    df[col].replace('unknown',NaN)


# 1.3 Remove Null Values (if Null < 10% of data, [dropna], else if Null < 40% of data, [fillna] with median/mode, else [drop feature/col])
for col in df.columns:
    if(df[col].dtype in ('int64', 'float64'):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

#### drop Null rows from specific columns -->
df = df.dropna(subset=['col1', 'col2', 'col3'])


# 1.4 Remove Duplicates
df = df.drop_duplicates()


# 1.5 Outliers - 
#### Check for outliers - Outliers Analysis

for col in df.columns:
    if(df[col].dtype in ('int64', 'float64'):
        sns.boxplot(data = df, y = col)
        plt.show()
        
# OR

fig = plt.figure(figsize=(15,12),dpi=300)
i = 0
for col in df.columns:
    if df[col].dtype in ('int64', 'float64'):
        i += 1
        plt.subplot(df.shape[1]//3, 3, i)
        sns.boxplot(data=df, x=col, width=0.2, color='violet')
        # or
        # plt.boxplot(x=df[col])
        # plt.title(col)
plt.show()



#### Remove outliers
initial_size = df.shape[0]
for col in df.columns:
    if(df[col].dtype in ('int64', 'float64')):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3-Q1
        LB = Q1 - 1.5 * (IQR)
        UB = Q3 + 1.5 * (IQR)
        df = df[ (df[col] >= LB) & (df[col] <= UB) ]
final_size = df.shape[0]
print(f"rows removed: {initial_size - final_size}")


# 1.6 Label Encoding
#### Label encoding on all the non-numeric columns
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
for col in df.columns:
   if(df[col].dtype == 'object'):
       df[col] = LE.fit_transform(df[col])
       df[col] = LE.fit_transform(df[col])






###############################################################################################################
#### 2. Machine Learning (ML) - Model Fitting
###############################################################################################################


# 2.1 X-y Split
X = df[['col1','col2']]
y = df['tgt_col']
#or
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
#or
X = df.iloc[:,[0,1,2,3,4,5,6,7]]
y = df.iloc[:,[8]]


# 2.2 Train-Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)


# 2.3 Initializing Different ML Model

## 2.3.1 Linear Regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

from sklearn.metrics import *
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2_score = r2_score(y_test, y_pred)

## 2.3.2 Logistic Regression
from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
log.fit(X_train, y_train)
y_pred = log.predict(X_test)

from sklearn.metrics import *
accuracy_score(y_test, y_pred)
confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
precision = tp / (tp + fp)
recall_or_sensitivity = tp / (tp + fn)
f1_score = 2 * precision * recall / (precision + recall)
negative_precision = tn / (tn + fn)
specificity = tn / (tn + fp)
total_support_value = tp + tn + fp + fn

## 2.3.3 Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt = DecisionTreeClassifier(max_depth = 5)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)

from sklearn.metrics import *
accuracy_score(y_test, y_pred)
confusion_matrix(y_test, y_pred)

## 2.3.4 Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf = RandomForestClassifier(n_estimators = 52, max_depth = 7, criterion = 'entropy', random_state = 2)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

from sklearn.metrics import *
accuracy_score(y_test, y_pred)
confusion_matrix(y_test, y_pred)

## 2.3.5 Grid Search CV
param_grid = {
    'n_estimators' : [100,200,300],
    'max_depth' : [None,5,10,15],
    'min_samples_split' : [2,5,10],
    'min_samples_leaf' : [1,2,4],
    'criterion' : ['gini','entropy']
}

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, cv = 5, scoring = 'accuracy')
grid_search.fit(X_train, y_train)

grid_search.best_estimator_
grid_search.score(X,y)
grid_search.best_score_
grid_search.best_params_















#### ML MODELS & TECHNIQUES

#### Regression Types:
######## 1) Linear Regression
######## 2) Ridge Regression
######## 3) Lasso Regression
######## 4) 

#### Classification Types:
######## 1) Logistic Regression
######## 2) Decision Tree
######## 3) Random Forest
######## 4) K-Nearest Neighbours
######## 5) Naive Bayes



#### 1) Linear Regression
######## 1) Bias-Variance Trade-Off
############ 1) Regularization - Ridge Regression
############ 2) Regularization - Lasso Regression
############ 3) Regularization - Elastic Net Regression

#### 2) Multiple Linear Regression

#### 3) Gradient Descent
######## 2.1) Batch Gradient Descent
######## 2.2) Stochastic Gradient Descent
######## 2.3) Mini Batch Gradient Descent

#### 4) Polynomial Linear Regression
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, random_state = 42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

from sklearn.metrics import *
print(f"R2 Score: {r2_score(y_test, y_pred)}")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_test, y_pred))}")
sns.regplot(x = y_pred, y = y_test, line_kws = {'color':'red'})




#### 6) Logistic Regression
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

from sklearn.metrics import classification_report, confusion_matrix
print(f"Classification Report: {classification_report(y_test, y_pred)}")
print(f"Confusion Matrix: {confusion_matrix(y_test, y_pred)}")






#### 7) Decision Tree Classification
######## Maximum (Entropy Reduction) OR (Info Gain) is required
######## General Formula for Entropy at a node = H = P1*log(P1) + P2*log(P2) ------> Max value 1 at P1=P2=0.5
######## where P1, P2 are probabilities of event 1, 2 at the node
######## Info_Gain = H_parent - w_avg(H_children)

######## Gini = Measure of impurity (alternative of Entropy H)
######## Gini = 1 - [P1^2 + P2^2] ------> Max value 0.5 at P1=P2=0.5 [Computationally easier than Entropy calculation]
######## Info_Gain = Gini_parent - w_avg(Gini_children)

#### 8) Decision Tree Regression
######## Info_Gain = Variance_parent - w_avg(Variance_children)

#### 9) Random Forest Classification














###############################################################################################################
#### sklearn

######## 1) preprocessing
############ LabelEncoder class
############ StandardScaler class

######## 2) linear_model
############ LinearRegression class

######## 3) model_selection
############ train_test_split class
############ cross_val_score class

######## 4) metrics
############ r2_score
############ f1_score
############ mean_absolute_error
############ mean_squared_error

######## 5) ensemble
############ RandomForestRegressor class
###############################################################################################################







###############################################################################################################
#### 2. Statistics
###############################################################################################################

# IMPORT LIBRARY
import statistics as st                                                               #for descriptive statistics - in built in python
from scipy import stats                                                               #for descriptive & inferential statistics

# arr1, arr2 are lists of data

st.mean(arr1)       
st.median(arr1)     
st.mode(arr1)       
st.stdev(arr1)                                                                        #sample Standard Deviation
st.pstdev(arr1)                                                                       #population Standard Deviation
st.variance(arr1)                                                                     #sample Variance
st.pvariance(arr1)                                                                    #population Variance
      
st.covariance(arr1, list_2)     
st.correlation(arr1, list_2)        
st.linear_regression(arr1, list_2)      
      

st.geometric_mean(arr1)
st.harmonic_mean(arr1)


# create random Sample of 500 datapoints from population
df_sample = df.sample(500, random_state=0)














###############################################################################################################
#### Z-Test, Z Test
###############################################################################################################

z_stat = (st.mean(arr1) - pop_mean) / (pop_std/math.sqrt(N))                            #N = population size
p_val = stats.norm.cdf(z_stat)                                                          #probability to the left of z_stat

# OR

from statsmodels.stats.weightstats import ztest                                         #one sampled, z test, z-test

z_stat, p_val = ztest(x1=arr1, value = pop_mean, alternative='two-sided')               #for H1: arr1.mean != pop_mean
z_stat, p_val = ztest(x1=arr1, value = pop_mean, alternative='larger')                  #for H1: arr1.mean > pop_mean




z_stat, p_val = ztest(x1=arr1,x2=arr2, value=pop_mean_diff, alternative='larger')       #two sample difference, z test, z-test

# OR

z_stat = ((mean(arr1)-mean(arr2)) - pop_mean_diff)/(s1_std**2/n1 + s2_std**2/n2)        #N = number of sample data-points
 





###############################################################################################################
#### Proportion Z-Test, Z Test
###############################################################################################################


from statsmodels.stats.proportion import proportions_ztest                              #z-test for proportion

z_stat, p_val = proportions_ztest(count=arr1_count, nobs=total_pop, value=0.50, alternative="two-sided")

 


 


###############################################################################################################
#### T-Test, T Test
###############################################################################################################

####one sampled T-Test

t_stat = (st.mean(arr1) - pop_mean) / (sample_std/math.sqrt(n-1))                     #n = number of sample data-points
p_val = stats.t.cdf(t_stat, df=(n-1))                                                 #area to the left of t_stat
p_val = stats.t.sf(t_stat, df=(n-1))                                                  #area to the left of t_stat - survival fqn (more accurate)

# OR

from scipy.stats import ttest_1samp
t_stat, p_val = ttest_1samp(a=arr1, pop_mean)



####two independent sampled T-Test
t_stat = (s1_mean - s2_mean) / (s1_std**2/n1 + s2_std**2/n2)                          #n1, n2 = number of sample data-points in s1, s2

# OR

from scipy.stats import ttest_ind
t_stat, p_val = ttest_ind(arr1, arr2)



####Paired (related) t-test:
from scipy.stats import ttest_rel

 


 


 
###############################################################################################################
#### Chi2-Test, Chi2 Test
###############################################################################################################
#
from scipy.stats import chi2

chi2_stat = sum((obs_arr - exp_arr)**2 / exp_arr)                                     #(observed - expected) / expected
p_val = chi2.cdf(chi2_stat, df)                                                       #df = n-1, p_val is prob to the left of chi2_stat

# OR

from scipy.stats import chi2_contingency
contingency_table = pd.crosstab(df['obs_arr1'], df['obs_arr2'])                       #two observed categorical variables
chi2_stat, p_val, df, exp_frequencies = chi2_contingency(contingency_table)

# OR

from scipy.stats import chisquare
chi2_stat, p_val = chisquare(f_obs = obs_arr, f_exp = exp_arr)
 
 
 
 
 
 
 
###############################################################################################################
#### F-Test, F Test (ANOVA)
###############################################################################################################

f_stat = max_var/min_var                                                              #ratio of two chi-square fqn, variance is chi-square
p_val = stats.f.cdf(f_stat, df1, df2)                                                 #p_val to the left of f_stat, df1-numerator, df2-denominator

# OR

from scipy.stats import f_oneway                                                      #one way anova
f_stat, p_val = f_oneway(arr1, arr2, arr3)                                            #one way anova


















###############################################################################################################
#### 3. Machine Learning - Model Building
###############################################################################################################

# IMPORT LIBRARY
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import *


# x-y SPLIT
x = df.drop(columns = [out_col])
y = df[out_col]


# TRAIN-TEST SPLIT
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size= 0.7, random_state = 42)


# TRAINING
my_model = LinearRegression()
my_model.fit(x_train,y_train)


# TESTING
y_pred = my_model.predict(x_test)


# EVALUATION
r2_score(y_test,y_pred)                                            #r-squared value
mean_absolute_error(y_test,y_pred)
mean_squared_error(y_test,y_pred)
np.sqrt(mse)                                                       #root-mean-squared error (rmse)
sns.regplot(x = y_pred, y =y_test,line_kws={'color':'red'})


# 10-different models for same data
r_sq = []
rmse = []
for i in range(10):
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size= 0.7)
    my_model = LinearRegression()
    my_model.fit(x_train,y_train)
    y_pred = my_model.predict(x_test)
    r2_score(y_test,y_pred)
    mean_absolute_error(y_test,y_pred)
    mse = mean_squared_error(y_test,y_pred)
    rmse.append(np.sqrt(mse))

print(r_sq)
print(rmse)












###############################################################################################################
#### numpy - Everything
###############################################################################################################

import numpy as np
np.set_printoption(precision=2, supress=True)                   #2 decimal places, without scientific notation

#initializing np array
np.array([1,2,3],dtype=float)                                   #creating a numpy array of float dtype
np.arange(11)                                                   #[0 1 2 3 4 5 6 7 8 9 10]
np.arange(1,11)                                                 #[1 2 3 4 5 6 7 8 9 10]
np.arange(1,11,2)                                               #points bw 1 & 10 with equal distance=2
np.linspace(1,11,10)                                            #10 equi-distant points from 1 to 10(=11-1)

np.ones((rows, cols))
np.zeros((rows, cols))
np.full((rows, cols), n)                                        #an array of rows x columns filled with n
np.identity(3)                                                  #identity Matrix of 3 x 3
np.eye(3,4)                                                     #identity Matrix of rectangular array
np.eye(3,4,k=1)                                                 #diag(1) shifted right Matrix
np.eye(4,3,k=-1)                                                #diag(1) shifted left Matrix

np.random.seed(42)                                              #set randomness to reproduce
np.random.random((rows, cols))                                  #rows x cols array of random numbers bw 0 and 1
np.random.rand(rows, cols)                                      #rows x cols array of random numbers bw 0 and 1
np.random.randn(rows, cols)                                     #rows x cols array of standard normal distribution
np.random.randint(start, end, n).reshape(rows,cols)             #n random numbers bw start & end reshaped to rows x cols
np.random.shuffle(a1)                                           #shuffle the position of items in array
np.random.choice(a1,3)                                          #choose 3 items randomly from a1 with replacement
np.random.choice(a1,3,replace=False)                            #choose 3 items randomly from a1 without replacement

a1.resize(rows, cols)                                           #changes the shape in original array.
a1.reshape(rows, cols)                                          #orig a1 is not affected.
a1.reshape(4,-1)                                                #reshape a 1-d a1 to 4 rows & possible no. of cols.
a1.reshape(-1,3)                                                #reshape a 1-d a1 to possible no. of rows & 3 cols.
a1.reshape(-1)                                                  #reshape any-dimension a1 1-d (or Flatten a1).

#np attributes
a1.ndim                                                         #returns number of dimensions [3 here]
a1.shape                                                        #returns shape of a [(2,3,4) here]
a1.size                                                         #total number of elements in an array
a1.itemsize                                                     #size of each elements in an array
a1.dtype                                                        #data type of each elements in an array

#Fancy indexing
a1[[0,2,3]]                                                     #return rows at index 0,2 and 3
a1[:,[0,2,3]]                                                   #return cols at index 0,2 and 3

#Boolean indexing
a1[a1>50]                                                       #all elements of a1 which are > 50
a1[(a1>50) & (a1%2==0)]                                         #all even elements of a1 which are > 50
a1[~(a1%7==0)]                                                  #all elements of a1 which are NOT divisible by 7

#changing data type
a.astype(np.int8)                                               #changing data type to int8

#scalar operations
a1 * 2
a1 + 5
a1 // 3
a1 ** 2
a1 > 5
a1 == 4

#vector (two arrays of same shape) operations
a1 + a2
a1 - a2
a1 * a2         #item-wise (Hadamard) multiplication
a1 / a2
a1 // a2
a1 ** a2
a1 % a2
a1 > a2
a1 == a2

#vector operation functions (element-wise operation)
np.add(a1, a2)
np.subtract(a1, a2)
np.multiply(a1, a2)
np.divide(a1, a2)
np.floor_divide(a1, a2)
np.power(a1, a2)
np.mod(a1, a2)

#numpy functions (apply operation on every element)
np.max(a1, axis=0)                                              #take all rows, find max -->> i.e. column-wise max
np.min(a1, axis=1)                                              #take all cols, find min -->> i.e. row-wise min
np.sum(a1, axis=0)                                              #take all rows, find sum -->> i.e. column-wise sum
np.prod(a1, axis=1)                                             #take all cols, find product -->> i.e. row-wise product
np.mean(a1, axis=0)
np.median(a1, axis=1)
np.std(a1, axis=1)
np.var(a1, axis=1)

np.sqrt(a1)
np.pi
np.sin(a1)
np.cos(a1)
np.tan(a1)
np.log(a1)
np.exp(a1)

np.round(a1,3)                                                  #round to 3 decimal places
np.ceil(a1)                                                     #round to lower integers
np.floor(a1)                                                    #round to higher integers
np.rint(a1)                                                     #round to nearest integers

np.concatenate((a1,a2))                                         #concat two arrays one after another
np.concatenate((a1,a2), axis=0)                                 #hstack
np.concatenate((a1,a2), axis=1)                                 #vstack
np.hstack((a1,a2))                                              #concatenate horizontally
np.vstack((a1,a2))                                              #concatenate vertically
np.column_stack((a1, a2))                                       #Transposed of vstack result

np.hsplit(a1,2)                                                 #split horizontally in 2 equal parts
np.vsplit(a1,3)                                                 #split vertically in 3 equal parts
np.hsplit(a1,np.array([3]))                                     #split into one part of 3 cols and another part of remaining cols

a1.T                                                            #Transpose numpy array without changing the original array
np.transpose(a1)                                                #Transpose numpy array without changing the original array
a1.ravel()                                                      #converts any dimensional array into 1-d
a1.flatten()                                                    #Flatten a1 to 1-d
a1.reshape(-1)                                                  #reshape a1 to 1-d (or Flatten a1).

np.diag(a1)                                                     #diagonal of a Matrix
np.fliplr(a1)                                                   #flipping an a1ay from left to right
np.rot90(a1)                                                    #rotating an array by 90 degrees anticlock-wise

#Matrices functions
np.dot(a1,a2)                                                   #dot product
np.matmul(a1,a2)                                                #dot product
a1 @ a2                                                         #dot product
np.cross(a1, a2)                                                #cross product
np.inner(a1, a2)                                                #inner product of a1 & a2, returns a scalar
np.outer(a1, a2)                                                #outer product of a1 & a2, returns an array

np.linalg.norm(a1)                                              #magnitude of a1
np.linalg.det(a1)                                               #determinant
np.linalg.inv(a1)                                               #inverse
np.linalg.matrix_rank(a1)                                       #rank
np.linalg.eig(a1)                                               #(eig_val, eig_vector)

#Advance Functions
sorted(a1)                                                      #returns a LIST of sorted arr4 without saving to orig arr4
np.sort(a1)                                                     #sort a1, not permanent change [faster than sorted(list)]
np.append(a1, n)                                                #append item n at the end
np.append(a1, n, axis=1)                                        #append a col, each row=n
np.unique(a1)                                                   #unique items from a1
np.expanddims(a1)                                               #converts a 1-d array into 2-d
np.where(a1>50)                                                 #returns index of items where condition meets
np.where(a1>50,n,a1)                                            #replace with n where condition meets (condition,ifTRUE,else)
np.isin(a1,[x,y,z])                                             #checks if x,y,z exist in a1
np.in1d(a1, 100)                                                #checks if 100 exist in 1-d a1
np.clip(a1, a_min=25, a_max=75)                                 #keeps all values of a1 bw 25 and 75
np.equal(a1, a2)                                                #item-wise comparison, returns an array of True/False
np.array_equal(a1, a2)                                          #if whole a1 = whole a2, returns True/False

np.argmax(a1)                                                   #index of maximum
np.argmax(a1,axis=0)                                            #index of maximum col wise, all rows
np.argmin(a1)                                                   #index of minimum
np.argmin(a1,axis=1)                                            #index of minimum row wise, all cols
np.cumsum(a1)                                                   #cumulative sum
np.cumsum(a1,axis=0)                                            #cumulative sum col wise, all rows
np.cumprod(a1)                                                  #cumulative product
np.cumprod(a1,axis=0)                                           #cumulative product col wise, all rows
np.flip(a1)                                                     #reverses 1-d array, 2-array on both dimensions
np.flip(a1,axis=0)                                              #reverses 2-d array along col, all rows

np.percentile(a1,90)                                            #90th percentile element
np.histogram(a1,bins=[0,10,20,30])                              #frequency count in bins of 10-20, 20-30, ...
np.corrcoef(a1,a2)                                              #pearson correlation coefficient matrix

np.put(a1,[0,3],[100,200])                                      #set index 0 as 100, index 3 as 200 in a1
np.delete(a1, i)                                                #delete element at index i
np.insert(a1, i, n)                                             #insert element n at index i in a1

#Set functions
np.union1d(a1, a2)                                              #union of two 1-d arrays
np.intersect1d(a1, a2)                                          #intersection of two 1-d arrays
np.setdiff1d(a1, a2)                                            #all items of a1 not present in a2
np.setxor1d(a1, a2)                                             #union minus intersection

#Meshgrid
x=np.linspace(-10,9,20)
y=np.linspace(-10,9,20)
xx,yy=np.meshgrid(x,y)                                          #grid of all value combination of x & y


#customised structured array
dt = 









###############################################################################################################
#### pandas - Everything
###############################################################################################################

import pandas as pd

#Series - creating series
pd.Series([1,2,3],index=['a','b','c'],name='abc')                   #pd.Series from a list
pd.Series(my_dict)                                                  #pd.Series from a dictionary
pd.Series(list(my_set))                                             #pd.Series from a set
pd.Series(np_a1,index=labels)                                       #pd.Series from a np.array

sr.drop(2)                                                          #remove row at index 2
sr.append(5)                                                        #append element=5 at the end of sr
sr.reset_index(drop = True)                                         #reset index without making previous index a column
sr.reset_index()                                                    #reset index making previous index a column

#Series to other data structures
list(sr)                                                            #pd.Series to list
tuple(sr)                                                           #pd.Series to tuple
sr.to_dict()                                                        #pd.Series to dictionary
set(sr)                                                             #pd.Series to set

#Series attributes
sr = pd.Series([1,2,3],index=['a','b','c'],name='abc')
sr.size                                                             #sr item counts (inc. NaN)
sr.size - sr.count()                                                #count of missing (NaN) values
sr.dtype
sr.name
sr.is_unique                                                        #True if all items are unique
sr.index
sr.values                                                           #sr values in 1-d np.array

#reading series from csv
sr = pd.read_csv('file_nm',squeeze=True)                            #csv file with only 1 col, squeeze converts csv to pd.Series
sr = pd.read_csv('file_nm',index='col1',squeeze=True)               #csv file with 2 cols, col1=index, col2=values

#Series methods
sr.head(3)
sr.tail()
sr.sample()                                                         #random 1 row
sr.value_counts()                                                   #groupby values & give count
sr.sort_values(ascending=False, inplace=False)                      #sorting series by values
sr.sort_index(ascending=False, inplace=False)                       #sorting series by index

#Series Math methods
sr.count()                                                          #counts non-missing values only
sr.isnull()                                                         #counts missings (NaN) values
sr.size - sr.count()                                                #counts missing (NaN) values
sr.sum()
sr.product()
sr.mean()
sr.median()
sr.mode()
sr.std()
sr.var()
sr.min()
sr.max()
sr.describe()

#Indexing & Slicing
sr[2]                                                               #Series Indexing
sr[2]=100                                                           #set value 100 at index 2
sr[-1]                                                              #works only when index is text datatype
sr[[1,3,6,7]]                                                       #Fancy indexing in pd.Series
sr[[1,3,6,7]]=[100,200,300,400]
sr[5:16]                                                            #Series slicing
sr[-5:]=[1,1,1,1,1]                                                 #set value 1 in last 5 indices

#fetch item using iloc
sr.iloc[2]                                                          #index 2
sr.iloc[0:3]                                                        #index 0 to 2
sr.iloc[[2,3,6]]                                                    #index 2,3,6

#fetch item using loc
sr.loc['index2']                                                    #index 2
sr.loc['index1':'index3']                                           #index 1 to 3(inc.)
sr.loc[['index2','index6']]                                         #index 2,6
sr[::-1]

#Series with python in-built functionality
len(sr)
type(sr)                                                            #shows dtype of sr
dir(sr)                                                             #shows all attributes & methods of series
sorted(sr)                                                          #sorted sr in LIST form
min(sr)
max(sr)
list(sr)                                                            #shows sr in list form
dict(sr)                                                            #shows sr in dictionary form

#other important series methods
sr.astype('int16')                                                  #converts dtype of series.values to int8, saves memory
sr.between(5,10)                                                    #TRUE if value is bw 5 & 10
sr.clip(5,10)                                                       #5 if value <5, 10 if value >10
sr.duplicated()                                                     #TRUE if duplicate
sr.duplicated().sum()                                               #count of duplicates
sr.drop_duplicates()                                                #drop duplicate, keep 1st occurence of each value
sr.drop_duplicates(keep='last')                                     #drop duplicate, keep last occurence of each value
sr.dropna()                                                         #remove NaN
sr.drop(index=[2,3,6])                                              #drop rows with index 2,3,6
sr.fillna(sr.mean())                                                #replace NaN with mean
sr[(sr==4)|(sr==7)|(sr==2)]                                         #TRUE if each value is 4,7 or 2
sr.isin([4,7,2])                                                    #TRUE if each value is in 4,7,2; same as above
sr.apply(lambda x: x.split()[0].upper())                            #apply custom function lambda --> 1st word uppercase from sr.values
sr1 = sr                                                            #creates a view of same sr
sr1 = sr.copy()                                                     #creates a copy of sr

#membership operator
'abc' in sr                                                         #TRUE if 'abc' exists in sr.index
'abc' in sr.values                                                  #TRUE if 'abc' exists in sr.values

#looping
for i in sr: print(i)                                               #prints sr.values one-by-one
for i in sr.index: print(i)                                         #prints sr.index one-by-one

#Arithmetic operators
100 - sr                                                            #broadcasting 100 to the size of sr & subtracting each item

#Relational operators
sr>=5

#Boolean indexing
sr[sr>=5]                                                           #items >=5
sr[sr>=5].size                                                      #count of items >=5x

#plotting graphs using pd
sr.plot()                                                           #line chart with index on x-axis, values on y-axis
sr.plot(kind='bar')                                                 #bar chart with index on x-axis, values on y-axis
sr.plot(kind='pie')                                                 #pie chart with %age of values













# #### sr.insert()                                          #pandas series don't have insert method, so, convert to dataframe first
pd.concat([s[:5], pd.Series([50], index=[5]), s[5:]])             #use concat to insert at index 5 in pandas series


sr + sr2                                               #gives union of both the series














#Pandas DataFrame
#setting display options
pd.set_option('display.max_columns', None)                          #display all columns while printing dataset
pd.set_option('display.max_rows', 5)                                #display only 5 rows while printing dataset
print(df.head().to_string())                                        #print every column for first 5 rows when columns hide normally
print(df.to_string())                                               #print every column for all rows when columns hide normally

#Creating DataFrame
df = pd.DataFrame([[],[],[]], columns =['x','y'])                   #DataFrame from list
df = pd.DataFrame(my_dict)                                          #DataFrame from dict (col name comes from dict.keys)
df = pd.read_csv('my_csv.csv')                                      #read data from csv file into df
df = pd.read_table('my_file.txt')                                   #read data from delimited text file
df = pd.read_excel('my_excel.xlsx', sheet='Sheet1')                 #read data from particular sheet of an excel file
df = pd.read_sql(query, connection_obj)                             #read data from sql database
df = pd.read_json(json_string)                                      #read data from json
df = pd.read_html(url)                                              #read data from web

#Export DataFrame to files
df.values.tolist()                                                  #All DataFrame values to list
df.to_dict()                                                        #DataFrame to a dictionary
df.to_csv('my_csv.csv')                                             #write to a csv file
df.to_excel('my_excel.xlsx')                                        #write to an excel file
df.to_sql('my_table', connection_obj)                               #write to an sql database table
df.to_json('my_json.json')                                          #write to a file in json format

#DataFrame attributes
df.shape                                                            #returns a tuple of size (rows, cols)
df.dtypes                                                           #shows dtypes of all the cols
df.index                                                            #show the index range
df.columns                                                          #shows col names
df.T                                                                #transpose all the data of df
df.values                                                           #DataFrame values in 2-d np.array

#DataFrame Methods - Inspect Data
df.head(3)                                                          #first 3 rows
df.tail(2)                                                          #last 2 rows
df.sample()                                                         #1 random row
df.info()                                                           #col-wise non-null counts, dtypes & memory usage
df.describe()                                                       #numeric col-wise statistical summary
df.describe(include = 'O')                                          #statistical summary for non-numeric col
df.describe(include = 'all')                                        #Statistical summary for all cols
df.value_counts()                                                   #col-wise count of unique values [sr & df both]
df.isnull().sum()                                                   #col-wise count of null values [sr & df both]
df.notnull().sum()                                                  #col-wise count of non-null values [sr & df both]
df.duplicated().sum()                                               #row-wise count of duplicates
df.rename(columns={'old':'new','old2':'new2'},inplace=True)         #rename columns
df.transpose()                                                      #transpose all the data of df
df.nlargest(N, 'col1')                                              #TOP N rows by col1
df.nsmallest(N, 'col1')                                             #BOTTOM N rows by col1

#Mathematical methods
df.min()                                                            #col-wise min
df.min(axis=1)                                                      #row-wise min
df.max()                                                            #col-wise max
df.sum()                                                            #col-wise sum
df.count()                                                          #col-wise count
df.mean()                                                           #col-wise mean
df.median()                                                         #col-wise median
df.std()                                                            #col-wise standard deviation
df.var()                                                            #col-wise variance
df.corr(numeric_only = True)                                        #numerical col-wise corr coef

#fetch cols
df['col1']                                                          #select 1 col as pd.Series
df[['col1']]                                                        #select 1 col as pd.DataFrame
df[['col1','col2']]                                                 #select multiple cols as pd.DataFrame

#fetch rows using iloc(index position)
df.iloc[0]                                                          #row at index 0 as pd.Series
df.iloc[0:1]                                                        #row at index 0 as pd.DataFrame
df.iloc[[0,4,5]]                                                    #Fancy Indexing: rows at index 0,4,5 as pd.DataFrame

#fetch rows using loc(index label), when custom index
df.loc['index1']                                                    #row by index label, same as iloc[0]
df.loc['index1':'index3']                                           #rows from index1 to index3(inc.)
df.loc[['index3','index6','index9']]                                #Fancy indexing

#fetch rows,cols both using iloc
df.iloc[0, 0]                                                       #row index 0, col index 0
df.iloc[0:3,1:5]                                                    #row 0 to 2 & col 1 to 4
df.iloc[[2,3,6],[5,2]]                                              #Fancy indexing: row 2,3,6 & col 5,2

#fetch rows,cols both using loc
df.loc['index1', 'col1']                                            #select an element by label
df.loc['index1':'index3', 'col1':'col4']                            #row 1 to 3(inc.), col 1 to 4(inc.)
df.loc[['index6','index8'],['col1','col3']]                         #Fancy indexing: row 6,8 & col 1,3

#Filtering rows
df['col1'] > 5                                                      #True if col1.value > 5
df[df['col1'] > 5]                                                  #rows where condition is true
df[(df['col1'] > 5) & (df['col2'] < 10)]                            #rows where both the conditions meet
df[df['col1'].isin(['Alice', 'David'])]                             #True if col1.value is either 'Alice' or 'David'

df = df.query('col1 > 2 and col2 != "apple"')                       #filter using a query string
a, b = 2, 'apple'
df = df.query('col1 > @a and col2 == @b')                           #filter using a query string

#Filtering index or cols
df.filter(like = 'abc')                                             #filter index contaning abc
df.filter(like = 'abc', axis = 1)                                   #filter cols containing abc in their name
df.filter(regex = '^N', axis = 1)                                   #selects cols starting with 'N'

#col (pd.Series) attributes
df['col1'].dtype                                                    #col1 dtype
df['col1'].hasnans                                                  #True if col1 has NaNsr.size                                                             
df['col1'].size                                                     #col1 item counts (inc. NaN)

#col methods
df['col1'].value_counts()                                           #col1 (in pd.Series form) unique value count [sr & df both]
df['col1'].unique()                                                 #col1 unique values (shows NaN)
df['col1'].nunique()                                                #col1 unique value count (doesn't show NaN)
df['col1'].tolist()                                                 #col1 to list
df['col1'].astype(int)                                              #change dtype to integer
df['col1'].astype(float)                                            #change dtype to float
df['col1'].astype('category')                                       #change dtype to category
pd.to_numeric(df['col1'], errors='coerce')                          #change dtype to numbers, space becomes NaN
df['col1'].nlargest(N)                                              #TOP N values from col1
df['col1'].nsmallest(N)                                             #BOTTOM N values from col1

#sort df
df.sort_values('col1')                                              #sort by col1 [sr & df both]
df.sort_values('col1', na_position='first')                         #sort by col1 with NaN showing on top
df.sort_values('col1', ascending = False)                           #sort by col1 descending
df.sort_values(['col1','col2'], ascending = [True, False])          #sort multiple columns

#rank method
df['col1'].rank()                                                   #rank based on col1 (min val is rank 1)
df['col1'].rank(ascending=False)                                    #rank based on col1 (max var is rank 1)

#index operations
df.sort_index()                                                     #sort by index [sr & df both]
df.sort_index(ascending=False)                                      #sort by index [sr & df both]
df.set_index('col2')                                                #set col2 as index
df.reset_index(drop = True)                                         #reset index making previous index a column

#rename in df
df.rename(columns={'col1':'c1','col2':'c2'})                        #rename cols
df.rename(index={'index1':'i1','index2':'i2'})                      #rename custom index

#fill NaN values
df.fillna(0)                                                        #fill all NaN values with 0
df['col1'].fillna('abc')                                            #fill NaN with 'abc'
df['col1'].fillna(method='ffill')                                   #forward fill: NaN replaced with value above
df['col1'].fillna(method='bfill')                                   #backward fill: NaN replaced with value below

#remove NaN values
df.dropna()                                                         #drop rows having any NaN
df.dropna(how='all')                                                #drop rows with all cols NaN
df.dropna(subset=['col1','col3'])                                   #drop rows where col1,col3 have NaN
df.dropna(axis=0)                                                   #drop all rows with null in any col
df.dropna(axis=1)                                                   #drop all cols with null in any row
df.dropna(thresh=2)                                                 #drop all the rows with values above 2

#remove duplicate rows
df.drop_duplicates()                                                #drops duplicate rows
df.drop_duplicates(keep='last')                                     #drops duplicate rows & keep last instance
df.drop_duplicates(subset=['col2','col3'])                          #drops duplicate based on col2,col3

#remove rows, cols: Fancy indexing
df.drop(index=[2,3,4])                                              #remove rows with index 2,3,4
df.drop(['col1','col3'])                                            #remove col1, col3

#groupby col1
grp = df.groupby('col1')                                            #group by col1; grp is pandas groupby object
for a,b in grp: print(a, b)                                         #a is group name string, b is DataFrame containing all rows of that group

grp.size()                                                          #count of rows
grp.sum()                                                           #col-wise sum of all numeric cols
grp.min()                                                           #col-wise minimum of all cols
grp.max()                                                           #col-wise maximum of all cols
grp.count()                                                         #col-wise count of all cols

grp.sum()['col2']                                                   #sum of all cols, select col2
grp['col2'].sum()                                                   #sum of col2
grp['col2'].min()                                                   #minimum of col2
grp['col2'].max()                                                   #maximum of col2
grp['col2'].count()                                                 #count of col2
grp['col2'].mean()                                                  #mean of col2
grp['col2'].std()                                                   #standard deviation of col2
grp['col2'].var()                                                   #variance of col2

grp.agg(['min','max','mean','sum'])                                 #min,max,mean,sum of all numeric cols
grp.agg(                                                            #customize aggregation on diff numeric cols
            {
                'col1':['sum','min','max'],
                'col2':['sum','mean'],
                'col3':['min','max'],
                'col4':'min',
                'col5':'sum'
            }
        )

grp.first()                                                         #fetch 1st row of each group
grp.last()                                                          #fetch last row of each group
grp.nth(7)                                                          #fetch 7th row of each group

grp.get_group('val1')                                               #same as df[df['col1']=='val1']; get_group is faster
grp.groups                                                          #a dict with (groups as keys) & (list of indices in this grp) as values
grp.describe()                                                      #group-wise describe
grp.sample()                                                        #group-wise 1 random row
grp.sample(2)                                                       #group-wise 2 random rows
grp.nunique()                                                       #group-wise & col-wise unique rows count [PIVOT TABLE]

#groupby col1,col2
grp=df.groupby(['col1','col2'])

#Concatenate Data or stacking data(df.append has been discontinued)
pd.concat([df1,df2])                                                #concatenate data vertically / append rows
pd.concat([df1,df2],ignore_index=True)                              #create new index, remove previous index
df=pd.concat([df1,df2],keys=['d1','d2'])                            #multiple index, mainindex=d1,d2 & subindex=orig index
df.loc[('d1',2)]                                                    #indexing--> mainindex=d1, subindex=2
pd.concat([df1,df2],axis=0)                                         #concatenate data vertically / append rows
pd.concat([df1,df2],axis=1)                                         #concatenate data horizontally / add colums

#Merge Data (SQL joins)
pd.merge(df1,df2,how='inner',on='col3')                             #SQL INNER JOIN on col3
pd.merge(df1,df2,how='inner',left_on='col3',right_on='col1')        #common col has diff name in both tables/df
pd.merge(df1,df2,how='outer',on=['col3','col5'])                    #SQL OUTER JOIN on col3 and col5
pd.merge(df1,df2,how='left',on='col5')                              #SQL LEFT JOIN on col5

#Join Data
df1.join(df2)                                                       #SQL INNER JOIN based on row_index
df1.join(df2,how='left')                                            #SQL LEFT JOIN based on row_index

#MultiIndex Series
mi=pd.MultiIndex.from_product([['i1','i2'],[3,4]])                  #Cartisian prod of 2 indices: index i1 has 2 vals 1,2; i2 has 2 vals 1,2
mi=pd.MultiIndex.from_tuples([('i1',3),('i1',4),('i2',3),('i2',4)]) #multi index created manually
mi.levels[1]                                                        #showing vals in index level 1
sr=pd.Series([1,2,3,4,5,6,7,8],index=mi)                            #Creating Series with multi index
sr.unstack()                                                        #last index converted to col-index
sr.stack()                                                          #col-index converted to row index

#MultiIndex DataFrame
data=[[1,2],[5,6],[7,8],[9,0]]
df=pd.DataFrame(data,index=mi,columns=['col1','col2'])              #creating df with multi index in rows
df=pd.DataFrame(data,index=['i1','i2'],columns=mi)                  #creating df with multi index in cols
df.sort_index(level=1,ascending=False)                              #sort index 1 descending 
df.sort_index(ascending=[False,True])                               #sort index 0 descending, index 1 ascending
df.transpose()
df.swaplevel(axis=1)                                                #col index swap with each other

#Pivot Table
df.pivot_table(index='col1',columns='col2',values='col3')           #pivot table, col3 will be avg/mean by default
df.pivot_table(index='col1',columns='col2',aggfunc='std')           #analyse all numeric cols
df.pivot_table(index='col1',columns='col2',
                aggfunc='sum',margins=True)                         #also shows row-wise & col-wise totals
df.pivot_table(index='col1',columns='col2',
                values='col3',aggfunc='std')                        #pivot table, col3 will be avg/mean by default
df.pivot_table(index=['col1','col2'],
                columns=['col3','col4'],values='col5')              #analyse all numeric cols
df.pivot_table(index=['col1','col2'],
                columns=['col3','col4'],
                aggfunc={'col5':'sum','col6':'min'}                 #diff cols, diff aggregations

#vectorized String operations using pandas
df['col1'].str.upper()                                              #all upper case
df['col1'].str.lower()                                              #all lower case
df['col1'].str.capitalize()                                         #1st letter capital in each item
df['col1'].str.title()                                              #1st letter of each word in caps
df['col1'].str.len()                                                #length of each item
df['col1'].str.len().max()                                          #max length out of all items
df['col1'].str[0:6:2]                                               #slicing

df['col1'].str.strip()                                              #removes leading & trailing spaces
df['col1'].str.split()                                              #split items at every space
df['col1'].str.split(',')                                           #split items at every comma
df['col1'].str.split(n=1,expand=True)                               #split once at first space only, make two new cols
df['col1'].str.split(n=2)                                           #split twice at first 2 spaces

df['col1'].str.replace('abc','xyz')                                 #replace abc with xyz
df['col1'].str.startswith('a')                                      #True if item starts with 'a'
df['col1'].str.endswith('a')                                        #True if item ends with 'a'
df['col1'].str.isdigit()                                            #True if item is numeric
df['col1'].str.contains('abc')                                      #True if item contains abc
df['col1'].str.contains('^[^aeiouAEIOU].+[aeiouAEIOU]$')            #^ means 1st char, . means any no of chars, $ means last char
                                                                    #^ starts wit consonant (NOT vowel), $ ends with vowel

#Pandas Timestamp
pd.Timestamp.now()
pd.Timestamp.now().year
pd.to_datetime(df['date'])                                          #object to Datetime
pd.to_datetime(df['date'], errors='coerce')                         #object to Datetime, ignore errors
pd.to_datetime(df['date'], format='%d-%m-%Y')                       #object(dd-mm-YYYY) to Datetime(YYYY-mm-dd)
df['Date'].dt.year                                                  #year
df['Date'].dt.month                                                 #month
df['Date'].dt.day                                                   #day
df['Date'].dt.hour                                                  #hour
df['Date'].dt.minute                                                #minute
df['Date'].dt.second                                                #second
df['Date'].dt.month_name()                                          #month name
df['Date'].dt.day_name()                                            #day name

df['Date'].dt.is_month_start()                                      #True if month start date
df['Date'].dt.is_month_end()                                        #True if month end date
df['Date'].dt.is_quarter_start()                                    #True if month start date
df['Date'].dt.is_quarter_end()                                      #True if month end date

#Datetime Index (contains items with dtype pd.Timestamp)
import Datetime as dt
dt_index=pd.DatetimeIndex(dt.datetime(2025,1,1),
                    dt.datetime(2024,1,1),
                    dt.datetime(2023,1,1))                          #using python Datetime module [slower]
dt_index=pd.DatetimeIndex(pd.Timestamp(2025,1,1),
                    dt.Timestamp(2024,1,1),
                    dt.Timestamp(2023,1,1))                         #using pandas Timestamp [faster]
pd.Series([1,2,3],index=dt_index)                                   #create series with date index

st_dt = pd.Timestamp(2025,1,1)
end_dt= pd.Timestamp(2027,12,31)
pd.date_range(start=st_dt, end=end_dt, freq='D')                    #Datetime index with dates ranging bw st_dt & end_dt daily
pd.date_range(start=st_dt, end=end_dt, freq='2D')                   #alternate dates index
pd.date_range(start=st_dt, end=end_dt, freq='B')                    #Business dates index
pd.date_range(start=st_dt, end=end_dt, freq='W')                    #weekly dates index
pd.date_range(start=st_dt, end=end_dt, freq='W-THU')                #weekly Thursday dates index
pd.date_range(start=st_dt, end=end_dt, freq='H')                    #Hourly Timestamp index
pd.date_range(start=st_dt, end=end_dt, freq='M')                    #Month end dates index
pd.date_range(start=st_dt, end=end_dt, freq='MS')                   #Month start dates index
pd.date_range(start=st_dt, end=end_dt, freq='A')                    #Annual end dates index (31-Dec)
pd.date_range(start=st_dt, periods=25, freq='D')                    #Datetime index with 25 dates from st_dt daily
pd.date_range(start=st_dt, periods=25, freq='H')                    #Datetime index with 25 hours from st_dt hourly
pd.date_range(start=st_dt, periods=25, freq='M')                    #Datetime index with 25 months from st_dt monthly

# pandas plot - sr Plot Visualization
sr.plot(kind='line')
sr.plot(kind='bar')
sr.plot(kind='barh')
sr.plot(kind='hist')
sr.plot(kind='box')
sr.plot(kind='kde')
sr.plot(kind='area')
sr.plot(kind='pie')
sr.plot(kind='scatter',x='col1',y='col2')

# pandas plot - df Plot Visualization
df.plot(kind='scatter',
        x='col1',
        y='col2',
        title='title_1',
        marker='+',
        figsize=(12,8),
        s='col3',
        c='col4',
        cmap='virdis')                                              #c:color as per categorical col4, s:size as per numeric col3
df.plot(kind='line',x='date_col')                                   #plots line trend for all possible combinations in one plot
df.plot(kind='line',x='date_col',subplots=True)                     #plots line trend for all possible combinations in diff subplots
df.groupby('col1')['col2'].mean().plot(kind='bar')                  #col1 categorical, col2 numeric, clustered bar chart automatically made
df.plot(kind='bar',stacked=True)                                    #col1 categorical, col2 numeric, clustered bar chart automatically made
df.plot(kind='hist',bins=20)                                        #20 bins
df['col1'].plot(kind='pie',
                labels=df['col2'].values,
                autopct='%.1f%%',
                explode=[0.1,0,0...])                               #as many values in explode as the number of categories in col2
df['col1','col2','col3'].plot(kind='pie',
                                subplots=True,
                                figsize=(15,8))                     #multiple pie charts on col1, col2, col3









np.array_split(df, 2)                                             #split df into 2 np arrays of almost equal rows
np.array_split(df, 2, axis=0)                                     #split df into 2 np arrays of almost equal rows
np.array_split(df, 2, axis=1)                                     #split df into 2 np arrays of almost equal columns

df.transform(lambda x: x+10)                                      #transform data column-wise



















###############################################################################################################
#### matplotlib.pyplot - Everything
###############################################################################################################

#univariate     (1-axis)    ::  countplot,histogram,box,pie
#bivariate      (2-axes)    ::  bar,scatter,line,pie
#multivariate   (>1-axes)   ::  heatmap,pairplot

#relation plots             ::  scatter,line
#distribution plots         ::  histogram,kde plot,pie chart,countplot
#categorical plots          ::  barplot,countplot,box plot,violin plot

import matplotlib.pyplot as plt

##CampusX
#matplotlib styles
plt.style.available                                                 #shows available styles in plt
plt.style.use('classic')                                            #use style in plt

#x,y,z are different cols of df
#Line Plot - Bivariate (numeric-datetime)
plt.figure(figsize=(15,7))
plt.plot(x,y,color='#199274',
            linestyle='dashdot',
            linewidth=2,
            marker='o',
            markersize=10,
            label='abc')
plt.legend()
plt.ylim(0,500)
plt.xlim(0,20)
plt.grid()
plt.title('title_1')
plt.show()

#Scatter Plot - Bivariate (numeric-numeric)
plt.figure(figsize=(15,7))
plt.scatter(x,y,
            color='#199274',
            marker='o',
            markersize=10,
            )
plt.xlabel('x')
plt.ylabel('y')
plt.title('title_1')
plt.show()

#Scatter Plot with c[hue in sns]
plt.figure(figsize=(15,7))
plt.scatter(x,y,
            s=numeric_col,                                          #size of the bubble based on numeric_col
            c=categorical_col,
            cmap='jet',
            alpha=0.6,                                              #transparency; 0=Transparent; 1=Opaque
            marker='o',
            markersize=10)
plt.xlabel('x')
plt.ylabel('y')
plt.text(x1,y1,'p1')                                                #name the point 'p1' at x=x1,y=y1
plt.text(x2,y2,'p2',fontdict={'size':12,'color':'blue'})            #name the point 'p2' at x=x2,y=y2
plt.axhline(5,color='red')                                          #horizontal red line at y=5
plt.axvline(10,color='green')                                       #vertical green line at x=10
plt.title('title_1')
plt.show()

#Bar/Col chart - Bivariate (numeric-categorical)
plt.figure(figsize=(15,7))
plt.bar(x,y,color='#199274',width=0.2)
plt.xlabel('a')
plt.ylabel('count of a')
plt.xticks(rotation=75)
plt.title('title_1')
plt.show()

#Stacked Bar/Col chart - Bivariate (numeric-categorical)
plt.figure(figsize=(15,7))
plt.bar(x,y1,label='y1')
plt.bar(x,y2,bottom=y1,label='y2')
plt.bar(x,y3,bottom=y1+y2,label='y3')
plt.legend()
plt.title('title_1')
plt.show()

#Clustered Bar/Col chart - Bivariate (numeric-categorical)
#done be shifting x-axis (jugaad)

#Histogram - Univariate (numeric only) - Frequency count in each bin
plt.figure(figsize=(15,7))
plt.hist(x,bins=[0,10,20,30,40,50,60],log=True)                     #log for logarithmic scale in case of uneven distribution
plt.title('title_1')
plt.show()

#Pie chart - Univariate/Bivariate (numeric/categorical)
#Univariate (categorical) - count of each category
#Bivariate (categorical-numeric) - revenue sum based on each category
#Univariate (numeric) - sum proportion of self col
#Bivariate (numeric-numeric) - sum proportion of one numeric col based on other numeric col
plt.figure(figsize=(15,7))
plt.pie(data=x,
        labels=y,
        autopct='%0.1f%%',
        colors=[c1,c2...],
        explode=[0.1,0,0,...],
        shadow=True)                                                #explode is to cut out a slice, autopct is to show %age
plt.title('title_1')
plt.show()

#save chart in png format
plt.savefig('sample.png')                                           #don't use plt.show() before saving

#Scatter Plot - for comparison with OOP below
plt.figure(figsize=(15,7))
plt.scatter(x,y,color='red',marker='+',markersize=10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('title_1')
plt.show()

#Scatter Plot with Object Oriented Programming (OOP) - as compared with non-OOP above
fig,ax=plt.subplots(figsize=(15,7))
ax.scatter(x,y,color='red',marker='+')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title_1')
fig.show()

#Multiple (2) subplots with Object Oriented Programming OOP
fig,ax = plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(15,6))   #sharex is to use single x-axis in 2 charts up & down
ax[0].scatter(x,y,color='red')
ax[0].set_title('x vs. y')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y']

ax[1].scatter(x,z)
ax[1].set_title('x vs. z')
ax[1].set_xlabel('x')
ax[1].set_ylabel('z']
fig.show()

#Multiple (2x2) subplots with Object Oriented Programming OOP
fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(15,6))
ax[0,0].scatter(x,y,color='red')
ax[0,1].scatter(x,z,color='green')
ax[1,0].hist(x)
ax[1,1].hist(z)
fig.show()

#Multiple (2x2) subplots with Object Oriented Programming OOP - another way
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.scatter(x,y,color='red')
ax2 = fig.add_subplot(2,2,2)
ax2.scatter(x,z,color='green')
ax3 = fig.add_subplot(2,2,3)
ax3.hist(x)
ax4 = fig.add_subplot(2,2,4)
ax4.hist(z)
fig.show()

#3-D scatter plot with Object Oriented Programming OOP
fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(x,y,z)
ax.set_title('title_1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
fig.show()

#3-D line plot with Object Oriented Programming OOP
fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(x,y,z,s=[100,100,100,...])                             #s=size of marker for each point, ... represent as many scatter points in data
ax.plot3D(x,y,z,color='red')                                        #line to connect the points
fig.show()

#3-D surface plot with OOP
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
xx,yy = np.meshgrid(x,y)
z = xx**2 + yy**2

fig = plt.figure(figsize=(12,8))
ax = plt.subplot(projection='3d')
p = ax.plot_surface(xx,yy,z,cmap='virdis')
fig.colorbar(p)
fig.show()

#Contour plot (lines only) with OOP
fig = plt.figure(figsize=(12,8))
ax = plt.subplot()
p = ax.contour(xx,yy,z,cmap='virdis')
fig.colorbar(p)
fig.show()

#Contour plot (filled with colors) with OOP
fig = plt.figure(figsize=(12,8))
ax = plt.subplot()
p = ax.contourf(xx,yy,z,cmap='virdis')
fig.colorbar(p)
fig.show()

#Heatmap
grid = df.pivot_table(index='col1',columns='col2',values='col3',aggfunc='count')
fig = plt.figure(figsize=(12,8))
plt.imshow(grid)
plt.xlabel('x')
plt.ylabel('y')





















## Intellipaat
x = range(32)
y = df['col1']

# Single Chart/Plot
plt.figure(figsize=(4, 10))
plt.bar(x,df['col2'])                                      #vertical bar chart
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('title_1')
plt.legend('legend_1')
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

plt.plot(x,y)                                     #line chart
plt.barh(x,y)                                     #horizontal bar chart
plt.scatter(x,y)                                  #scatter plot
plt.stackplot(x,y)                                #Area/stack plot, y can be 2-d array
plt.pie(y)                                                 #Pie Chart
plt.boxplot(y)                                             #used to find outlier
plt.violinplot(y)                                          #used to find outlier
plt.imshow(y, cmap='summer')                               #heatmap
plt.hist(x, bins=8, edgecolor="white")                     #histogram with 8 bins

plt.subplot(2,3,4).plot(x,y,'g--')                #2 rows, 3 coloumns, 4th plot, g-- green dashed line
plt.subplot(r,c,sn).plot(x,y,'y*-')               #y*- yellow line with * marker
            
                
# arguments of pie() method:            
    # labels='col1'                                                 #Pie chart only
    # explode=()                                                    #Pie chart only
    # autopct='%1.2f%%'                                             #Pie chart only
                
# arguments of imshow() method:         
    # cmap = 'autumn', 'summer', 'winter','spring'                  #different color schemes
            
# Multiple Charts/Plots in Grid of 1x3                              # 1-row, 3-columns
plt.subplot(1,3,1).scatter(x=x,y=y)               # 1- rows, 3 - col 1 - position
plt.subplot(1,3,2).scatter(x=x,y=y)               # 1- rows, 3 - col 2 - position
plt.subplot(1,3,3).scatter(x=x,y=y)               # 1- rows, 3 - col 3 - position
plt.show()







# Udemy
# Regular Plotting
x = np.linspace(0,5,21)
y = x**2
plt.plot(x,y)

plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.plot(y,x)

# Object Oriented Plotting (OOP) - Manual Method of creating figure and axes separately
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('title')
ax.set_xlim([4,7])                                                   #set lower and upper limit on x-axis
ax.set_ylim([15,50])

fig = plt.figure()
ax0 = fig.add_axes([0,0,1,1])
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax2 = fig.add_axes([0.2,0.5,0.4,0.3])
ax1.plot(x,y)
ax2.plot(y,x)


# Object Oriented Plotting (OOP) - Automatic Method of creating figure and axes simultaneously
fig,axes = plt.subplot(nrows=1,ncols=2)                             #automatic execution of [fig = plt.figure()] & [ax = fig.add_axes()]
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()                                                  #remove the issue of overlapping plots


fig = plt.figure(figsize=(3,2),dpi=200)
fig,axes = plt.subplots(figsize=(3,2))
axes.plot(x,y)

fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(8,3))
axes[0].plot(x,y)
axes[1].plot(y,x)

fig.savefig('x-y sq plot.png', dpi=200)

ax.plot(x, x**2, label='x-squared')
ax.plot(x, x**3, label='x-cubed')
ax.legend(loc=0)                                                    #0-best fit location

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
    # hue='col2'                                                    #Segregate based on col2





























###############################################################################################################
#### Seaborn
###############################################################################################################

import seaborn as sns
sns.get_dataset_names()                                             #shows the names of dataset in sns
sns.load_dataset('planets')

##CampusX
#1) Relational Plot [figure level plot is called relplot]
#scatterplot (bivariate) - using axes level plot
sns.scatterplot(data=df,
                x='col1',
                y='col2',
                hue='col3',
                style='col4'
                size='col5')                                        #hue:color categorically; style:marker categorically

#scatterplot (bivariate) - using figure level plot
sns.relplot(data=df,
            x='col1',
            y='col2',
            kind='scatter',
            hue='col3',
            style='col4'
            size='col5')

#lineplot (bivariate) - using axes level plot
sns.lineplot(data=df,
            x='date_col',
            y='col2',
            hue='col3',
            style='col4',
            size='col5')

#lineplot (bivariate) - using figure level plot
sns.relplot(kind='line',
            data=df,
            x='date_col',
            y='col2',
            hue='col3',
            style='col4',
            size='col5')

#facet plot - 
#hue gives diff colors for diff categories in same chart
#if we want to plot those diff categories in diff charts, we need facet plots.
#facet plot can only be made on figure level plots (not axes level plots)
#below code will plot a grid of scatterplot:
#a) males & females on diff charts juxtaposed side by side, 
#b) diff continents on diff charts juxtaposed up-down.
#col_wrap will keep only 4 charts in each row here.
sns.relplot(kind='scatter',
            data=df,
            x='col1',
            y='col2',
            row='sex_col',
            col='continent_col',
            col_wrap=4)



#2) Distribution Plot [figure level plot is called distplot]
#histplot - using axes level plot - (Univariate) numeric/categorical
sns.histplot(data=df,
                x='col1',
                bins=20,
                hue='sex_col',
                element='step')                     

#histplot - using figure level plot - (col='sex_col' will plot 2 histograms side by side for each sex)
sns.distplot(kind='hist',
                data=df,
                x='col1',
                bins=20,
                col='sex_col',
                element='step')

#histplot (2-D) - using axes level plot - (Bivariate)
sns.histplot(data=df,
                x='col1',
                y='col2')                     

#histplot (2-D) - using figure level plot
sns.distplot(kind='hist',
                data=df,
                x='col1',
                y='col2')

#KDE plot - using axes level plot - (Univariate) numeric/categorical
sns.kdeplot(data=df,
                x='col1',
                hue='sex_col',
                fill=True)

#KDE plot - using figure level plot
sns.distplot(kind='kde',
                data=df,
                x='col1',
                hue='sex_col',
                fill=True)

#KDE plot (2-D) - using axes level plot - (Bivariate)
sns.kdeplot(data=df,
                x='col1',
                y='col2')                     

#KDE plot (2-D) - using figure level plot
sns.distplot(kind='kde',
                data=df,
                x='col1',
                y='col2')

#rug plot - using axes level plot - (Univariate) numeric/categorical
sns.kdeplot(data=df,
            x='col1')

#rug plot - using figure level plot
sns.distplot(kind='rug',
                data=df,
                x='col1')

#3) Categorical Plots
#3.1) Categorical Scatter Plot - Bivariate
#stripplot = scatter plot with a categorical col on x-axis
#stripplot - using axes level plot
sns.stripplot(data=df,
                x='col1',
                y='col2',
                hue='col3',
                jitter=False)

#stripplot - using figure level plot
sns.catplot(kind='strip',
                data=df,
                x='col1',
                y='col2',
                hue='col3',
                jitter=0.1)

#swarmplot: like stripplot, gives distribution info as well
#swarmplot - using axes level plot
sns.swarmplot(data=df,
                x='col1',
                y='col2',
                hue='col3')

#swarmplot - using figure level plot
sns.catplot(kind='swarm',
                data=df,
                x='col1',
                y='col2',
                hue='col3')


#3.2) Categorical Distribution Plot - Univariate
#single boxplot - using axes level plot
sns.boxplot(data=df,
                y='num_col')

#multiple boxplot - using axes level plot
sns.boxplot(data=df,
                x='cat_col',
                y='num_col',
                hue='col3')

#multiple boxplot - using figure level plot
sns.catplot(kind='box',
                data=df,
                x='cat_col',
                y='num_col',
                hue='col3')

#violinplot - using axes level plot
sns.violinplot(data=df,
                y='num_col')

#multiple violinplot - using axes level plot
sns.violinplot(data=df,
                x='cat_col',
                y='num_col',
                hue='col3')

#multiple violinplot - using figure level plot
sns.catplot(kind='violin',
                data=df,
                x='cat_col',
                y='num_col',
                hue='col3')


#3.3) Categorical Estimate Plot -> for central tendency
#barplot - using axes level plot
sns.barplot(data=df,
                x='cat_col',
                y='num_col',
                hue='col3',
                estimator=np.median)

#barplot - using figure level plot
sns.catplot(kind='bar',
                data=df,
                x='cat_col',
                y='num_col',
                hue='col3',
                estimator=np.median)

#pointplot - using axes level plot
sns.pointplot(data=df,
                x='cat_col',
                y='num_col')

#pointplot - using figure level plot
sns.catplot(kind='point',
                data=df,
                x='cat_col',
                y='num_col')

#countplot = histplot for categorical col
#countplot - using axes level plot
sns.countplot(data=df,
                x='cat_col',
                hue='col3')

#countplot - using figure level plot
sns.catplot(kind='count',
                data=df,
                x='cat_col',
                hue='col3')



#4) Reg Plot (Regression Plot) = Scatter Plot with Best Fit Line having 95% confidence interval
#regplot - using axes level plot [hue not available]
sns.regplot(data=df,
                x='col1',
                y='col2')

#regplot - using figure level plot [hue available]
sns.lmplot(data=df,
                x='col1',
                y='col2',
                hue='cat_col')

#residplot - residual plot (for above regression plot, residplot plots errors around the best fit line)
sns.residplot(data=df,
                x='col1',
                y='col2')


#5) Matrix Plot [only axes level plots exist]
#Heatmap - using axes level plot (No figure level plot function exists)
#grid_df :: wide format data with col1 on index, col2 on columns
plt.figure(figsize=(15,10))
sns.heatmap(data=grid_df,
            annot=True,
            linewidth=0.5,
            cmap='summer')                                          #linewidth creates space bw grid boxes
plt.show()

#Clustermap - using axes level plot (No figure level plot function exists)
sns.clustermap(iris.iloc[:,[0,1,2,3]])                              #not that useful graph.

#6) Multiplots - FacetGrid, PairGrid, JointGrid
#6.1) FacetGrid
#FacetGrid for boxplot
g = sns.FacetGrid(data=df, col='col1', row='col2')                  #col & row decide the size of grid
g.map(sns.boxplot, 'cat_col', 'num_col')
g.add_legend()

#FacetGrid for scatterplot
g = sns.FacetGrid(data=df,col='cat_col1',row='cat_col2')            #col & row decide the size of grid
g.map(sns.scatter,'num_col1','num_col2',hue='cat_col3')
g.add_legend()

#6.2) PairGrid
#PairPlot (Special case of PairGrid) - scatterplot + histplot for each pair of numeric cols
sns.pairplot(df,hue='cat_col')                                      #histplot converts into kdeplot while using hue

#PairGrid - customizable pairplot - all scatterplots
g = sns.PairGrid(data=df,hue='cat_col')
g.map(sns.scatterplot)

#Customized PairGrid - scatterplot + histplot
g = sns.PairGrid(data=df,hue='cat_col')
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)

#Customized PairGrid - histplot + boxplot
g = sns.PairGrid(data=df,hue='cat_col')
g.map_diag(sns.boxplot)
g.map_offdiag(sns.histplot)

#Customized PairGrid - diff plots above & below diagonal
g = sns.PairGrid(data=df,hue='cat_col')
g.map_diag(sns.histplot)
g.map_upper(sns.kdeplot)
g.map_lower(sns.scatterplot)

#6.3)JointGrid
#JointPlot (Special case of JointGrid)
sns.jointplot(data=df,
                x='num_col1',
                y='num_col2',
                kind='hist',
                hue='cat_col')

#JointGrid - customizable jointplot
g = sns.JointGrid(data=df,x='num_col1',y='num_col2')
g.plot(sns.scatterplot,sns.histplot)











##Intellipaat
sns.pairplot(data=df)                                               #scatterplot for all the column pairs
sns.countplot(data=df, x='col1')                                   #vertical bar chart of col1 summarized with its count
sns.countplot(data=df, y='col1')                                   #horizontal bar chart of col1 summarized with its count
sns.boxplot(data=df, y='col1')                                     #used to find outlier
sns.scatterplot(data=df, x='col1', y='col2')                      #scatter plot
sns.barplot(data=df, x='col1', y='col2')                          #bar chart
sns.regplot(data=df, x='col1', y='col2')                          #regression plot = scatter plot with best fit line
sns.heatmap(data=df, y=3x3_array)                                   #heat map
sns.boxplot(data=df, y='col1', hue='col2')                        #box plot
sns.histplot(data=df, x='col1', hue='col2')                       #histogram plot
sns.lineplot(data=df, x='col1', y='col2')                         #line plot
sns.kdeplot(arr1)                                                   #KDE plot

# arguments of scatterplot() method:
    # color 'r','g','b','k','y','c','m'
    # palette for multiple colors
    # hue for group by on col2
    # marker '^','-','--','*','o','+'
    # s for size of the marker
    # edgecolor is for the edge color of the marker
    # alpha is for transparency of the marker

################## Subplots in seaborn
fig, axis = plt.subplots(nrows=2, ncols=2, figsize=(12,8))
sns.barplot(data=df, x='col1', y='col2', hue='col3', ax = axis[0,0])





























###############################################################################################################
#### Plotly
###############################################################################################################

import plotly.offline as pyo
import plotly.graph_objs as go

#scatter plot
trace = go.Scatter(x=df['num_col1'],
                    y=df['num_col2'],
                    mode='markers',
                    text=df['cat_col'],
                    marker={'color':'#00a65a', 'size':16})
data = [trace]
layout = go.Layout(title='title of graph',
                    xaxis={'title':'x_title'},
                    yaxis={'title':'y_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#single line chart
trace = go.Scatter(x=df['datetime_col'],
                    y=df['num_col'],
                    mode='lines',
                    #mode='lines+markers',
                    marker={'color':'#00a65a', 'size':16})
data = [trace]
layout = go.Layout(title='title of graph',
                    xaxis={'title':'timeline'},
                    yaxis={'title':'y_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#multi-line chart
trace1 = go.Scatter(x=df['datetime_col'],
                    y=df['num_col1'],
                    mode='lines+markers',
                    marker={'color':'#00a65a', 'size':16},
                    name='line1_label')
trace2 = go.Scatter(x=df['datetime_col'],
                    y=df['num_col2'],
                    mode='lines+markers',
                    marker={'color':'#007399', 'size':16},
                    name='line2_label')
data = [trace1, trace2]
layout = go.Layout(title='title of graph',
                    xaxis={'title':'timeline'},
                    yaxis={'title':'y_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#bar graph
trace = go.Bar(x=df['cat_col'],
                    y=df['num_col'])
data = [trace]
layout = go.Layout(title='title of graph',
                    xaxis={'title':'x_title'},
                    yaxis={'title':'y_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)





































###############################################################################################################
#### sys - Everything
###############################################################################################################

import sys
sys.getsizeof(a)                                                    #memory size occupied by a(can be anything)
























###############################################################################################################
#### General
###############################################################################################################

divmod(a,b)                                 #returns a tuple with quotient and remainder of a/b
a//b                                        #returns quotient of a/b
a%b                                         #returns remainder of a/b
pow(a,b)                                    #returns a^b
pow(a,b,m)                                  #returns a^b % m





###############################################################################################################
#### strings - Everything
###############################################################################################################

s1 = 'abcdefghij'                           #string
s1[3]                                       #string indexing
s1[-1]                          
s1[2:]                                      #string slicing
s1[:8]                          
s1[1:5]                         
s1[::2]                                     #every character from string s with step size 2
s1[::-1]                                    #string backwards
        
s2 = 'welcome'                          
s1 + s2                                     #concatenation
char = 'a'                          
char * 10                                   #'aaaaaaaaaa'
                        
s1.upper()                                  #upper case
s1.lower()                                  #lower case
s1.capitalize()                             #capitalize first character of first word
s1.title()                                  #capitalize first character of all word
                        
s1.replace('d','z')                         #replace 'd' with 'z' in s1
s1.strip()                                  #remove white space before and after s1
s1.rstrip()                                 #remove white space after s1
s1.lstrip()                                 #remove white space before s1
s1.split()                                  #split the string at space and provide a list of strings
s1.split('c')                               #split the string at 'c'
" ".join(arr_of_str)                        #join an array of string with space in between
len(s1)                                     #length of string
        
str.isalnum()                               #checks if string is alphanumeric
str.isalpha()                               #checks if string is alphabetical
str.isdigit()                               #checks if string is numeric
str.islower()                               #checks if string is all lower characters
str.isupper()                               #checks if string is all upper characters
                    
                    
                    

###############################################################################################################
#### list - Everything
###############################################################################################################
                    
my_list = ['A string',23,100.232,'o']       #a list can contain anything
len(my_list)                                #number of elements in a list
my_list[2]                                  #element at index 2
my_list[2:]                                 #elements from index 2 to end
my_list[:3]                                 #elements from start to index 2
my_list[2:5]                                #elements at index 2,3,4
my_list[::2]                                #every 2nd element from the list
my_list[::-1]                               #reverse the list
my_list + ['new item']                      #concatenate element to the list
my_list * 2                                 #repeat the list
my_list.append('append_me')                 #append element to the list
my_list.pop()                               #remove last element from the list and return it
my_list.pop(2)                              #remove element at index 2 from the list and return it
my_list.reverse()                           #reverse the list
my_list.count(element_1)                    #count the number of element_1 in my_list
my_list.sort()                              #sort the list - in place
sorted(my_list)                             #just show the sorted list, not sort original list
[i**2 for i in my_list if i%2==0]           #list comprehension
my_list = list(tuple_1)                     #convert tuple_1 to list





###############################################################################################################
#### dictionary - Everything
###############################################################################################################

d = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
d['key3']                                                                             #give the value of key3 i.e. ['item0','item1','item2']
d['key3'][0]                                                                          #'item0'
d['key3'][0].upper()                                                                  #'ITEM0'
d.keys()                                                                              #all the keys of the dictionary
d.values()                                                                            #all the values of the dictionary
d.items()                                                                             #all the key:value pairs of the dictionary
                    
                    
                    
                    
###############################################################################################################
#### tuples - Everything                   
###############################################################################################################
                    
t = ('one', 2, 3.1)                                                                   #initializing a tuple
len(t)                                                                                #number of elements in the tuple
t[-1]                                                                                 #last element of the tuple
t.index('one')                                                                        #index of element 'one' in the tuple
t.count('one')                                                                        #count of element 'one' in the tuple
                    
                    
                    
###############################################################################################################
#### sets - Everything           
###############################################################################################################      
                    
x = set()                                                                             #creating a set
x.add(1)                                                                              #adding element to set
x.add(2)                                                                              #adding element to set
set(my_list)                                                                          #convert my_list to set: show any duplicate values only once

sum(x)                                                                                #sum of all elements of set x
len(x)                                                                                #number of elements in set x

x.discard(n)                                                                          #delete n without error when not found
x.remove(n)                                                                           #delete n with error when not found

x = set()
y = set()
x.union(y)                                                                            #set function union
x.intersection(y)                                                                     #set function intersection
x.differences(y)                                                                      #elements in x but not in y

                
                    
                    
###############################################################################################################
#### scope - Local, Enclosing, Global, Builtin (LEGB Rule)
###############################################################################################################
                
                    
                    
###############################################################################################################
#### Decorators
###############################################################################################################


#actual way of calling a decorator
def my_decorator(my_func,my_val):
    def wrapper():
        print('**********************')
        my_func(my_val)
        print('**********************')
    return wrapper

def sq(val):
    print(val**2)

a = my_decorator(sq, 3)
a()


#short-cut way of calling same decorator
def my_decorator(my_func,my_val):
    def wrapper():
        print('**********************')
        my_func(my_val)
        print('**********************')
    return wrapper

@my_decorator
def sq(val):
    print(val**2)

sq(3)

#actual use case example of decorator
#displaying time taken by a function to execute

import time
def timer(func):
    def wrapper():
        print('**********************')
        start = time.time()
        func()
        print("time taken by",func.__name__," = ",time.time() - start,"secs")
        print('**********************')
    return wrapper

@timer
def hello():
    print("Hello World")
    time.sleep(2)

@timer
def display():
    print("Displaying something")
    time.sleep(0.5)

hello()
display()

#this kind of decorator will work only when functions (hello, display) don't have an input
#when a function comes where there is one or more input arguments, 
#then def wrapper(*args) as well as func(*args) needs to be changed.


import time
def timer(func):
    def wrapper(*args):
        print('**********************')
        start = time.time()
        func(*args)
        print("time taken by",func.__name__," = ",time.time() - start,"secs")
        print('**********************')
    return wrapper

@timer
def hello():
    print("Hello World")
    time.sleep(2)

@timer
def square(num):
    num**2

hello()
square(5)






###############################################################################################################
#### Import Methodology
###############################################################################################################

##Import                            ##Style                             ##Example Usage
Import whole module	                import math	                        Use with prefix math.sqrt()
Import whole module with alias	    import numpy as np	                Use alias np.array()
Import specific names	            from math import sqrt	            Use directly sqrt()
Import specific names with alias    from math import sqrt as s	        Use alias s()
Wildcard import all	                from math import *	                Imports all public names (discouraged)
Import submodule	                import package.submodule	        Access with full path





###############################################################################################################
#### Create New Python Environment in VS Code
###############################################################################################################
conda create --name .venv python=3.13
conda activate .venv/