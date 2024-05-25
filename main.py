import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

quotes_lst = []
tags_lst = []
for i in range(len(quotes)):
    tags_lst = []
    tagsforquote = tags[i].find_all("a", class_="tag")
    for tagforquote in tagsforquote:
        tags_lst.append(tagforquote.text)
    quote_info = {
        "tags": tags_lst,
        "author": authors[i].text,
        "quote": quotes[i].text,
    }
    quotes_lst.append(quote_info)

#print(json.dumps(quotes_lst, ensure_ascii=False, indent=4))

author_links = soup.find_all("a", string='(about)', href=True)
authors_lst=[]

for link in author_links:
    author_url = link.get('href')
    full_author_url = url + author_url

    author_response = requests.get(full_author_url) 
    soup_author = BeautifulSoup(author_response.text, "html.parser")

    fullname = soup_author.find("h3", class_="author-title")
    born_date = soup_author.find("span", class_="author-born-date")
    born_location = soup_author.find("span", class_="author-born-location")
    description = soup_author.find("div", class_="author-description")

    
    author_info= {
        'fullname': fullname.text,
        'born_date': born_date.text,
        'born_location': born_location.text,
        'description': description.text.strip().replace("\n", '')
    }
    authors_lst.append(author_info)

    #print(json.dumps(authors_lst, ensure_ascii=False, indent=4))
    with open('authors.json', 'w') as file:
        json.dump(authors_lst, file, ensure_ascii=False, indent=4)


# quotes_lst = []
# for i in range(len(quotes)):
#     tags_lst = []
#     tagsforquote = tags[i].find_all("a", class_="tag")
#     for tagforquote in tagsforquote:
#         tags_lst.append(tagforquote.text)
#     quote_info = {
#         "tags": tags_lst,
#         "author": authors[i].text,
#         "quote": quotes[i].text,
#     }
#     quotes_lst.append(quote_info)
# print(json.dumps(authors_lst, ensure_ascii=False, indent=4))
    # with open('authors.json', 'w') as file:
    #     json.dump(authors_lst, file, ensure_ascii=False, indent=4)

# print(json.dumps(quotes_lst, ensure_ascii=False, indent=4))
# with open('quotes.json', 'w') as file:
#     json.dump(quotes_lst, file, ensure_ascii=False, indent=4)


