from bs4 import BeautifulSoup
import requests
import re

#this is all used to get number of pages then display

search_term = input("What gpu are you looking for?")

url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"

page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong

pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found ={}

#now that we have all those pages we loop and get price


for page in range (1, pages  + 1):

    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"

    page = requests.get(url).text

    doc = BeautifulSoup(page, "html.parser")

    #now we get the div of the product to get the price

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    items = div.find_all(string=re.compile(search_term))
    #using re.compile will get you results which include
    #more than just "the search term"
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
            # we have the link here
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")

        try: 

            price = next_parent.find(class_="price-current").find("strong").string

            items_found[item] = {"price": int(price.replace(",","")), "link": link}
            
        except:
            pass
                             
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])


for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("------------------------------")














        
        
        #we have gotten the prices now we need the names!!!


