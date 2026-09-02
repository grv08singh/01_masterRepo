# AWS : 
# Root User
# 
# Account name
# grv08singh
# 
# AWS account ID
# 676206921654
# 
# Email address
# grv08singh@gmail.com
# 
# Canonical user ID
# f739ae74a5939eb618aed0b1ce6fb5b1946e95f9a1083dfbdc014a6e326cef90
# 
# MFA Device Name for google authenticator
# aws_grv08singh



#linkedin
#https://www.linkedin.com/in/grv08singh


#Power BI: Divya@intellipaatsoft.onmicrosoft.com / Hadoop#4585

#E97550 #1D78B7 #0F5989 #FACE0F

# WSL2 Ubuntu
cd 
jupyter notebook --no-browser --notebook-dir='/mnt/d/05 GIT/18_NLP_DuplicateQuestionPair/notebooks'
jupyter notebook --no-browser --notebook-dir='/mnt/f/Grv/Grv/05 GIT/01_masterRepo/01_My_Learnings/02_Python/05_NLP'


jupyter lab --no-browser --notebook-dir='/mnt/d/05 GIT/01_masterRepo/01_My_Learnings/02_Python/05_NLP'
jupyter lab --no-browser --notebook-dir='/mnt/f/Grv/Grv/05 GIT/01_masterRepo/01_My_Learnings/02_Python/05_NLP'



# Windows
jupyter notebook --notebook-dir="C:\Users\Dex\Desktop\TN WP 2026-27"
jupyter notebook --notebook-dir="D:\05 GIT\01_masterRepo\01_My_Learnings\02_Python\05_NLP"
jupyter lab --notebook-dir="D:\05 GIT\01_masterRepo\01_My_Learnings\02_Python\05_NLP"







#### production ready project steps:
01) Create GitHub repository & clone it onto local.
02) Open VS Code in project repo.
03) Create a Python Environment and activate it.
04) Add Python env path to .gitignore
05) Create template.py and run it
06) write README.md
07) write code for logger and CustomException
08) write code for setup.py
09) write requirements.txt and do pip install -r requirements.txt
10) write source code
11) write app.py code





Projects:
    ML:
        1) 99Acres data:
            1) Price Prediction
            2) Apartment Recommendation
            3) Analytics
    DL:
        2) Real Time Object Detection
        3) Medical Image Analysis
        4) DeepFake Video detection
    GenAI:
        5) Eng-Hin Translator
        6) RAG based Organization chatbot


ML Project Checklist:
    1) Problem Statement
    2) Data Collection
        2.1) Import Data and Required Packages
        2.2) Dataset Info
    3) Data Checks
        3.1) Import numpy, pandas
        3.2) Import dataset from csv (df = pd.read_csv('file_name.csv')
        3.3) Check Missing Values - df.isna.sum()
        3.4) Check Duplicates - df.duplicated(), df.drop_duplicates()
        3.5) Check data type - df.info()
        3.6) Check number of unique values of each column - df.nunique()
        3.7) Check statistics of dataset - df.describe()
        3.8) Check various categories present in different categorical columns - df['col1'].unique(), df['col1'].value_counts()
        3.9) Use Pandas Dataset Profiling for further inspection of data
    4) Exploratory Data Analysis (Visualization)
        4.1) Import numpy, pandas, matplotlib, seaborn, plotly
        4.2) Import dataset from csv
        4.3) Numerical Features: Visualize Mean (Avg.)/ Median/ Mode on Histograms/ KDE for frequency distribution
        4.4) Categorical Features: Visualize if data is balanced or not
        4.5)  
    5) Model Building
        5.01) Import numpy, pandas, sklearn, catboost, xgboost
        5.02) Import dataset from csv
        5.03) X-y split
        5.04) Create ColumnTransformer for Encoding, Scaling, Imputing missing values
                from sklearn.compose import ColumnTransformer
                num_features = df.select_dtypes(exclude='object').columns           #numerical features
                cat_features = df.select_dtypes(include='object').columns           #categorical features
                ssc_tnf = StandardScaler()
                ohe_tnf = OneHotEncoder(drop='First', sparse=False)
                ord_tnf = OrdinalEncoder(categories=[['low','medium','high']])

                ct = ColumnTransformer(
                        transformers=[
                            ('tnf1', ssc_tnf, num_features),
                            ('tnf2', ohe_tnf, cat_features),
                            ('tnf3', ord_tnf, ['col1']),
                            ('tnf4', SimpleImputer(), ['col4'])
                        ],
                        remainder = 'passthrough'))
                ct.fit_transform(df)
        5.05) Train-Test split
        5.06) Create an Evaluation Method for after training evaluation on test data
                def evaluate_model(y_test, y_pred):
                    mae = mean_absolute_error(y_test, y_pred)
                    mse = mean_squared_error(y_test, y_pred)
                    rmse = np.sqrt(mse)
                    r2_val = r2_score(y_test, y_pred)
                    return mae, mse, rmse, r2_val
        5.07) Create a list of models
                models = {
                    'Linear Regression': LinearRegression(),
                    'Ridge Regression': Ridge(),
                    'Lasso Regression': Lasso(),
                    'KNN Regressor': KNeighborsRegressor(),
                    'Decision Tree': DecisionTreeRegressor(),
                    'Random Forest': RandomForestRegressor(),
                    'Gradient Boosting': GradientBoostingRegressor(),
                    'Ada Boost': AdaBoostRegressor(),
                    'SVM': SVR(),
                    'XGBoost': XGBRegressor(),
                    'CatBoost': CatBoostRegressor(verbose=False)
                }
        5.08) 
        5.09) 
        5.10) 








###############################################################################################################
#### LangChain - Everything
###############################################################################################################
# --- Model Provider Keys (Choose what you use) ---
OPENAI_API_KEY=your_actual_openai_api_key_here
ANTHROPIC_API_KEY=your_actual_anthropic_api_key_here
GOOGLE_API_KEY=your_actual_gemini_api_key_here

# --- LangSmith Tracing & Observability (Optional) ---
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=my-langchain-app

##################################################################
# LLM Invoking
##################################################################
import os
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace, HuggingFacePipeline

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

#for api based LLMs
load_dotenv()

#1) Paid Cloud LLM
#Unified Initializer (Recommended) - dynamic way
model = init_chat_model("google_genai:gemini-3.7-flash")

#static way
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')                          #Gemini
model = ChatAnthropic(model='claude-3-5-sonnet-20241022')                       #Claude
model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)    #OpenAI
model = ChatOllama(model="tinyllama", temperature=0.7)                          #Ollama    

#2) Free Cloud LLM
llm = HuggingFaceEndpoint(
            repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            task="text-generation"
        )
model = ChatHuggingFace(llm=llm)

#3) Free Local LLM
os.environ['HF_HOME'] = 'D:/huggingface_cache'
llm = HuggingFacePipeline.from_model_id(
            model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
            task='text-generation',
            pipeline_kwargs=dict(
                temperature=0.5,
                max_new_tokens=100
            )
        )
model = ChatHuggingFace(llm=llm)


#Querying LLM model
prompt = 'What is the capital of India'
result = model.invoke(prompt)
print(result.content)


#keeping chat history
messages=[
            SystemMessage(content='You are a helpful assistant'),
            HumanMessage(content='Tell me about LangChain')
        ]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))









##################################################################
# LangChain Prompts
##################################################################
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder

#1)Create Simple Text Only Prompt - using PromptTemplate
template = "Write a poem about {topic}."
prompt_template = PromptTemplate(template=template, input_variables=["topic"], validate_template=True)
prompt_template.save('template.json')
prompt = prompt_template.format(topic="AI")                 #output: 'Write a poem about AI.'
or
prompt = prompt_template.invoke({'topic': 'AI'})            #ouput: StringPromptValue(text='Write a poem about AI.')


#2)Create Structured Prompt - using ChatPromptTemplate
chat_prompt_template = ChatPromptTemplate([
                            ("system", "You are a helpful poetic assistant. You only reply in rhyming poems."),
                            ("human", "Write a poem about {topic}.")
                        ])
prompt = chat_prompt_template.format_messages(topic="AI")   #list of messages
or
prompt = chat_prompt_template.invoke({'topic':'AI'})        #ChatPromptValue object having list of messages    










##################################################################
# with Structured Output
##################################################################

# set output structure using json schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

# set output structure using pydantic model base class
from pydantic import BaseModel, Field
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model = model.with_structured_output(json_schema)
or
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(prompt)









##################################################################
# HuggingFace LLMs
##################################################################
import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage

repo_id = "google/gemma-4-31B-it"
llm = HuggingFaceEndpoint(
            repo_id=repo_id,
            task="text-generation", # Required for ChatHuggingFace mapping
            max_new_tokens=512,
            temperature=0.7,
            do_sample=True,
        )
model = ChatHuggingFace(llm=llm)
messages = [
                SystemMessage(content="You are an expert, concise coding assistant."),
                HumanMessage(content="Write a Python list comprehension that filters out negative numbers.")
            ]
result = model.invoke(messages)
print(result.content)















##################################################################
# Output Parsers
##################################################################
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field

#1) step 1
#for json, pydantic, string output parser
class CustomSchema(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")

#2) step 2
parser = JsonOutputParser(pydantic_object=CustomSchema)             #json output parser
or
parser = PydanticOutputParser(pydantic_object=CustomSchema)         #pydantic output parser
or
parser = StrOutputParser()                                          #string output parser

#3) step 3
template = PromptTemplate(
                template='Give 3 fact about {topic} \n {format_instruction}',
                input_variables=['topic'],
                partial_variables={'format_instruction':parser.get_format_instructions()}   #for json and pydantic only, wont work with string
            )

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})
print(result)








##################################################################
# Embedding Models
##################################################################
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

emb_model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)                #OpenAI
emb_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')      #HuggingFace

#single query
query = "Delhi is the capital of India"
result = emb_model.embed_query(query)

#vector query
documents = [
                "Delhi is the capital of India",
                "Kolkata is the capital of West Bengal",
                "Paris is the capital of France"
            ]
result_vector = emb_model.embed_documents(documents)

#Finding Cosine Similarity
scores = cosine_similarity([result], result_vector)[0]
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("similarity score is:", score)












        








        


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








###############################################################################################################
#### streamlit - st online cloud deployment
###############################################################################################################
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_overall_analysis():
    st.title('Overall Analysis')
    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    # total funded startups
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Total',str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')
    with col3:
        st.metric('Avg',str(round(avg_funding)) + ' Cr')
    with col4:
        st.metric('Funded Startups',num_startups)

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig3)


def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    with col2:
        verical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series,labels=verical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)
        
    print(df.info())
    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('YoY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)
    st.pyplot(fig2)



st.set_page_config(layout='wide',page_title='StartUp Analysis')
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])
if option == 'Overall Analysis':
    load_overall_analysis()
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select StartUp',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
 



##########################################################

import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('Salman Khan!')

st.write('This is a normal text')

st.markdown("""
### My favorite movies
- Race 3
- Humshakals
- Housefull
""")

st.code("""
def foo(input):
    return foo**2

x = foo(2)
""")

st.latex('x^2 + y^2 + 2 = 0')
df = pd.DataFrame({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})
st.dataframe(df)
st.metric('Revenue', 'Rs 3L', '-3%')
st.json({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})
st.image('unnamed.jpg')
st.video('Task12.m4v')
st.sidebar.title('Sidebar ka Title')
col1, col2, col3 = st.columns(3)
with col1:
    st.image('unnamed.jpg')
with col2:
    st.image('unnamed.jpg')
with col3:
    st.image('unnamed.jpg')
st.error('Login Failed')
st.success('Login Successful')
st.info('Login Successful')
st.warning('Login Successful')
bar = st.progress(0)
for i in range(1, 101):
    bar.progress(i)
email = st.text_input('Enter email')
number = st.number_input('Enter age')
st.date_input('Enter regis date')
email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender',['male','female','others'])
btn = st.button('Login Karo')

# if the button is clicked
if btn:
    if email == 'nitish@gmail.com' and password == '1234':
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')
file = st.file_uploader('Upload a csv file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())







###############################################################################################################
#### GenAI
###############################################################################################################
import google.generativeai as genai
genai.configure(api_key=<__________>)
available_models = genai.list_models()
print("Available models:")
for model in available_models:
    print(model.name)












###############################################################################################################
#### Python Dependencies - pip/conda install
###############################################################################################################

base:
    pip install numpy pandas matplotlib seaborn plotly scipy statsmodels scikit-learn xgboost imbalanced-learn mlxtend emoji contractions nltk openpyxl pyodbc kaggle

gpu_tf:
    

gpu_pytorch:
    

pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install plotly

pip install scipy
pip install statsmodels

pip install scikit-learn
pip install xgboost
pip install imbalanced-learn
pip install mlxtend

conda install tensorflow
pip install nltk
pip install contractions
pip install emoji

pip install requests
pip install beautifulsoup4
pip install selenium
pip install scrapy
pip install lxml
pip install html5lib

pip install Pillow
pip install pytesseract
pip install opencv-python

pip install openpyxl
pip install pyodbc
pip install kaggle
conda install -c conda-forge opencv

pip install langchain
pip install langchain-community
pip install langchain_openai
pip install langchain_chroma

pip install google-generativeai






pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install plotly
pip install scikit-learn
pip install tensorflow
pip install PyTorch
pip install contractions
pip install spacy
pip install nltk
pip install emoji
pip install gensim
pip install tqdm
pip install distance
pip install fuzzywuzzy
pip install xgboost
pip install optuna
pip install catboost
pip install langchain
pip install langgraph
pip install imblearn
pip install streamlit
pip install textblob
pip install collections
pip install mlxtend
pip install scipy
pip install statistics
pip install statsmodel
pip install kaggle















###############################################################################################################
#### Python Imports
###############################################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

#### Machine Learning (ML): sci-kit learn, xgboost, imblearn
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder,StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV,RandomizedSearchCV
from imblearn.over_sampling import SMOTE                #SMOTE - Synthetic Minority Oversampling Technique

from sklearn.linear_model import LinearRegression,LogisticRegression,SGDRegressor,SGDClassifier,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier,GradientBoostingRegressor,GradientBoostingClassifier
from sklearn.svm import SVR,SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import r2_score,accuracy_score,roc_auc_score,precision_score,recall_score,f1_score
                            ,confusion_matrix,ConfusionMatrixDisplay,classification_report
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import SelectKBest, chi2

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline

from xgboost import XGBRegressor, XGBClassifier


####Deep Learning (DL): tensorflow, keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist,fashion_mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import TensorBoard, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, Activation, Embedding
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.preprocessing.text import Tokenizer
from keras.layers import TextVectorization
from keras.preprocessing.sequence import pad_sequences








###############################################################################################################
#### GenAI (LangChain) - Build a Chatbot
###############################################################################################################
import os
from langchain_chroma import Chroma                                     #Database Setup
from langchain_core.prompts import PromptTemplate                       #to give instructions to LLM
from langchain_openai import ChatOpenAI, OpenAIEmbeddings               #to load encoder and model
from langchain_text_splitters import CharacterTextSplitter              #to divide text file into smaller chunks
from langchain_core.runnables import RunnablePassthrough                #to take input from user
from langchain_core.output_parsers.string import StrOutputParser        #to format the output























###############################################################################################################
#### Generative AI (GenAI) - LSTM based Encoder Decoder in Keras - Eng to French Translation
###############################################################################################################
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input,LSTM,Embedding,Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

eng = ['hi','hello','how are you','thank you']
fr = ['salut','bonjour','comment ca va','merci']

#tokenize english
tok_eng = Tokenizer()
tok_eng.fit_on_texts(eng)
x = tok_eng.texts_to_sequences(eng)
x = pad_sequences(x)

#tokenize french
tok_fr = Tokenizer()
tok_fr.fit_on_texts(fr)
y = tok_fr.texts_to_sequences(fr)
y = pad_sequences(y)

y_in = y[:,:-1]
y_out = y[:,1:]

#lstm - 3d - (samples,timesteps,vocab_size)
#our labels must be in 3d shape as well
#3d - adding 1 to it at the end
y_out = y_out.reshape((y_out.shape[0],y_out.shape[1],1))

vocab_eng = len(tok_eng.word_index)+1
vocab_fr = len(tok_fr.word_index)+1

#encoder
enc_in =Input(shape =(x.shape[1],))                 #each english input seq
enc_emb = Embedding(vocab_eng,8)(enc_in)            #learn word embeddings
_,h,c  = LSTM(32,return_state= True)(enc_emb)       #_ is output, h is hidden state, c is candidate state

#decoder
dec_in= Input(shape =(y_in.shape[1],))
dec_emb = Embedding(vocab_fr,8)(dec_in)
dec_out = LSTM(32, return_sequences=True)(dec_emb,initial_state =[h,c])
out = Dense(vocab_fr ,activation= 'softmax')(dec_out)

#build, compile model
model = Model([enc_in,dec_in],out)
model.compile(optimizer = 'adam',loss ='sparse_categorical_crossentropy')

#train
model.fit([x,y_in],y_out,epochs = 300)

#predict
preds = model.predict([x,y_in])
for i,pred in enumerate(preds):
  ids = np.argmax(pred,axis = 1)
  words = [tok_fr.index_word.get(idx, "??") for idx in ids]
  print(f"English : {eng[i]} ----> pred french: {' '.join(words)}")

#return_state ---> give h,c state as well along with output
#resturn_sequences ---> tell LSTM to output at every time step ,not just at the end







###############################################################################################################
#### Generative AI (GenAI) - LSTM based EncDec in Keras - Eng to Hindi Translation
###############################################################################################################
#%%
import numpy as np
import pandas as pd
import re
import pickle
import json
import time
import os
import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense, Layer, Input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#%%
tf.random.set_seed(42)
np.random.seed(42)
#%%
df = pd.read_csv("Dataset_English_Hindi.csv")
df.drop_duplicates(inplace=True)
df = df.dropna()
df["English"] = df["English"].astype(str)
df["Hindi"]   = df["Hindi"].astype(str)
print(f"Total pairs: {len(df)}")
#%%
def clean_english(sentence):
    sentence = sentence.lower().strip()
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
    sentence = re.sub(r'https?://\S+|www\.\S+', '', sentence)
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    sentence = emoji_pattern.sub(r'', sentence)
    return sentence.strip()
#%%
def clean_hindi(sentence):
    sentence = sentence.strip()
    sentence = re.sub(r'[^\u0900-\u097F\s]', '', sentence)
    sentence = re.sub(r'https?://\S+|www\.\S+', '', sentence)
    return sentence.strip()
#%%
df["English"] = df["English"].apply(clean_english)
df["Hindi"]   = df["Hindi"].apply(clean_hindi)
#%%
# Filter by sentence length for efficient training
MAX_ENG_WORDS = 25
MAX_HIN_WORDS = 30
mask = (
    df["English"].str.split().str.len().between(5, MAX_ENG_WORDS) &
    df["Hindi"].str.split().str.len().between(5, MAX_HIN_WORDS)
)
df = df[mask].reset_index(drop=True)
print(f"Pairs after length filter: {len(df)}")
#%%
# Add <start> / <end> tokens to Hindi
df["Hindi_in"]  = "<sos> " + df["Hindi"]          # decoder input
df["Hindi_out"] = df["Hindi"] + " <eos>"          # decoder target
#%%
# English tokenizer
eng_tok = Tokenizer(filters="", lower=True, oov_token="<OOV>")
eng_tok.fit_on_texts(df["English"])
ENG_VOCAB = len(eng_tok.word_index) + 1
#%%
# Hindi tokenizer  (case-sensitive for Devanagari)
hin_tok = Tokenizer(filters="", lower=False, oov_token="<OOV>")
hin_tok.fit_on_texts(df["Hindi_in"].tolist() + df["Hindi_out"].tolist())
HIN_VOCAB = len(hin_tok.word_index) + 1
#%%
print(f"English vocab: {ENG_VOCAB}  |  Hindi vocab: {HIN_VOCAB}")
#%%
df_enc_inp = pad_sequences(
    eng_tok.texts_to_sequences(df["English"]),
    maxlen = MAX_ENG_WORDS, padding="post"
)
df_dec_inp = pad_sequences(
    hin_tok.texts_to_sequences(df["Hindi_in"]),
    maxlen = MAX_HIN_WORDS + 1, padding="post"
)
df_dec_out = pad_sequences(
    hin_tok.texts_to_sequences(df["Hindi_out"]),
    maxlen = MAX_HIN_WORDS + 1, padding="post"
)
#%%
ENG_SEQ_LEN = df_enc_inp.shape[1]
HIN_SEQ_LEN = df_dec_inp.shape[1]
print(f"Encoder seq len: {ENG_SEQ_LEN}  |  Decoder seq len: {HIN_SEQ_LEN}")
print(f"df_enc_inp shape: {df_enc_inp.shape}")
print(f"df_dec_out shape: {df_dec_out.shape}")
#%%
#Model Hyper Parameters
EMBED_DIM = 512
BATCH_SIZE = 32
EPOCHS = 50
#%%
#Encoder
enc_input = Input(shape=(ENG_SEQ_LEN,))
enc_embed = Embedding(ENG_VOCAB, EMBED_DIM)(enc_input)
enc_lstm = LSTM(EMBED_DIM, return_state=True)
enc_out, enc_h, enc_c = enc_lstm(enc_embed)
enc_model = Model(enc_input, [enc_out, enc_h, enc_c])
#%%
#Decoder
dec_input = Input(shape=(HIN_SEQ_LEN,))
dec_embed  = Embedding(HIN_VOCAB, EMBED_DIM, name="dec_embedding")(dec_input)
dec_lstm = LSTM(EMBED_DIM, return_sequences=True, return_state=True)
dec_out, dec_h, dec_c = dec_lstm(dec_embed, initial_state=[enc_h, enc_c])
dec_dense  = Dense(HIN_VOCAB, activation='softmax', name="dec_dense")(dec_out)
#%%
#Model
model = Model([enc_input, dec_input], dec_dense)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
#%%
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
early_stopping = EarlyStopping(monitor='accuracy', patience=5, restore_best_weights=True)
#%%
#Training
history = model.fit(
    x=[df_enc_inp, df_dec_inp],
    y=df_dec_out,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    callbacks = [early_stopping]
)
#%%
#model.save("my_model.keras")
#model.save_weights("my_model.weights.h5")
#with open("my_model_architecture.json", 'w') as f:
#    f.write(model.to_json())

history_df = pd.DataFrame(history.history)
history_df.index      = range(1, len(history_df) + 1)   # epochs start from 1
history_df.index.name = "epoch"
history_df.to_csv("training_history.csv")
#%%
#Inference
encoder_inf_model = Model(enc_input, [enc_h, enc_c])
dec_emb_layer   = model.get_layer("dec_embedding")
dec_dense_layer = model.get_layer("dec_dense")

dec_inf_input   = Input(shape=(1,))
dec_state_inp_h = Input(shape=(EMBED_DIM,))
dec_state_inp_c = Input(shape=(EMBED_DIM,))

dec_inf_embed = dec_emb_layer(dec_inf_input)
dec_inf_out, dec_inf_h, dec_inf_c = dec_lstm(dec_inf_embed, initial_state=[dec_state_inp_h, dec_state_inp_c])
dec_inf_dense = dec_dense_layer(dec_inf_out)

decoder_inf_model = Model(
    inputs  = [dec_inf_input, dec_state_inp_h, dec_state_inp_c],
    outputs = [dec_inf_dense, dec_inf_h, dec_inf_c]
)
#%%
#Translate
hin_idx2word = {idx: word for word, idx in hin_tok.word_index.items()}
sos_token    = hin_tok.word_index["<sos>"]
eos_token    = hin_tok.word_index["<eos>"]
#%%
def translate(english_sentence, max_len=MAX_HIN_WORDS):
    # Step 1: Clean and pad English input
    eng_clean = clean_english(english_sentence)
    eng_seq   = eng_tok.texts_to_sequences([eng_clean])
    eng_pad   = pad_sequences(eng_seq, maxlen=ENG_SEQ_LEN, padding="post")

    # Step 2: Encode → get initial states
    h, c = encoder_inf_model.predict(eng_pad, verbose=0)

    # Step 3: Start decoding with <sos>
    target_token    = np.zeros((1, 1))
    target_token[0, 0] = sos_token

    translated = []

    # Step 4: Decode one token at a time
    for _ in range(max_len):
        pred, h, c = decoder_inf_model.predict(
            [target_token, h, c], verbose=0
        )

        predicted_id   = np.argmax(pred[0, 0, :])
        predicted_word = hin_idx2word.get(predicted_id, "")

        if predicted_id == eos_token or predicted_word == "":
            break

        translated.append(predicted_word)
        target_token[0, 0] = predicted_id   # feed output as next input

    return " ".join(translated)
#%%
#Test
test_sentences = [
    "How are you doing today",
    "I want to eat food",
    "The weather is very cold outside",
    "She is going to the market",
    "My name is Rahul",
    "I love my country",
    "He is a very good student",
    "Please open the door",
    "I am feeling very tired today",
    "The dog is running in the park",
    "Can you help me please",
    "I want to drink water",
    "She loves to read books",
    "The sun rises in the east",
    "I go to school every day",
    "He does not like cold weather",
    "We are going to the temple",
    "The train is very late today",
    "I want to sleep now",
    "My mother cooks very delicious food"
]

for s in test_sentences:
    print(f"English : {s}")
    print(f"Hindi   : {translate(s)}")
    print("-" * 40)
#%%












###############################################################################################################
#### Generative AI (GenAI) - LSTM based EncDec in Keras with Bahdanau Attention - Eng to Hindi Translation
###############################################################################################################
#%%
import numpy as np
import pandas as pd
import re
import pickle
import json
import time
import os
import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense, Layer, Input, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#%%
tf.random.set_seed(42)
np.random.seed(42)
#%%
df = pd.read_csv("Dataset_English_Hindi.csv")
df.drop_duplicates(inplace=True)
df = df.dropna()
df["English"] = df["English"].astype(str)
df["Hindi"]   = df["Hindi"].astype(str)
print(f"Total pairs: {len(df)}")
#%%
def clean_english(sentence):
    sentence = sentence.lower().strip()
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
    sentence = re.sub(r'https?://\S+|www\.\S+', '', sentence)
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    sentence = emoji_pattern.sub(r'', sentence)
    return sentence.strip()
#%%
def clean_hindi(sentence):
    sentence = sentence.strip()
    sentence = re.sub(r'[^\u0900-\u097F\s]', '', sentence)
    sentence = re.sub(r'https?://\S+|www\.\S+', '', sentence)
    return sentence.strip()
#%%
df["English"] = df["English"].apply(clean_english)
df["Hindi"]   = df["Hindi"].apply(clean_hindi)
#%%
# Filter by sentence length for efficient training


MAX_ENG_WORDS = 25
MAX_HIN_WORDS = 30


mask = (
    df["English"].str.split().str.len().between(5, MAX_ENG_WORDS) &
    df["Hindi"].str.split().str.len().between(5, MAX_HIN_WORDS)
)
df = df[mask].reset_index(drop=True)
print(f"Pairs after length filter: {len(df)}")
#%%
# Add <start> / <end> tokens to Hindi
df["Hindi_in"]  = "<sos> " + df["Hindi"]          # decoder input
df["Hindi_out"] = df["Hindi"] + " <eos>"          # decoder target
#%%
# English tokenizer
eng_tok = Tokenizer(filters="", lower=True, oov_token="<OOV>")
eng_tok.fit_on_texts(df["English"])
ENG_VOCAB = len(eng_tok.word_index) + 1
#%%
# Hindi tokenizer  (case-sensitive for Devanagari)
hin_tok = Tokenizer(filters="", lower=False, oov_token="<OOV>")
hin_tok.fit_on_texts(df["Hindi_in"].tolist() + df["Hindi_out"].tolist())
HIN_VOCAB = len(hin_tok.word_index) + 1
#%%
print(f"English vocab: {ENG_VOCAB}  |  Hindi vocab: {HIN_VOCAB}")
#%%
df_enc_inp = pad_sequences(
    eng_tok.texts_to_sequences(df["English"]),
    maxlen = MAX_ENG_WORDS, padding="post"
)
df_dec_inp = pad_sequences(
    hin_tok.texts_to_sequences(df["Hindi_in"]),
    maxlen = MAX_HIN_WORDS + 1, padding="post"
)
df_dec_out = pad_sequences(
    hin_tok.texts_to_sequences(df["Hindi_out"]),
    maxlen = MAX_HIN_WORDS + 1, padding="post"
)
#%%
ENG_SEQ_LEN = df_enc_inp.shape[1]
HIN_SEQ_LEN = df_dec_inp.shape[1]
print(f"Encoder seq len: {ENG_SEQ_LEN}  |  Decoder seq len: {HIN_SEQ_LEN}")
print(f"df_enc_inp shape: {df_enc_inp.shape}")
print(f"df_dec_out shape: {df_dec_out.shape}")
#%%
#Model Hyper Parameters
EMBED_DIM = 512
BATCH_SIZE = 32
EPOCHS = 50
#%%
#as Keras doesn't have an in-built Bahdanau Attention Class
#here is a custom class for the same
class BahdanauAttention(Layer):
    def __init__(self, units, **kwargs):
        super().__init__(**kwargs)
        self.units = units
        self.W1 = Dense(units, name="attn_W1")   # projects encoder states
        self.W2 = Dense(units, name="attn_W2")   # projects decoder states
        self.V  = Dense(1,     name="attn_V")    # scalar score per enc step

    def call(self, query, values):
        # query  : (batch, dec_len, EMBED_DIM)  — decoder hidden states
        # values : (batch, enc_len, EMBED_DIM)  — encoder hidden states

        # Expand for broadcasting over both sequence axes
        query_exp  = tf.expand_dims(query,  2)   # (batch, dec_len, 1,       EMBED_DIM)
        values_exp = tf.expand_dims(values, 1)   # (batch, 1,       enc_len, EMBED_DIM)

        # score : (batch, dec_len, enc_len)
        score = self.V(tf.nn.tanh(self.W1(values_exp) + self.W2(query_exp)))
        score = tf.squeeze(score, axis=-1)

        # Softmax over the encoder-length axis
        attn_weights = tf.nn.softmax(score, axis=-1)   # (batch, dec_len, enc_len)

        # Weighted sum of encoder states → context
        context = tf.matmul(attn_weights, values)      # (batch, dec_len, EMBED_DIM)
        return context, attn_weights

    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config
#%%
#Encoder Model
enc_input = Input(shape=(ENG_SEQ_LEN,), name="enc_input")

enc_embedding_layer = Embedding(ENG_VOCAB, EMBED_DIM, name="enc_embedding") #shared layer
enc_embed = enc_embedding_layer(enc_input)

enc_lstm = LSTM(EMBED_DIM, return_sequences=True, return_state=True, name="enc_lstm") #shared layer
enc_out, enc_h, enc_c = enc_lstm(enc_embed)

enc_model = Model(enc_input, [enc_out, enc_h, enc_c])
#%%
#Decoder Model
dec_input = Input(shape=(HIN_SEQ_LEN,), name="dec_input")

dec_embedding_layer = Embedding(HIN_VOCAB, EMBED_DIM, name="dec_embedding") #shared layer
dec_embed = dec_embedding_layer(dec_input)

dec_lstm = LSTM(EMBED_DIM, return_sequences=True, return_state=True, name="dec_lstm") #shared layer
dec_out, dec_h, dec_c = dec_lstm(dec_embed, initial_state=[enc_h, enc_c])

#dec_dense  = Dense(HIN_VOCAB, activation='softmax', name="dec_dense")(dec_out)
#%%
#Bahdanau Attention Model
attn_layer = BahdanauAttention(EMBED_DIM, name="bahdanau_attention") #shared layer
context_vector, _ = attn_layer(dec_out, enc_out)

concat_layer = Concatenate(axis=-1, name="context_concat") #shared layer
dec_combined = concat_layer([dec_out, context_vector])
#%%
#Dense Layer
dec_dense_layer = Dense(HIN_VOCAB, activation='softmax', name="dec_dense") #shared layer
dec_dense = dec_dense_layer(dec_combined)
#%%
#Model
model = Model([enc_input, dec_input], dec_dense)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
#%%
from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='accuracy', patience=5, restore_best_weights=True)
#%%
#Training
history = model.fit(
    x=[df_enc_inp, df_dec_inp],
    y=df_dec_out,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    callbacks = [early_stopping]
)
#%%
#model.save("my_model.keras")
#model.save_weights("my_model.weights.h5")
#with open("my_model_architecture.json", 'w') as f:
#    f.write(model.to_json())

