import requests
import pandas as pd
import numpy as np
import math
BATCH = 50 # number of bottle to scrape per page (max 50)
def get_wine_data(page,price):
    r = requests.get(
    "https://www.vivino.com/api/explore/explore",
    params={
        "price_range_max": price+0.49,
        "price_range_min": price,
        "min_rating": 1,
        "per_page": f'{BATCH}',
        "page": f'{page}',
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
    },)
    
    results = results = [
    [
        t["vintage"]["wine"]["winery"]["name"] if t["vintage"] is not None and t["vintage"]["wine"] is not None and t["vintage"]["wine"]["winery"] is not None  else "No Winery Name Found",
        t["vintage"]["wine"]["name"] if t["vintage"] is not None and t["vintage"]["wine"] is not None else "No Wine Name Found",
        t["vintage"]["year"] if t["vintage"] is not None else "No Year Found",
        t["vintage"]["wine"]["id"] if t["vintage"] is not None and t["vintage"]["wine"] is not None else "No ID Found",
        t["vintage"]["statistics"]["ratings_average"] if t["vintage"]["statistics"] is not None else "No Ratings Found",
        t["vintage"]["image"]["location"][2:] if t["vintage"]["image"] is not None else "No Image Found",
        f'{t["vintage"]["wine"]["region"]["name"]} - {t["vintage"]["wine"]["region"]["country"]["name"]}' if t["vintage"]["wine"]["region"] is not None else "No Region Found",
        f'{t["price"]["amount"]:.2f} {t["price"]["currency"]["name"]}' if t["price"] is not None else "No Price Found",
        t["price"]["bottle_type"]["volume_ml"] if t["price"] is not None else "No Volume Found",
        t["price"]["url"] if t["price"] is not None else "No URL Found",
    ]
    for t in r.json()["explore_vintage"]["matches"]
    ]   

    dataframe = pd.DataFrame(
        results, columns=["winery_name","wine_name","year", "wine_id", "rating", "bottle_photo", "country", "price", "volume_ml","url"]
    )
    return dataframe



dataframe = pd.DataFrame(
columns=["winery_name","wine_name","year", "wine_id", "rating", "bottle_photo", "country", "price", "volume_ml","url"]
)

for price in np.arange(0,500,0.5):
    rtemp = requests.get(
    "https://www.vivino.com/api/explore/explore",
    params={
        "price_range_max": price+0.49,
        "price_range_min": price,
        "per_page": f'{BATCH}',
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
    },)

    NB_Bottles = rtemp.json()["explore_vintage"]["records_matched"]
    print(f"{NB_Bottles} bottles found for {price}€")
    if NB_Bottles > 2000:
        print("Too many bottles found, please reduce the price range") # if we exceed 2000 bottles in one request we can't scrape them all because after 2000 it's the same request repeated with a higher page number
        if input("Continue? (y/n)") == "y":
            continue
        else:
            break
    NB_Pages = math.ceil(NB_Bottles/BATCH)

    for page in range(NB_Pages):
        print(f'Page {page+1}')
        df = get_wine_data(page+1,price)
        dataframe = pd.concat([dataframe,df], ignore_index=True)
        
print(dataframe)
dataframe.to_csv("wine_data.csv",sep="|",index=False)
