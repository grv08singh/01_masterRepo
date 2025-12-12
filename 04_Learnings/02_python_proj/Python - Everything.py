# AWS
# Acc ID: 676206921654
# Username: grv08singh@gmail.com
# pw: 
# 



###############################################################################################################
#### Python Environment
###############################################################################################################

## Open jupyter notebook at a specified path:
## Type in Anaconda Prompt
## jupyter notebook --notebook-dir="specified_path"
## jupyter notebook --notebook-dir="D:\05 GIT\01_Docs\02_EPGC_Intellipaat\01 EPGC - Live Classes\2025.11.30 - EPGC DL - CNN HandsOn"
## jupyter notebook --notebook-dir="D:\git_repo_DS\02_EPGC_Intellipaat\03 EPGC - Mandatory Assignments\17 EPGC - ML - Decision Tree Quiz"
## jupyter notebook --notebook-dir="D:\Projects\streamlit_startup_dashboard"
## C:\Users\grv06\AppData\Roaming\Code\User\settings.json

#Create Python env using conda
conda create --name dummy_env python=3.8
#list of env
conda env list
#activate an env
conda activate dummy_env
#deactivate current env
conda deactivate
#list of installed packages in activated env
conda list
#export env
conda env export --name dummy_env --file dummy_env.yml
#import env OR create env from yml file
conda env create --file dummy_env.yml
#remove / delete env
conda remove --name dummy_env --all
#create an appropriate Jupyter Notebook kernel mapped to new environment
python -m ipykernel install --user --name=dummy_env



# Create Python environment using python
# python -m venv .venv
# .\.venv\Scripts\activate.bat
# 
# pip install -r requirements.txt



pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install plotly

pip install scipy
pip install statsmodels

pip install scikit-learn
pip install imbalanced-learn
pip install mlxtend

pip install tensorflow

pip install requests
pip install beautifulsoup4
pip install selenium
pip install scrapy
pip install lxml
pip install html5lib

pip install Pillow
pip install pytesseract
pip install opencv-python







###############################################################################################################
#### Deep Learning (DL)
###############################################################################################################
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








###############################################################################################################
#### Data Science
###############################################################################################################



#Proj_01: use mnist dataset to learn a MBGD,DT,RF,KNN,DL model and create an online app to recognize handwritten digits.
#Proj_02: use cifar-100 dataset to learn



###############################################################################################################
#### End-to-End ML Flow
###############################################################################################################
# ML Flow:
#
## 01) Data Gathering
##      01.01) df.info
##      01.02) df.shape
##      01.03) df.describe()
##      01.04) df.duplicated()
##      01.05) df['col1'].info() - check null vals
## 02) Data Wrangling / Cleaning / Preprocessing
##      02.01) df.drop_duplicates()
##      02.02) df.fillna(mean) / Missing Value Imputation
##      02.03) df['col1'].astype(int)
##      02.04) Outlier Detection & Removal
## 03) Exploratory Data Analysis (EDA)
##      03.01) Explore Data
##          03.01.01) Univariate Analysis:
##                          Histogram
##                          Frequency plot
##                          Pie chart
##                          Box plot
##                          Frequency distribution
##          03.01.02) Bivariate Analysis:
##                          Scatter plot
##                          Bar chart
##                          Line chart
##                          Pie chart
##          03.01.03) Multivariate Analysis:
##                          3D Scatter plot
##                          Heatmap
##                          Pair plot
##                          Bar chart with hue
##                          Histogram with hue
##          03.01.04) Correlation
##          03.01.05) Covariance
##      03.02) Augment Data / Feature Engineering
##          03.02.01) Merging DataFrames
##          03.02.02) Adding New Cols
## 04) Feature Selection
## 05) Model Building
## 06) Model Selection
## 07) Hyper Parameter Tuning
## 08) Convert to Website/App
## 09) Deploy
## 10) Monitor









#### ML MODELS & TECHNIQUES

#### Regression Algo:
######## 1) Linear Regression [OLS] - Ridge, Lasso, ElasticNet
######## 2) Linear Regression [GD] - Batch GD, Stochastic GD, Mini Batch GD 
######## 3) Polynomial Linear Regression
######## 4) Decision Tree Regression
######## 5) Random Forest Regression
######## 6) Support Vector Regression

#### Classification Algo:
######## 1) Logistic Regression
######## 2) Decision Tree Classifier
######## 3) Random Forest Classifier
######## 4) K-Nearest Neighbours
######## 5) Naive Bayes
######## 6) Support Vector Classifier

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

#### 6) Logistic Regression

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




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')


from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder,StandardScaler,MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV,RandomizedSearchCV
from imblearn.over_sampling import SMOTE                #SMOTE - Synthetic Minority Oversampling Technique

from sklearn.linear_model import LinearRegression,LogisticRegression,SGDRegressor,SGDClassifier,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
from sklearn.svm import SVR,SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import r2_score,accuracy_score,roc_auc_score,precision_score,recall_score,f1_score
                            ,confusion_matrix,ConfusionMatrixDisplay,classification_report

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.feature_selection import SelectKBest,chi2
from sklearn.compose import ColumnTransformer,make_column_transformer
from sklearn.pipeline import Pipeline,make_pipeline




###############################################################################################################
#### EDA :: Exploratory Data Analysis
###############################################################################################################

# 1 Cleaning
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


# 2 Checking Datatype Inconsistency
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


# 3 Remove Null Values (if Null < 10% of data, [dropna], else if Null < 40% of data, [fillna] with median/mode, else [drop feature/col])
for col in df.columns:
    if(df[col].dtype in ('int64', 'float64'):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])
#### drop Null rows from specific columns -->
df = df.dropna(subset=['col1', 'col2', 'col3'])