history_df = pd.DataFrame(history.history)
history_df.index = range(1, len(history_df) + 1)   # epochs start from 1
history_df.index.name = "epoch"
history_df.to_csv("training_history.csv")
#%%
# Inference — Encoder Model
encoder_inf_model = Model(enc_input, [enc_out, enc_h, enc_c])

# Inference — Decoder Model (one token at a time)
dec_inf_input = Input(shape=(1,), name="dec_inf_input")
dec_state_inp_h = Input(shape=(EMBED_DIM,), name="dec_state_inp_h")
dec_state_inp_c = Input(shape=(EMBED_DIM,), name="dec_state_inp_c")
enc_outputs_inp = Input(shape=(ENG_SEQ_LEN, EMBED_DIM), name="enc_outputs_inp")

dec_inf_embed = dec_embedding_layer(dec_inf_input)    # (batch, 1, EMBED_DIM)

dec_inf_out, dec_inf_h, dec_inf_c = dec_lstm(
    dec_inf_embed, initial_state=[dec_state_inp_h, dec_state_inp_c]
)  # dec_inf_out : (batch, 1, EMBED_DIM)

# Attend over the full encoder output sequence at every decode step
context_inf, attn_inf = attn_layer(dec_inf_out, enc_outputs_inp)
# context_inf : (batch, 1, EMBED_DIM)

dec_inf_combined = concat_layer([dec_inf_out, context_inf])
dec_inf_dense    = dec_dense_layer(dec_inf_combined)
# dec_inf_dense : (batch, 1, HIN_VOCAB)

decoder_inf_model = Model(
    inputs  = [dec_inf_input, dec_state_inp_h, dec_state_inp_c, enc_outputs_inp],
    outputs = [dec_inf_dense, dec_inf_h, dec_inf_c]
)
#%%
#Translate
hin_idx2word = {idx: word for word, idx in hin_tok.word_index.items()}
sos_token    = hin_tok.word_index["<sos>"]
eos_token    = hin_tok.word_index["<eos>"]
#%%
def translate(english_sentence, max_len=MAX_HIN_WORDS):
    # Step 1: Clean and pad English input
    eng_clean = clean_english(english_sentence)
    eng_seq   = eng_tok.texts_to_sequences([eng_clean])
    eng_pad   = pad_sequences(eng_seq, maxlen=ENG_SEQ_LEN, padding="post")

    # Step 2: Encode → all encoder hidden states + initial decoder states
    enc_outs, h, c = encoder_inf_model.predict(eng_pad, verbose=0)

    # Step 3: Start decoding with <sos>
    target_token = np.zeros((1, 1))
    target_token[0, 0] = sos_token

    translated = []

    # Step 4: Decode one token at a time, attending over enc_outs each step
    for _ in range(max_len):
        pred, h, c = decoder_inf_model.predict(
            [target_token, h, c, enc_outs], verbose=0
        )

        predicted_id   = np.argmax(pred[0, 0, :])
        predicted_word = hin_idx2word.get(predicted_id, "")

        if predicted_id == eos_token or predicted_word == "":
            break

        translated.append(predicted_word)
        target_token[0, 0] = predicted_id   # feed output as next input

    return " ".join(translated)
#%%
#Test
test_sentences = [
    "How are you doing today",
    "I want to eat food",
    "The weather is very cold outside",
    "She is going to the market",
    "My name is Rahul",
    "I love my country",
    "He is a very good student",
    "Please open the door",
    "I am feeling very tired today",
    "The dog is running in the park",
    "Can you help me please",
    "I want to drink water",
    "She loves to read books",
    "The sun rises in the east",
    "I go to school every day",
    "He does not like cold weather",
    "We are going to the temple",
    "The train is very late today",
    "I want to sleep now",
    "My mother cooks very delicious food"
]

for s in test_sentences:
    print(f"English : {s}")
    print(f"Hindi   : {translate(s)}")
    print("-" * 40)
#%%

#%%

#%%














###############################################################################################################
#### Generative AI (GenAI) - LSTM based EncDec in Keras with Luong Attention - Eng to Hindi Translation
###############################################################################################################
#%%
import numpy as np
import pandas as pd
import re
import pickle
import json
import time
import os
import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense, Layer, Input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#%%
tf.random.set_seed(42)
np.random.seed(42)
#%%
df = pd.read_csv("Dataset_English_Hindi.csv")
df.drop_duplicates(inplace=True)
df = df.dropna()
df["English"] = df["English"].astype(str)
df["Hindi"] = df["Hindi"].astype(str)
print(f"Total pairs: {len(df)}")
#%%
def clean_english(sentence):
    sentence = sentence.lower().strip()
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
    sentence = re.sub(r'https?://\S+|www\.\S+', '', sentence)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    sentence = emoji_pattern.sub(r'', sentence)
    return sentence.strip()
#%%
def clean_hindi(sentence):
    sentence = sentence.strip()
    sentence = re.sub(r'[^\u0900-\u097F\s]', '', sentence)
    sentence = re.sub(r'https?://\S+|www\.\S+', '', sentence)
    return sentence.strip()
#%%
df["English"] = df["English"].apply(clean_english)
df["Hindi"] = df["Hindi"].apply(clean_hindi)
#%%
MAX_ENG_WORDS = 25
MAX_HIN_WORDS = 30
mask = (
    df["English"].str.split().str.len().between(5, MAX_ENG_WORDS) &
    df["Hindi"].str.split().str.len().between(5, MAX_HIN_WORDS)
)
df = df[mask].reset_index(drop=True)
print(f"Pairs after length filter: {len(df)}")
#%%
# Add <start> / <end> tokens to Hindi
df["Hindi_in"] = "<sos> " + df["Hindi"]   # decoder input
df["Hindi_out"] = df["Hindi"] + " <eos>"  # decoder target
#%%
# English tokenizer
eng_tok = Tokenizer(filters="", lower=True, oov_token="<OOV>")
eng_tok.fit_on_texts(df["English"])
ENG_VOCAB = len(eng_tok.word_index) + 1
#%%
# Hindi tokenizer (case-sensitive for Devanagari)
hin_tok = Tokenizer(filters="", lower=False, oov_token="<OOV>")
hin_tok.fit_on_texts(df["Hindi_in"].tolist() + df["Hindi_out"].tolist())
HIN_VOCAB = len(hin_tok.word_index) + 1
#%%
print(f"English vocab: {ENG_VOCAB} | Hindi vocab: {HIN_VOCAB}")
#%%
df_enc_inp = pad_sequences(
    eng_tok.texts_to_sequences(df["English"]),
    maxlen=MAX_ENG_WORDS, padding="post"
)
df_dec_inp = pad_sequences(
    hin_tok.texts_to_sequences(df["Hindi_in"]),
    maxlen=MAX_HIN_WORDS + 1, padding="post"
)
df_dec_out = pad_sequences(
    hin_tok.texts_to_sequences(df["Hindi_out"]),
    maxlen=MAX_HIN_WORDS + 1, padding="post"
)
#%%
ENG_SEQ_LEN = df_enc_inp.shape[1]
HIN_SEQ_LEN = df_dec_inp.shape[1]
print(f"Encoder seq len: {ENG_SEQ_LEN} | Decoder seq len: {HIN_SEQ_LEN}")
print(f"df_enc_inp shape: {df_enc_inp.shape}")
print(f"df_dec_out shape: {df_dec_out.shape}")
#%%
EMBED_DIM = 512
BATCH_SIZE = 32
EPOCHS = 25
#%%
# Custom Luong Attention Layer
class LuongAttention(Layer):
    """
    Luong 'general' attention:
        score(s_t, h_i) = s_t^T * W_a * h_i
        alpha            = softmax(scores)
        context          = sum(alpha * encoder_outputs)
    """
    def __init__(self, units, **kwargs):
        super(LuongAttention, self).__init__(**kwargs)
        self.units = units
        self.W = Dense(units, use_bias=False, name="attention_W")

    def call(self, decoder_outputs, encoder_outputs):
        # decoder_outputs : (batch, dec_len, units)
        # encoder_outputs : (batch, enc_len, units)

        # Linear transform on decoder side → (batch, dec_len, units)
        query = self.W(decoder_outputs)

        # Dot with encoder outputs → scores (batch, dec_len, enc_len)
        scores = tf.matmul(query, encoder_outputs, transpose_b=True)
        attention_weights = tf.nn.softmax(scores, axis=-1)

        # Weighted sum of encoder outputs → (batch, dec_len, units)
        context = tf.matmul(attention_weights, encoder_outputs)

        return context, attention_weights

    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config
#%%
# Encoder
# CHANGED: return_sequences=True  →  gives all timestep outputs for attention
enc_input = Input(shape=(ENG_SEQ_LEN,))
enc_embed = Embedding(ENG_VOCAB, EMBED_DIM)(enc_input)
enc_lstm  = LSTM(EMBED_DIM, return_sequences=True, return_state=True, name="enc_lstm")
enc_all_out, enc_h, enc_c = enc_lstm(enc_embed)

enc_model = Model(enc_input, [enc_all_out, enc_h, enc_c])
#%%
# Decoder
dec_input = Input(shape=(HIN_SEQ_LEN,))
dec_embed = Embedding(HIN_VOCAB, EMBED_DIM, name="dec_embedding")(dec_input)
dec_lstm  = LSTM(EMBED_DIM, return_sequences=True, return_state=True, name="dec_lstm")
dec_out, dec_h, dec_c = dec_lstm(dec_embed, initial_state=[enc_h, enc_c])
#%%
# Luong Attention
attention_layer = LuongAttention(EMBED_DIM, name="luong_attention")
context, _ = attention_layer(dec_out, enc_all_out)
#%%
#concat_out = tf.concat([dec_out, context], axis=-1)        # (batch, dec_len, 2*EMBED_DIM)
concat_out = tf.keras.layers.Concatenate(axis=-1, name="concat_attn_train")([dec_out, context])
attn_dense = Dense(EMBED_DIM, activation='tanh', name="attn_dense")
attn_out   = attn_dense(concat_out)                        # (batch, dec_len, EMBED_DIM)

dec_dense    = Dense(HIN_VOCAB, activation='softmax', name="dec_dense")
dec_final_out = dec_dense(attn_out)
#%%
#Model
model = Model([enc_input, dec_input], dec_final_out)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
#%%
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
early_stopping = EarlyStopping(monitor='accuracy', patience=5, restore_best_weights=True)
#%%
# Training
history = model.fit(
    x=[df_enc_inp, df_dec_inp],
    y=df_dec_out,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    callbacks=[early_stopping]
)
#%%
model.save("my_model.keras")
model.save_weights("my_model.weights.h5")
with open("my_model_architecture.json", 'w') as f:
    f.write(model.to_json())

history_df = pd.DataFrame(history.history)
history_df.index = range(1, len(history_df) + 1)
history_df.index.name = "epoch"
history_df.to_csv("training_history.csv")
#%%
# Inference
# Encoder inference: returns all outputs + final states
encoder_inf_model = Model(enc_input, [enc_all_out, enc_h, enc_c])

# Reuse trained layers
dec_emb_layer   = model.get_layer("dec_embedding")
dec_dense_layer = model.get_layer("dec_dense")
attn_dense_layer = model.get_layer("attn_dense")

# Decoder inference inputs
dec_inf_input      = Input(shape=(1,))
dec_state_inp_h    = Input(shape=(EMBED_DIM,))
dec_state_inp_c    = Input(shape=(EMBED_DIM,))
enc_outputs_input  = Input(shape=(ENG_SEQ_LEN, EMBED_DIM), name="enc_outputs_input")  # NEW

dec_inf_embed = dec_emb_layer(dec_inf_input)
dec_inf_out, dec_inf_h, dec_inf_c = dec_lstm(
    dec_inf_embed, initial_state=[dec_state_inp_h, dec_state_inp_c]
)

# Single-step attention
context_inf, _ = attention_layer(dec_inf_out, enc_outputs_input)
concat_inf = tf.keras.layers.Concatenate(axis=-1, name="concat_attn_inf")([dec_inf_out, context_inf])
attn_inf_out    = attn_dense_layer(concat_inf)
dec_inf_dense   = dec_dense_layer(attn_inf_out)

decoder_inf_model = Model(
    inputs  = [dec_inf_input, dec_state_inp_h, dec_state_inp_c, enc_outputs_input],
    outputs = [dec_inf_dense, dec_inf_h, dec_inf_c]
)
#%%
# Translate
hin_idx2word = {idx: word for word, idx in hin_tok.word_index.items()}
sos_token    = hin_tok.word_index["<sos>"]
eos_token    = hin_tok.word_index["<eos>"]
#%%
def translate(english_sentence, max_len=MAX_HIN_WORDS):
    # Step 1: Clean and pad English input
    eng_clean = clean_english(english_sentence)
    eng_seq   = eng_tok.texts_to_sequences([eng_clean])
    eng_pad   = pad_sequences(eng_seq, maxlen=ENG_SEQ_LEN, padding="post")

    # Step 2: Encode → get all outputs + initial states
    enc_all_outputs, h, c = encoder_inf_model.predict(eng_pad, verbose=0)

    # Step 3: Start decoding with <sos>
    target_token = np.zeros((1, 1))
    target_token[0, 0] = sos_token

    translated = []

    # Step 4: Decode one token at a time
    for _ in range(max_len):
        pred, h, c = decoder_inf_model.predict(
            [target_token, h, c, enc_all_outputs], verbose=0
        )

        predicted_id   = np.argmax(pred[0, 0, :])
        predicted_word = hin_idx2word.get(predicted_id, "")

        if predicted_id == eos_token or predicted_word == "":
            break

        translated.append(predicted_word)
        target_token[0, 0] = predicted_id  # feed output as next input

    return " ".join(translated)
#%%
# Test
test_sentences = [
    "How are you doing today",
    "I want to eat food",
    "The weather is very cold outside",
    "She is going to the market",
    "My name is Rahul",
    "I love my country",
    "He is a very good student",
    "Please open the door",
    "I am feeling very tired today",
    "The dog is running in the park",
    "Can you help me please",
    "I want to drink water",
    "She loves to read books",
    "The sun rises in the east",
    "I go to school every day",
    "He does not like cold weather",
    "We are going to the temple",
    "The train is very late today",
    "I want to sleep now",
    "My mother cooks very delicious food"
]

for s in test_sentences:
    print(f"English : {s}")
    print(f"Hindi   : {translate(s)}")
    print("-" * 80)
#%%












###############################################################################################################
#### Generative AI (GenAI) - LSTM based EncDec in Keras with with Transformers - Eng to Hindi Translation
###############################################################################################################
#%%
import numpy as np
import pandas as pd
import re
import pickle
import json
import time
import os
import tensorflow as tf
from tensorflow.keras.layers import Embedding, Dense, Layer, Input, Dropout, LayerNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#%%
tf.random.set_seed(42)
np.random.seed(42)
#%%
df = pd.read_csv("Dataset_English_Hindi.csv")
df.drop_duplicates(inplace=True)
df = df.dropna()
df["English"] = df["English"].astype(str)
df["Hindi"]   = df["Hindi"].astype(str)
print(f"Total pairs: {len(df)}")
#%%
def clean_english(sentence):
    sentence = sentence.lower().strip()
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
    sentence = re.sub(r'https?://\S+|www\.\S+', '', sentence)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    sentence = emoji_pattern.sub(r'', sentence)
    return sentence.strip()
#%%
def clean_hindi(sentence):
    sentence = sentence.strip()
    sentence = re.sub(r'[^\u0900-\u097F\s]', '', sentence)
    sentence = re.sub(r'https?://\S+|www\.\S+', '', sentence)
    return sentence.strip()
