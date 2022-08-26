import pandas as pd


"""
csvs = (
    "wine_data_high.csv",
    "wine_data_low.csv"
)
dataFrame = pd.concat(
   map(pd.read_csv, csvs), ignore_index=True)

dataFrame.to_csv("wine_data.csv",sep="|",index=False)
"""

df = pd.read_csv('wine_data.csv', sep=",")
df_reorder = df[["winery_name","wine_name","year", "wine_id", "rating", "bottle_photo", "country", "price", "volume_ml","url"]] # rearrange column here
#you may need to use zip(*[['A', 'B', 'C', 'D', 'E']])
df_reorder.to_csv('wine_data.csv',sep="|", index=False)