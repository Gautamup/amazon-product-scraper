from bs4 import BeautifulSoup
import requests
import pandas as pd
# import openpyxl
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.172'
}
data = {'Title': [], 'Price': []}
# pd.DataFrame.from_dict(data)
url = "https://www.amazon.in/s?k=zephyrus+g14&crid=1R7V57U849F5H&sprefix=zephyrus+g14%2Caps%2C212&ref=nb_sb_noss_1"

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans:
    # print(span.string)
    data["Title"].append(span.string)
    
for price in prices:
    if not ("a-text-price" in price.get("class")):
        # print(price.find("span").get_text())
        data["Price"].append(price.find("span").get_text()) 
        if(len(data["Price"]) == len(data["Title"])):
            break  

df = pd.DataFrame.from_dict(data)
# df.to_csv("data.csv",index=False)
df.to_excel("data.xlsx",index=False)