#%%
df["English"] = df["English"].apply(clean_english)
df["Hindi"]   = df["Hindi"].apply(clean_hindi)
#%%
MAX_ENG_WORDS = 25
MAX_HIN_WORDS = 30
mask = (
    df["English"].str.split().str.len().between(5, MAX_ENG_WORDS) &
    df["Hindi"].str.split().str.len().between(5, MAX_HIN_WORDS)
)
df = df[mask].reset_index(drop=True)
print(f"Pairs after length filter: {len(df)}")
#%%
df["Hindi_in"]  = "<sos> " + df["Hindi"]
df["Hindi_out"] = df["Hindi"] + " <eos>"
#%%
eng_tok = Tokenizer(filters="", lower=True, oov_token="<OOV>")
eng_tok.fit_on_texts(df["English"])
ENG_VOCAB = len(eng_tok.word_index) + 1
#%%
hin_tok = Tokenizer(filters="", lower=False, oov_token="<OOV>")
hin_tok.fit_on_texts(df["Hindi_in"].tolist() + df["Hindi_out"].tolist())
HIN_VOCAB = len(hin_tok.word_index) + 1
#%%
print(f"English vocab: {ENG_VOCAB} | Hindi vocab: {HIN_VOCAB}")
#%%
df_enc_inp = pad_sequences(
    eng_tok.texts_to_sequences(df["English"]),
    maxlen=MAX_ENG_WORDS, padding="post"
)
df_dec_inp = pad_sequences(
    hin_tok.texts_to_sequences(df["Hindi_in"]),
    maxlen=MAX_HIN_WORDS + 1, padding="post"
)
df_dec_out = pad_sequences(
    hin_tok.texts_to_sequences(df["Hindi_out"]),
    maxlen=MAX_HIN_WORDS + 1, padding="post"
)
#%%
ENG_SEQ_LEN = df_enc_inp.shape[1]
HIN_SEQ_LEN = df_dec_inp.shape[1]
print(f"Encoder seq len: {ENG_SEQ_LEN} | Decoder seq len: {HIN_SEQ_LEN}")
print(f"df_enc_inp shape: {df_enc_inp.shape}")
print(f"df_dec_out shape: {df_dec_out.shape}")
#%%
EMBED_DIM    = 256
NUM_HEADS    = 8
DFF          = 512
NUM_LAYERS   = 4
DROPOUT_RATE = 0.1
BATCH_SIZE   = 64
EPOCHS       = 30
#%%
def get_positional_encoding(max_len, embed_dim):
    positions = np.arange(max_len)[:, np.newaxis]
    dims      = np.arange(embed_dim)[np.newaxis, :]
    angles    = positions / np.power(10000, (2 * (dims // 2)) / np.float32(embed_dim))
    angles[:, 0::2] = np.sin(angles[:, 0::2])
    angles[:, 1::2] = np.cos(angles[:, 1::2])
    return tf.cast(angles[np.newaxis, :, :], dtype=tf.float32)
#%%
class PositionalEmbedding(Layer):
    """Token embedding scaled by sqrt(embed_dim) + fixed sinusoidal positional encoding."""
    def __init__(self, vocab_size, embed_dim, max_len, dropout_rate=0.1, **kwargs):
        super().__init__(**kwargs)
        self.vocab_size   = vocab_size
        self.embed_dim    = embed_dim
        self.max_len      = max_len
        self.dropout_rate = dropout_rate
        # mask_zero=True → padding mask auto-propagates into MultiHeadAttention (TF ≥ 2.10)
        self.embedding    = Embedding(vocab_size, embed_dim, mask_zero=True)
        self.pos_enc      = get_positional_encoding(max_len, embed_dim)
        self.dropout      = Dropout(dropout_rate)

    def call(self, x, training=False):
        seq_len = tf.shape(x)[1]
        x  = self.embedding(x)
        x *= tf.math.sqrt(tf.cast(self.embed_dim, tf.float32))  # scale as in "Attention Is All You Need"
        x += self.pos_enc[:, :seq_len, :]
        return self.dropout(x, training=training)

    # Propagate the padding mask from the embedding through subsequent layers
    def compute_mask(self, inputs, mask=None):
        return self.embedding.compute_mask(inputs)

    def get_config(self):
        config = super().get_config()
        config.update({"vocab_size": self.vocab_size, "embed_dim": self.embed_dim,
                        "max_len": self.max_len, "dropout_rate": self.dropout_rate})
        return config
#%%
class EncoderLayer(Layer):
    """One Transformer encoder block: self-attention + position-wise FFN (both with Add & Norm)."""
    def __init__(self, embed_dim, num_heads, dff, dropout_rate=0.1, **kwargs):
        super().__init__(**kwargs)
        self.embed_dim    = embed_dim
        self.num_heads    = num_heads
        self.dff          = dff
        self.dropout_rate = dropout_rate
        self.self_attn    = tf.keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim // num_heads, dropout=dropout_rate
        )
        self.ffn_dense1   = Dense(dff, activation='relu')
        self.ffn_dense2   = Dense(embed_dim)
        self.norm1        = LayerNormalization(epsilon=1e-6)
        self.norm2        = LayerNormalization(epsilon=1e-6)
        self.dropout1     = Dropout(dropout_rate)
        self.dropout2     = Dropout(dropout_rate)

    def call(self, x, training=False):
        attn_out = self.self_attn(x, x, training=training)         # padding mask auto-applied from x's mask
        x = self.norm1(x + self.dropout1(attn_out, training=training))
        ffn_out = self.ffn_dense2(self.ffn_dense1(x))
        x = self.norm2(x + self.dropout2(ffn_out, training=training))
        return x

    def get_config(self):
        config = super().get_config()
        config.update({"embed_dim": self.embed_dim, "num_heads": self.num_heads,
                        "dff": self.dff, "dropout_rate": self.dropout_rate})
        return config
#%%
class DecoderLayer(Layer):
    """
    One Transformer decoder block:
      1. Masked self-attention  (causal — prevents peeking at future tokens)
      2. Cross-attention        (attends to encoder output)
      3. Position-wise FFN
    All three sub-layers wrapped with Add & Norm.
    """
    def __init__(self, embed_dim, num_heads, dff, dropout_rate=0.1, **kwargs):
        super().__init__(**kwargs)
        self.embed_dim    = embed_dim
        self.num_heads    = num_heads
        self.dff          = dff
        self.dropout_rate = dropout_rate
        self.self_attn    = tf.keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim // num_heads, dropout=dropout_rate
        )
        self.cross_attn   = tf.keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim // num_heads, dropout=dropout_rate
        )
        self.ffn_dense1   = Dense(dff, activation='relu')
        self.ffn_dense2   = Dense(embed_dim)
        self.norm1        = LayerNormalization(epsilon=1e-6)
        self.norm2        = LayerNormalization(epsilon=1e-6)
        self.norm3        = LayerNormalization(epsilon=1e-6)
        self.dropout1     = Dropout(dropout_rate)
        self.dropout2     = Dropout(dropout_rate)
        self.dropout3     = Dropout(dropout_rate)

    def call(self, x, enc_output, training=False):
        # 1. Masked self-attention: use_causal_mask=True prevents future-token leakage
        attn1 = self.self_attn(x, x, use_causal_mask=True, training=training)
        x = self.norm1(x + self.dropout1(attn1, training=training))

        # 2. Cross-attention: query = decoder state, key/value = encoder output
        attn2 = self.cross_attn(x, enc_output, training=training)  # encoder padding mask auto-applied
        x = self.norm2(x + self.dropout2(attn2, training=training))

        # 3. Position-wise FFN
        ffn_out = self.ffn_dense2(self.ffn_dense1(x))
        x = self.norm3(x + self.dropout3(ffn_out, training=training))
        return x

    def get_config(self):
        config = super().get_config()
        config.update({"embed_dim": self.embed_dim, "num_heads": self.num_heads,
                        "dff": self.dff, "dropout_rate": self.dropout_rate})
        return config
#%%
class TransformerEncoder(Layer):
    def __init__(self, num_layers, embed_dim, num_heads, dff,
                 vocab_size, max_len, dropout_rate=0.1, **kwargs):
        super().__init__(**kwargs)
        self.num_layers = num_layers; self.embed_dim = embed_dim
        self.num_heads  = num_heads;  self.dff       = dff
        self.vocab_size = vocab_size; self.max_len   = max_len
        self.dropout_rate = dropout_rate
        self.pos_emb    = PositionalEmbedding(vocab_size, embed_dim, max_len, dropout_rate)
        self.enc_layers = [
            EncoderLayer(embed_dim, num_heads, dff, dropout_rate, name=f"enc_layer_{i}")
            for i in range(num_layers)
        ]

    def call(self, x, training=False):
        x = self.pos_emb(x, training=training)
        for layer in self.enc_layers:
            x = layer(x, training=training)
        return x

    def get_config(self):
        config = super().get_config()
        config.update({"num_layers": self.num_layers, "embed_dim": self.embed_dim,
                        "num_heads": self.num_heads,  "dff": self.dff,
                        "vocab_size": self.vocab_size,"max_len": self.max_len,
                        "dropout_rate": self.dropout_rate})
        return config
#%%
class TransformerDecoder(Layer):
    def __init__(self, num_layers, embed_dim, num_heads, dff,
                 vocab_size, max_len, dropout_rate=0.1, **kwargs):
        super().__init__(**kwargs)
        self.num_layers = num_layers; self.embed_dim = embed_dim
        self.num_heads  = num_heads;  self.dff       = dff
        self.vocab_size = vocab_size; self.max_len   = max_len
        self.dropout_rate = dropout_rate
        self.pos_emb    = PositionalEmbedding(vocab_size, embed_dim, max_len, dropout_rate)
        self.dec_layers = [
            DecoderLayer(embed_dim, num_heads, dff, dropout_rate, name=f"dec_layer_{i}")
            for i in range(num_layers)
        ]

    def call(self, x, enc_output, training=False):
        x = self.pos_emb(x, training=training)
        for layer in self.dec_layers:
            x = layer(x, enc_output, training=training)
        return x

    def get_config(self):
        config = super().get_config()
        config.update({"num_layers": self.num_layers, "embed_dim": self.embed_dim,
                        "num_heads": self.num_heads,  "dff": self.dff,
                        "vocab_size": self.vocab_size,"max_len": self.max_len,
                        "dropout_rate": self.dropout_rate})
        return config
#%%
enc_input = Input(shape=(ENG_SEQ_LEN,), name="enc_input")
dec_input = Input(shape=(HIN_SEQ_LEN,), name="dec_input")

transformer_encoder = TransformerEncoder(
    NUM_LAYERS, EMBED_DIM, NUM_HEADS, DFF,
    ENG_VOCAB, ENG_SEQ_LEN, DROPOUT_RATE,
    name="transformer_encoder"
)
transformer_decoder = TransformerDecoder(
    NUM_LAYERS, EMBED_DIM, NUM_HEADS, DFF,
    HIN_VOCAB, HIN_SEQ_LEN, DROPOUT_RATE,
    name="transformer_decoder"
)

enc_output    = transformer_encoder(enc_input)
dec_output    = transformer_decoder(dec_input, enc_output)

dec_dense     = Dense(HIN_VOCAB, activation='softmax', name="dec_dense")
dec_final_out = dec_dense(dec_output)

model = Model([enc_input, dec_input], dec_final_out)
#%%
class TransformerLRSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    """Warmup then inverse-square-root decay as in Vaswani et al. 2017."""
    def __init__(self, embed_dim, warmup_steps=4000):
        super().__init__()
        self.embed_dim    = embed_dim
        self.warmup_steps = warmup_steps

    def __call__(self, step):
        step  = tf.cast(step, tf.float32)
        d     = tf.cast(self.embed_dim, tf.float32)
        arg1  = tf.math.rsqrt(step)
        arg2  = step * (self.warmup_steps ** -1.5)
        return tf.math.rsqrt(d) * tf.math.minimum(arg1, arg2)

    def get_config(self):
        return {"embed_dim": self.embed_dim, "warmup_steps": self.warmup_steps}
#%%
lr_schedule = TransformerLRSchedule(EMBED_DIM, warmup_steps=4000)
optimizer   = tf.keras.optimizers.Adam(lr_schedule, beta_1=0.9, beta_2=0.98, epsilon=1e-9)

model.compile(
    optimizer=optimizer,
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()
#%%
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

early_stopping = EarlyStopping(monitor='accuracy', patience=5, restore_best_weights=True)
checkpoint     = ModelCheckpoint("best_transformer.keras", monitor='accuracy', save_best_only=True)
#%%
history = model.fit(
    x=[df_enc_inp, df_dec_inp],
    y=df_dec_out,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    callbacks=[early_stopping, checkpoint]
)
#%%
#model.save("my_model.keras")
#model.save_weights("my_model.weights.h5")
#with open("my_model_architecture.json", 'w') as f:
#    f.write(model.to_json())

history_df = pd.DataFrame(history.history)
history_df.index = range(1, len(history_df) + 1)
history_df.index.name = "epoch"
history_df.to_csv("training_history.csv")
#%%
hin_idx2word = {idx: word for word, idx in hin_tok.word_index.items()}
sos_token    = hin_tok.word_index["<sos>"]
eos_token    = hin_tok.word_index["<eos>"]
#%%
def translate(english_sentence, max_len=MAX_HIN_WORDS):
    # Step 1: Clean and encode the English sentence
    eng_clean = clean_english(english_sentence)
    eng_seq   = eng_tok.texts_to_sequences([eng_clean])
    eng_pad   = pad_sequences(eng_seq, maxlen=ENG_SEQ_LEN, padding="post")

    # Step 2: Start decoder input with <sos>
    dec_input_ids = [sos_token]

    # Step 3: Autoregressively generate one token at a time
    for _ in range(max_len):
        dec_pad     = pad_sequences([dec_input_ids], maxlen=HIN_SEQ_LEN, padding="post")
        predictions = model.predict([eng_pad, dec_pad], verbose=0)

        # Read prediction at the position of the last real token
        next_token_id = int(np.argmax(predictions[0, len(dec_input_ids) - 1, :]))

        if next_token_id == eos_token or next_token_id == 0:
            break

        dec_input_ids.append(next_token_id)

    translated_words = [hin_idx2word.get(idx, "") for idx in dec_input_ids[1:]]
    return " ".join([w for w in translated_words if w])
#%%
test_sentences = [
    "How are you doing today",
    "I want to eat food",
    "The weather is very cold outside",
    "She is going to the market",
    "My name is Rahul",
    "I love my country",
    "He is a very good student",
    "Please open the door",
    "I am feeling very tired today",
    "The dog is running in the park",
    "Can you help me please",
    "I want to drink water",
    "She loves to read books",
    "The sun rises in the east",
    "I go to school every day",
    "He does not like cold weather",
    "We are going to the temple",
    "The train is very late today",
    "I want to sleep now",
    "My mother cooks very delicious food"
]

for s in test_sentences:
    print(f"English : {s}")
    print(f"Hindi   : {translate(s)}")
    print("-" * 80)



















###############################################################################################################
#### Natural Language Processing (NLP) - Everything
###############################################################################################################

#important terms:
#word = word
#corpus = all words from all sentences [definitely contains duplicates]
#vocabulary = unique words from corpus
#document = a complete sentence

##################################################################
# NLP - Text Preprocessing
##################################################################
# Convert text to lowercase
text = "<p>This <b>bold text</b> contains exactly twenty words, carefully styled with basic HTML tags to format its online structural presentation.</p>"
text = text.lower()

# Remove HTML tags using Regular Expressions (REGEX)
import re
def remove_html(text):
    pattern = re.compile(r'<.*?>')    #start with <(once), any character any number of times, end with >
    return pattern.sub('', text)
html_text = "<p>This <b>bold text</b> contains exactly twenty words, carefully styled with basic HTML tags to format its online structural presentation.</p>"
remove_html(html_text)

# Remove URL
def remove_url(text):
    pattern = re.compile(r'http\S+|www\.\S+')
    return pattern.sub('', text)
text = 'alfksdkj https://www.youtube.com/watch?v=6C0sLtw5ctc&list=PLKnIA16_RmvZo7fp5kkIth6nRTeQQsjfX&index=3&t=3790s jflsk'

remove_url(text)

# Remove multiple spaces
def remove_multi_space(text):
    pattern = re.compile(r'\s+')
    return pattern.sub(' ', text)
text = 'abdfs lsdkfj  lskdjfk   lsdkfjk      sldkfjl'
remove_multi_space(text)

# Remove Punctuations
import string
#### slower method
def rem_punc1(text):
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, '')
    return text
text = 'Hi! is this obvious? my dog is running.'
rem_punc1(text)

#### faster method
def rem_punc2(text):
    return text.translate(str.maketrans('','',string.punctuation))
rem_punc2(text)

# Handle Chat Words
#### create a dictionary of chat words
def correct_chat_words(text):
    chat_abbreviations = {
        "A3": "Anytime, Anywhere, Anyplace",
        "ADIH": "Another Day In Hell",
        "AFK": "Away From Keyboard",
        "AFAIK": "As Far As I Know",
        "ASAP": "As Soon As Possible",
        "ASL": "Age, Sex, Location",
        "ATK": "At The Keyboard",
        "ATM": "At The Moment",
        "BAE": "Before Anyone Else",
        "BAK": "Back At Keyboard",
        "BBL": "Be Back Later",
        "BBS": "Be Back Soon",
        "BFN": "Bye For Now",
        "B4N": "Bye For Now",
        "BRB": "Be Right Back",
        "BRUH": "Bro",
        "BRT": "Be Right There",
        "BSAAW": "Big Smile And A Wink",
        "BTW": "By The Way",
        "BWL": "Bursting With Laughter",
        "CSL": "Can’t Stop Laughing",
        "CU": "See You",
        "CUL8R": "See You Later",
        "CYA": "See You",
        "DM": "Direct Message",
        "FAQ": "Frequently Asked Questions",
        "FC": "Fingers Crossed",
        "FIMH": "Forever In My Heart",
        "FOMO": "Fear Of Missing Out",
        "FR": "For Real",
        "FWIW": "For What It's Worth",
        "FYP": "For You Page",
        "FYI": "For Your Information",
        "G9": "Genius",
        "GAL": "Get A Life",
        "GG": "Good Game",
        "GMTA": "Great Minds Think Alike",
        "GN": "Good Night",
        "GOAT": "Greatest Of All Time",
        "GR8": "Great!",
        "HBD": "Happy Birthday",
        "IC": "I See",
        "ICQ": "I Seek You",
        "IDC": "I Don’t Care",
        "IDK": "I Don't Know",
        "IFYP": "I Feel Your Pain",
        "ILU": "I Love You",
        "ILY": "I Love You",
        "IMHO": "In My Honest Opinion",
        "IMU": "I Miss You",
        "IMO": "In My Opinion",
        "IOW": "In Other Words",
        "IRL": "In Real Life",
        "IYKYK": "If You Know, You Know",
        "JK": "Just Kidding",
        "KISS": "Keep It Simple, Stupid",
        "L": "Loss",
        "L8R": "Later",
        "LDR": "Long Distance Relationship",
        "LMK": "Let Me Know",
        "LMAO": "Laughing My Ass Off",
        "LOL": "Laughing Out Loud",
        "LTNS": "Long Time No See",
        "M8": "Mate",
        "MFW": "My Face When",
        "MID": "Mediocre",
        "MRW": "My Reaction When",
        "MTE": "My Thoughts Exactly",
        "NVM": "Never Mind",
        "NRN": "No Reply Necessary",
        "NPC": "Non-Player Character",
        "OIC": "Oh I See",
        "OP": "Overpowered",
        "PITA": "Pain In The Ass",
        "POV": "Point Of View",
        "PRT": "Party",
        "PRW": "Parents Are Watching",
        "ROFL": "Rolling On The Floor Laughing",
        "ROFLOL": "Rolling On The Floor Laughing Out Loud",
        "ROTFLMAO": "Rolling On The Floor Laughing My Ass Off",
        "RN": "Right Now",
        "SK8": "Skate",
        "STATS": "Your Sex And Age",
        "SUS": "Suspicious",
        "TBH": "To Be Honest",
        "TFW": "That Feeling When",
        "THX": "Thank You",
        "TIME": "Tears In My Eyes",
        "TLDR": "Too Long, Didn’t Read",
        "TNTL": "Trying Not To Laugh",
        "TTFN": "Ta-Ta For Now!",
        "TTYL": "Talk To You Later",
        "U": "You",
        "U2": "You Too",
        "U4E": "Yours For Ever",
        "W": "Win",
        "W8": "Wait",
        "WB": "Welcome Back",
        "WTF": "What The Fuck",
        "WTG": "Way To Go!",
        "WUF": "Where Are You From?",
        "WYD": "What You Doing?",
        "WYWH": "Wish You Were Here",
        "ZZZ": "Sleeping, Bored, Tired"
    }
    new_text = []
    for word in text.split():
        word = word.replace(',','')
        word = word.replace('.','')
        word = word.upper()
        if word in chat_abbreviations.keys():
            new_text.append(chat_abbreviations[word])
        else:
            new_text.append(word)
    return " ".join(new_text).lower()
txt = 'Omg tbh, I was AFK when the TBH DM dropped, but IMO it’s NGL totally lit RN ngl'
correct_chat_words(txt)

# Handle Contractions
import contractions
def expand_contractions(text):
    return contractions.fix(text)

# Correct the Spelling
from textblob import TextBlob
incorrect_text = "Thsi si a teext wiht sepling mitkase."
txt_blob = TextBlob(incorrect_text)
txt_blob.correct()  #returns correct spellings

# Remove stop words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
def remove_stopwords(text):
    filtered_words = [word for word in text.split() if word not in stopwords]
    return " ".join(filtered_words)


# Handle Emojis
#### encode emoji to utf-8 text
emoji_text = "Let us grab a hot coffee and catch up today! ☕✨ I am so excited to see you and hear all your news! 😊💬"
emoji_text.encode('utf-8')  #returns emoji encoded into utf-8 text

#### demojize the emojis
import emoji
emoji.demojize(emoji_text)    #gives text in place of emoji

#### remove emojis
import re
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Remove Digits
def remove_digits(text):
    pattern = re.compile(r'\d+')
    return pattern.sub('', text)

# Tokenize (Tokenization) - sentence/word
text = 'I am going to Delhi? I will stay there for 3 days! Let\'s hope the trip to be great.'

#### Sentence Tokenization
text.split('.') #only splits at one character
#### word Tokenization
text.split()    #also keeps punctuations attached to words
#### split function splits on one character only.
#### what if sentences end with . ? ! 
#### to overcome this, use REGEX

#### sentence Tokenization
import re
re.compile('[.!?] ').split(text)
#### word Tokenization
import re
re.findall("[\w]+", text)

#### Tokenize using NLTK library
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize
sent_tokenize(text)
word_tokenize(text)

#### Tokenize using Spacy library (most advance)
import spacy
!python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")    #load english dictionary
doc = nlp(text)
for token in doc:
    print(token)

# Stemming - root words [rule based - may give wrong spelling]
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def stem_words(text):
    return " ".join([ps.stem(word) for word in text.split()])
text = 'walk walks walking walked'
stem_words(text)

# Lemmatization - root words [using Lexical Dictionary - slower]
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def lem_word(text):
  return " ".join([lemmatizer.lemmatize(word, pos='v') for word in text.split()])
#pos='v' - verb form of root word










##################################################################
# NLP - Text Vectorization/Representation [text to numbers]
##################################################################

# One Hot Encoding (OHE)
#### if one doc/sentence contains 3 words
#### each word is represented by a vector of dimension equal to the total number of words in vocab.
#### one dimension is 1 where word matches, others are 0 --> sparse

#### Implementation using pandas
pd.get_dummies(df,columns=['col1','col2'],drop_first=True)      #OHE for col1 and col2

#### Implementation using sklearn
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(drop='First', sparse_output=False, handle_unknown='ignore')
df['review'] = pd.DataFrame(ohe.fit_transform(df[['review']]))

#### Implementation using keras
from keras.utils import to_categorical
y_train_ohe = to_categorical(y_train, num_classes)

#### problems in OHE
#### 1) Sparsity, 2) OOV, 4) No Semantic Meaning capture,
#### 4) Sentence size varies, Not able to train ML model




# Bag of Words (BOW) - [helpful in text classification]
#### if one doc/sentence contains 3 words
#### each SENTENCE is represented by a vector of dimensions equal to the total number of words in vocab.
#### each dimension contains the total number of times that word appears in the sentence
#### unseen words get handled by ignoring.
from sklearn.feature_extraction.text import CountVectorizer
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
cv = CountVectorizer( analyzer='word',
                tokenizer=word_tokenize, lowercase=True,
                ngram_range=(1,1), stop_words='english',
                max_features=10000)
X_train_bow = cv.fit_transform(X_train['review'])
print(cv.vocabulary_)
print(X_train_bow[0].toarray())  #1st sentence numbers in train data

X_test_bow = cv.transform(X_test['review'])

x_tr1=pd.DataFrame(x_train_bow.toarray(),columns=cv.get_feature_names_out())
x_tr1.head()

x_ts1=pd.DataFrame(x_test_bow.toarray(),columns=cv.get_feature_names_out())
x_ts1.head()
#### Advantages in BOW
#### 1) Less sparsity, 2) solves OOV by ignoring new words,
#### 3) captures Sematic relationship (similarity) to some extent,
#### 4) works with diff sentence sizes

#### Disadvantages in BOW
#### 1) Sparcity still exists to a very great extent
#### 2) OOV is ignored (word may be important)
#### 3) sequence of words is ignored (context not captured)



# Bag of ngrams/ n-grams/ bi-grams/ tri-grams
#### BOW was made with single word
#### Bag of ngrams is made of n-words taken at a time (2-bi, 3-tri)
#### BOW = Bag of 1-gram
#### code modification for Bag of bi-gram
cv = CountVectorizer(ngram_range=(2,2))
#### code modification for Bag of bi-gram & tri-gram both
cv = CountVectorizer(ngram_range=(2,3))

#### Advantages in n-grams
#### 1) Able to capture semantic meaning
#### 2) Easy implementation

#### Disadvantages in n-grams
#### 1) more features/ slow training
#### 2) OOV is ignored





# TF-IDF (TFIDF): Term Frequency Inverse Document Frequency
#### a word comes in one doc & not others, then its weightage in that sentence is higher
#### TF = (#occurences of term t in doc d)/(total #terms in d)
#### IDF = 1 + LOG[(total #docs in corpus)/(#docs with term t)]
#### calculate TF x IDF for each word in every document
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(analyzer='word', tokenizer=word_tokenize,
            lowercase=True, ngram_range=(1,1), max_features=10000)
x_tr1=tfidf.fit_transform(x_train['review'])
x_ts1=tfidf.transform(x_test['review'])

x_tr1=pd.DataFrame(x_tr1.toarray(),columns=tfidf.get_feature_names_out())
x_tr1.head()

