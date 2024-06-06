from ast import pattern
import pandas as pd
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from fuzzywuzzy import utils

df = pd.read_csv('desc_data.csv')
print(df)
#df_clean = df.drop_duplicates(subset=['Description']) Oops I didn't want to do that

df_clean =  df['Description'].str.replace('disc code|do not use|discountinued', '', 
                                          regex=True, case=False)

print(df_clean)


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
