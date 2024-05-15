import pandas as pd
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

df = pd.read_csv("C:/Users/misl7603-RDP/Desktop/Fuzzy/sample.csv")

res = [process.extractOne(w, df.col2)[0] for w in df.col1]
sam = df.assign(col2=res)
print(sam)

def get_ratio(sam):
    name1 = sam['col1']
    name2 = sam['col2']
    
    out = fuzz.partial_ratio(name1, name2) 
    print(out)
    
    return fuzz.partial_ratio(name1, name2)
    
print(sam[sam.apply(get_ratio, axis=1) > 80].head(10))