x_ts1=pd.DataFrame(x_ts1.toarray(),columns=tfidf.get_feature_names_out())
x_ts1.head()

#### Advantages in TF-IDF
#### 1) Works well in information retrieval systems [Google]

#### Disadvantages in TF-IDF
#### 1) Sparsity exists
#### 2) OOV is ignored
#### 3) High Dimensionality
#### 4) Semantic relationship is not captured





# Word2Vec - word embedding technique to convert a word to vector
#### invented by Google
#### Captures Semantic Meaning
#### Low dimentionality - Fast Training
#### Dense/Non-Sparse Vectors
#### based on Deep Learning
#### Word2Vec using pre-trained model from google
#### 300 dimensional embedding of 3 Million words
import gensim

!pip install wget
!wget -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"

model = KeyedVectors.load_word2vec_format(
                    'GoogleNews-vectors-negative300.bin.gz',
                    binary=True, limit=500000)
#### print the embedding of different words
model['cricket']
model['man']
model.most_similar('man')
#### similarity score (0 to 1) of 'man' & 'woman'
model.similarity('man','woman')
#### odd word out of the given words
model.doesnt_match(['PHP','java','monkey'])
#### create a vector = king - man + woman, must be similar to queen
vec = model['king'] - model['man'] + model['woman']
model.most_similar([vec])

vec = model['INR'] - model ['India'] + model['England']
model.most_similar([vec])


####Word2Vec using own model
!pip install gensim
import gensim
import os
from nltk import sent_tokenize
from gensim.utils import simple_preprocess
from gensim.models import Word2Vec

text = []
#from a directory named data present in cwd, load all files
for filename in os.listdir('data'):
    f = open(os.path.join('data',filename))
    corpus = f.read()
    sentences = sent_tokenize(corpus)   #tokenize sentences
    for sentence in sentences:
        text.append(simple_preprocess(sentence))               #simple_preprocess = sentence.split().strip()
text    #a 2-d list, [[words in sentence1],[words in sentence2],...]

#### method 1
model = Word2Vec(window=10,     # #words to consider at a time
            vector_size=100,    #final vector size for each word
            min_count=2,    #ignore words with frequency lower than 2
            workers=4)      #use 4 processor threads
model.build_vocab(text)
model.train(text, total_examples=model.corpus_count, epochs=model.epochs)
#### method 2 - giving text in input automatically executes build_vocab and train
model = Word2Vec(sentences=text,
            window=10,
            vector_size=100,
            min_count=2,
            workers=4)

model.wv['king']        #embedding (numpy array) of the word king
model.wv.most_similar('daenerys', topn=5)
    #result below, because the corpus is from GOT books
model.wv.similarity('arya','sansa') #similarity score of arya and sansa
model.wv.doesnt_match(['jon','rikon','robb','arya','sansa','bran'])
    #prints the odd one i.e. jon


model.wv.get_normed_vectors()   #normalized vectors
model.wv.index_to_key           #all words in text form

#### method to create sentence embeddings from word embeddings
def doc_vector(doc):
    # only keep sentence words which are considered in corpus vocab
    doc = [word for word in doc.split() if word in model.wv.index_to_key]
    # return mean embeddings of whole sentence
    return np.mean(model.wv[doc], axis=0)








##################################################################
# NLP Project - Text Classification [Positive/Negative]
##################################################################
import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk import sent_tokenize
import emoji
import tqdm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('datasets/IMDB Dataset.csv')

# check class balance
df['sentiment'].value_counts()
# check missing values
df.isnull().sum()
# drop duplicates
df.drop_duplicates(inplace=True)
# convert text to lowercase
df['review'] = df['review'].str.lower()
# remove html tags
def remove_html(text):
    pattern = re.compile(r'<.*?>')
    return pattern.sub('', text)
df['review'] = df['review'].apply(remove_html)
# remove URLs
def remove_url(text):
    pattern = re.compile(r'http\S+|www\.\S+')
    return pattern.sub('', text)
df['review'] = df['review'].apply(remove_url)
# remove multiple spaces
def remove_multiple_spaces(text):
    pattern = re.compile(r'\s+')
    return pattern.sub(' ', text)
df['review'] = df['review'].apply(remove_multiple_spaces)
# remove punctuations
def remove_punctuations(text):
    return text.translate(str.maketrans('','',string.punctuation))
df['review'] = df['review'].apply(remove_punctuations)

# handle emojis
from tqdm.auto import tqdm
tqdm.pandas(desc="Processing Data")
df['review'] = df['review'].progress_apply(emoji.demojize)
# remove stop words
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
def remove_stopwords(text):
    filtered_words = [word for word in text.split() if word not in stopwords]
    return " ".join(filtered_words)
df['review'] = df['review'].progress_apply(remove_stopwords)
# X,y split
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
# label encode y
le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1)

#################################
# Using Techniques BOW / TFIDF
#################################
# BOW
cv = CountVectorizer(ngram_range=(1,1), min_df=5, max_df=0.95, max_features=5000)
X_train_bow = cv.fit_transform(X_train['review']).toarray()
X_test_bow = cv.transform(X_test['review']).toarray()

# TFIDF
tfidf = TfidfVectorizer(ngram_range=(1,1), min_df=5, max_df=0.95, max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train['review']).toarray()
X_test_tfidf = tfidf.transform(X_test['review']).toarray()

# Gaussian Naive Bayes Model with BOW
gnb = GaussianNB()
gnb.fit(X_train_bow, y_train)
y_pred1 = gnb.predict(X_test_bow)
confusion_matrix(y_test, y_pred1), accuracy_score(y_test, y_pred1), f1_score(y_test, y_pred1)

# Random Forest Model with TFIDF
rf = RandomForestClassifier(n_estimators=300, max_depth=5, n_jobs=-1, verbose=1, random_state=42)
rf.fit(X_train_tfidf, y_train)
y_pred22 = rf.predict(X_test_tfidf)
confusion_matrix(y_test, y_pred22), accuracy_score(y_test, y_pred22), f1_score(y_test, y_pred22)

#################################
# Using Word2Vec Embeddings
#################################
# tokenized words for each sentence in all the rows
story = []
for doc in df['review']:
    sentences = sent_tokenize(doc)
    for sentence in sentences:
        story.append(simple_preprocess(sentence))

# Word2Vec - method 1
model_wv = Word2Vec(window=10, vector_size=300, min_count=2, workers=12)
model_wv.build_vocab(story)
model_wv.train(story, total_examples=model_wv.corpus_count, epochs=model_wv.epochs)

# Word2Vec - method 2
model_wv = Word2Vec(sentences=story, window=10, vector_size=300, min_count=2, workers=12)

# all words in vocab of model_wv
model_wv.wv.index_to_key

# get document (review) embeddings from word embeddings
def doc_vector(doc):
    #In the doc (review), keep only the words that are present in vocab of model
    doc = [word for word in doc.split() if word in model_wv.wv.index_to_key]
    #each word has an embedding of 300 dimensions.
    #take mean of embeddings of all the words in a doc (review)
    return np.mean(model_wv.wv[doc], axis=0)
# apply above method
X = []
for doc in tqdm(df['review'].values):
    X.append(doc_vector(doc))
y = df.iloc[:,-1]
# train test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1)
# Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, max_depth=8, n_jobs=-1, verbose=1)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

confusion_matrix(y_test, y_pred), accuracy_score(y_test, y_pred), f1_score(y_test, y_pred)








##################################################################
# NLP Project - Parts of Speech (POS) Tagging
##################################################################
# Applications of POS tagging:
# 1) Named Entity Recognition
# 2) Question Answering system
# 3) Word sense disambiguation (same word used with diff meanings)
# 4) Chatbots

# Using spacy library, Hidden Markov Model & Viterbi optimization

import spacy
nlp = spacy.load('en_core_web_sm')
# POS tagging code
doc = nlp(u"I will google about facebook")

doc.text                #output= 'I will google about facebook'
doc[0]                  #output= I
doc[0].pos_             #overview POS: output= 'PRON'
doc[0].tag_             #detailed POS: output= 'PRP'
spacy.explain('PRP')    #explain PRP: output= pronoun, personal

# print POS for every word
for word in doc:
    print(word.text,"-->",word.pos_, spacy.explain(word.tag_))

# sentence visualization using spacy
from spacy import displacy
doc = nlp(r'The quick brown fox jumped over the lazy dog')
displacy.render(doc,style='deep',jupyter=True)
OR
options={'distance':80,
        'compact':True,
        'color':'#fff',
        'bg':'#00a65a'}
displacy.render(doc,style='dep',jupyter=True,options=options)








##################################################################
# NLP Project - Duplicate Question Recognition (Quora) using ML
##################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('datasets/Quora Duplicate Questions Dataset/train.csv')
new_df = df.sample(30000,random_state=2)

def preprocess(q):
    q = str(q).lower().strip()    
    # Replace certain special characters with their string equivalents
    q = q.replace('%', ' percent')
    q = q.replace('$', ' dollar ')
    q = q.replace('₹', ' rupee ')
    q = q.replace('€', ' euro ')
    q = q.replace('@', ' at ')
    # The pattern '[math]' appears around 900 times in the whole dataset.
    q = q.replace('[math]', '')    
    # Replacing some numbers with string equivalents (not perfect, can be done better to account for more cases)
    q = q.replace(',000,000,000 ', 'b ')
    q = q.replace(',000,000 ', 'm ')
    q = q.replace(',000 ', 'k ')
    q = re.sub(r'([0-9]+)000000000', r'\1b', q)
    q = re.sub(r'([0-9]+)000000', r'\1m', q)
    q = re.sub(r'([0-9]+)000', r'\1k', q)
    
    # Decontracting words
    # https://en.wikipedia.org/wiki/Wikipedia%3aList_of_English_contractions
    # https://stackoverflow.com/a/19794953
    contractions = { 
    "ain't": "am not",
    "aren't": "are not",
    "can't": "can not",
    "can't've": "can not have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "i'd": "i would",
    "i'd've": "i would have",
    "i'll": "i will",
    "i'll've": "i will have",
    "i'm": "i am",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you would",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have"
    }

    q_decontracted = []
    for word in q.split():
        if word in contractions:
            word = contractions[word]
        q_decontracted.append(word)

    q = ' '.join(q_decontracted)
    q = q.replace("'ve", " have")
    q = q.replace("n't", " not")
    q = q.replace("'re", " are")
    q = q.replace("'ll", " will")    
    # Removing HTML tags
    q = BeautifulSoup(q)
    q = q.get_text()    
    # Remove punctuations
    pattern = re.compile('\W')
    q = re.sub(pattern, ' ', q).strip()   
    return q

new_df['question1'] = new_df['question1'].apply(preprocess)
new_df['question2'] = new_df['question2'].apply(preprocess)

new_df['q1_len'] = new_df['question1'].str.len() 
new_df['q2_len'] = new_df['question2'].str.len()

new_df['q1_num_words'] = new_df['question1'].apply(lambda row: len(row.split(" ")))
new_df['q2_num_words'] = new_df['question2'].apply(lambda row: len(row.split(" ")))

def common_words(row):
    w1 = set(map(lambda word: word.lower().strip(), row['question1'].split(" ")))
    w2 = set(map(lambda word: word.lower().strip(), row['question2'].split(" ")))    
    return len(w1 & w2)
new_df['word_common'] = new_df.apply(common_words, axis=1)

def total_words(row):
    w1 = set(map(lambda word: word.lower().strip(), row['question1'].split(" ")))
    w2 = set(map(lambda word: word.lower().strip(), row['question2'].split(" ")))    
    return (len(w1) + len(w2))
new_df['word_total'] = new_df.apply(total_words, axis=1)
new_df['word_share'] = round(new_df['word_common']/new_df['word_total'],2)

# Advanced Features
from nltk.corpus import stopwords
def fetch_token_features(row):    
    q1 = row['question1']
    q2 = row['question2']
    SAFE_DIV = 0.0001
    STOP_WORDS = stopwords.words("english")    
    token_features = [0.0]*8    
    # Converting the Sentence into Tokens: 
    q1_tokens = q1.split()
    q2_tokens = q2.split()    
    if len(q1_tokens) == 0 or len(q2_tokens) == 0:
        return token_features
    # Get the non-stopwords in Questions
    q1_words = set([word for word in q1_tokens if word not in STOP_WORDS])
    q2_words = set([word for word in q2_tokens if word not in STOP_WORDS])    
    #Get the stopwords in Questions
    q1_stops = set([word for word in q1_tokens if word in STOP_WORDS])
    q2_stops = set([word for word in q2_tokens if word in STOP_WORDS])    
    # Get the common non-stopwords from Question pair
    common_word_count = len(q1_words.intersection(q2_words))    
    # Get the common stopwords from Question pair
    common_stop_count = len(q1_stops.intersection(q2_stops))    
    # Get the common Tokens from Question pair
    common_token_count = len(set(q1_tokens).intersection(set(q2_tokens)))    
    token_features[0] = common_word_count / (min(len(q1_words), len(q2_words)) + SAFE_DIV)
    token_features[1] = common_word_count / (max(len(q1_words), len(q2_words)) + SAFE_DIV)
    token_features[2] = common_stop_count / (min(len(q1_stops), len(q2_stops)) + SAFE_DIV)
    token_features[3] = common_stop_count / (max(len(q1_stops), len(q2_stops)) + SAFE_DIV)
    token_features[4] = common_token_count / (min(len(q1_tokens), len(q2_tokens)) + SAFE_DIV)
    token_features[5] = common_token_count / (max(len(q1_tokens), len(q2_tokens)) + SAFE_DIV)    
    # Last word of both question is same or not
    token_features[6] = int(q1_tokens[-1] == q2_tokens[-1])    
    # First word of both question is same or not
    token_features[7] = int(q1_tokens[0] == q2_tokens[0])    
    return token_features

token_features = new_df.apply(fetch_token_features, axis=1)

new_df["cwc_min"]       = list(map(lambda x: x[0], token_features))
new_df["cwc_max"]       = list(map(lambda x: x[1], token_features))
new_df["csc_min"]       = list(map(lambda x: x[2], token_features))
new_df["csc_max"]       = list(map(lambda x: x[3], token_features))
new_df["ctc_min"]       = list(map(lambda x: x[4], token_features))
new_df["ctc_max"]       = list(map(lambda x: x[5], token_features))
new_df["last_word_eq"]  = list(map(lambda x: x[6], token_features))
new_df["first_word_eq"] = list(map(lambda x: x[7], token_features))

import distance
def fetch_length_features(row):    
    q1 = row['question1']
    q2 = row['question2']    
    length_features = [0.0]*3    
    # Converting the Sentence into Tokens: 
    q1_tokens = q1.split()
    q2_tokens = q2.split()    
    if len(q1_tokens) == 0 or len(q2_tokens) == 0:
        return length_features    
    # Absolute length features
    length_features[0] = abs(len(q1_tokens) - len(q2_tokens))    
    #Average Token Length of both Questions
    length_features[1] = (len(q1_tokens) + len(q2_tokens))/2    
    strs = list(distance.lcsubstrings(q1, q2))
    length_features[2] = len(strs[0]) / (min(len(q1), len(q2)) + 1)    
    return length_features

length_features = new_df.apply(fetch_length_features, axis=1)
new_df['abs_len_diff'] = list(map(lambda x: x[0], length_features))
new_df['mean_len'] = list(map(lambda x: x[1], length_features))
new_df['longest_substr_ratio'] = list(map(lambda x: x[2], length_features))

# Fuzzy Features
from fuzzywuzzy import fuzz
def fetch_fuzzy_features(row):    
    q1 = row['question1']
    q2 = row['question2']    
    fuzzy_features = [0.0]*4    
    # fuzz_ratio
    fuzzy_features[0] = fuzz.QRatio(q1, q2)
    # fuzz_partial_ratio
    fuzzy_features[1] = fuzz.partial_ratio(q1, q2)
    # token_sort_ratio
    fuzzy_features[2] = fuzz.token_sort_ratio(q1, q2)
    # token_set_ratio
    fuzzy_features[3] = fuzz.token_set_ratio(q1, q2)
    return fuzzy_features
fuzzy_features = new_df.apply(fetch_fuzzy_features, axis=1)

# Creating new feature columns for fuzzy features
new_df['fuzz_ratio'] = list(map(lambda x: x[0], fuzzy_features))
new_df['fuzz_partial_ratio'] = list(map(lambda x: x[1], fuzzy_features))
new_df['token_sort_ratio'] = list(map(lambda x: x[2], fuzzy_features))
new_df['token_set_ratio'] = list(map(lambda x: x[3], fuzzy_features))

# Using TSNE for Dimentionality reduction for 15 Features(Generated after cleaning the data) to 3 dimention
from sklearn.preprocessing import MinMaxScaler
X = MinMaxScaler().fit_transform(new_df[['cwc_min', 'cwc_max', 'csc_min', 'csc_max' , 'ctc_min' , 'ctc_max' , 'last_word_eq', 'first_word_eq' , 'abs_len_diff' , 'mean_len' , 'token_set_ratio' , 'token_sort_ratio' ,  'fuzz_ratio' , 'fuzz_partial_ratio' , 'longest_substr_ratio']])
y = new_df['is_duplicate'].values

from sklearn.manifold import TSNE
tsne2d = TSNE(
    n_components=2,
    init='random', # pca
    random_state=101,
    method='barnes_hut',
    n_iter=1000,
    verbose=2,
    angle=0.5
).fit_transform(X)

x_df = pd.DataFrame({'x':tsne2d[:,0], 'y':tsne2d[:,1] ,'label':y})
# draw the plot in appropriate place in the grid
sns.lmplot(data=x_df, x='x', y='y', hue='label', fit_reg=False, size=8,palette="Set1",markers=['s','o'])
tsne3d = TSNE(
    n_components=3,
    init='random', # pca
    random_state=101,
    method='barnes_hut',
    n_iter=1000,
    verbose=2,
    angle=0.5
).fit_transform(X)

import plotly.graph_objs as go
import plotly.tools as tls
import plotly.offline as py
py.init_notebook_mode(connected=True)

trace1 = go.Scatter3d(
    x=tsne3d[:,0],
    y=tsne3d[:,1],
    z=tsne3d[:,2],
    mode='markers',
    marker=dict(
        sizemode='diameter',
        color = y,
        colorscale = 'Portland',
        colorbar = dict(title = 'duplicate'),
        line=dict(color='rgb(255, 255, 255)'),
        opacity=0.75
    )
)
data=[trace1]
layout=dict(height=800, width=800, title='3d embedding with engineered features')
fig=dict(data=data, layout=layout)
py.iplot(fig, filename='3DBubble')

ques_df = new_df[['question1','question2']]
final_df = new_df.drop(columns=['id','qid1','qid2','question1','question2'])

from sklearn.feature_extraction.text import CountVectorizer
# merge texts
questions = list(ques_df['question1']) + list(ques_df['question2'])
cv = CountVectorizer(max_features=3000)
q1_arr, q2_arr = np.vsplit(cv.fit_transform(questions).toarray(),2)
temp_df1 = pd.DataFrame(q1_arr, index= ques_df.index)
temp_df2 = pd.DataFrame(q2_arr, index= ques_df.index)
temp_df = pd.concat([temp_df1, temp_df2], axis=1)
final_df = pd.concat([final_df, temp_df], axis=1)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(final_df.iloc[:,1:].values,final_df.iloc[:,0].values,test_size=0.2,random_state=1)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
rf = RandomForestClassifier()
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)
accuracy_score(y_test,y_pred)

from xgboost import XGBClassifier
xgb = XGBClassifier()
xgb.fit(X_train,y_train)
y_pred1 = xgb.predict(X_test)
accuracy_score(y_test,y_pred1)

from sklearn.metrics import confusion_matrix
# for random forest model
confusion_matrix(y_test,y_pred)
# for xgboost model
confusion_matrix(y_test,y_pred1)

def test_common_words(q1,q2):
    w1 = set(map(lambda word: word.lower().strip(), q1.split(" ")))
    w2 = set(map(lambda word: word.lower().strip(), q2.split(" ")))    
    return len(w1 & w2)
def test_total_words(q1,q2):
    w1 = set(map(lambda word: word.lower().strip(), q1.split(" ")))
    w2 = set(map(lambda word: word.lower().strip(), q2.split(" ")))    
    return (len(w1) + len(w2))
def test_fetch_token_features(q1,q2):    
    SAFE_DIV = 0.0001 
    STOP_WORDS = stopwords.words("english")    
    token_features = [0.0]*8    
    # Converting the Sentence into Tokens: 
    q1_tokens = q1.split()
    q2_tokens = q2.split()    
    if len(q1_tokens) == 0 or len(q2_tokens) == 0:
        return token_features
    # Get the non-stopwords in Questions
    q1_words = set([word for word in q1_tokens if word not in STOP_WORDS])
    q2_words = set([word for word in q2_tokens if word not in STOP_WORDS])    
    #Get the stopwords in Questions
    q1_stops = set([word for word in q1_tokens if word in STOP_WORDS])
    q2_stops = set([word for word in q2_tokens if word in STOP_WORDS])    
    # Get the common non-stopwords from Question pair
    common_word_count = len(q1_words.intersection(q2_words))    
    # Get the common stopwords from Question pair
    common_stop_count = len(q1_stops.intersection(q2_stops))    
    # Get the common Tokens from Question pair
    common_token_count = len(set(q1_tokens).intersection(set(q2_tokens)))    
    token_features[0] = common_word_count / (min(len(q1_words), len(q2_words)) + SAFE_DIV)
    token_features[1] = common_word_count / (max(len(q1_words), len(q2_words)) + SAFE_DIV)
    token_features[2] = common_stop_count / (min(len(q1_stops), len(q2_stops)) + SAFE_DIV)
    token_features[3] = common_stop_count / (max(len(q1_stops), len(q2_stops)) + SAFE_DIV)
    token_features[4] = common_token_count / (min(len(q1_tokens), len(q2_tokens)) + SAFE_DIV)
    token_features[5] = common_token_count / (max(len(q1_tokens), len(q2_tokens)) + SAFE_DIV)    
    # Last word of both question is same or not
    token_features[6] = int(q1_tokens[-1] == q2_tokens[-1])    
    # First word of both question is same or not
    token_features[7] = int(q1_tokens[0] == q2_tokens[0])    
    return token_features
    
def test_fetch_length_features(q1,q2):
    length_features = [0.0]*3
    # Converting the Sentence into Tokens: 
    q1_tokens = q1.split()
    q2_tokens = q2.split()    
    if len(q1_tokens) == 0 or len(q2_tokens) == 0:
        return length_features    
    # Absolute length features
    length_features[0] = abs(len(q1_tokens) - len(q2_tokens))    
    #Average Token Length of both Questions
    length_features[1] = (len(q1_tokens) + len(q2_tokens))/2    
    strs = list(distance.lcsubstrings(q1, q2))
    length_features[2] = len(strs[0]) / (min(len(q1), len(q2)) + 1)    
    return length_features

def test_fetch_fuzzy_features(q1,q2):    
    fuzzy_features = [0.0]*4    
    # fuzz_ratio
    fuzzy_features[0] = fuzz.QRatio(q1, q2)
    # fuzz_partial_ratio
    fuzzy_features[1] = fuzz.partial_ratio(q1, q2)
    # token_sort_ratio
    fuzzy_features[2] = fuzz.token_sort_ratio(q1, q2)
    # token_set_ratio
    fuzzy_features[3] = fuzz.token_set_ratio(q1, q2)
    return fuzzy_features

def query_point_creator(q1,q2):    
    input_query = []    
    # preprocess
    q1 = preprocess(q1)
    q2 = preprocess(q2)    
    # fetch basic features
    input_query.append(len(q1))
    input_query.append(len(q2))    
    input_query.append(len(q1.split(" ")))
    input_query.append(len(q2.split(" ")))    
    input_query.append(test_common_words(q1,q2))
    input_query.append(test_total_words(q1,q2))
    input_query.append(round(test_common_words(q1,q2)/test_total_words(q1,q2),2))    
    # fetch token features
    token_features = test_fetch_token_features(q1,q2)
    input_query.extend(token_features)    
    # fetch length based features
    length_features = test_fetch_length_features(q1,q2)
    input_query.extend(length_features)    
    # fetch fuzzy features
    fuzzy_features = test_fetch_fuzzy_features(q1,q2)
    input_query.extend(fuzzy_features)    
    # bow feature for q1
    q1_bow = cv.transform([q1]).toarray()    
    # bow feature for q2
    q2_bow = cv.transform([q2]).toarray()
    return np.hstack((np.array(input_query).reshape(1,22),q1_bow,q2_bow))

q1 = 'Where is the capital of India?'
q2 = 'What is the current capital of Pakistan?'
q3 = 'Which city serves as the capital of India?'
q4 = 'What is the business capital of India?'
rf.predict(query_point_creator(q1,q4))

import pickle
pickle.dump(rf,open('model.pkl','wb'))
pickle.dump(cv,open('cv.pkl','wb'))












###############################################################################################################
#### Deep Learning DL in PyTorch - Everything
###############################################################################################################
import torch

