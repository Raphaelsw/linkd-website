import streamlit as st
from importer import import_data
from charts import make_charts, make_charts_horizontal, filtered_keywords
import nltk

nltk.download('punkt')


st.set_page_config('Linkedin in Tel Aviv')
'''
# An analysis of Linkedin in Tel Aviv
'''

# Import Data
df = import_data()


# Top page build
# st.markdown("## 🛠️ What is the TOP Skill for Data Analysts?!?")

if 'orientation_state' not in st.session_state:
    st.session_state.orientation_state = False

# col1, col2 = st.columns(2, gap='large')
# with col1:
#     keyword_list = ["Industries", "Job function", "Title", "Company", "Seniority level"]
#     keyword_choice = st.radio('Column:', keyword_list, key = 'job', horizontal=True)
# with col2:
#     graph_list = ["Bar", "Pie"]
#     graph_choice = st.radio('Chart type:', graph_list, horizontal=True, disabled=bool(st.session_state.orientation_state))



# Number skill selctor for slider
skill_dict = {"Top 5": 5, "Top 10": 10, "Top 20": 20, "Top 50": 50, "All" : len(df)}

#Orientation
orientation_lst = [False, True]

analysis_lst = ["General data", "Text/tokenization"]


with st.sidebar:
    st.markdown("# 🛠️ Filters")
    analysis_type = st.radio("Analysis on the:", analysis_lst)
    top_n_choice = st.radio("Number of entries:", list(skill_dict.values()), format_func= lambda x: 'Top ' + str(x))
    orientation = st.selectbox("Orientation:", orientation_lst, key = 'orientation_state', format_func= lambda x: 'vertical' if x == False else 'horizontal')


if analysis_type == 'General data':
    col1, col2 = st.columns(2, gap='large')
    with col1:
        keyword_list = ["Industries", "Job function", "Title", "Company", "Seniority level"]
        keyword_choice = st.radio('Column:', keyword_list, key = 'job', horizontal=True)
    with col2:
        graph_list = ["Bar", "Pie"]
        graph_choice = st.radio('Chart type:', graph_list, horizontal=True, disabled=bool(st.session_state.orientation_state))
else:
        prog_list = ["Programming languages", "General "]
        prog_choice = st.radio('Column:', prog_list, key = 'prog', horizontal=True)


# Picked out keywords based on all keywords (only looked words with 100+ occurrences)
keywords_programming = [
'sql', 'python', 'r', 'c', 'c#', 'javascript', 'js',  'java', 'scala', 'sas', 'matlab',
'c++', 'c/c++', 'perl', 'go', 'typescript', 'bash', 'html', 'css', 'php', 'powershell', 'rust',
'kotlin', 'ruby',  'dart', 'assembly', 'swift', 'vba', 'lua', 'groovy', 'delphi', 'objective-c',
'haskell', 'elixir', 'julia', 'clojure', 'solidity', 'lisp', 'f#', 'fortran', 'erlang', 'apl',
'cobol', 'ocaml', 'crystal', 'javascript/typescript', 'golang', 'nosql', 'mongodb', 't-sql', 'no-sql',
'visual_basic', 'pascal', 'mongo', 'pl/sql',  'sass', 'vb.net', 'mssql',
]

keywords_libraries = [
'scikit-learn', 'jupyter', 'theano', 'openCV', 'spark', 'nltk', 'mlpack', 'chainer', 'fann', 'shogun',
'dlib', 'mxnet', 'node.js', 'vue', 'vue.js', 'keras', 'ember.js', 'jse/jee',
    'tensorflow', 'pycharm', 'keras',
]

keywords_analyst_tools = [
'excel', 'tableau',  'word', 'powerpoint', 'looker', 'powerbi', 'outlook', 'azure', 'jira', 'twilio',  'snowflake',
'shell', 'linux', 'sas', 'sharepoint', 'mysql', 'visio', 'git', 'mssql', 'powerpoints', 'postgresql', 'spreadsheets',
'seaborn', 'pandas', 'gdpr', 'spreadsheet', 'alteryx', 'github', 'postgres', 'ssis', 'numpy', 'power_bi', 'spss', 'ssrs',
'microstrategy',  'cognos', 'dax', 'matplotlib', 'dplyr', 'tidyr', 'ggplot2', 'plotly', 'esquisse', 'rshiny', 'mlr',
'docker', 'linux', 'jira',  'hadoop', 'airflow', 'redis', 'graphql', 'sap', 'tensorflow', 'node', 'asp.net', 'unix',
'jquery', 'pyspark', 'pytorch', 'gitlab', 'selenium', 'splunk', 'bitbucket', 'qlik', 'terminal', 'atlassian', 'unix/linux',
'linux/unix', 'ubuntu', 'nuix', 'datarobot',
]

keywords_cloud_tools = [
'aws', 'azure', 'gcp', 'snowflake', 'redshift', 'bigquery', 'aurora',
]

# Not using
keywords_general_tools = [
'microsoft', 'slack', 'apache', 'ibm', 'html5', 'datadog', 'bloomberg',  'ajax', 'persicope', 'oracle',
]

# using
keywords_general = [
'coding', 'server', 'database', 'cloud', 'warehousing', 'scrum', 'devops', 'programming', 'saas', 'ci/cd', 'cicd',
'ml', 'data_lake', 'frontend',' front-end', 'back-end', 'backend', 'json', 'xml', 'ios', 'kanban', 'nlp',
'iot', 'codebase', 'agile/scrum', 'agile', 'ai/ml', 'ai', 'paas', 'machine_learning', 'macros', 'iaas',
'fullstack', 'dataops', 'scrum/agile', 'ssas', 'mlops', 'debug', 'etl', 'a/b', 'slack', 'erp', 'oop',
'object-oriented', 'etl/elt', 'elt', 'dashboarding', 'big-data', 'twilio', 'ui/ux', 'ux/ui', 'vlookup',
'crossover',  'data_lake', 'data_lakes', 'bi',
]
#
keywords_education = [
'undergraduate', 'master', 'masters',
]

keywords_industry = [
'software', 'business', 'financial', 'insurance', 'information', 'pharmaceutical', 'banking',
'gaming', 'renewable energy semiconductor manufacturing, motor vehicle manufacturing, and utilities',
'security',
]


#
keywords = keywords_programming + keywords_libraries + keywords_analyst_tools + keywords_cloud_tools + keywords_general+ keywords_education + keywords_industry



if analysis_type == "General data":

    if orientation == False:
        make_charts(column = st.session_state.job, size = top_n_choice, chart_type = graph_choice)
    else:
        make_charts_horizontal(column = st.session_state.job, size = top_n_choice)

else:
    if prog_choice == 'Programming languages':
        filtered_keywords(df, keywords_programming, title= f"Top {top_n_choice} Programming Languages", head = top_n_choice)
    else:
        filtered_keywords(df, keywords, title= f"Top {top_n_choice} tokens", head = top_n_choice)