# 4 Remove Duplicates
df = df.drop_duplicates()


# 5 Outliers - 
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



###############################################################################################################
#### Feature Engineering
###############################################################################################################

# 1 Feature Transformation
## 1.1 Missing Value Imputation
## 1.2 Handling Categorical Features
## 1.3 Outlier Detection
## 1.4 Feature Scaling

# 2 Feature Construction


# 3 Feature Selection
## 3.1 Filter Methods [Individual feature effect is studied]
#### 3.1.1 Drop Duplicate Cols

#### 3.1.2 Variance Threshold Method
######## 3.1.2.1 Constant value: Drop cols with variance = 0
######## 3.1.2.2 Quasi-Constant value: Drop cols with variance ~ 0
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold = 0.05)
sel.fit_transform(X_train_scaled)
sel.transform(X_test_scaled)

#### 3.1.3 Correlation Method: Drop cols with corr near 0

#### 3.1.4 ANOVA Method;    H0 : feature has no relation with tgt
from sklearn.feature_selection import f_classif, SelectKBest
sel = SelectKBest(f_classif, k=25).fit(X_train, y_train)
sel.get_support()

#### 3.1.5 CHI-Square Method;    H0 : feature has no relation with tgt
ct = pd.crosstab('col1', y_train, margin=True)
from scipy.stats import chi2_contingency
p_val = chi2_contingency(ct)[1]

#### 3.1.6 Mutual Information Method;
from sklearn.feature_selection import mutual_info_classif
mi = mutual_info_classif(X,y)
for i,mi_val in enumerate(mi):
    print(f"feature {i}: Mutual Infomation = {mi_val}")

#OR
from sklearn.feature_selection import SelectKBest,mutual_info_classif
selector = SelectKBest(mutual_info_classif,k=2)
X_new = selector.fit_transform(X,y)
cols = selector.get_support(indices=True)           #indices of selected cols


## 3.2 Wrapper Methods [combined effect of features is studied - computationally slower]
#### 3.2.1 Exhaustive Feature Selection: try out each subset combination, and select the best
######## needs to train 2^n - 1 models to find the best subset of features
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
LoR = LogisticRegression()
efs = EFS(LoR, max_features=4, scoring='accuracy', cv=5)
#OR
LR = LinearRegression()
efs = EFS(LR, max_features=4, scoring='r2', cv=5, n_jobs=-1)
efs = efs.fit(X_train, y_train)
efs.best_score_
efs.best_feature_names_
efs.subsets_

#### 3.2.2 Sequential Forward Selection
######## needs to train n(n+1)/2 models to find the best subset of features
######## use only 1 feature & calculate accuracy; do for all cols; choose best score
######## do this process until all features are selected
######## choose the best score of all, that subset is the best subset
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
LoR = LogisticRegression()
sfs = SFS(LoR, k_features='best', forward=True, floating=False, scoring='accuracy', cv=5)
#OR
LR = LinearRegression()
sfs = SFS(LR, k_features='best', forward=True, floating=False, scoring='r2', cv=5)
sfs = sfs.fit(X_train, y_train)
sfs.k_feature_idx_

#### 3.2.3 Backward Elimination
######## needs to train n(n+1)/2 models to find the best subset of features
######## remove 1 feature & calculate accuracy; do for all cols; choose best score
######## do this process until 1 feature remains
######## choose the best score of all, that subset is the best subset
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
LoR = LogisticRegression()
sfs = SFS(LoR, k_features='best', forward=False, floating=False, scoring='accuracy', cv=5)
#OR
LR = LinearRegression()
sfs = SFS(LR, k_features='best', forward=False, floating=False, scoring='r2', cv=5)
sfs = sfs.fit(X_train, y_train)
sfs.k_feature_idx_

#### 3.2.4 Recursive Feature Elimination (RFE)
######## recursively find importance score & remove the one with lowest score
######## RFE is also part of Embedded Methods
from sklearn.feature_selection import RFE
from sklearn.feature_selection import RFECV
model = RandomForestClassifier()

rfe = RFE(estimator=model, step=2, n_features_to_select=2)      #step=2 means remove 2 features with lowest scores
#OR
rfecv = RFECV(estimator=model, step=2, n_features_to_select=2, cv=5)

rfe.fit(X_train_scaled, y_train)
rfe.ranking_


## 3.3 Embedded Methods [trains ML model along with scoring feature importance]
#### Algo having coef_ OR feature_importance_ attributes can be used as embedded methods
#### coef_ e.g. Linear Regression, Logistic Regression, Ridge, Lasso, Elastic Net, 
#### feature_importance_ e.g. Decision Tree, Random Forest, Gradient Boosting
#### sklearn.feature_selection.SelectFromModel --> Transformer to use embedded methods


## 3.4 Hybrid Methods



# 2 Feature Extraction
## 2.1 Principal Component Analysis (PCA)
## 2.2 Linear Discriminant Analysis (LDA)



###############################################################################################################
#### Machine Learning (ML) - Model Fitting
###############################################################################################################


# 1 X-y Split
#selection using col name
X = df[['col1','col2']]     #pd.DataFrame
y = df['tgt_col']           #pd.Series
#or selection using col indexing & slicing
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
#or selection using fancy col indexing
X = df.iloc[:,[0,1,2,3,4,5,6,7]]
y = df.iloc[:,[8]]


# 2 Train-Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)


# 3.1 Encoding - Manually
# 3.1.1 Label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = pd.DataFrame(le.fit_transform(df[[col]]))

# 3.1.2 Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=[['low','medium','high']])
df['col1'] = pd.DataFrame(oe.fit_transform(df[['col1']]))