# Create tensor in torch:
## empty tensor of shape (2,3) - values are from previously stored at those locations
x = torch.empty(2,3)
x.shape                             # Tensor Shape
x.dtype                             #torch.int64, torch.float32, etc..
type(x)                             ## check type - torch.Tensor
id(x)                               #memory location of where x is pointing

torch.zeros(2,3)                    ## using zeros
torch.ones(2,3)                     ## using ones
torch.rand(2,3)                     ## using rand
torch.manual_seed(100)              ## use of seed
torch.rand(2,3)
torch.randint(size=(2,3), low=0, high=10)
torch.tensor([[1,2,3],[4,5,6]])     ## using tensor
torch.arange(0,19,2)                ## using arange
torch.linspace(1,10,10)             ## using linspace
torch.eye(5)                        ## using eye
torch.full((3,3),5)                 ## using full

## this will create integer tensor
torch.tensor([[1.0,2.0,3.0],[4.0,5.0,6.0]], dtype=torch.int32)
## this will create float tensor
torch.tensor([[1,2,3],[4,5,6]], dtype=torch.float64)
## change dtype of existing tensor
x.to(torch.float32)



torch.empty_like(x)                 ## empty tensor with shape that of x
torch.zeros_like(x)                 ## zeros tensor with shape that of x
torch.ones_like(x)                  ## ones tensor with shape that of x
## random tensor with shape that of x
torch.rand_like(x)          #error - coz x is INT, rand creates float
torch.rand_like(x,dtype=torch.float64)

# Mathematical Scalar Operations
x + 2                               ## addition
x - 2                               ## subtraction
x * 3                               ## multiplication
x / 3                               ## division
(x * 100)//3                        ## int division
(x * 100)%2                         ## mod
x**2                                ## power

# Mathematical tensor Operations (element-by-element)
x + y                               ## addition
x - y                               ## subtraction
x * y                               ## multiplication
x / y                               ## division
x//y                                ## int division
x%y                                 ## mod
x**y                                ## power

# other Mathematical operations
torch.abs(x)                        ## absolute values of elements
torch.neg(x)                        ## negative of all values in a tensor
torch.round(x)                      ## round all numbers in a tensor
torch.ceil(x)                       ## ceil all numbers in a tensor
torch.floor(x)                      ## floor all numbers in a tensor
torch.clamp(x, min=2, max=3)        ## clamp all numbers in a range, 2 for <=2, 3 for >=3
torch.sum(x)                        ## sum of all numbers in a tensor
torch.sum(x, dim=0)                 ## sum along columns in a tensor
torch.sum(x, dim=1)                 ## sum along rows in a tensor
torch.mean(x)                       ## mean of all numbers in a tensor - d.type(x) must be torch.float
torch.mean(x, dim=0)                ## mean along columns in a tensor
torch.mean(x, dim=1)                ## mean along rows in a tensor
torch.max(x, dim=0)                 ## maximum along columns in a tensor
torch.min(x, dim=1)                 ## minimum along rows in a tensor
torch.product(x)                    ## product of all numbers in a tensor
torch.std(x)                        ## standard deviation of all numbers in a tensor
torch.var(x)                        ## variance of all numbers in a tensor
torch.argmax(x)                     ## position of maximum in a tensor
torch.argmin(x)                     ## position of minimum in a tensor

# Matrix Operations
torch.matmul(x,y)                   ## Matrix Multiplication
torch.dot(x, y)                     ## dot product #x and y are two vectors
torch.transpose(f,0,1)              ## Transpose --> swap 0th dimension with 1st
torch.det(a)                        ## determinant - only possible for square matrix
torch.inverse(a)                    ## inverse - only possible for square matrix

# Comparison Operations
x > y
x < y
x >= y
x <= y
x == y

# Special Functions
torch.log(x)
torch.exp(x)
torch.sqrt(x)
torch.sigmoid(x)
torch.softmax(x, dim=0)
torch.relu(x)

# all the above functions return a tensor, that occupies space
# what if we don't want to save the resultant tensor at a new place
# what if we wanna save resultant tensor in x itself.
# This is called inplace=True operation
x.add_(y)                           ## add x and y and save the resultant in x
x.relu_()                           ## relu of x saved to x
y = x.clone()                       ## copy tensor x to y


# GPU operations
torch.cuda.is_available()           ## check if gpu is available
device = torch.device('cuda')       ## create new tensor on GPU
torch.rand((2,3), device=device)
a.to(device)                        ## move existing CPU tensors to GPU

a = torch.ones(4,4)
a.reshape(2,2,2,2)                  ## Reshape
a.flatten()                         ## Flatten

a = torch.rand(2,3,4)
a.permute(2,0,1).shape              ## permute - change the index of the shape #(4,2,3) changed the shape sequence

a = torch.rand(226,226,3)
a.unsqueeze(0).shape                ## unsqueeze - add a new dimension at a position    #(1,226,226,3) added a new dim at position 0

a = torch.rand(1,20)                #2-D tensor
a.squeeze(0).shape                  ## squeeze - remove a dimension #([20]) 1-D tensor


## convert a PyTorch Tensor to NumPy Tensor
a = torch.tensor([1,2,3])
b = a.numpy()                       ## PyTorch to Numpy
c = torch.from_numpy(b)             ## Numpy to PyTorch


# Autograd - Automatic Gradient in PyTorch
## example 1
x = torch.tensor(3, requires_grad=True)
y = x**2                            ## relationship between x and y
y.backward()                        ## calculating gradient in backward direction
x.grad                              ## gives gradient automatically

## example 2
x = torch.tensor(3, requires_grad=True)
y = x**2                            ## relationship between x and y
z = torch.sin(y)                    ## relationship between y and z
z.backward()                        ## calculating gradient in backward direction
x.grad                              ## gives gradient automatically

## example 3
x = torch.tensor([1,2,3], requires_grad=True)
z = x**2.mean()                         ## relationship between x and z
y_hat = torch.sigmoid(z)                ## relationship between y and z
L = ylog(y_hat) - (1-y)log(1-y_hat)     ## Binary CrossEntropy Loss
L.backward()                            ## calculating gradient in backward direction
x.grad                                  ## gives gradient automatically

## Autograd keeps accumulating gradients over multiple runs
## therefore, it is necessary to clear the gradients before each run.
x.grad.zero_()

## Turn off gradient tracking
## method 1, backward() function doesn't work anymore, gradient tracking OFF
x.requires_grad_(False)
## method 2, detach() function
z = x.detach()
y1 = x**2                           ## gradient tracking ON
y2 = z**2                           ## gradient tracking OFF
y1.backward()                       ## POSSIBLE
y2.backward()                       ## NOT POSSIBLE
## method 3, with torch.no_grad()
with torch.no_grad:
    y = x**2    #gradient tracking OFF
    






##################################################################
# DL in PyTorch - Simple Neural Network from scratch
##################################################################
import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('https://raw.githubusercontent.com/gscdit/Breast-Cancer-Detection/refs/heads/master/data.csv')
df.head()
df.shape
df.drop(columns=['id', 'Unnamed: 32'], inplace= True)
df.head()

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:], df.iloc[:, 0], test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train
y_train

encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)
y_train

## Numpy arrays to PyTorch tensors
X_train_tensor = torch.from_numpy(X_train)
X_test_tensor = torch.from_numpy(X_test)
y_train_tensor = torch.from_numpy(y_train)
y_test_tensor = torch.from_numpy(y_test)

X_train_tensor.shape
y_train_tensor.shape

## Defining the model
class MySimpleNN():
def __init__(self, X):
    self.weights = torch.rand(X.shape[1], 1, dtype=torch.float64, requires_grad=True)
    self.bias = torch.zeros(1, dtype=torch.float64, requires_grad=True)

def forward(self, X):
    z = torch.matmul(X, self.weights) + self.bias
    y_pred = torch.sigmoid(z)
    return y_pred

def loss_function(self, y_pred, y):
    # Clamp predictions to avoid log(0)
    epsilon = 1e-7
    y_pred = torch.clamp(y_pred, epsilon, 1 - epsilon)
    # Calculate loss
    loss = -(y_train_tensor * torch.log(y_pred) + (1 - y_train_tensor) * torch.log(1 - y_pred)).mean()
    return loss

## Important Parameters
learning_rate = 0.1
epochs = 25

## Training Pipeline
### create model
model = MySimpleNN(X_train_tensor)
### define loop
for epoch in range(epochs):
    ### forward pass
    y_pred = model.forward(X_train_tensor)
    ### loss calculate
    loss = model.loss_function(y_pred, y_train_tensor)
    ### backward pass
    loss.backward()
    ### parameters update
    with torch.no_grad():
        model.weights -= learning_rate * model.weights.grad
        model.bias -= learning_rate * model.bias.grad
    ### zero gradients
    model.weights.grad.zero_()
    model.bias.grad.zero_()
    ### print loss in each epoch
    print(f'Epoch: {epoch + 1}, Loss: {loss.item()}')

model.bias

## model evaluation
with torch.no_grad():
    y_pred = model.forward(X_test_tensor)
    y_pred = (y_pred > 0.9).float()
    accuracy = (y_pred == y_test_tensor).float().mean()
    print(f'Accuracy: {accuracy.item()}')
  
  
  
  
  
  
  
  
##################################################################
# DL in PyTorch - Neural Network using torch.nn
##################################################################
import torch
import torch.nn as nn

## create model class: basic implementation
class Model(nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.linear1 = nn.Linear(num_features, 3)   #num_features=input branches, 3=output branches
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(3,1)
        self.sigmoid = nn.Sigmoid()
       
    def forward(self, features):
        out = self.linear1(features)
        out = self.relu(out)
        out = self.linear2(out)
        out = self.sigmoid(out)
        return out
        
## create model class: using sequential container
class Model(nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(num_features, 3),
            nn.ReLU(),
            nn.Linear(3,1),
            nn.Sigmoid()
        )

    def forward(self, features):
        out = self.network(features)
        return out
    
## create dataset
data = torch.rand(10,5)
## create model object
model = Model(data.shape[1])
## call model for forward pass
model.forward(data)             #not recommended by PyTorch
model(data)                     #recommended by PyTorch, calling the object of class automatically triggers the forward method
## show model weights
model.linear1.weights
model.linear1.bias
model.linear1.weights
model.linear1.bias
## to check model summary
!pip install torchinfo
from torchinfo import summary
summary(model, input_size=(10,5))
    








##################################################################
# DL in PyTorch - Simple Neural Network from scratch using torch.nn
##################################################################
import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('https://raw.githubusercontent.com/gscdit/Breast-Cancer-Detection/refs/heads/master/data.csv')
df.head()
df.shape
df.drop(columns=['id', 'Unnamed: 32'], inplace= True)
df.head()

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:], df.iloc[:, 0], test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train
y_train

encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)
y_train

## Numpy arrays to PyTorch tensors
X_train_tensor = torch.from_numpy(X_train)
X_test_tensor = torch.from_numpy(X_test)
y_train_tensor = torch.from_numpy(y_train)
y_test_tensor = torch.from_numpy(y_test)

X_train_tensor.shape
y_train_tensor.shape

## Defining the model
import torch.nn as nn
class MySimpleNN():
    def __init__(self, X):
        super.__init__()
        self.linear = nn.Linear(num_features, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, X):
        out = self.linear(features)
        out = self.sigmoid(out)
        return out

## Important Parameters
learning_rate = 0.1
epochs = 25

## Define Loss Function - Binary Cross Entropy
loss_function = nn.BCELoss()

## Training Pipeline
### create model
model = MySimpleNN(X_train_tensor.shape[1])
## Define Optimizer
optimizer = torch.optim.SGD(model.parameters, lr=learning_rate)
### define loop
for epoch in range(epochs):
    ### forward pass
    y_pred = model(X_train_tensor)
    ### loss calculate
    loss = loss_function(y_pred, y_train_tensor.view(-1,1)) #view as one less row, and 1 column
    ### zero gradients
    optimizer.zero_grad()
    ### backward pass
    loss.backward()
    ### parameters update
    optimizer.step()
    ### print loss in each epoch
    print(f'Epoch: {epoch + 1}, Loss: {loss.item()}')

## model evaluation
with torch.no_grad():
    y_pred = model.forward(X_test_tensor)
    y_pred = (y_pred > 0.9).float()
    accuracy = (y_pred == y_test_tensor).float().mean()
    print(f'Accuracy: {accuracy.item()}')


    






##################################################################
# DL in PyTorch
# Dataset & Dataloader Class (better management of data and code)
##################################################################
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels

    def __len__(self):
        len(self.features)

    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]

train_dataset = CustomDataset(X_train_tensor, y_train_tensor)
test_dataset = CustomDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)

import torch.nn as nn


class MySimpleNN(nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.linear = nn.Linear(num_features, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, features):
        out = self.linear(features)
        out = self.sigmoid(out)
        return out

learning_rate = 0.1
epochs = 25

## create model
model = MySimpleNN(X_train_tensor.shape[1])
## define optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
## define loss function
loss_function = nn.BCELoss()


# define loop
for epoch in range(epochs):
    for batch_features, batch_labels in train_loader:
        # forward pass
        y_pred = model(batch_features)
        # loss calculate
        loss = loss_function(y_pred, batch_labels.view(-1,1))
        # clear gradients
        optimizer.zero_grad()
        # backward pass
        loss.backward()
        # parameters update
        optimizer.step()
    # print loss in each epoch
    print(f'Epoch: {epoch + 1}, Loss: {loss.item()}')

# Model evaluation using test_loader
model.eval()  # Set the model to evaluation mode
accuracy_list = []
with torch.no_grad():
    for batch_features, batch_labels in test_loader:
        # Forward pass
        y_pred = model(batch_features)
        y_pred = (y_pred > 0.8).float()  # Convert probabilities to binary predictions
        # Calculate accuracy for the current batch
        batch_accuracy = (y_pred.view(-1) == batch_labels).float().mean().item()
        accuracy_list.append(batch_accuracy)
# Calculate overall accuracy
overall_accuracy = sum(accuracy_list) / len(accuracy_list)
print(f'Accuracy: {overall_accuracy:.4f}')


    








##################################################################
# DL in PyTorch - ANN/MLP using PyTorch [on CPU & GPU]
##################################################################
# Dataset => Fashion MNIST
# Input Layer => 784 Neurons
# Hidden Layer 1 => 128 Neurons => ReLU
# Hidden Layer => 64 Neurons => ReLU
# Output Layer => 10 Neurons (for 10 Classes) => Softmax
# 
# WorkFlow =>
#     1) create Dataloader obj for Training & Testing data
#     2) create Traing loop
#     3) create Evaluation code
# 
# 
# Code =>

import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# [Optional Code 1]: use GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Set seed
torch.manual_seed(42)

# load data
df = pd.read_csv("fmnist_small.csv")
df.head()

# create a 4x4 grid of images
fig, axes = plt.subplots(4,4,figsize=(10,10))
for i, ax in enumerate(axes.flat):
    img = df.iloc[i, 1:].values.reshape(28,28)
    ax.imshow(img)
    ax.axis("off")
    ax.set_title(f"Label: {df.iloc[i,0]}")
plt.tight_layout(rect=[0,0,1,0.96])
plt.show()

# train test split
X = df.iloc[:,1:].values()
y = df.iloc[:,0].values()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# scaling the features
X_train = X_train/255.0
X_test = X_test/255.0

# create Custom Dataset class
class CustomDataset(Dataset):
    def __init__(self, features, labels):
        self.features = torch.tensor(features, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)
    
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, index):
        return self.features[index], self.labels[index]

# create train dataset object
train_dataset = CustomDataset(X_train, y_train)
# create test dataset object
test_dataset = CustomDataset(X_test, y_test)

# create train and test loader
train_loader = Dataloader(train_dataset,batch_size=32,shuffle=True)
test_dataloader=Dataloader(test_dataset,batch_size=32,shuffle=False)

# create model / define NN class
class MyNN(nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(in_features=num_features, out_features=128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
            #no need to add softmax
            #softmax already built in nn.Module
        )
    def forwar(self, X):
        return self.model(X)

# set learning rate & epochs
epochs = 100
learning_rate = 0.1

# instantiate the model
model = MyNN(X_train.shape[1])
# [optional code 2]: move model to gpu
model = model.to(device)

# loss function
criterion = nn.CrossEntropyLoss()
# optimizer
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# training loop
for epoch in range(epochs):
    total_epoch_loss = 0
    for batch_features, batch_labels in train_loader:
        # [optional code 3]: move each batch of dataset to GPU
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        # forward pass
        outputs = model(batch_features)
        # calculate loss
        loss = criterion(outputs, batch_labels)
        # back pass
        optimizer.zero_grad()
        loss.backward()
        # update grads
        optimizer.step()
        # update total epoch loss
        total_epoch_loss += loss
    avg_loss = total_epoch_loss / len(train_loader)
    print(f"Epoch: {epoch + 1}, Loss: {avg_loss}")
    
# set model to eval mode
model.eval()

# evaluation code on test data
total = 0
correct  = 0
with torch.no_grad():
    for batch_features, batch_labels in test_loader:
        # [optional code 4]: move to GPU
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        # tensor of 10 probabilities for all rows
        outputs = model(batch_features)
        # extracting the argmax of probabilities of each row
        _, predicted = torch.max(outputs, 1)
        # calculating the number of rows predicted so far
        total += batch_labels.shape[0]
        # finding the number of correct predictions
        correct += (predicted == batch_labels).sum().item()
print(f"Accuracy: {correct/total}"

# evaluation code on train data
total = 0
correct  = 0
with torch.no_grad():
    for batch_features, batch_labels in train_loader:
        # [optional code 4]: move to GPU
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        # tensor of 10 probabilities for all rows
        outputs = model(batch_features)
        # extracting the argmax of probabilities of each row
        _, predicted = torch.max(outputs, 1)
        # calculating the number of rows predicted so far
        total += batch_labels.shape[0]
        # finding the number of correct predictions
        correct += (predicted == batch_labels).sum().item()
print(f"Accuracy: {correct/total}"



    








##################################################################
# DL in PyTorch - Reduce Overfitting
##################################################################
# 1) Add more data
# 2) Reduce complexity of NN Architecture
# 3) Regularization (L2)
    ## applied to weights of the model to penalize large values
    ## adds penalty term to the loss function
    ## PyTorch also applies Regularization using weight_decay
model = MyNN(X_train.shape[1])
model = model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate, weight_decay=1e-4)

# 4) Dropouts
    ## Applied to Hidden Layers only
    ## Applied after ReLU activation function
    ## Randomly turns off p% neurons in the hidden layers during each pass
    ## This has regularization effect
    ## During evaluation, dropout is not used
class MyNN(nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(in_features=num_features, out_features=128),
            nn.ReLU(),
            nn.Dropout(p=0.3),          #dropout code added
            nn.Linear(in_features=128, out_features=64),
            nn.ReLU(),
            nn.Dropout(p=0.3),          #dropout code added
            nn.Linear(in_features=64, out_features=10)
            #no need to add softmax
            #softmax already built in nn.Module
        )
    def forwar(self, X):
        return self.model(X)


# 5) Data Augmentation (CNN mainly)
# 6) Batch Normalization
    ## Applied to Hidden Layers only
    ## Applied after Linear & before Activation Function
    ## Improves Training stability by reducing Internal Covariance Shift (ICS) & allowing the use of higher learning rate
    ## output of each layer before activation is normalized using mean and standard deviation of that layer's output
    ## includes Learnable Parameters - gamma (scaling) & beta (shifting)
    ## creates the effect of regularization
    ## During evaluation, Batch Normalization is not used
class MyNN(nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(in_features=num_features, out_features=128),
            nn.BatchNorm1d(num_features=128),        #Batch Norm code added
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(in_features=128, out_features=64),
            nn.BatchNorm1d(num_features=64),         #Batch Norm code added
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(in_features=64, out_features=10)
            #no need to add softmax
            #softmax already built in nn.Module
        )
    def forwar(self, X):
        return self.model(X)
    

# 7) Early Stopping



    





##################################################################
# DL in PyTorch - Hyperparameter Tuning using Optuna
##################################################################
# 1) Number of Hidden Layers
# 2) Neurons in each Layer
# 3) Number of Epochs
# 4) Optimizer
# 5) Learning Rate
# 6) Batch Size
# 7) Dropout Rate
# 8) Weight Decay(Lambda)

import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import optuna

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
torch.manual_seed(42)
df = pd.read_csv("fmnist_small.csv")

X = df.iloc[:,1:].values()
y = df.iloc[:,0].values()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)

X_train = X_train/255.0
X_test = X_test/255.0

class CustomDataset(Dataset):
    def __init__(self, features, labels):
        self.features = torch.tensor(features, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)
    
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, index):
        return self.features[index], self.labels[index]

train_dataset = CustomDataset(X_train, y_train)
test_dataset = CustomDataset(X_test, y_test)

# create NN model
class MyNN(nn.Module):
    def __init__(self, input_dim, output_dim, num_hidden_layers, neurons_per_layer, dropout_rate):
        super().__init__()
        layers = []
        for i in range(num_hidden_layers):
            layers.append(nn.Linear(input_dim, neurons_per_layer))
            layers.append(nn.BatchNorm1d(neurons_per_layer)
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout_rate))
            input_dim = neurons_per_layer
        layers.append(nn.Linear(neurons_per_layer, output_dim)
        self.model = nn.Sequential(*layers)
        
    def forward(self, X):
        return self.model(X)

# create objective function
def objective(trial):
    # next hyperparameter values from the search space
    num_hidden_layers = trial.suggest_int("num_hidden_layers",1,5)
    neurons_per_layer = trial.suggest_int("neurons_per_layer",8,128,step=8)
    epochs = trial.suggest_int("epochs",10,50,step=10)
    learning_rate = trial.suggest_float("learning_rate", 1e-5, 1e-1, log=True)
    dropout_rate = trial.suggest_float("dropout_rate", 0.1,0.5,step=0.1)
    batch_size = trial.suggest_categorical("batch_size",[16,32,64,128])
    optimizer_name = trial.suggest_categorical("optimizer",["Adam","SGD","RMSprop"])
    weight_decay = trial.suggest_float("weight_decay",1e-5,1e-3,log=True)
    
    train_loader = Dataloader(train_dataset,batch_size=batch_size,shuffle=True)
    test_dataloader=Dataloader(test_dataset,batch_size=batch_size,shuffle=False)
    
    # model init
    input_dim = 784
    output_dim = 10
    
    model = MyNN(input_dim, output_dim, num_hidden_layers, neurons_per_layer, dropout_rate)
    model.to(device)
    
    # optimizer selection
    criterion = nn.CrossEntropyLoss()    
    if optimizer_name == "Adam":
        optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    elif optimizer_name == "SGD":
        optimizer = optim.SGD(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    else:
        optimizer = optim.RMSprop(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    
    # training loop
    for epoch in range(epochs):
        for batch_features, batch_labels in train_loader:
            batch_features = batch_features.to(device)
            batch_labels = batch_labels.to(device)
            
            outputs = model(batch_features)
            loss = criterion(outputs, batch_labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    # evaluation
    model.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for batch_features, batch_labels in test_loader:
            batch_features = batch_features.to(device)
            batch_labels = batch_labels.to(device)
            
            outputs = model(batch_features)
            _, predicted = torch.max(outputs, 1)
            total += batch_labels.shape[0]
            correct += (predicted == batch_labels).sum().item()
        accuracy = correct/total
    
    return accuracy

# create study

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=10)

# find best accuracy from study object
study.best_value
# find best parameters from study object
study.best_params












##################################################################
# DL in PyTorch - Basic CNN
##################################################################


import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
torch.manual_seed(42)

df = pd.read_csv("fmnist_small.csv")
df.head()

X = df.iloc[:,1:].values()
y = df.iloc[:,0].values()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)
X_train = X_train/255.0
X_test = X_test/255.0

class CustomDataset(Dataset):
    def __init__(self, features, labels):
        #self.features = torch.tensor(features, dtype=torch.float32)
        self.features = torch.tensor(features, dtype=torch.float32).reshape(-1,1,28,28)
        self.labels = torch.tensor(labels, dtype=torch.long)
    
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, index):
        return self.features[index], self.labels[index]

train_dataset = CustomDataset(X_train, y_train)
test_dataset = CustomDataset(X_test, y_test)
train_loader = Dataloader(train_dataset,batch_size=32,shuffle=True)
test_dataloader=Dataloader(test_dataset,batch_size=32,shuffle=False)

# create model / define NN class
class MyNN(nn.Module):
    def __init__(self, input_channels):
        super().__init__()
        #CNN - feature extraction
        self.features = nn.Sequential(
            nn.Conv2d(in_channels=input_channels,out_channels=32,kernel_size=3,padding='same'), #out_channels = Number of filters
            nn.ReLU(),
            nn.BatchNorm2d(num_features=32),
            nn.MaxPool2d(kernel_size=2,stride=2),
            
            nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3,padding='same'),
            nn.ReLU(),
            nn.BatchNorm2d(num_features=64),
            nn.MaxPool2d(kernel_size=2,stride=2)
        )
        #ANN
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=64*7*7, out_features=128),
            nn.ReLU(),
            nn.Dropout(p=0.4),
            
            nn.Linear(in_features=128, out_features=64),
            nn.ReLU(),
            nn.Dropout(p=0.4),
            
            nn.Linear(in_features=64, out_features=10),
        )

    def forward(self, X):
        X = self.features(X)
        X = self.classifier(X)
        return X

