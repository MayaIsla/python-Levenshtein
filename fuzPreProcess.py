from ast import pattern
import pandas as pd
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from fuzzywuzzy import utils
import nltk

#nltk.download('stopwords')

csv_file = 'C:/desc_data.csv'
out_file = 'C:/output.csv'

df = pd.read_csv(csv_file)

#df_clean = df.drop_duplicates(subset=['Description']) Oops I didn't want to do that

#df['Description'] =  df['Description'].str.replace('disc code|do not use|discountinued','')
#RegEx = '|'.join(r'\b(?:{})\b'.format(x) for x in stop_words)

#print(RegEx)
#df['Description_1'] = df['Description'].str.replace(RegEx,' ', regex=True)

#new_words = set(stop_words)
#format = lambda x: ' '.join(w for w in x.split() if not w in stop_words)
#df['Description_2'] = df['Description'].apply(format)


stop_words = ["DISC CODE","do not use","discontinued","discountinued","DO NOT USE",]


pat = r'\b(?:{})\b'.format('|'.join(stop_words))
df['Out'] = df['Description'].str.replace(pat, '')
df['Out'] = df['Out'].str.replace(r'\s+', ' ')
#df['Out'].to_csv(out_file, sep='\t', encoding='utf-8')

_list = []

invalid_query = "... //"


for i_dataframe in range(len(df_clean)-1):
    comparison_fullname = df_clean[i_dataframe]
    for entry_fullname, entry_score in process.extract(comparison_fullname, df_clean[i_dataframe], scorer=fuzz.ratio):
        if utils.full_process(invalid_query):
            process.extract(invalid_query, pattern)
        if entry_score >=90:
            _list.append((comparison_fullname, entry_fullname, entry_score))
print(_list)
