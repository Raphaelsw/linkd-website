import pandas as pd
from nltk.tokenize import word_tokenize, MWETokenizer
import nltk

if __name__ == '__main__':
    nltk.download('punkt')

def import_data():
    # df = pd.read_csv('../linkedindf.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/Raphaelsw/linkd-website/main/linkedindf.csv')
    # df.head()

    # for col in df.select_dtypes(include=['object']):
    #     df[col] = df[col].str.lower()
    # df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    # df.head(1)


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

    # jobs_all = jobs_all[jobs_all.description.notnull()] # filter out null values
    # jobs_all = jobs_all.reset_index() # throwing index issues if don't reset index
    # # jobs_all = jobs_all.head(10)

    df['description_tokens'] = ""


    for i in range(len(df)):
    #     print(df3['text'].iloc[i].lower())
        index = df.index[i]

    # for index, row in df3.iterrows():
        # lowercase words
    #     detail = row.description.lower()
        detail = df['Text'].iloc[i].lower()
        # tokenize words
        detail = word_tokenize(detail)
        # handle multi-word tokenization (e.g., 'Power BI')
        multi_tokens = [('power', 'bi'), ('data', 'lake'), ('data', 'lakes'), ('machine', 'learning'), ('objective', 'c'),
                        ('visual', 'basic')]
        tokenizer = MWETokenizer(multi_tokens)
        detail = tokenizer.tokenize(detail)
        # remove duplicates
        detail = list(set(detail))
        # filter for keywords only
        detail = [word for word in detail if word in keywords]
        # replace duplicate keywords
        replace_tokens = {'powerbi' : 'power_bi', 'spreadsheets': 'spreadsheet'}
        for key, value in replace_tokens.items():
            detail = [d.replace(key, value) for d in detail]
        # add to details list # row.description_tokens = detail
        df.at[index, 'description_tokens'] = detail


    df.loc[df['Seniority level'] == 'full-time', ['Employment type', 'Seniority level']] = df.loc[df['Seniority level'] == 'full-time', ['Seniority level', 'Employment type']].values


    row_labels = df[df['Text'] == 'Failed'].index
    df.drop(labels=row_labels, inplace=True)

    return df