epochs = 100
learning_rate = 0.01

model = MyNN(input_channels=1)
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate, weight_decay=1e-4)

for epoch in range(epochs):
    total_epoch_loss = 0
    for batch_features, batch_labels in train_loader:
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        outputs = model(batch_features)
        loss = criterion(outputs, batch_labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_epoch_loss += loss
    avg_loss = total_epoch_loss / len(train_loader)
    print(f"Epoch: {epoch + 1}, Loss: {avg_loss}")
    
model.eval()

total = 0
correct  = 0
with torch.no_grad():
    for batch_features, batch_labels in test_loader:
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        outputs = model(batch_features)
        _, predicted = torch.max(outputs, 1)
        total += batch_labels.shape[0]
        correct += (predicted == batch_labels).sum().item()
print(f"Accuracy: {correct/total}"

# evaluation code on train data
total = 0
correct  = 0
with torch.no_grad():
    for batch_features, batch_labels in train_loader:
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        outputs = model(batch_features)
        _, predicted = torch.max(outputs, 1)
        total += batch_labels.shape[0]
        correct += (predicted == batch_labels).sum().item()
print(f"Accuracy: {correct/total}"












##################################################################
# DL in PyTorch - CNN Transfer Learning
##################################################################
# 1) import pre trained model. e.g. VGG16
# 2) detach classifier
# 3) attach own classifier (ANN)
# 4) freeze features extraction (CNN) layers 
# 5) train for fine-tuning 

# VGG16 requires image in certain format,
# transformation required on fMNIST dataset:
# 1) reshape 1-d data to 2-d --> (28,28)
# 2) change datatype to np.uint8 --> required for PIL image
# 3) 1-d to 3-d tensor --> from (1,28,28) to (3,28,28)
# 4) convert to PIL Image --> (3,28,28)
# 5) resize to (3,256,256) --> input requirement of VGG16
# 6) centre crop (3,224,224)
# 7) convert to PyTorch.tensor & scale --> (0,1)
# 8) normalize using documentation mean & std for each channel


import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
torch.manual_seed(42)

df = pd.read_csv("fmnist_small.csv")
df.head()

X = df.iloc[:,1:].values()
y = df.iloc[:,0].values()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)
#X_train = X_train/255.0
#X_test = X_test/255.0

#required transformations
from torchvision.transforms import transforms
custom_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    #normalize and scale 0 to 1
    transforms.Normalize(mean=[0.485,0.456,0.406],std=[0.229,0.224,0.225])
])


from PIL import Image
import numpy as np

class CustomDataset(Dataset):
    #def __init__(self, features, labels):
    def __init__(self, features, labels, transform):
        self.features = torch.tensor(features, dtype=torch.float32).reshape(-1,1,28,28)
        self.labels = torch.tensor(labels, dtype=torch.long)
        self.transform = transform
    
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, index):
        #resize to (28,28)
        image = self.features[index].reshape(28,28)
        #change datatype to np.uint8
        image = image.astype(np.uint8)
        #change Black&White to Color, Channel x Height x Width
        #image = np.stack([image]*3)
        #PIL requirement is Height x Width x Channel
        image = np.stack([image]*3, axis=-1)
        #convert array to PIL image
        image = Image.fromarray(image)
        #apply transforms
        image = self.transform(image)
        #return
        return image, torch.tensor(self.labels[index], dtype=torch.long)
        

train_dataset = CustomDataset(X_train,y_train,transform=custom_transform)
test_dataset = CustomDataset(X_test, y_test,transform=custom_transform)

train_loader = Dataloader(train_dataset,batch_size=32,shuffle=True)
test_dataloader=Dataloader(test_dataset,batch_size=32,shuffle=False)

# fetch pretrained model
import torchvision.models as models
vgg16 =  models.vgg16(pretrained=True)
vgg16.features      #CNN part
vgg16.classifier    #ANN part

#freeze CNN weights
for param in vgg16.features.parameters():
    param.requires_grad=False

vgg16.classifier = nn.Sequential(
                            nn.Linear(25088, 1024),
                            nn.ReLU(),
                            nn.Dropout(0.5),
                            nn.Linear(1024, 512),
                            nn.ReLU(),
                            nn.Dropout(0.5),
                            nn.Linear(512, 10)
                        )


epochs = 10
learning_rate = 0.0001
vgg16 = vgg16.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(vgg16.classifier.parameters(), lr=learning_rate)

for epoch in range(epochs):
    total_epoch_loss = 0
    for batch_features, batch_labels in train_loader:
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        outputs = vgg16(batch_features)
        loss = criterion(outputs, batch_labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_epoch_loss += loss
    avg_loss = total_epoch_loss / len(train_loader)
    print(f"Epoch: {epoch + 1}, Loss: {avg_loss}")
    
vgg16.eval()

total = 0
correct  = 0
with torch.no_grad():
    for batch_features, batch_labels in test_loader:
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        outputs = vgg16(batch_features)
        _, predicted = torch.max(outputs, 1)
        total += batch_labels.shape[0]
        correct += (predicted == batch_labels).sum().item()
print(f"Accuracy: {correct/total}"

# evaluation code on train data
total = 0
correct  = 0
with torch.no_grad():
    for batch_features, batch_labels in train_loader:
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)
        outputs = vgg16(batch_features)
        _, predicted = torch.max(outputs, 1)
        total += batch_labels.shape[0]
        correct += (predicted == batch_labels).sum().item()
print(f"Accuracy: {correct/total}"












##################################################################
# DL in PyTorch - RNN [Question Answer System]
##################################################################
import pandas as pd
# a dataset containing 100 Questions and Answers
df = pd.read_csv('/content/100_Unique_QA_Dataset.csv')

# tokenize
def tokenize(text):
    text = text.lower()
    text = text.replace('?','')
    text = text.replace("'","")
    return text.split()

# vocab
vocab = {'<UNK>':0}
def build_vocab(row):
    tokenized_question = tokenize(row['question'])
    tokenized_answer = tokenize(row['answer'])
    merged_tokens = tokenized_question + tokenized_answer
    for token in merged_tokens:
        if token not in vocab:
            vocab[token] = len(vocab)

df.apply(build_vocab, axis=1)
len(vocab)

# convert words to numerical indices
def text_to_indices(text, vocab):
    indexed_text = []
    for token in tokenize(text):
        if token in vocab:
            indexed_text.append(vocab[token])
        else:
            indexed_text.append(vocab['<UNK>'])
    return indexed_text


import torch
from torch.utils.data import Dataset, DataLoader
# Custom Dataset Class
class QADataset(Dataset):
    def __init__(self, df, vocab):
        self.df = df
        self.vocab = vocab

    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, index):
        numerical_question = text_to_indices(self.df.iloc[index]['question'], self.vocab)
        numerical_answer = text_to_indices(self.df.iloc[index]['answer'], self.vocab)
        return torch.tensor(numerical_question), torch.tensor(numerical_answer)

dataset = QADataset(df, vocab)
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)

# architecture of model
import torch.nn as nn
class SimpleRNN(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim=50)
        self.rnn = nn.RNN(50, 64, batch_first=True)
        self.fc = nn.Linear(64, vocab_size)

    def forward(self, question):
        embedded_question = self.embedding(question)
        hidden, final = self.rnn(embedded_question)
        output = self.fc(final.squeeze(0))
        return output

# 
x = nn.Embedding(324, embedding_dim=50)
y = nn.RNN(50, 64, batch_first=True)
z = nn.Linear(64, 324)

a = dataset[0][0].reshape(1,6)
print("shape of a:", a.shape)
b = x(a)
print("shape of b:", b.shape)
c, d = y(b)
print("shape of c:", c.shape)
print("shape of d:", d.shape)

e = z(d.squeeze(0))

print("shape of e:", e.shape)


learning_rate = 0.001
epochs = 20
model = SimpleRNN(len(vocab))
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# training loop
for epoch in range(epochs):
    total_loss = 0
    for question, answer in dataloader:
        optimizer.zero_grad()
        # forward pass
        output = model(question)
        # loss -> output shape (1,324) - (1)
        loss = criterion(output, answer[0])
        # gradients
        loss.backward()
        # update
        optimizer.step()
        total_loss = total_loss + loss.item()
    print(f"Epoch: {epoch+1}, Loss: {total_loss:4f}")

def predict(model, question, threshold=0.5):
    # convert question to numbers
    numerical_question = text_to_indices(question, vocab)
    # tensor
    question_tensor = torch.tensor(numerical_question).unsqueeze(0)
    # send to model
    output = model(question_tensor)
    # convert logits to probs
    probs = torch.nn.functional.softmax(output, dim=1)
    # find index of max prob
    value, index = torch.max(probs, dim=1)
    if value < threshold:
        print("I don't know")
    print(list(vocab.keys())[index])

predict(model, "What is the largest planet in our solar system?")

list(vocab.keys())[7]









##################################################################
# DL in PyTorch - LSTM [Next Word Predictor]
##################################################################
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from collections import Counter
from torch.utils.data import Dataset, DataLoader
from nltk.tokenize import word_tokenize
import nltk


document = """About the Program
What is the course fee for  Data Science Mentorship Program (DSMP 2023)
The course follows a monthly subscription model where you have to make monthly payments of Rs 799/month.
What is the total duration of the course?
The total duration of the course is 7 months. So the total course fee becomes 799*7 = Rs 5600(approx.)
What is the syllabus of the mentorship program?
We will be covering the following modules:
Python Fundamentals
Python libraries for Data Science
Data Analysis
SQL for Data Science
Maths for Machine Learning
ML Algorithms
Practical ML
MLOPs
Case studies
You can check the detailed syllabus here - https://learnwith.campusx.in/courses/CampusX-Data-Science-Mentorship-Program-637339afe4b0615a1bbed390
Will Deep Learning and NLP be a part of this program?
No, NLP and Deep Learning both are not a part of this program’s curriculum.
What if I miss a live session? Will I get a recording of the session?
Yes all our sessions are recorded, so even if you miss a session you can go back and watch the recording.
Where can I find the class schedule?
Checkout this google sheet to see month by month time table of the course - https://docs.google.com/spreadsheets/d/16OoTax_A6ORAeCg4emgexhqqPv3noQPYKU7RJ6ArOzk/edit?usp=sharing.
What is the time duration of all the live sessions?
Roughly, all the sessions last 2 hours.
What is the language spoken by the instructor during the sessions?
Hinglish
How will I be informed about the upcoming class?
You will get a mail from our side before every paid session once you become a paid user.
Can I do this course if I am from a non-tech background?
Yes, absolutely.
I am late, can I join the program in the middle?
Absolutely, you can join the program anytime.
If I join/pay in the middle, will I be able to see all the past lectures?
Yes, once you make the payment you will be able to see all the past content in your dashboard.
Where do I have to submit the task?
You don’t have to submit the task. We will provide you with the solutions, you have to self evaluate the task yourself.
Will we do case studies in the program?
Yes.
Where can we contact you?
You can mail us at nitish.campusx@gmail.com
Payment/Registration related questions
Where do we have to make our payments? Your YouTube channel or website?
You have to make all your monthly payments on our website. Here is the link for our website - https://learnwith.campusx.in/
Can we pay the entire amount of Rs 5600 all at once?
Unfortunately no, the program follows a monthly subscription model.
What is the validity of monthly subscription? Suppose if I pay on 15th Jan, then do I have to pay again on 1st Feb or 15th Feb
15th Feb. The validity period is 30 days from the day you make the payment. So essentially you can join anytime you don’t have to wait for a month to end.
What if I don’t like the course after making the payment. What is the refund policy?
You get a 7 days refund period from the day you have made the payment.
I am living outside India and I am not able to make the payment on the website, what should I do?
You have to contact us by sending a mail at nitish.campusx@gmail.com
Post registration queries
Till when can I view the paid videos on the website?
This one is tricky, so read carefully. You can watch the videos till your subscription is valid. Suppose you have purchased subscription on 21st Jan, you will be able to watch all the past paid sessions in the period of 21st Jan to 20th Feb. But after 21st Feb you will have to purchase the subscription again.
But once the course is over and you have paid us Rs 5600(or 7 installments of Rs 799) you will be able to watch the paid sessions till Aug 2024.
Why lifetime validity is not provided?
Because of the low course fee.
Where can I reach out in case of a doubt after the session?
You will have to fill a google form provided in your dashboard and our team will contact you for a 1 on 1 doubt clearance session
If I join the program late, can I still ask past week doubts?
Yes, just select past week doubt in the doubt clearance google form.
I am living outside India and I am not able to make the payment on the website, what should I do?
You have to contact us by sending a mail at nitish.campusx@gmai.com
Certificate and Placement Assistance related queries
What is the criteria to get the certificate?
There are 2 criterias:
You have to pay the entire fee of Rs 5600
You have to attempt all the course assessments.
I am joining late. How can I pay payment of the earlier months?
You will get a link to pay fee of earlier months in your dashboard once you pay for the current month.
I have read that Placement assistance is a part of this program. What comes under Placement assistance?
This is to clarify that Placement assistance does not mean Placement guarantee. So we dont guarantee you any jobs or for that matter even interview calls. So if you are planning to join this course just for placements, I am afraid you will be disappointed. Here is what comes under placement assistance
Portfolio Building sessions
Soft skill sessions
Sessions with industry mentors
Discussion on Job hunting strategies
"""

# Tokenization
nltk.download('punkt')
nltk.download('punkt_tab')

# tokenize
tokens = word_tokenize(document.lower())
# build vocab
vocab = {'<unk>':0}

for token in Counter(tokens).keys():
  if token not in vocab:
    vocab[token] = len(vocab)
vocab
len(vocab)

# extract sentences from data
input_sentences = document.split('\n')

def text_to_indices(sentence, vocab):
    numerical_sentence = []
    for token in sentence:
    if token in vocab:
        numerical_sentence.append(vocab[token])
    else:
        numerical_sentence.append(vocab['<unk>'])
    return numerical_sentence

input_numerical_sentences = []
for sentence in input_sentences:
    input_numerical_sentences.append(text_to_indices(word_tokenize(sentence.lower()), vocab))

len(input_numerical_sentences)

training_sequence = []
for sentence in input_numerical_sentences:
    for i in range(1, len(sentence)):
        training_sequence.append(sentence[:i+1])

len(training_sequence)
training_sequence[:5]

len_list = []
for sequence in training_sequence:
    len_list.append(len(sequence))

max(len_list)

training_sequence[0]

padded_training_sequence = []
for sequence in training_sequence:
    padded_training_sequence.append([0]*(max(len_list) - len(sequence)) + sequence)

len(padded_training_sequence[10])
padded_training_sequence = torch.tensor(padded_training_sequence, dtype=torch.long)

X = padded_training_sequence[:, :-1]
y = padded_training_sequence[:,-1]


class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

dataset = CustomDataset(X,y)
len(dataset)

dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

#### LSTMModel input/intemediate/output states
# x = nn.Embedding(289, 100)
# y = nn.LSTM(100, 150, batch_first=True)
# z = nn.Linear(150, 289)
# row_input = dataset[0][0].unsqueeze(0)
# embedded_data = x(row_input)
# output = y(embedded_data)
## tuple unpacking
# intermediate_hidden_states, final_states = output
# final_hidden_state, final_cell_state = final_states
## LOGIT values at the end
# z(final_hidden_state.squeeze(0))

class LSTMModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, 100)
        self.lstm = nn.LSTM(100, 150, batch_first=True)
        self.fc = nn.Linear(150, vocab_size)

    def forward(self, x):
        embedded = self.embedding(x)
        intermediate_hidden_states, (final_hidden_state, final_cell_state) = self.lstm(embedded)
        output = self.fc(final_hidden_state.squeeze(0))
        return output



model = LSTMModel(len(vocab))
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

epochs = 50
learning_rate = 0.001
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# training loop
for epoch in range(epochs):
    total_loss = 0
    for batch_x, batch_y in dataloader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        optimizer.zero_grad()
        output = model(batch_x)
        loss = criterion(output, batch_y)
        loss.backward()
        optimizer.step()
        total_loss = total_loss + loss.item()
    print(f"Epoch: {epoch + 1}, Loss: {total_loss:.4f}")

# prediction
def prediction(model, vocab, text):
  # tokenize
  tokenized_text = word_tokenize(text.lower())
  # text -> numerical indices
  numerical_text = text_to_indices(tokenized_text, vocab)
  # padding
  padded_text = torch.tensor([0] * (61 - len(numerical_text)) + numerical_text, dtype=torch.long).unsqueeze(0)
  # send to model
  output = model(padded_text)
  # predicted index
  value, index = torch.max(output, dim=1)
  # merge with text
  return text + " " + list(vocab.keys())[index]

prediction(model, vocab, "The course follows a monthly")

import time
num_tokens = 10
input_text = "hi how are"

for i in range(num_tokens):
    output_text = prediction(model, vocab, input_text)
    print(output_text)
    input_text = output_text
    time.sleep(0.5)

dataloader1 = DataLoader(dataset, batch_size=32, shuffle=False)

# Function to calculate accuracy
def calculate_accuracy(model, dataloader, device):
    model.eval()  # Set the model to evaluation mode
    correct = 0
    total = 0
    with torch.no_grad():  # No need to compute gradients
        for batch_x, batch_y in dataloader1:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            # Get model predictions
            outputs = model(batch_x)
            # Get the predicted word indices
            _, predicted = torch.max(outputs, dim=1)
            # Compare with actual labels
            correct += (predicted == batch_y).sum().item()
            total += batch_y.size(0)
    accuracy = correct / total * 100
    return accuracy

# Compute accuracy
accuracy = calculate_accuracy(model, dataloader, device)
print(f"Model Accuracy: {accuracy:.2f}%")









##################################################################
# DL in PyTorch - GRU (Gated Recurrent Unit)
##################################################################

#### Example 1
import torch
import torch.nn as nn

# Define dimensions
batch_size = 4
seq_len = 10      # Number of steps in the sequence
input_size = 8    # Number of features per step
hidden_size = 16  # Size of the hidden state
num_layers = 1    # Number of stacked GRU layers

# Instantiate the GRU layer
# batch_first=True makes expected tensor format: (batch, seq, feature)
gru = nn.GRU(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)

# Create dummy input data
input_tensor = torch.randn(batch_size, seq_len, input_size)

# Optional: Initialize the initial hidden state (defaults to zeros if omitted)
h0 = torch.zeros(num_layers, batch_size, hidden_size)

# Forward pass through the GRU
output, hn = gru(input_tensor, h0)

# Check the shapes
print("Output shape (batch, seq, hidden):", output.shape)  # torch.Size([4, 10, 16])
print("Final hidden state shape (layers, batch, hidden):", hn.shape)  # torch.Size([1, 4, 16])





#### Example 2
class GRUClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(GRUClassifier, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # GRU layer
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        
        # Fully connected output layer
        self.fc = nn.Linear(hidden_size, num_classes)
        
    def forward(self, x):
        # Initialize hidden state with zeros
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # Forward propagate through GRU
        # output shape: (batch_size, seq_len, hidden_size)
        # hn shape: (num_layers, batch_size, hidden_size)
        out, hn = self.gru(x, h0)
        
        # Decode the hidden state of the last time step only
        # out[:, -1, :] slices out the last sequence step
        out = self.fc(out[:, -1, :])
        return out

# Instantiate model
model = GRUClassifier(input_size=5, hidden_size=32, num_layers=2, num_classes=3)

# Test with a mock batch of data
mock_data = torch.randn(8, 15, 5) # (batch_size=8, seq_len=15, features=5)
predictions = model(mock_data)

print("Predictions shape (batch_size, num_classes):", predictions.shape) # torch.Size([8, 3])






#### Example 3 - Quora Duplicate Questions Pair
import torch
import torch.nn as nn
import torch.nn.functional as F

class SiameseGRU(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super(SiameseGRU, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.gru = nn.GRU(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        # Combined features: [u, v, |u - v|, u * v] -> hidden_dim * 4 * 2 (due to bidirectional)
        self.fc = nn.Linear(hidden_dim * 8, 1)

    def forward_once(self, x):
        embedded = self.embedding(x)
        _, h_n = self.gru(embedded)
        # h_n shape: (num_layers * num_directions, batch, hidden_dim)
        # Concatenate forward and backward final hidden states
        h_cat = torch.cat((h_n[-2], h_n[-1]), dim=1)
        return h_cat

    def forward(self, q1, q2):
        u = self.forward_once(q1)
        v = self.forward_once(q2)
        # Compute absolute difference and element-wise product for similarity cues
        diff = torch.abs(u - v)
        prod = u * v
        combined = torch.cat((u, v, diff, prod), dim=1)
        out = torch.sigmoid(self.fc(combined))
        return out

# Example usage
vocab_size, embed_dim, hidden_dim = 10000, 300, 128
model = SiameseGRU(vocab_size, embed_dim, hidden_dim)

# Dummy batch of tokenized question pairs (Batch Size: 2, Seq Length: 5)
q1_tensor = torch.randint(0, vocab_size, (2, 5))
q2_tensor = torch.randint(0, vocab_size, (2, 5))

preds = model(q1_tensor, q2_tensor)
print("Duplicate probabilities:", preds)














###############################################################################################################
#### Deep Learning DL in Tensorflow Keras - Everything
###############################################################################################################

##################################################################
# DL in Keras - Single Perceptron architecture code from scratch
##################################################################

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def sigmoid(z):
    return 1/(1 + math.exp(-z))
    
def tanh(z):
    return ((math.exp(z) - math.exp(-z))/(math.exp(z) + math.exp(-z)))

def relu(z):
    return max(0,z)

#Sample Data
x1 = 3
x2 = 2
y_actual = 17
print(f"x1 = {x1}\nx2 = {x2}\ny_actual = {y_actual}")

#Feed Forward
w1 = np.random.randint(1,10,1)[0]
w2 = np.random.randint(1,10,1)[0]
print(f"w1 = {w1}\nw2 = {w2}")

#Prediction
y_pred = x1*w1 + x2*w2
print(y_pred)

#Loss (error) calculation
error = (y_actual - y_pred)**2
print(f"error = {error}")

#Back Propagation
grad_w1 = 2*(y_actual - y_pred)*(-x1)
grad_w2 = 2*(y_actual - y_pred)*(-x2)
print(f"grad_w1 = {grad_w1}\ngrad_w2 = {grad_w2}")

#update weights
learning_rate = 0.01
w1 -= learning_rate*grad_w1
w2 -= learning_rate*grad_w2
print(f"Updated weights: \nw1 = {w1}\nw2 = {w2}")

#train for 20 more epochs
y_pred_history = [y_pred]
error_history = [error]
for epoch in range(20):
    print(f"\nepoch {epoch+1}")
    y_pred = x1*w1 + x2*w2
    y_pred_history.append(y_pred)
    print(f"y_pred = {y_pred}")
    error = (y_actual - y_pred)**2
    error_history.append(error)
    print(f"error = {error}")
    grad_w1 = 2*(y_actual - y_pred)*(-x1)
    grad_w2 = 2*(y_actual - y_pred)*(-x2)
    print(f"grad_w1 = {grad_w1}\ngrad_w2 = {grad_w2}")
    w1 -= learning_rate*grad_w1
    w2 -= learning_rate*grad_w2
    print(f"Updated weights: \nw1 = {w1}\nw2 = {w2}")

#Loss vs. Epoch visulazation 
fig,ax = plt.subplots(figsize=(12,4))
ax.plot(np.arange(21),error_history,marker=".",markersize=10, label="Sum Squared Error", color='red')
plt.xlabel("Epoch Number")
plt.ylabel("Error")
plt.title("Cost vs. Epoch")
plt.legend()
plt.tight_layout()
plt.show()






##################################################################
# DL in Keras - Artificial Neural Network (ANN / MLP) Architecture
##################################################################
import warnings as wr
wr.filterwarnings('ignore')
print(f"TensorFlow Version: {tf.__version__}")
print(f"GPU Available: {tf.config.list_physical_devices('GPU')}")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist,fashion_mnist
from keras.utils import to_categorical
from keras.callbacks import TensorBoard, EarlyStopping, ReduceLROnPlateau
from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, Activation

from keras.optimizers import Adam
from keras.regularizers import l2

os.getcwd() #get the current working directory
os.listdir() #list the items in cwd


#load MNIST digits dataset
(X_train,y_train),(X_test,y_test) = mnist.load_data()
#load Fashion MNIST dataset
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

#visualize random images
n = 10
fig,ax=plt.subplots(1,n,figsize=(5,2))
for i in range(n):
    ax[i].imshow(X_train[i], cmap='gray')
    ax[i].set_title(y_train[i])
    ax[i].axis('off')
fig.tight_layout()
fig.show()

#bar chart of target class distribution in train & test
data = pd.DataFrame({
    'Class': np.concatenate([y_train, y_test]),
    'Data': ['Train Data']*len(y_train) + ['Test Data']*len(y_test)
})
plt.figure(figsize=(6,3))
sns.countplot(data=data, x='Class', hue='Data')
plt.title("Count Plot of Class Distribution")
plt.legend(loc=10)
plt.show()

#find minimum and maximum value of pixels
mx = []
mn = []
for i in range(X_train.shape[0]):
    mx.append(X_train[i].max())
    mn.append(X_train[i].min())
print(f"max = {max(mx)}")
print(f"min = {min(mn)}")

#Scale pixel data
X_train_scaled = X_train/255
X_test_scaled = X_test/255

#check class balance
np.unique(y_train,return_counts=True)
np.unique(y_test,return_counts=True)

#apply one hot encoding (OHE)
num_classes = 10
y_train_ohe = to_categorical(y_train, num_classes)
y_test_ohe = to_categorical(y_test, num_classes)

#build model: method_1
model = Sequential()
model.add(Flatten(input_shape = X_train_scaled.shape[1:]))

model.add(Dense(128), kernel_regularizer='l2'))         #kernel_regularizer optional
model.add(BatchNormalization())                         #optional: used to reduce overfitting
model.add(Activation('relu'))
model.add(Dropout(0.2))                                 #optional: used to reduce overfitting

model.add(Dense(128), kernel_regularizer='l2'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10, 'softmax'))

#build model: method_2
model = Sequential()
model.add(Flatten(input_shape = X_train_scaled.shape[1:]))
model.add(Dense(128, 'relu', kernel_regularizer='l2'))
model.add(Dropout(0.2))
model.add(Dense(128, 'relu', kernel_regularizer='l2'))
model.add(Dropout(0.2))
model.add(Dense(10, 'softmax'))

#build model: method_3
model = Sequential()
model.add(Flatten(input_shape = X_train_scaled.shape[1:]))
model.add(Dense(
            128, 
            activation = keras.activations.relu, 
            kernel_regularizer = keras.regularizers.l2(0.001)
            )
        )
model.add(Dropout(0.2))
model.add(Dense(
            128, 
            activation = keras.activations.relu, 
            kernel_regularizer = keras.regularizers.l2(0.001)
            )
        )
model.add(Dropout(0.2))
model.add(Dense(10, activation = keras.activations.softmax))

#build model: method_4
model = Sequential([
    Flatten(input_shape = X_train_scaled.shape[1:]),
    Dense(128, 'relu', kernel_regularizer='l2'),
    Dropout(0.2),
    Dense(128, 'relu', kernel_regularizer='l2'),
    Dropout(0.2),
    Dense(10, 'softmax')
])

#compile model: method_1
model.summary()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])          #for OHE target
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])   #for normal target