# 3.1.3 One Hot Encoding
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(drop='First', sparse=False, handle_unknown='ignore')
df['col1'] = pd.DataFrame(ohe.fit_transform(df[['col1']]))
## One Hot Encoding - using Pandas [column names retained]
pd.get_dummies(df,columns=['col1','col2'],drop_first=True)      #OHE for col1 and col2

# 3.1.4 Simple Imputer [replace missing values with col mean]
from sklearn.impute import SimpleImputer
si = SimpleImputer()                                            #mean by default
si = SimpleImputer(strategy = 'median')                         #median
si = SimpleImputer(strategy = 'most_frequent')                  #mode
df['col1'] = pd.DataFrame(si.fit_transform(df[['col1']]))

# 3.1.5 Encoding - Using Column Transformer [task of above steps becomes easier]
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(transformers=[
                                        ('tnf1', OrdinalEncoder(categories=[['low','medium','high']]), ['col1']),
                                        ('tnf2', OneHotEncoder(drop='First', sparse=False), ['col2', 'col3']),
                                        ('tnf3', SimpleImputer(), ['col4'])
                                    ],
                        remainder = 'passthrough'))
ct.fit_transform(df)



# 4 Scaling
# 4.1 Standard Scaler
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

# 4.2 Min Max Scaler
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)


# 5 SMOTE - Synthetic Minority Oversampling Technique
# make class balanced
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
#now X_resampled & y_resampled will not have class imbalance


# 6 Dimensionality Reduction
## 6.1 PCA (Principal Component Analysis) [Unsupervised Technique - Not Algo]
#manual work
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
cov_matrix = np.cov(X_scaled.T)     #np.cov needs to transpose data due to its functionality
#OR
cov_matrix = df.cov(X_scaled)       #df.cov works fine as it is
eigen_values,eigen_vectors = np.linalg.eig(cov_matrix)
pc = eigen_vectors[:2]
transformed_df = np.dot(df.iloc[:,:3],pc.T)
new_df = pd.DataFrame(transformed_df,columns=['PC1','PC2'])

#sklearn implementation
from sklearn.decomposition import PCA
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
#principal components = Eigen Vectors
pca.components_
#explained variance = Eigen Values
pca.explained_variance_
#%age variance explained by each PC
pca.explained_variance_ratio_

## 6.2 LDA (Linear Discriminant Analysis) [Supervised Technique - Not Algo]
#used with classification problem only
#Fisher Discriminant Ratio = (mu1 - mu2)^2/(s1^2 + s2^2)      after projection on line
#we have to find max of numerator, min of denominator
#class1 & class2 projected on a line,
#must have both classes' mean as far as possible, 
#& variance within class as low as possible
#
#to find n_components in LDA, the formula is MIN(independent_features, num_of_classes-1)
#for MNIST dataset, n_components = MIN(784, 10-1) = 9
#for digit_dataset, n_components = MIN(64, 10-1) = 9
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
LDA = LinearDiscriminantAnalysis(n_components=9)
X_train_lda = LDA.fit_transform(X_train, y_train)
X_test_lda = LDA.transform(X_test)



# 7 Initializing Different ML Model
## 7.1 Linear Regressor (OLS)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
sns.regplot(x = y_pred, y = y_test, line_kws = {'color':'red'})

## 7.2 SGDRegressor (GD)
from sklearn.linear_model import SGDRegressor
sgd_r = SGDRegressor(loss='squared_error', penalty='l2', random_state=42)

## 7.3 Lasso Regressor
from sklearn.linear_model import Lasso
lasso_r = Lasso(alpha=1.0)

## 7.4 Ridge Regressor
from sklearn.linear_model import Ridge
ridge_r = Ridge(alpha=1.0)

## 7.5 Elastic Net Regressor
from sklearn.linear_model import ElasticNet
elastic_net_r = ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)

## 7.6 KNN Regressor
from sklearn.neighbors import KNeighborsRegressor
knnr = KNeighborsRegressor(n_neighbors=5)

## 7.7 Support Vector Regressor (SVR)
from sklearn.svm import SVR
svr = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)

## 7.8 Decision Tree Regressor
from sklearn.tree import DecisionTreeRegressor
dt_r = DecisionTreeRegressor(max_depth=5, random_state=0)

## 7.9 Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
rf_r = RandomForestRegressor(n_estimators=100, random_state=42)

## 7.10 Gradient Boosting Regressor
from sklearn.ensemble import GradientBoostingRegressor
gb_r = GradientBoostingRegressor(n_estimators=500, learning_rate=0.01,
                                    max_depth=4, loss='ls', random_state=42)

## 7.11 XGBoost Regressor
from xgboost import XGBRegressor
xgb_r = XGBRegressor(objective='reg:squarederror',n_estimators=100, 
                         learning_rate=0.1,max_depth=5,random_state=42)

## 7.12 Logistic Regressor - Binary Classifier
from sklearn.linear_model import LogisticRegression
LoR = LogisticRegression()

## 7.13 SGDClassifier
from sklearn.linear_model import SGDClassifier
sgd_c = SGDClassifier(loss='log_loss', penalty='l2', max_iter=1000, random_state=42)

## 7.14 Lasso Classifier (No direct method)
from sklearn.linear_model import LogisticRegression
lasso_c = LogisticRegression(penalty='l1', solver='liblinear', C=0.1)

## 7.15 Ridge Classifier
from sklearn.linear_model import RidgeClassifier
ridge_c = RidgeClassifier(alpha=1.0, solver='auto')

## 7.16 Elastic Net Classifier (No direct method)
from sklearn.linear_model import SGDClassifier
elastic_net_c = SGDClassifier(loss='log_loss', penalty='elasticnet', l1_ratio=0.5)
#OR
elastic_net_c = LogisticRegression(penalty='elasticnet', solver='saga', l1_ratio=0.5)

