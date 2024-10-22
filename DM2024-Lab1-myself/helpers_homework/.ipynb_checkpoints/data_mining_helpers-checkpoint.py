import nltk

"""
Helper functions for data mining lab session 2018 Fall Semester
Author: Elvis Saravia
Email: ellfae@gmail.com
"""

def format_rows(docs):
    """ format the text field and strip special characters """
    
    D = []
    for d in range(len(docs)):
        # 獲取 sentiment 和 comment 並去除換行符
        temp_s = " ".join(docs.iloc[d]['sentiment'].split("\n")).strip('\n\t')
        temp_d = " ".join(docs.iloc[d]['comment'].split("\n")).strip('\n\t')
        # 將格式化後的結果添加到 D 中
        D.append([temp_s, temp_d])  # 將 sentiment 和 comment 放在同一列表中
    return D # 返回 DataFrame


def format_labels_number(target, docs):
    """ format the labels based on sentiment_name """
    if target == 'nostalgia':
        return 0
    elif target == 'not nostalgia':
        return 1
    else:
        return -1  # Handle unexpected cases

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in row:
        if element == True:
            counter+=1
    return ("The amoung of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    tokens = []
    #將他根據標點符號分為一個一個句子
    for d in nltk.sent_tokenize(text, language='english'):
        #將每一個句子分為一個一個的文字
        for word in nltk.word_tokenize(d, language='english'):
            # filters here
            tokens.append(word)
    return tokens
