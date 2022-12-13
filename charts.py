import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from importer import import_data

# Import Data
# df = import_data()


def make_charts(df, column = 'Job function', size = 10, chart_type = 'Bar'):
    x = []
    y = []
    for i in range(len(df[column].value_counts())):
        x.append(df[column].value_counts().index[i])
        y.append(df[column].value_counts()[i])


    fig, ax = plt.subplots(figsize=(7, 3))
    if chart_type == 'Bar':
        ax.bar(x[:size], y[:size])
    else:
        ax.pie(y[:size], labels = x[:size])
    ax.set_title(f'{column}', fontsize = 14)
    ax.tick_params(axis='both', which='major', labelsize=6, rotation=15)

    return st.pyplot(fig)


def make_charts_horizontal(df, column = 'Job function', size = 10):
    x = []
    y = []
    for i in range(len(df[column].value_counts())):
        x.append(df[column].value_counts().index[i])
        y.append(df[column].value_counts()[i])

    # Figure Size
    fig, ax = plt.subplots(figsize =(8, 4))

    # Horizontal Bar Plot
    ax.barh(x[:size], y[:size])

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)

    # Add x, y gridlines
    ax.grid(visible = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)

    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight ='bold',
                color ='grey')

    # Add Plot Title
    ax.set_title(f'{column}',
                loc ='left', )

    # Add Text watermark
    fig.text(0.9, 0.15, '', fontsize = 12,
            color ='grey', ha ='right', va ='bottom',
            alpha = 0.7)
    return st.pyplot(fig)





def filtered_keywords(df, keywords, title="Keyword Analysis", head=10):
    # get keywords in a column
    count_keywords = pd.DataFrame(df.description_tokens.sum()).value_counts().rename_axis('keywords').reset_index(name='counts')

    # get frequency of occurence of word (as word only appears once per line)
    length = len(df) # number of job postings
    count_keywords['percentage'] = 100 * count_keywords.counts / length

    # plot the results
    count_keywords = count_keywords[count_keywords.keywords.isin(keywords)]
    count_keywords = count_keywords.head(head)

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.bar(x="keywords", height="percentage", data=count_keywords , color=np.random.rand(len(count_keywords.keywords), 3))
    ax.set_ylabel("Likelyhood to be in job posting (%)")
    ax.set_title(title)
    ax.tick_params(rotation = 45)

    return st.pyplot(fig)