## 7.17 KNN Classifier
from sklearn.neighbors import KNeighborsClassifier
knn_c = KNeighborsClassifier(n_neighbors=5)

## 7.18 Support Vector Classifier (SVC)
from sklearn.svm import SVC
svc = SVC(kernel='rbf', C=1, gamma='scale')

## 7.19 Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
dt_c = DecisionTreeClassifier(max_depth = 5)

## 7.20 Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rf_c = RandomForestClassifier()
rf_c = RandomForestClassifier(n_estimators = 52, max_depth = 7, criterion = 'entropy', random_state = 2)

## 7.21 Gradient Boosting Classifier
from sklearn.ensemble import GradientBoostingClassifier
gb_c = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

## 7.22 XGBoost Classifier
from xgboost import XGBClassifier
xgb_c = XGBClassifier(objective="binary:logistic", n_estimators=100,
                        learning_rate=0.1, max_depth=3, random_state=42)

## 7.23 Naive Bayes Classifier (good for text data)
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)


## 7.24 K-Means Clustering [Unsupervised Algo]
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, init='k-means++', 
                n_init='auto', random_state=0, max_iter=200)
kmeans.fit(X)
clustered_result = kmeans.labels_
centers = kmeans.cluster_centers_
sum_of_within_cluster_variance = kmeans.inertia_
cluster_pred_for_new_data_point = kmeans.predict(X_new)







## 8 Scores
## 8.1 Regression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2_score = r2_score(y_test, y_pred)
adjusted_r2 = 1 - (1 - r2) * ((n - 1) / (n - p - 1))

## 8.2 Classification
## 8.2.1 automatic calculation
from sklearn.metrics import confusion_matrix,accuracy_score,roc_auc_score,precision_score,recall_score,f1_score,classification_report
confusion_matrix(y_test, y_pred)
accuracy_score(y_test, y_pred)
precision_score(y_test, y_pred)
recall_score(y_test, y_pred)
f1_score(y_test, y_pred)
classification_report(y_test, y_pred)
roc_auc_score(y_test, y_pred)   #better measure of accuracy in unbalanced dataset

## 8.2.2 manual calculation
[tn, fp], [fn, tp] = confusion_matrix(y_test, y_pred).ravel()
precision = tp / (tp + fp)
recall_or_sensitivity = tp / (tp + fn)
f1_score = 2 * precision * recall / (precision + recall)
negative_precision = tn / (tn + fn)
specificity = tn / (tn + fp)
total_support_value = tp + tn + fp + fn


## 9 Finding Best Hyper Parameters
## 9.1 Values to try
param_grid = {
    'n_estimators' : [100,200,300],
    'max_depth' : [None,5,10,15],
    'min_samples_split' : [2,5,10],
    'min_samples_leaf' : [1,2,4],
    'criterion' : ['gini','entropy'],
    'bootstrap': [True, False]
}

## 9.2.1 Grid Search CV
rf = RandomForestClassifier()
grid_search = GridSearchCV(estimator = rf, 
                            param_grid = param_grid, 
                            cv = 5, 
                            scoring = 'accuracy', 
                            n_jobs = -1,
                            verbose = 1)
grid_search.fit(X_train, y_train)

## 9.2.2 Randomized Search CV
rand_grid_cv = RandomizedSearchCV(estimator = rf, 
                                    param_distributions = param_grid, 
                                    cv = 5, 
                                    scoring = 'accuracy', 
                                    n_jobs = -1,
                                    verbose = 1)
rand_grid_cv.fit(X_train, y_train)

## 9.3 Finding best params/models from grid
grid_search.best_estimator_
grid_search.score(X,y)
grid_search.best_score_
grid_search.best_params_


## 10 Pipeline
#single model
from sklearn.pipeline import Pipeline,make_pipeline
#imputation transformer - applying imputation on col with index 3 & 5
trf1 = ColumnTransformer([
        ('impute1', SimpleImputer(), [5]),
        ('impute2', SimpleImputer(strategy='most_frequent'), [3])
        ], remainder='passthrough')
#one hot encoding transformer - applying ohe on col index 2 & 4
trf2 = ColumnTransformer([
        ('ohe1', OneHotEncoder(sparse=False,handle_unknown='ignore'), [2,4])
        ], remainder='passthrough')
#scaling transformer - applying scaling on all cols with index 0 through 9
trf3 = ColumnTransformer([
        ('scale1',MinMaxScaler(),slice(0,10))
        ])
#feature selection - selecting 5 best features
trf4 = SelectKBest(score_func=chi2, k=5)

#train model
trf5 = DecisionTreeClassifier()

#create pipeline
pipe = Pipeline([
        ('trf1',trf1),
        ('trf2',trf2),
        ('trf3',trf3),
        ('trf4',trf4),
        ('trf5',trf5)
        ])
#or 
pipe = make_pipeline(trf1,trf2,trf3,trf4,trf5)

#train
from sklearn import set_config
set_config(display = 'diagram')
pipe.fit(X_train, y_train)

#exploring pipeline
pipe.named_steps

#prediction
y_pred = pipe.predict(X_test)


#Cross Validation using pipeline
from sklearn.model_selection import GridSearchCV
params = {
    'n_estimators' : [100,200,300],
    'max_depth' : [None,5,10,15],
    'min_samples_split' : [2,5,10],
    'min_samples_leaf' : [1,2,4],
    'criterion' : ['gini','entropy'],
    'bootstrap': [True, False]
}
grid = GridSearchCV(pipe, params, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)
grid.best_score_
grid.best_params_

#Exporting the pipeline
import pickle
pickle.dump(pipe,open('pipe.pkl','wb'))
ct.fit_transform(df)




