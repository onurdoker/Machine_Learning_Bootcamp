# %%
import pandas as pd
import requests

# quotes.toscrape.com
# jsonplaceholder.typicode.com

# API URL
api_url = "https://jsonplaceholder.typicode.com/users"

# %%
# ! GET request
response = requests.get(api_url, timeout=10)

print(response.status_code)  # 200

if response.status_code == 200:
    print("Connection successful", response.status_code)
    response_data = response.json()

    # Not normalized data
    response_df = pd.DataFrame(response_data)
    response_df.to_excel("response_df.xlsx", index=False)

    # Normalized data
    normalize_df = pd.json_normalize(response_data)
    normalize_df.to_excel("normalized_df.xlsx", index=False)

else:
    print("Connection failed", response.status_code)


# %%
# ! POST

post_url = "https://jsonplaceholder.typicode.com/posts"

student = {"Name": "John", "Age": 40}

post_response = requests.post(post_url, json=student)

if post_response.status_code == 201:
    print("Data send successfully")
else:
    print("Data dont send", post_response.status_code)


# %%
# ! Web Scrapping
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response_web = requests.get(url)

if response_web.status_code == 200:
    soup = BeautifulSoup(response_web.content, "html.parser")
    page_title = soup.find("h1").text
    page_title_style = soup.find("h1").find("a")
    print(page_title_style["style"])

else:
    print("Error", response_web.status_code)

# sure= 1:28:04

# %%

url = "https://quotes.toscrape.com/"

response_web = requests.get(url)

data_list = []

if response_web.status_code == 200:
    soup = BeautifulSoup(response_web.content, "html.parser")

    divs = soup.find_all("div", class_="quote")

    for div in divs:
        text_ = div.find("span", class_="text").text
        author = div.find("small", class_="author").text

        data_list.append({"Author": author, "Text": text_})

else:
    print("Error", response_web.status_code)


data_df = pd.DataFrame(data_list)
print(data_df.head())


# %%
# Pagination

url = "https://quotes.toscrape.com/"
data_list = []

for i in range(1, 6):
    url_page = f"{url}page/{i}"
    print(url_page)

    request_page = requests.get(url_page)
    soup_page = BeautifulSoup(request_page.content, "html.parser")

    divs = soup_page.find_all("div", class_="quote")
    for div in divs:
        text_page = div.find("span", class_="text").text
        author_page = div.find("small", class_="author").text
        data_list.append({"Author": author_page, "Text": text_page})

# %%
# Practice
import time

ibb_url = "https://www.ibb.istanbul/gundem/duyurular"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}


response_ibb = requests.get(ibb_url, headers=headers)

if response_ibb.status_code == 200:
    ibb_soup = BeautifulSoup(response_ibb.content, "html.parser")
    time.sleep(10)

    announcements = ibb_soup.find_all("div", class_="grid gap-x-5 gap-y-5")

    for announcement in announcements:
        title = announcement.find("span", class_="pl-4 font-bold w-10/12").text
        # link = announcement.a["href"]
else:
    print("Error:", response_ibb.status_code)

# %%