#compile model: method_2
model.compile(optimizer = keras.optimizers.Adam(learning_rate = 0.01),
    loss = keras.losses.categorical_crossentropy,
    metrics = ['accuracy']
)

#train model with OHE target using categorical_crossentropy
history = model.fit(X_train_scaled, y_train_ohe, batch_size=32, epochs=20)
#train model with normal target usig spart_categorical_crossentropy
history = model.fit(X_train_scaled, y_train, batch_size=32, epochs=20)

#Save the trained model, learned weights & model's architecture
model.save("my_model.keras")
model.save_weights("my_model.weights.h5")
with open("my_model_architecture.json", 'w') as f:
    f.write(model.to_json())

#visualize loss & accuracy Vs. Epoch
epoch = np.arange(len(history.history['accuracy']))
training_acc, training_loss = history.history['accuracy'], history.history['loss']
val_acc, val_loss = history.history['val_accuracy'], history.history['val_loss']

fig,ax = plt.subplots(1,2,figsize=(9,3))
ax[0].plot(epoch,training_acc,color='b', label='Training')
ax[0].plot(epoch,val_acc,color='g', label='Test')
ax[0].set_xlabel("Epochs")
ax[0].set_ylabel("Accuracy")
ax[0].legend(loc=5)

ax[1].plot(epoch,training_loss,color='r', label='Training')
ax[1].plot(epoch,val_loss,color='orange', label='Test')
ax[1].set_xlabel("Epochs")
ax[1].set_ylabel("Loss")
ax[1].legend(loc=5)

plt.tight_layout()
plt.show()

#Evaluate model
model.evaluate(x=X_test, y=y_test_ohe)          #for OHE targets
model.evaluate(x=X_test, y=y_test)              #for normal targets

#make prediction on a single image
random_ix = np.random.randint(0,X_test.shape[0],1)[0]
y_pred = model.predict(x=X_test[random_ix,:,:].reshape(1,28,28))
print(f"Prediction : {np.argmax(y_pred)}")
print(f"Actual     : {y_test[random_ix]}")

#make prediction on a batch of n images
n = 30
random_ix = np.random.randint(0,X_test.shape[0],n)
y_pred = model.predict(x=X_test[random_ix,:,:])
y_pred_int = np.array([np.argmax(yy) for yy in y_pred])
print(f"Prediction : {y_pred_int}")
print(f"Actual     : {y_test[random_ix]}")

#overfitting is reduced by using
# 1) BatchNormalization
# 2) Dropout
# 3) Regularization






##################################################################
# DL in Keras - CNN Architecture with tensorboard
##################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from keras.datasets import fashion_mnist
from keras.utils import to_categorical
from keras.callbacks import TensorBoard, EarlyStopping, ReduceLROnPlateau
from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, Activation

import warnings as wr
wr.filterwarnings('ignore')

print(f"TensorFlow Version: {tf.__version__}")
print(f"GPU Available: {tf.config.list_physical_devices('GPU')}")

#load data
(X_train, y_train),(X_test, y_test) = fashion_mnist.load_data()

#scale data
X_train_norm = X_train/255
X_test_norm = X_test/255

#one hot encode (OHE) target column
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

#build model
model = Sequential()

model.add(Conv2D(filters=64, kernel_size=(3,3), padding='valid', input_shape=(28, 28, 1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2))

model.add(Conv2D(filters=64, kernel_size=(3,3), padding='valid'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2))

model.add(Conv2D(filters=64, kernel_size=(3,3), padding='valid'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2))

model.add(Flatten())

model.add(Dense(512))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(256))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#callbacks
tensorboard_callback = TensorBoard(
    log_dir="logs/",
    histogram_freq = 1, #one histogram every epoch
    write_graph = True,
    update_freq = 'epoch'
)
early_stopping_callback = EarlyStopping(
    monitor = 'val_loss',
    patience = 10,
    restore_best_weights = True,
    verbose = 1
)
lr_reduce_callback = ReduceLROnPlateau(
    monitor = 'val_loss',
    factor = 0.5,
    patience = 10,
    min_lr = 1e-5,
    verbose = 1,
)
callbacks = [tensorboard_callback, early_stopping_callback, lr_reduce_callback]

#train model
history = model.fit(
    x = X_train_norm,
    y = y_train_cat,
    epochs = 100,
    validation_data = (X_test_norm, y_test_cat),
    callbacks = callbacks
)

#evaluate
train_loss = history.history['loss']
val_loss = history.history['val_loss']
train_accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

fig,ax = plt.subplots(1,2,figsize=(12,3))
ax[0].plot(train_loss, label='Training Loss')
ax[0].plot(val_loss, label='Test Loss')
ax[0].set_xlabel("Epoch")
ax[0].set_ylabel("Loss")
ax[0].legend()
ax[0].grid(True)

ax[1].plot(train_accuracy, label='Training Accuracy')
ax[1].plot(val_accuracy, label='Test Accuracy')
ax[1].set_xlabel("Epoch")
ax[1].set_ylabel("Accuracy")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()

#tensorboard analysis
%load_ext tensorboard
#%reload_ext tensorboard
%tensorboard --logdir logs/






##################################################################
# DL in Keras - Cat vs. Dog classifier on Image Data (kaggle/api)
##################################################################
import numpy as np
import pandas as pd

import json
import os
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Flatten, Dense, Dropout

import cv2

import warnings
warnings.filterwarnings('ignore')


#kaggle api
#load kaggle credentials from json file api
kaggle_json_path = Path.home() / ".kaggle" / "kaggle.json"
with open(kaggle_json_path, "r") as f:
    creds = json.load(f)
#set kaggle credentials in environment
os.environ["KAGGLE_USERNAME"] = creds["username"]
os.environ["KAGGLE_KEY"] = creds["key"]
#authenticate kaggle api with credentials
api = KaggleApi()
api.authenticate()
#download data from kaggle
dataset_slug = 'salader/dogsvscats'           #kaggle dataset online path
download_path = 'D:/Downloads/data'           #local machine download path
api.dataset_download_files(dataset=dataset_slug, path=download_path, unzip=True)

#without Data Augmentation
#load downloaded data into keras
train_ds = keras.utils.image_dataset_from_directory(
    directory = 'D:/Downloads/data/train',
    labels = 'inferred',
    label_mode = 'int',
    batch_size = 32,
    image_size = (256,256)
)
test_ds = keras.utils.image_dataset_from_directory(
    directory = 'D:/Downloads/data/test',
    labels = 'inferred',
    label_mode = 'int',
    batch_size = 32,
    image_size = (256,256)
)

def process(image, label):
    imgage = tf.cast(image/255. , tf.float32)
    return image, label
train_ds = train_ds.map(process)
validation_ds = validation_ds.map(process)

#with Data Augmentation [optional]


#Data Augmentation process (create new images from existing ones)
#training on all data - No validation split
train_datagen = ImageDataGenerator(
    rotation_range = 30,
    rescale = 1/255,
    shear_range = 0.2,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
)
test_datagen = ImageDataGenerator(rescale = 1/255)
#generate data for generalization of model
train_generator = train_datagen.flow_from_directory(
    directory = 'D:/Downloads/data/train',
    target_size = (256,256),
    batch_size = 32,
    class_mode = 'binary'
)

test_generator = test_datagen.flow_from_directory(
    directory = 'D:/Downloads/data/test',
    target_size = (256,256),
    batch_size = 32,
    class_mode = 'binary'
)

#Data Augmentation process - with validation split
datagenerator = ImageDataGenerator(
    rotation_range = 40,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode = 'nearest',
    rescale = 1./255,
    validation_split = 0.2
)

dataflow_kwargs = dict(
    directory=train_dir,
    target_size = image_size[:-1],
    batch_size = batch_size,
    class_mode="categorical",
    interpolation = "bilinear"
)

train_generator = datagenerator.flow_from_directory(
    subset="training",
    shuffle=True,
    **dataflow_kwargs
)

valid_generator = datagenerator.flow_from_directory(
    subset="validation",
    shuffle=False,
    **dataflow_kwargs
)

steps_per_epoch = train_generator.samples // train_generator.batch_size
validation_steps = valid_generator.samples // valid_generator.batch_size

model.fit(
    train_generator,
    epochs=50,
    steps_per_epoch=steps_per_epoch,
    validation_data=valid_generator,
    validation_steps=validation_steps
)

#build model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), padding='valid', activation='relu', input_shape=(256,256,3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

model.add(Conv2D(32, kernel_size=(3,3), padding='valid', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

model.add(Conv2D(32, kernel_size=(3,3), padding='valid', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

model.summary()

#compile model
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

#train model
history = model.fit(
    #x = train_ds,                               #without data augmentation
    x = train_generator,                        #with data augmentation
    steps_per_epoch = len(train_generator),
    validation_data = test_generator,
    validation_steps=len(test_generator),
    epochs = 100
)

#predict on new data
paths = [
    "D:/Downloads/data/new_images/cat_1.jpg"
    ,"D:/Downloads/data/new_images/cat_2.jpg"
    ,"D:/Downloads/data/new_images/cat_3.jpg"
    ,"D:/Downloads/data/new_images/cat_4.jpg"
    ,"D:/Downloads/data/new_images/cat_5.jpg"
    ,"D:/Downloads/data/new_images/dog_1.jpg"
    ,"D:/Downloads/data/new_images/dog_2.jpg"
    ,"D:/Downloads/data/new_images/dog_3.jpg"
    ,"D:/Downloads/data/new_images/dog_4.jpg"
    ,"D:/Downloads/data/new_images/dog_5.jpg"
]
for image_path in paths:
    img = image.load_img(image_path, target_size=(256,256))
    plt.figure(figsize=(1,1))
    plt.imshow(img)
    plt.show()
    
    img_arr = image.img_to_array(img)
    img_arr = np.expand_dims(img_arr, axis=0)
    img_arr_scaled = img_arr/255.
    
    prediction = model.predict(img_arr_scaled)
    confidence = prediction[0][0]
    
    if confidence > 0.5:
        class_name = 'Dog'
        confidence = confidence
    else:
        class_name = 'Cat'
        confidence = 1 - confidence
    
    print(f"Predicted Class: {class_name} with Confidence Level: {confidence:.2%}")






##################################################################
# DL in Keras - Transfer Learning CNN (VGG16)
##################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

import tensorflow as tf
from tensorflow import keras
from keras import Sequential

from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.layers import Flatten, Dense, Dropout, BatchNormalization, Activation
from keras.applications.vgg16 import VGG16


import warnings as wr
wr.filterwarnings('ignore')

#downloading data from kaggle.
kaggle_json_path = Path.home() / ".kaggle" / "kaggle.json"
with open(kaggle_json_path, "r") as f:
    creds = json.load(f)

os.environ["KAGGLE_USERNAME"] = creds["username"]
os.environ["KAGGLE_KEY"] = creds["key"]

api = KaggleApi()
api.authenticate()

dataset_slug = 'salader/dogsvscats'           #kaggle dataset online path
download_path = 'D:/Downloads/data'           #local machine download path
api.dataset_download_files(dataset=dataset_slug, path=download_path, unzip=True)

#Utilizing VGG16 convolution base
conv_base = VGG16(
    weights = 'imagenet',
    include_top = False,
    input_shape = (150,150,3)
)

conv_base.summary()

#loading data
train_ds = keras.utils.image_dataset_from_directory(
    directory = 'D:/Downloads/data/train',
    labels = 'inferred',
    label_mode = 'int',
    batch_size = 32,
    image_size = (150,150)
)

test_ds = keras.utils.image_dataset_from_directory(
    directory = 'D:/Downloads/data/test',
    labels = 'inferred',
    label_mode = 'int',
    batch_size = 32,
    image_size = (150,150)
)

#Data Augmentation
train_datagen = ImageDataGenerator(
    rotation_range = 40,
    rescale = 1/255,
    shear_range = 0.2,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
)
test_datagen = ImageDataGenerator(rescale = 1/255)

train_generator = train_datagen.flow_from_directory(
    directory = 'D:/Downloads/data/train',
    target_size = (150,150),
    batch_size = 32,
    class_mode = 'binary'
)
test_generator = test_datagen.flow_from_directory(
    directory = 'D:/Downloads/data/test',
    target_size = (150,150),
    batch_size = 32,
    class_mode = 'binary'
)

#build model
model = Sequential()

model.add(conv_base)
model.add(Flatten())

model.add(Dense(256))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(128))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(1, activation='sigmoid'))

model.summary()

#freeze convolution base weights/biases
conv_base.trainable = False
model.summary()

#compile
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

#Train
history = model.fit(
    train_generator,
    epochs = 20,
    validation_data = test_generator
)

#Evaluate Accuracy
train_acc = history.history['accuracy']
test_acc = history.history['val_accuracy']

plt.figure(figsize=(15,3))
plt.plot(train_acc, label="Training Accuracy")
plt.plot(test_acc, label="Test Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

#make a system to predict single image/batch of images
paths = [
    "D:/Downloads/data/new_images/cat_1.jpg"
    ,"D:/Downloads/data/new_images/cat_2.jpg"
    ,"D:/Downloads/data/new_images/cat_3.jpg"
    ,"D:/Downloads/data/new_images/cat_4.jpg"
    ,"D:/Downloads/data/new_images/cat_5.jpg"
    ,"D:/Downloads/data/new_images/dog_1.jpg"
    ,"D:/Downloads/data/new_images/dog_2.jpg"
    ,"D:/Downloads/data/new_images/dog_3.jpg"
    ,"D:/Downloads/data/new_images/dog_4.jpg"
    ,"D:/Downloads/data/new_images/dog_5.jpg"
]

for image_path in paths:
    img = image.load_img(image_path, target_size=(150,150))
    plt.figure(figsize=(1,1))
    plt.imshow(img)
    plt.show()

    img_arr = image.img_to_array(img)
    img_arr = np.expand_dims(img_arr, axis=0)
    img_arr_scaled = img_arr/255

    prediction = model.predict(img_arr_scaled)
    confidence = prediction[0][0]

    if confidence > 0.5:
        class_name = 'Dog'
    else:
        class_name = 'Cat'
        confidence = 1 - confidence

    print(f"{class_name} | Confidence = {confidence}")









##################################################################
# DL in Keras - create and save images with data augmentation
##################################################################
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

img = image.load_img("D:\Downloads\data\train\dogs\dog.99.jpg", target_size=(200,200))
datagen = ImageDataGenerator(
    rotation_range = 30,
    rescale = 1/255,
    shear_range = 0.2,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
)
img_arr = image.img_to_array(img)
img_arr.shape                       #output = (200,200,3)

input_batch = img_arr.reshape(1,200,200,3)

i=0
for output in datagen.flow(input_batch, batch_size=1, save_to_dir='D:/Downloads/data/aug'):
    i += 1
    if i == 10:                     #create only 10 images
        break









##################################################################
# DL in Keras - RNN : Sentiment Analysis (imdb)
##################################################################
import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from keras.datasets import imdb
#from keras.utils import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.layers import TextVectorization
from keras.preprocessing.sequence import pad_sequences
from keras import Sequential
from keras.layers import Dense, SimpleRNN, Embedding

import warnings as wr
wr.filterwarnings('ignore')

#loading data that is not Integer Encoded: list of sentences
reviews = ['go india',
		'india india',
		'hip hip hurray',
		'jeetega bhai jeetega india jeetega',
		'bharat mata ki jai',
		'kohli kohli',
		'sachin sachin',
		'dhoni dhoni',
		'modi ji ki jai',
		'inquilab zindabad']
#so, there is need of Tokenization & Integer Encoding
#Tokenization
tokenizer = Tokenizer(oov_token='abcd')             #oov_token: out of vocab token, words not found in vocab will be replaced with 'abcd'
tokenizer.fit_on_texts(reviews)
tokenizer.word_index                                #dict of all unique words along index assigned to them
vocab_size = len(tokenizer.word_index)
tokenizer.word_counts                               #all unique words along with their count in reviews vocabulary
tokenizer.document_count                            #count of sentences in reviews
#Integer Encoding
X_train = tokenizer.texts_to_sequences(reviews)     #converts all the words to their integer index

X_train_pad = pad_sequences(X_train, padding='post')#pad zeros at the end, making length of every sentence same as the maximum length sentence


#loading data that is Integer Encoded: i.e. imdb data
#this imdb data is already tokenized & Integer Encoded
#so, there is no need to do Tokenization + text_to_sequence()
#loading data, with 10k most used vocabulary(words)

(X_train, y_train),(X_test, y_test) = imdb.load_data(num_words=vocab_cap)

#keeping only first 500 words from each review
max_len = 500
X_train_pad = pad_sequences(X_train, maxlen=max_len)
X_test_pad = pad_sequences(X_test, maxlen=max_len)

#build model
#input_dim: Size of the vocabulary
#output_dim: Size of the output of embedding layer
#input_length: Size of each review (number of words in each review.)
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=32, input_length=max_len))
model.add(SimpleRNN(64, return_sequences=False, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

#compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#train model
history = model.fit(
    X_train_pad,
    y_train,
    batch_size=128,
    epochs=10,
    validation_split=0.2
)

#evaluate model
test_loss, test_accuracy = model.evaluate(x=X_test_pad, y=y_test, batch_size=128)
print(f"Test Accuracy: {test_accuracy}")

#predict sentiment: predicting first n reviews from test dataset
n = 100
pred = model.predict(X_test_pad[:n])
for i in range(n):
    if i%5 == 0:
        print()
    if pred[i][0] > 0.5:
        confidence = pred[i][0]
        pred_sentiment = 'Positive'
    else:
        confidence = 1 - pred[i][0]
        pred_sentiment = 'Negative'
    actual = 'Positive' if y_test[i] == 1 else 'Negative'
    print(f"Confidence Level : {100*confidence:.0f}% | Predicted Sentiment : {pred_sentiment} | Actual Sentiment : {actual}")










##################################################################
# DL in Keras - LSTM (Long Short-Term Memory) - Predict next word
##################################################################
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.utils import to_categorical

with open("2024_state_of_the_union.txt", mode='r', encoding='utf-8') as my_file:
    my_text = my_file.read()

#making tokens
my_tokenizer = Tokenizer()
my_tokenizer.fit_on_texts([my_text])
total_words = len(my_tokenizer.word_index)+1

#create n-gram sequence
my_input_sequences = []
for line in my_text.split('\n'):
    token_list = my_tokenizer.texts_to_sequences([line])[0]
    for i in range(1,len(token_list)):
        my_ngram_seq = token_list[:i+1]
        my_input_sequences.append(my_ngram_seq)

#padding sequences with zeros
max_len = max([len(seq) for seq in my_input_sequences])
input_seq=np.array(pad_sequences(my_input_sequences,maxlen=max_len,padding='pre'))

X = input_seq[:,:-1]
y = input_seq[:,-1]

#OHE of target column
y = np.array(to_categorical(y, num_classes=total_words))

#build model
model = Sequential()
model.add(Embedding(total_words, 100))
model.add(LSTM(150))
model.add(Dense(total_words, activation='softmax'))
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X,y, epochs=100, verbose=1)


#prediction
input_text = 'Many years ago, there was a king'
predict_next_words = 20
for n in range(predict_next_words):
    token_list = my_tokenizer.texts_to_sequences([input_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_len-1, padding='pre')
    prediction = np.argmax(model.predict(token_list), axis=-1)
    for word, index in my_tokenizer.word_index.items():
        if index==prediction:
            predicted_word = word
            break
    input_text += ' ' + predicted_word

print(input_text)
	
	
	
	
	
	











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
        df[col] = le.fit_transform(df[col])

# 3.1.2 Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=[['low','medium','high']])
df['col1'] = pd.DataFrame(oe.fit_transform(df[['col1']]))

# 3.1.3 One Hot Encoding
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(drop='First', sparse_output=False, handle_unknown='ignore')
df['col1'] = pd.DataFrame(ohe.fit_transform(df[['col1']]))
## One Hot Encoding - using Pandas [column names retained]
pd.get_dummies(df,columns=['col1','col2'],drop_first=True)          #OHE for col1 and col2

# 3.1.4 Simple Imputer [replace missing values with col mean]
from sklearn.impute import SimpleImputer
si = SimpleImputer()                                                #mean by default
si = SimpleImputer(strategy = 'median')                             #median
si = SimpleImputer(strategy = 'most_frequent')                      #mode
df['col1'] = pd.DataFrame(si.fit_transform(df[['col1']]))

# 3.1.5 Encoding - Using Column Transformer [task of above steps becomes easier]
from sklearn.compose import ColumnTransformer

num_features = df.select_dtypes(exclude='object').columns           #numerical features
cat_features = df.select_dtypes(include='object').columns           #categorical features

ssc_tnf = StandardScaler()
ohe_tnf = OneHotEncoder(drop='First', sparse=False)
ord_tnf = OrdinalEncoder(categories=[['low','medium','high']])

ct = ColumnTransformer(
        transformers=[
            ('tnf1', ssc_tnf, num_features),
            ('tnf2', ohe_tnf, cat_features),
            ('tnf3', ord_tnf, ['col1']),
            ('tnf4', SimpleImputer(), ['col4'])
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

#PCA with sklearn implementation
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
## Regressors
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
                                    max_depth=4, loss='squared_error', random_state=42)

## 7.11 XGBoost Regressor
from xgboost import XGBRegressor
xgb_r = XGBRegressor(objective='reg:squarederror',n_estimators=100, 
                         learning_rate=0.1,max_depth=5,random_state=42)

## 7.12 Logistic Regressor - Binary Classifier
from sklearn.linear_model import LogisticRegression
LoR = LogisticRegression()



## Classifiers
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
## 8.2.1 manual calculation
from sklearn.metrics import confusion_matrix
[tn, fp], [fn, tp] = confusion_matrix(y_test, y_pred).ravel()
PPV_or_precision = tp / (tp + fp)                                       #PPV=Positive Predictive Value
TPR_or_recall_or_sensitivity = tp / (tp + fn)                           #TPR=True Positive Rate #Probability of Detection
f1_score = 2 * precision * recall / (precision + recall)

NPV_or_negativePrecision = tn / (tn + fn)                               #NPV=Negative Predictive Value #Negative Precision
TNR_or_specificity_or_selectivityOfModel = tn / (tn + fp)               #TNR=True Negative Rate #Specificity #Selectivity of Model

total_support_value = tp + tn + fp + fn

## 8.2.2 automatic calculation
from sklearn.metrics import confusion_matrix,accuracy_score,roc_auc_score,precision_score,recall_score,f1_score,classification_report
confusion_matrix(y_test, y_pred)

accuracy_score(y_test, y_pred)
precision_score(y_test, y_pred)
recall_score(y_test, y_pred)
f1_score(y_test, y_pred)

diff_thresholds = [0.01,0.02,0.03,0.04,0.05,0.1,0.2,0.3,0.5,0.7,0.8,0.9,0.95,0.96,0.97,0.98,0.99]
FPR, TPR, diff_thresholds = roc_curve(y_test, y_pred)
roc_auc_score(y_test, y_pred)   #better measure of accuracy in unbalanced dataset

classification_report(y_test, y_pred)




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
#### EDA :: Exploratory Data Analysis
###############################################################################################################

# 1 Cleaning
df.shape
df.info()
df.columns.tolist()
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

#bar chart with count of values in a col
px.histogram(df,
            x='cat_col',
            title='chart_title',
            text_auto=True)

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
plt.axis(True)
plt.show()

#Scatter Plot with Object Oriented Programming (OOP) - as compared with non-OOP above
fig,ax=plt.subplots(figsize=(15,7))
ax.scatter(x,y,color='red',marker='+')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title_1')
ax.axis(True)
fig.show()

#Multiple (2) subplots with Object Oriented Programming OOP
fig,ax = plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(15,6))   #sharex is to use single x-axis in 2 charts up & down
ax[0].scatter(x,y,color='red')
ax[0].set_title('x vs. y')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y']
ax[0].axis(True)

ax[1].scatter(x,z)
ax[1].set_title('x vs. z')
ax[1].set_xlabel('x')
ax[1].set_ylabel('z']
ax[1].axis(True)
fig.show()

#Multiple (2x2) subplots with Object Oriented Programming OOP
fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(15,6))
ax[0,0].scatter(x,y,color='red')
ax[0,1].scatter(x,z,color='green')
ax[1,0].hist(x)
ax[1,1].hist(z)
ax[1,1].axis(True)
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
ax.axis(True)
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
#### Numpy (np.array) Vs. Pandas DataFrame (df) Vs. PyTorch Tensor
###############################################################################################################

arr1 = [1,2,3]
arr2 = [4,5,6]

np.stack((arr1, arr2), axis=0)      #result [[1,2,3],[4,5,6]]
np.stack((arr1, arr2), axis=1)      #result [[1,4],[2,5],[3,6]] #important

np.vstack((arr1, arr2))             #result [[1,2,3],[4,5,6]]
np.hstack((arr1, arr2))             #result [1,2,3,4,5,6]


pd.concat([df1,df2])                #append rows, default axis=0
pd.concat([df1,df2], axis=1)        #like hstack



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

df = df.query('index2 > 5 and col3 != "apple"')                     #filter using a query string
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
num_features = df.select_dtypes(exclude='object').columns           #numerical features
cat_features = df.select_dtypes(include='object').columns           #categorical features

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

#Column based joins
pd.merge(df1,df2,how='inner',on='col3')                             #SQL INNER JOIN on col3
pd.merge(df1,df2,how='inner',left_on='col3',right_on='col1')        #common col has diff name in both tables/df
pd.merge(df1,df2,how='outer',on=['col3','col5'])                    #SQL OUTER JOIN on col3 and col5
pd.merge(df1,df2,how='left',on='col5')                              #SQL LEFT JOIN on col5

#Index based joins
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
df['col1'].str.extract(r"(\d\.\d+)")                                #extract float in 1.2, 3.45, 6.789 etc. format
df['col1'].str.extract(r"\((.*?)(?= sq.m.)")
df['col1'].str.contains('abc')                                      #True if item contains abc
df['col1'].str.contains('^[^aeiouAEIOU].+[aeiouAEIOU]$')            #1st char not alphabet, then . once or more times, then last char alphabet

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




######################################
#pandas method chain
######################################
df_properties = (
	pd
	.DataFrame(data)
	.drop_duplicates()
	.apply(lambda col: col.str.strip().str.lower() if col.dtype == "object" else col)
	.assign(
		is_starred=lambda df_: df_.name.str.contains("\n").astype(int),
		name=lambda df_: (
			df_
			.name
			.str.replace("\n[0-9.]+", "", regex=True)
			.str.strip()
			.replace("adroit district s", "adroit district's")
		),
		location=lambda df_: (
			df_
			.location
			.str.replace("chennai", "")
			.str.strip()
			.str.replace(",$", "", regex=True)
			.str.split("in")
			.str[-1]
			.str.strip()
		),
		price=lambda df_: (
			df_
			.price
			.str.replace("?", "")
			.apply(lambda val: float(val.replace("lac", "").strip()) if "lac" in val else float(val.replace("cr", "").strip()) * 100)
		),
		area=lambda df_: (
			df_
			.area
			.str.replace("sqft", "")
			.str.strip()
			.str.replace(",", "")
			.pipe(lambda ser: pd.to_numeric(ser))
		),
		bhk=lambda df_: (
			df_
			.bhk
			.str.replace("bhk", "")
			.str.strip()
			.pipe(lambda ser: pd.to_numeric(ser))
		)
	)
	.rename(columns={
		"price": "price_lakhs",
		"area": "area_sqft"
	})
	.reset_index(drop=True)
	.to_excel("chennai-properties-99acres.xlsx", index=False)
)












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
np.unique(a1)                                                   #returns an array of unique values in a1
np.unique(a1,return_counts=True)                                #returns two arrays with unique values & their counts in a1 (aggregation)
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
#### Web Scraping - selenium
###############################################################################################################
pip install requests beautifulsoup4 selenium lxml html5lib webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-http2")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--enable-features=NetworkServiceInProcess")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
)



driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 5)

#OR -- headless browser instance (No GUI)
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
element = driver.find_element(By.ID,"<element id>")
element = driver.find_element(By.CLASS_NAME,"<element class id>")
element = driver.find_element(By.TAG_NAME,"<element tag>")
element = driver.find_element(By.XPATH,"<element xpath link>")

#entering Text value in Text Box
txt_element = driver.find_element(By.XPATH, "<element xpath link>")
txt_element.clear()                                                     #clear the text box
txt_element.send_keys("machine learning")                               #enter the value "machine learning"

#hitting enter on keyboard
from selenium.webdriver.common.keys import Keys
txt_element.send_keys(Keys.ENTER)

#clicking a button or a link
button = driver.find_element(By.XPATH, "<element xpath link>")
button.click()

#selecting value from dropdown
drop_field = driver.find_element(By.XPATH, "<element xpath link>")
drop_down = Select(drop_field)
drop_down.select_by_index(5)
drop_down.select_by_visible_text("<any visible value from dropdown>")

#multiselect values
multi_field = driver.find_element(By.XPATH, "<element xpath link>")
multi_select = Select(multi_field)
multi_select.select_by_index(1)
multi_select.select_by_visible_text("<any visible value from dropdown>")

multi_select.deselect_by_index(2)
multi_select.deselect_all()

#scrolling a webpage
#scroll down to a specific element using scrollIntoView
driver.execute_script("arguments[0].scrollIntoView(true);",element)
#scroll down 500px vertically using scrollBy
driver.execute_script("window.scrollBy(0,500);")
#scroll up 500px vertically using scrollBy
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
EC.presence_of_element_located((By.XPATH, "<>absolute XPATH"))      #wait for page title to contain specific text
#wait until the page is fully loaded
page_title = driver.title
try:
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    #here, d will automatically pick driver instance
except:
    print(f"The page {page_title} didn't load in given duration.")
else:
    print(f"The page {page_title} Succesfully loaded.")
    
#wait until presence of an element is located on webpage
#hovering on an element
actions = ActionChains(driver)
element1 = wait.until(EC.presence_of_element_located((By.XPATH, "<absolute XPATH>")))
actions.move_to_element(element1).perform()
#waiting for an element to be clickable
element2 = wait.until(EC.element_to_be_clickable(By.XPATH, "<absolute XPATH>"))
element2.click()


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
#### Python Image Library (PIL)
###############################################################################################################

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
#### sets - Everything           
###############################################################################################################      
                    
my_set = set()                                                                        #creating a set
my_set.add(element)                                                                   #add element to my_set
my_set.add(my_list)                                                                   #add my_list as one single element to my_set (just like list.append)
my_set.update(my_list)                                                                #add elements of my_list to my_set (just like list.extend)
set(my_list)                                                                          #convert my_list to set: show any duplicate values only once

sum(x)                                                                                #sum of all elements of set x
len(x)                                                                                #number of elements in set x

my_set.discard(n)                                                                     #delete n without error when not found
my_set.remove(n)                                                                      #delete n with error when not found

my_set.union(my_set2)                                                                 #set function union
my_set.intersection(my_set2)                                                          #set function intersection
my_set.differences(my_set2)                                                           #elements in x but not in y






###############################################################################################################
#### tuples - Everything                   
###############################################################################################################
                    
t = ('one', 2, 3.1)                                                                   #initializing a tuple
len(t)                                                                                #number of elements in the tuple
t[-1]                                                                                 #last element of the tuple
t.index('one')                                                                        #index of element 'one' in the tuple
t.count('one')                                                                        #count of element 'one' in the tuple






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
my_list.append('element_1')                 #append element_1 to the list
my_list.append('list_2')                    #append list_2 as one single element to my_list
my_list.extend('list_2')                    #extend the list with elements of list_2
my_list.pop()                               #remove last element from the list and return it
my_list.pop(2)                              #remove element at index 2 from the list and return it
my_list.remove(14)                          #remove element with value=14
my_list.reverse()                           #reverse the list
my_list.count(element_1)                    #count the number of element_1 in my_list
my_list.sort()                              #sort the list - in place
sorted(my_list)                             #just show the sorted list, not sort original list
[i**2 for i in my_list if i%2==0]           #list comprehension
[i**2 if i>5 else i**3 for i in my_list]    #list comprehension
my_list = list(tuple_1)                     #convert tuple_1 to list

from collections import Counter
groupby_count = Counter(my_list)            #SQL groupby count





###############################################################################################################
#### Python Regular Expressions (RE) or (regex) - Everything
###############################################################################################################
import re

#Meta Characters
# \.^$*+?{}[]()|

\                       #special meta character
\.                      #dot
.                       #any character
^                       #start after this meta character
$                       #end after this meta character
*                       #match previous character or class any number of times
+                       #match previous character or class at least once
?                       #match previous character either once or zero times.
{}                      #quantifier
{m,n}                   #match previous character m through n times
{m}                     #match previous character exactly m times
{m,}                    #match previous character m through infinite number of times
{,n}                    #match previous character 0 through n times
[]                      #to specify a character class
()
|                       #OR operator




\b                      #any boundary: start or end of the word
\w                      #any alphanumeric
\d                      #any digit
\s                      #any white space

\W                      #any non-alphanumeric
\D                      #any non-digit
\S                      #any non-white space



#Examples
[0-9]                   #matches any digit_dataset
[368]                   #matches 3, 6, 8 from digits

[^0-9]                  #matches any non-digit character
[^5]                    #matches any character except 5

[a-zA-Z0-9_]            #matches any alphanumeric pattern
[abc]                   #matches characters in 'a', 'b' or 'c'
[a-c]                   #matches characters in 'a' through 'c'
[a-z]                   #matches characters in 'a' through 'z' in smallcap
[abc\+]                 #matches characters in 'a', 'b', 'c' or '+'

[^a-zA-Z0-9_]           #matches any non-alphanumeric pattern
[^a-c]                  #matches characters in 'a' through 'c'

[ \t\n\r\f\v]           #matches any white space character

[^ \t\n\r\f\v]          #matches any non-white space character

$                       #end of line character
^                       #start of line character





[ca*t]                  #matches 'ct', 'cat', 'caat', 'caaat' and so on..
a[bcd]*b                #matches letter 'a' + zero or more letters from class [bcd] + letter 'b'
[ca+t]                  #matches 'cat', 'caat', 'caaat' and so on..
[home-?brew]            #matches 'homebrew' or 'home-brew'
[a/{1,3}b]              #matches 'a/b', 'a//b' and 'a///b'
[a/{,3}b]               #matches 'ab', 'a/b', 'a//b' and 'a///b'
[a/{1,}b]               #matches 'a/b', 'a//b', 'a///b', and so on...
[a/{3}b]                #matches 'a///b'


Pattern = re.compile(pattern_, flags=0)                 #compile a regular expression pattern into Pattern object

re.match(pattern_, string, flags=0)                     #returns match obj if pattern matches the beginning of string
re.fullmatch(pattern_, string, flags=0)                 #returns match obj if pattern matches the whole string
re.search(pattern_, string, flags=0)                    #returns match obj if pattern matches anywhere in the string
re.findall(pattern_, string, flags=0)                   #returns match obj return all non-overlapping matches of pattern in string
re.finditer(pattern_, string, flags=0)                  #

re.split(pattern_, string, maxsplit=0, flags=0)         #split the string wherever pattern is found
re.sub(pattern_, repl, string, count=0, flags=0)        #replace the leftmost occurrence of pattern in string by repl & return string
re.subn(pattern_, repl, string, count=0, flags=0)       #replace all occurrences of pattern in string by repl & return tuple (string, no_of_subs)
re.escape(pattern_)
re.purge()                                              #clear regex cache

Pattern.match(string[, pos[, endpos]])                  #same as re.match()
Pattern.fullmatch(string[, pos[, endpos]])              #same as re.fullmatch()
Pattern.search(string[, pos[, endpos]])                 #same as re.search()
Pattern.findall(string[, pos[, endpos]])                #same as re.findall()
Pattern.finditer(string[, pos[, endpos]])               #same as re.finditer()

Pattern.split(string, maxsplit=0)                       #same as re.split()
Pattern.sub(repl, string, count=0)                      #same as re.sub()
Pattern.subn(repl, string, count=0)                     #same as re.subn()
Pattern.pattern                                         #pattern_ string

m=re.match(r"(\w+) (\w+)","Isaac Newton, physicist")    #m = Match_obj is return by class match & search
m.expand(template)                                      #
m.group()                                               #Returns one or more subgroups of the match
m.group(0)                                              #Returns the entire match
m[0]                                                    #same as above
m.group(1)                                              #Returns the 1st parenthesized subgroup = 'Isaac'
m[1]                                                    #same as above
m.group(2)                                              #Returns the 2nd parenthesized subgroup = 'Newton'
m.group(1,2)                                            #Returns a tuple (1st, 2nd) parenthesized subgroup = ('Isaac','Newton')

m = re.match(r"(\d+)\.(\d+)", "24.1632")
m.groups()                                              #('24', '1632')

m = re.match(r"(\d+)\.?(\d+)?", "24")
m.groups()                                              #('24', None)
m.groups('0')                                           #('24', '0')



re.match("c", "abcdef")                             #'c' matches 'abcdef'?; No Match
re.search("c", "abcdef")                            #'c' found in 'abcdef'?; Match
re.fullmatch("p.*n", "python")                      #'p_____n' matches completely with 'python'?; Match
re.fullmatch("r.*n", "python")                      #'r_____n' matches completely with 'python'?; No Match

re.search("^c", "abcdef")                           #'abcdef' starts with 'c'?; No Match
re.search("^a", "abcdef")                           #'abcdef' starts with 'a'?; Match

re.match("X", "A\nB\nX", re.MULTILINE)









###############################################################################################################
#### Python strings - Everything
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
#### General Python
###############################################################################################################

divmod(a,b)                                 #returns a tuple with quotient and remainder of a/b
a//b                                        #returns quotient of a/b
a%b                                         #returns remainder of a/b
pow(a,b)                                    #returns a^b
pow(a,b,m)                                  #returns a^b % m








###############################################################################################################
#### sys - Everything
###############################################################################################################

import sys
sys.getsizeof(a)                                                    #memory size occupied by a(can be anything)







###############################################################################################################
#### Kaggle API
###############################################################################################################
API Token
    KGAT_67df385ef61e5bd0599b1a558295c50a

To use this token, set the KAGGLE_API_TOKEN environment variable:
    export KAGGLE_API_TOKEN=KGAT_67df385ef61e5bd0599b1a558295c50a

After setting KAGGLE_API_TOKEN, you can use the client as follows:
    kaggle competitions list




import os
os.environ['KAGGLE_USERNAME'] = 'grv08singh'                        #kaggle username
os.environ['KAGGLE_KEY'] = 'ffaf1f8f5a0a37757293ea35a2352255'       #kaggle password key

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

dataset_slug = 'salader/dogsvscats'           #kaggle dataset online path
download_path = 'D:/Downloads/data'           #local machine download path
api.dataset_download_files(dataset=dataset_slug, path=download_path, unzip=True)







###############################################################################################################
#### Create Production Grade Project Directory Structure - template.py
###############################################################################################################
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "facial-expression-recognition"

list_of_files = [
    ".github/workflows/.gitkeep",
    "artifacts/.gitkeep",
    "logs/.gitkeep",
    "notebooks/data/.gitkeep",
    "notebooks/01_test.ipynb",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/model_training.py",
    "src/components/prepare_base_model.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/constants/__init__.py",
    "src/entities/__init__.py",
    "src/entities/config_entity.py",
    "src/pipelines/__init__.py",
    "src/pipelines/data_ingestion_pipeline.py",
    "src/pipelines/model_evaluation_pipeline.py",
    "src/pipelines/model_training_pipeline.py",
    "src/pipelines/prepare_base_model_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    "templates/index.html",
    ".gitignore",
    "config.yaml",
    "dvc.yaml",
    "main.py",
    "params.yaml",
    "README.md",
    "requirements.txt",
    "setup_tf_gpu_env.txt",
    "setup.py",
    "template.py",
    "verify_gpu.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")











###############################################################################################################
#### pathlib Module - Everything (More New)
###############################################################################################################
from pathlib import Path

curr_dir = Path.cwd()                       #current directory path    
child_dir = curr_dir / "child folder"       #concat paths
file_path = child_dir / "abc.xlsx"          #file path
file_path.parent                            #name of folder containing file
file_path.name                              #name of file from path
file_path.stem                              #name of file without extension
file_path.suffix                            #extension of file
file_path.exists()                          #returns True if a file/directory exists
child_dir.isdir()                           #returns True if this path is of a directory
child_dir.isfile()                          #returns True if this path is of a file
for item in child_dir.iterdir()             #loop over all items in child_dir









###############################################################################################################
#### os Module - Everything
###############################################################################################################
import os

# count the number of directories in 
dir_count = sum(1 for entry in os.scandir(dir_path) if entry.is_dir())

# scan a directory and return a list of folders/files/both
def dir_content(dir_path):
    subdir_list = []
    files_list = []
    dir_content = os.listdir()
    for entry in entries:
        if entry.is_dir():
            subdir_list.append(entry.name)
        if not entry.is_dir():
            files_list.append(entry.name)
    return subdir_list, files_list, dir_content










###############################################################################################################
#### Archive Files - ZIP, RAR, TAR
###############################################################################################################

# Extract Zip File to extracted_files folder/directory
import zipfile
import os
with zipfile.ZipFile(zip_path, 'r') as zf:
    zf.extractall(extract_path, pwd=password)

# Extract Rar File to extracted_files folder/directory
import rarfile
with rarfile.RarFile(rar_path) as rf:
    rf.extractall(extract_path, pwd=password)
    
# Extract Tar File to extracted_files folder/directory
import tarfile
with tarfile.open(tar_path, 'r') as tar:
    tar.extractall(extract_to)




# List of files/folders present in a zip file
with zipfile.ZipFile(zip_path, 'r') as zf:
    namelist = zf.namelist()
    return namelist




# Check if a file is a ZIP File
def is_zip_file(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            return True
    except zipfile.BadZipFile:
        return False

# Check if a file is a Rar File
def is_rar_file(file_path):
    try:
        with rarfile.RarFile(file_path) as rf:
            return True
    except (rarfile.RarCannotExec, rarfile.BadRarFile):
        return False








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
#### GIT Everything - version management
###############################################################################################################

#######################################################
#### GIT Setup
#######################################################
git config --global user.name "Gaurav Singh"
git config --global user.email "grv08singh@gmail.com"
git config --list --global





#######################################################
#### Clone a Repository
#######################################################
git clone https://github.com/grv08singh/02_mlprojects.git

#### Push local changes onto GIT
git pull
git add .
git commit -m "<commit message>"
git push -u origin main

#### 






#######################################################
#### Remove already pushed files from git and future push
#######################################################
git rm --cached notebooks/data/data.zip             #file
git rm --cached -rf artifacts/evaluation/            #directory
git commit -m "files removed from git"
git push origin main



#######################################################
#### Replace the local repo with remote one (in case of conflict)
#######################################################
git fetch --all
git reset --hard origin/main
git clean -fd
git stash -u            #optional - to save untracked files
git pull
git stash pop           #optional - to recover changes



#######################################################
#### Resolve File Conflict with same branch versions
#######################################################

#### 1) Keep Local Changes
git stash
git pull
git stash pop
git add .
git commit -m "conflict msg"
git push

#### 2) Keep Remote Changes (Overwrite Local Changes)
git checkout -- <file path>
git pull

#### 3) To manually check the file which changes to keep
git add <file path>
git commit -m "<commit message>"
git pull                                #both the changes will be in the file, remove one manually 






#######################################################
#### resolve demerged branches (on different commit versions)
#### keep remote branch
#######################################################
git rebase --abort
git fetch origin
git reset --hard origin/main






#######################################################
#### GIT LFS (Large File System) - Track a file
#######################################################

#### install git LFS
winget install -e --id GitHub.GitLFS
git lfs install


#### Track Files via GIT LFS
git lfs track "*.pdf"           #keep pdf files on LFS
git lfs track "*.h5"            #keep h5 files on LFS
git lfs track "*.csv"           #keep csv files on LFS

cd <directory containing large file>

git add model.h5
git commit -m "large file commit message"
git push origin main

#### Untrack a file
git lfs untrack "file_path"
git rm --cached "file_path"
git add "file_path"
git add .gitattributes
git commit -m "Stop tracking file via Git LFS"
git push origin main


#### Untrack a directory
git lfs untrack "directory_path/**"
git rm --cached -r "directory_path/"
git add "directory_path/"
git add .gitattributes
git commit -m "Stop tracking directory via Git LFS"
git push origin main

#######################################################
#### Untrack an LFS file/directory - Purge complete history
#######################################################
## install git-filter-repo -->
pip3 install git-filter-repo

## Untrack an LFS file - Purge complete history
pip install 
git lfs untrack "file_path"
git rm --cached "file_path"
git add "file_path"
git add .gitattributes
git commit -m "Stop tracking file via Git LFS"
git push origin main

#### Untrack an LFS directory - Purge complete history
git filter-repo --invert-paths --path path/to/directory/
git push origin --force --all




















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

#Office System
CPUScore              : 9.4
D3DScore              : 9.9
DiskScore             : 8.95
GraphicsScore         : 8.1
MemoryScore           : 9.4
TimeTaken             : MostRecentAssessment
WinSATAssessmentState : 1
WinSPRLevel           : 8.1
PSComputerName        :







###############################################################################################################
#### Python Environment - Ubuntu (with sh file)
###############################################################################################################
# save a script with name setup_wsl_ml.sh, then run
chmod +x setup_wsl_ml.sh
./setup_wsl_ml.sh

# Open a new WSL terminal, then activate the environment with:
eval "$(~/miniconda3/bin/conda shell.bash hook)"
conda activate base_cpu




###############################################################################################################
#### Python Environment - Windows
###############################################################################################################

## C:\Users\grv06\AppData\Roaming\Code\User\settings.json

#### create conda env at default path
conda create -n venv python=3.9 -y
conda activate venv

#### create conda env in current directory
conda create -p venv python=3.9 -y
conda activate venv/

#### export environment
conda env export --name venv --file venv.yml
conda env create --file venv.yml

#### remove environment
conda deactivate
conda remove --name venv --all
conda remove --p venv --all

#### list all conda environments
conda env list

#### list all installed packages in selected conda environment
conda list

#### create a Jupyter Notebook kernel mapped to new environment
pip install ipykernel
python -m ipykernel install --user --name=venv_ipykernel

#### list all jupyter notebook kernels for current environment
jupyter kernelspec list

#### uninstall jupyter notebook kernel
jupyter kernelspec uninstall venv_ipykernel




python -m venv .venv                                                # Create Python environment using python
# .\.venv\Scripts\activate.bat

pip install -r requirements.txt


######Tensorflow-GPU env in cmd
conda create --name tf-gpu python=3.9 -y
conda activate tf-gpu
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y
pip install tensorflow-gpu==2.10.1
#pip install tensorflow==2.10.1
pip uninstall -y numpy
pip install numpy==1.23.5
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
pip install jupyter notebook ipykernel
python -m ipykernel install --user --name=tf-gpu --display-name "tf-gpu-ipykernel"

#:: Verify GPU Installation ::
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"


###### PyTorch-GPU env in cmd
conda create -n env_PyTorch_gpu python=3.11 -y
conda activate env_PyTorch_gpu
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia -y

#:: Verify GPU Installation ::
python -c "import torch; print(torch.cuda.is_available())"