###############################################################################################################
#### Statistics
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
pd.set_option('display.max_rows', 5)                                #display only 5 rows
pd.set_option('display.max_rows', None)                             #display all rows
pd.set_option('display.max_columns', None)                          #display all cols
pd.set_option('display.max_colwidth', None)                         #proper col width

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

#Melt (opposite of Pivot)
df_pivot.melt()                                                     #gives long format data

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
# Single Chart/Plot
plt.stackplot(x,y)                                #Area/stack plot, y can be 2-d array
plt.boxplot(y)                                             #used to find outlier
plt.violinplot(y)                                          #used to find outlier
                
# arguments of imshow() method:         
    # cmap = 'autumn', 'summer', 'winter','spring'                  #different color schemes




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
################## Subplots in seaborn
fig, axis = plt.subplots(nrows=2, ncols=2, figsize=(12,8))
sns.barplot(data=df, x='col1', y='col2', hue='col3', ax = axis[0,0])





###############################################################################################################
#### Plotly Graph Objects (Plotly go)
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

#bar chart
trace = go.Bar(x=df['cat_col'],
                    y=df['num_col'])
data = [trace]
layout = go.Layout(title='title of graph',
                    xaxis={'title':'x_title'},
                    yaxis={'title':'y_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#bar chart - NESTED / CLUSTERED (by default behaviour)
trace1 = go.Bar(x=df['cat_col'],
                    y=df['num_col1'],
                    name='num_col1_name',
                    marker={'color':'#00a65a'})
trace1 = go.Bar(x=df['cat_col'],
                    y=df['num_col2'],
                    name='num_col2_name',
                    marker={'color':'#06a65a'})
data = [trace1,trace2]
layout = go.Layout(title='title of graph',
                    xaxis={'title':'x_title'},
                    yaxis={'title':'y_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
pyo.plot(fig)

#bar chart - OVERLAY
trace1 = go.Bar(x=df['cat_col'],
                    y=df['num_col1'],
                    name='num_col1_name',
                    marker={'color':'#00a65a'})
trace1 = go.Bar(x=df['cat_col'],
                    y=df['num_col2'],
                    name='num_col2_name',
                    marker={'color':'#06a65a'})
data = [trace1,trace2]
layout = go.Layout(title='title of graph',
                    xaxis={'title':'x_title'},
                    yaxis={'title':'y_title'},
                    barmode='overlay')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#bar chart - STACK
trace1 = go.Bar(x=df['cat_col'],
                    y=df['num_col1'],
                    name='num_col1_name',
                    marker={'color':'#00a65a'})
trace1 = go.Bar(x=df['cat_col'],
                    y=df['num_col2'],
                    name='num_col2_name',
                    marker={'color':'#06a65a'})
data = [trace1,trace2]
layout = go.Layout(title='title of graph',
                    xaxis={'title':'x_title'},
                    yaxis={'title':'y_title'},
                    barmode='stack')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#bubble plot (3-D or 4-D scatter plot)
trace = go.Scatter(x=df['cat_col'],
                    y=df['num_col1'],
                    mode='markers',
                    marker={'size':df['num_col2']})
data = [trace]
layout = go.Layout(title='Bubble Chart',
                    xaxis={'title':'x_title'},
                    yaxis={'title':'y_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#box plot
trace = go.Box(x=df['num_col',
                name='num_col_name',
                marker={'color':'#00a65a'})
data = [trace]
layout = go.Layout(title='Box Plot',
                    xaxis={'title':'x_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#box plots juxtaposed
trace1 = go.Box(x=df['num_col1',
                name='num_col1_name',
                marker={'color':'#00a65a'})
trace2 = go.Box(x=df['num_col2',
                name='num_col2_name')
data = [trace1,trace2]
layout = go.Layout(title='Box Plot',
                    xaxis={'title':'x_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#histogram (frequency plot)
trace = go.Histogram(x=df['num_col'],
                        xbins={'size':10,
                                'start':5,
                                'end':95})
data = [trace]
layout = go.Layout(title='hist_title',
                    xaxis={'title':'x_title'})
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#heatmap
trace = go.Heatmap(x=df['cat_col1'],
                    y=df['cat_col2'],
                    z=df['num_col'])
data = [trace]
layout = go.Layout(title='heatmap_title')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

#heatmaps juxtaposed in subplots [two subplots in one single plot]
from plotly import tools
trace1 = go.Heatmap(x=df['cat_col1'],
                    y=df['cat_col2'],
                    z=df['num_col'].values.tolist())
trace2 = go.Heatmap(x=df['cat_col1'],
                    y=df['cat_col2'],
                    z=df['num_col'].values.tolist())
fig = tools.make_subplots(rows=1,
                            cols=2,
                            subplot_titles=['heatmap1 title','heatmap2 title'],
                            shared_yaxes=True)
fig.append_trace(trace1,1,1)
fig.append_trace(trace2,1,2)
pyo.plot(fig)

#dist plot (combination of histplot, kdeplot, rugplot)
import plotly.figure_factory as ff
hist_data = [df['num_col1'], df['num_col2']]
group_labels = ['num_col1_label','num_col2_label']
fig = ff.create_distplot(hist_data,group_labels,bin_size=[10,20])
pyo.plot(fig)

#3-D surface plots (can't be made using px)
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
xx,yy = np.meshgrid(x,y)

trace = go.Surface(x=x,y=y,z=z)
data = [trace]
layout = go.Layout(title='3D Surface Plot')
fig = go.Figure(data,layout)
fig.show()

#contour plot (top view of 3-D surface plot)
trace = go.Contour(x=x,y=y,z=z)
data = [trace]
layout = go.Layout(title='Contour Plot')
fig = go.Figure(data,layout)
fig.show()

#subplots [1 figure, multiple axis, diff kind of charts]
from plotly.subplots import make_subplots
fig = make_subplots(rows=2,cols=2)
fig.add_trace(
        go.Scatter(x=[1,2,3,4,5,6],y=[1,1,5,2,6,8]),
        row=1,
        col=1)
fig.add_trace(
        go.Histogram(x=[4,5,2,5,2,5,7,3,4,8,9,1]),
        row=1,
        col=2)
fig.add_trace(
        go.Scatter(x=[1,2,3,4,5,6],y=[1,1,5,2,6,8],mode='markers'),
        row=2,
        col=1)
fig.add_trace(
        go.Histogram(x=[4,5,2,5,2,5,7,3,4,8,9,1]),
        row=2,
        col=2)
fig.update_layout(title='figure_title')
fig.show()

#Plotly supports map data unlike matplotlib or seaborn





###############################################################################################################
#### Plotly Express (px)
###############################################################################################################

import plotly.express as px

df = px.data.tips()                                                 #in-built dataset in px
df = px.data.iris()                                                 #in-built dataset in px
df = px.data.____()                                                 #other in-built datasets in px

#scatter plot
px.scatter(df,
            x='num_col1',
            y='num_col2',
            color='cat_col1',
            size='num_col3',
            size_max=100,
            hover_name='cat_col2')

#scatter plot animation on timeline
px.scatter(df,
            x='num_col1',
            y='num_col2',
            color='cat_col1',
            size='num_col3',
            size_max=100,
            hover_name='cat_col2',
            range_x=[10,100],
            animation_frame='date_col',
            animation_group='cat_col2')

#scatter matrix (just like pair plot in sns)
px.scatter_matrix(iris,
                    dimensions=['sepal_length',
                                'sepal_width',
                                'petal_length',
                                'petal_width'],
                    color='species')

#3-D scatter plot
px.scatter_3d(df,
                x='num_col1',
                y='num_col2',
                z='num_col3',
                log_y=True,
                color='cat_col1',
                hover_name='cat_col2')

#line chart - one line for each column
px.line(df,
            x=df.index,
            y=df.columns,
            title='chart_title')

#bar chart
px.bar(df,
            x='cat_col',
            y='num_col',
            title='chart_title',
            text_auto=True)

#STACKED bar chart with index & multiple cols (default is stacked)
px.bar(df,
            x=df.index,
            y=df.columns,
            title='chart_title',
            text_auto=True)

#STACKED bar chart with cols only
px.bar(df,
            x='cat_col1',
            y='num_col',
            color='cat_col2',
            title='chart_title',
            text_auto=True)

#GROUPED / CLUSTERED bar chart
px.bar(df,
            x=df.index,
            y=df.columns,
            title='chart_title',
            text_auto=True,
            barmode='group',
            log_y=True)

#bar chart animation on timeline
px.bar(df,
            x='cat_col1',
            y='num_col',
            color='cat_col1',
            title='chart_title',
            animation_frame='date_col',
            animation_group='cat_col2',
            range_y=[0,100])

#histogram - multiple histograms for diff categories in `cat_col` on same axis
px.histogram(df,
                x='num_col',
                nbins=20,
                color='cat_col',
                text_auto=True)

#pie chart
px.pie(df,
            values='num_col',
            names='cat_col')

#sunburst plot - Donut around Pie chart (centre=higher heirarchy, circumference=lower heirarchy)
px.sunburst(df,
                path=['continent_col','country_col','state_col'],
                values='num_col',
                color='cat_col3')

#treemap chart
px.treemap(df,
                path=[px.constant('continent_col'),'country_col','state_col'],
                values='num_col',
                color='cat_col3')

#heatmap chart (df has to be grid dataframe)
px.imshow(df)

#facet plots [1 figure, multiple axis, same kind of chart]
px.scatter(df,
                x='num_col1',
                y='num_col2',
                facet_col='cat_col1',
                facet_row='cat_col2',
                color='cat_col3')



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
#### Web Scraping - requests
###############################################################################################################


import requests

#GET: normal request fetching response
response = request.get(uri)

#GET: request with query: all repositories with requests module used using python
uri = "https://api.github.com/search/repositories"
params = {"q":"requests+language:python"}
response = request.get(uri, params=params)

#POST: 
uri = "https://httpbin.org/post"
data = {
	"username": "bruce",
	"password": "bruce123"
}
response = request.post(uri, data=data)
OR
response = request.post(uri, json=data)

#PUT:
uri = "https://httpbin.org/put"
data = {"param1":"value1"}
response = request.put(uri, data=data)

#DELETE:
uri = "https://httpbin.org/delete"
response = request.delete(uri)


#response attributes & methods
response.status_code                    #status_code=200 succesful
response.headers                        #headers from server
response.text                           #response content in string format
response.content                        #response content in binary format
response.json()                         #response content in json format
print(response.raise_for_status())      #error if any


#exception handling in get
uri = "https://jsonplaceholder.typicode.com/posts"
try:
	response = requests.get(uri)
	response.raise_for_status()
except Exception as e:
	print(e)
else:
	status_code = response.status_code
	print(f"Status Code: {status_code}")
	if status_code == 200:
		print("\nSuccessful GET request!")
		posts = response.json()
		for i in range(3):
			print(f"\nPost {i + 1}:")
			print(posts[i])
	else:
		print("Unsuccessful GET request!")







###############################################################################################################
#### Web Scraping - beautifulsoup4
###############################################################################################################
from bs4 import BeautifulSoup

#create soup obj from html file
with open("abc.html") as file:
    soup = BeautifulSoup(file, "html.parser")
#OR create soup obj from direct website
soup = BeautifulSoup(response.content, "html.parser")

soup.prettify()

soup.title                                      #title tag
soup.p                                          #1st paragraph tag
soup.a                                          #1st anchor tag

soup.title.text                                 #title in str form
soup.title.name                                 #label of tag i.e. title in str form
soup.title.parent                               #parent tag

soup.body.get_text(strip=True)                  #print all text in body tag

#print child tags only
for child in soup.body.children:
    print(child)

#print nested children
for descendant in soup.body.descendant:
    print(descendant)

#find 1st occurence of a tag
soup.find('div', class_='<class_name>')
#find all occurences of a particular tag
soup.find_all('div', class_='<class_name>')

#when a particular tag contains multiple attributes in it.
#i.e.
#<a class="sister" href="https://example.com/elsie" id="link1">Elsie</a>
soup.a["class"]                                 #'sister'
soup.a["href"]                                  #"https://example.com/elsie"
soup.a["id"]                                    #"link1"
#OR
soup.a.get('class')                             #"sister"
soup.a.get('href')                              #"https://example.com/elsie"
soup.a.get('id')                                #"link1"



url = "https://jsonplaceholder.typicode.com/posts"
try:
	response = requests.get(url)
	response.raise_for_status()
except Exception as e:
	print(e)
else:
	soup = BeautifulSoup(response.content, "html.parser")
    print("Successful..!!")
    print(soup.prettify())















###############################################################################################################
#### Web Scraping - selenium
###############################################################################################################
pip install requests beautifulsoup4 selenium lxml html5lib webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

#OR -- headless browser instance (No GUI)
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://www.google.com"
driver.get(url)
time.sleep(2)

driver.title                                                        #tab title
driver.current_url                                                  #https://www.google.com
driver.save_screenshot("goog_scr.png")                              #take screenshot of webpage

element = driver.find_element("id","<element id>")                  #fast
element = driver.find_element("name","<element name>")              #fast
element = driver.find_element("class name","<element class id>")
element = driver.find_element("tag name","<element tag>")
element = driver.find_element("xpath","<element xpath link>")       #slow
#OR
from selenium.webdriver.common.by import By
element = driver.find_element(by=By.ID,"<element id>")
element = driver.find_element(by=By.CLASS_NAME,"<element class id>")
element = driver.find_element(by=By.TAG_NAME,"<element tag>")
element = driver.find_element(by=By.XPATH,"<element xpath link>")

#entering Text value in Text Box
txt_element = driver.find_element(by=By.XPATH, "<element xpath link>")
txt_element.clear()                                                     #clear the text box
txt_element.send_keys("machine learning")                               #enter the value "machine learning"

#hitting enter on keyboard
from selenium.webdriver.common.keys import Keys
txt_element.send_keys(Keys.ENTER)

#clicking a button or a link
button = driver.find_element(by=By.XPATH, "<element xpath link>")
button.click()

#selecting value from dropdown
drop_field = driver.find_element(by=By.XPATH, "<element xpath link>")
drop_down = Select(drop_field)
drop_down.select_by_index(5)
drop_down.select_by_visible_text("<any visible value from dropdown>")

#multiselect values
multi_field = driver.find_element(by=By.XPATH, "<element xpath link>")
multi_select = Select(multi_field)
multi_select.select_by_index(1)
multi_select.select_by_visible_text("<any visible value from dropdown>")

multi_select.deselect_by_index(2)
multi_select.deselect_all()

#scrolling a webpage
#scroll to a specific element using scrollIntoView
driver.execute_script("arguments[0].scrollIntoView();",element)
#scroll 1000px down vertically using scrollBy
driver.execute_script("window.scrollBy(0,500);")
#scroll 500px up vertically using scrollBy
driver.execute_script("window.scrollBy(0,-500);")
#scroll down to page bottom using scrollTo
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#scroll up to page top using scrollTo
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
#infinite scrolling 
prev_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    new_height = driver.execute_script('return document.body.scrollHeight')
    if prev_height == new_height:
        break
    prev_height = new_height


#explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 5)
wait.until(EC.element_to_be_clickable((By.XPATH, '<XPATH of button>')))
txt_element.send_keys(Keys.ENTER)

#types of explicit waits
EC.element_to_be_clickable                                          #wait for the button to be enabled
EC.alert_is_present                                                 #wait for a browser alert to pop up
EC.title_is                                                         #wait for page title to match a given value
EC.title_contains                                                   #wait for page title to contain specific text


#implicit wait - waits untill an element is loaded/recognized
#unlike explicit wait code, implicit wait code is written once only
#works for find_element() and find_elements() methods
driver.get(url)
driver.implicitly_wait(5)                                           #wait until element loads or 5 secs


#frames / iframes (another html doc inside an html doc)
iframe_element = driver.find_element(By.XPATH, "<iframe XPATH>")
driver.switch_to.frame(iframe_element)                              #to work with elements in iframe
driver.switch_to.default_content()                                  #to work with parent frame


#handling javascript alerts
#alert()    shows a message & a button with OK
#confirm()  shows a message, two buttons with OK, Cancel
#prompt()   shows a message, takes an input, submits input with OK, submits None with Cancel button
print(driver.switch_to.alert.text)                                  #print alert content
driver.switch_to.alert.accept()                                     #click OK
driver.switch_to.alert.dismiss()                                    #click Cancel
driver.switch_to.alert.send_keys("text123")                         #enter text into alert text box
driver.switch_to.default_content()                                  #to work with parent frame


#OOP scraping technique
driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.google.com"
driver.get(url)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.XPATH, "<XPATH of username field>")
        self.password = (By.XPATH, "<XPATH of password field>")
        self.login_button = (By.XPATH, "<XPATH of login button>")
    
    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

login_page = LoginPage(driver)
login_page.login("user_1", "password1")



driver.quit()                                                       #close browser









###############################################################################################################
#### Web Scraping - CAPTCHA Handling
###############################################################################################################
import cv2                              #image preprocessing library
import time
import pytesseract                      #OCR library
import numpy as np

from PIL import Image                   #image basic library
from selenium import webdriver
from selenium.webdriver.common.by import By

#handling CAPTCHA manually
driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.hackthissite.org/user/login'
driver.get(url)
time.sleep(2)

username_field = driver.find_element(By.ID, 'login_username')
password_field = driver.find_element(By.ID, 'login_password')
login_button = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td/input')

username_field.send_keys('abc')
password_field.send_keys('1234')
login_button.click()

captcha_xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[5]/td/img'
captcha_element = driver.find_element(By.XPATH, captcha_xpath)
if captcha_element:
	x = input('This will halt the script.. solve your Captcha..')

print('\nCaptcha handled! Write rest of the script..')
time.sleep(1)
driver.quit()


#handling CAPTCHA automatically using TESSERACT
#installation path of tesseract application
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.hackthissite.org/user/login'
driver.get(url)
time.sleep(2)

username_field = driver.find_element(By.ID, 'login_username')
password_field = driver.find_element(By.ID, 'login_password')
login_button = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td/input')

username_field.send_keys('abc')
password_field.send_keys('1234')
login_button.click()
time.sleep(5)

try:
    captcha_xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[5]/td/img'
    captcha_image = driver.find_element(By.XPATH, captcha_xpath)
    driver.save_screenshot('webpage.png')

    location = captcha_image.location
    size = captcha_image.size
    device_pixel_ratio = driver.execute_script("return window.devicePixelRatio;")
    x = int(location['x'] * device_pixel_ratio)
    y = int(location['y'] * device_pixel_ratio)
    w = int(size['width'] * device_pixel_ratio)
    h = int(size['height'] * device_pixel_ratio)

    img = Image.open('webpage.png')
    captcha_image = img.crop((x, y, x + w, y + h))
    captcha_image.save('captcha.png')

    captcha_cv = np.array(captcha_image)
    captcha_cv = cv2.cvtColor(captcha_cv, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(captcha_cv, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 3)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((2, 2), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=1)
    cv2.imwrite('captcha-processed.png', thresh)

    captcha_text = pytesseract.image_to_string(Image.fromarray(thresh), config='--psm 8').strip()
    print(f'Detected captcha text: {captcha_text}')

    if captcha_text:
        username_field = driver.find_element(By.ID, 'login_username')
        password_field = driver.find_element(By.ID, 'login_password')
        captcha_field = driver.find_element(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/form[1]/table[1]/tbody[1]/tr[4]/td[2]/input[1]')
        login_button = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td/input')

        username_field.clear()
        password_field.clear()
        captcha_field.clear()

        username_field.send_keys('abc')
        password_field.send_keys('1234')
        captcha_field.send_keys(captcha_text)
        login_button.click()
    else:
        print('Unable to read Captcha.')
		
except Exception as e:
    print('Unable to locate Captcha:', e)
	
finally:
    time.sleep(2)
    driver.quit()












###############################################################################################################
#### Web Scraping - scrapy
###############################################################################################################

import scrapy

#create project folder structure
#in terminal
scrapy startproject <proj_name>

#Adding a new website to scrape         -       add a new file in spiders/
#changing export format                 -       settings.py
#Validating data                        -       pipelines.py
#dealing with CAPTCHAs or blocking      -       middlewares.py
#Testing a single spider                -       scrapy crawl spider_name
#reusing data structures                -       define once in items.py & use across spiders

#creating a spider (scraper) in spiders folder 
#terminal in project folder
scrapy genspider spider_name website_url

#create code i.e.
def parse(self, response):
    yield('response':response)

#run the spider and save the json
scrapy crawl spider_name -o output.json

















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
#### cmd
###############################################################################################################
#1) Windows not genuine watermark removal:
bcdedit -set TESTSIGNING OFF;
or
slmgr /rearm
or
irm https://get.activated.win | iex

#2) get disk names
wmic logicaldisk get name

#3) Make Backup using cmd:
robocopy <source> <destination> /E /Z /DCOPY:DAT;
#OR
#max speed, use all threads, copy everything, with timestamp:
robocopy <source> <destination> /E /MT:64 /R:3 /W:3 /NP /A-:SH /DCOPY:DAT /COPYALL 
#OR
#exclude recycle bin content:
robocopy <source> <destination> /E /MT:64 /R:3 /W:3 /NP /A-:SH /DCOPY:DAT /COPYALL /XD "$RECYCLE.BIN" 
#OR
#unhide folder:
attrib -s -h <folder_path>
#OR
#parallel thread copying:
robocopy <source> <destination> /E /MT:64 /R:3 /W:3 /NFL /NDL

#4) Check battery health:
powercfg /batteryreport;

#5) Wifi Pw:
netsh wlan show profile;
netsh wlan export profile <profile name> folder=C:\ key=clear;

#6) remove temp files:
del /q/f/s %temp%\*

#7) download youtube videos in highest available quality
winget install yt-dlp;
yt-dlp "youtube_video_link";

#8) check windows assessment score [Win Power Shell only]:
winsat formal;
get-ciminstance win32_winsat;





###############################################################################################################
#### GIT
###############################################################################################################
git config --global user.name "Gaurav Singh"
git config --global user.email "grv08singh@gmail.com"
git config --list --global

git clone https://github.com/grv08singh/02_mlprojects.git
git clone https://github.com/grv08singh/03_g_translator.git
git clone https://github.com/grv08singh/04_st_startups.git
git clone https://github.com/grv08singh/05_selenium_ktk_v1.git
git clone https://github.com/grv08singh/06_selenium_ktk_v2.git
git clone https://github.com/grv08singh/07_st_censusDA.git
git clone https://github.com/grv08singh/01_Docs.git