from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import wikipedia

def data_parse(data_url):

    #opens connection, grabs the page
    uClient = uReq(data_url)
    page_html = uClient.read()
    uClient.close()

    #html parsing
    page_soup = soup(page_html, "html.parser")


    #grabs each product
    container = page_soup.findAll("div", {"class":"infobox"})

    #gender = container.

    for container in containers:
        #brand = container.div.div.a.img["title"]
        
        title_container = container.findAll("a", {"class":"item-title"})
        product_name = title_container[0].text
        
        shipping_container = container.findAll("li", {"class": "price-ship"})
        shipping = shipping_container[0].text.strip()

        #print("brand" + brand)
        print("product name: " + product_name)
        print("shipping: " + shipping)
        print("---------------------------------")


name = input("Hello to GOT character info page! Enter a character's name: ")
try:
    wiki_data = wikipedia.page(name)
except:
    print("Hmm, that doesn't seem like a GOT Character. Try again?")
#data_parse(wiki_data)
summary = wikipedia.summary(name, sentences=3)
if("fictional" in summary):
    print(summary)
else:
    print("Hmm, that doesn't seem like a GOT Character. Try again?")
