import requests
from bs4 import BeautifulSoup

def jpm_our_insight():
#With requests.get you can get the HTML of a webpage.
    response = requests.get("https://am.jpmorgan.com/private-bank/public/gl/en/home")
    html = response.text
    bs = BeautifulSoup(html, "html.parser")
#With this foe you can loop through all the tags "div" with a class equal to "band band-one-column-promo vertical-gap--external--top"
    for link in bs.find_all("div", {"class" : "band band-one-column-promo vertical-gap--external--top"}):
#Inside every single "div" tag, we look for all the "a" tags, where the title of the article is written
        for title_link in link.find_all("a", {"class" : "strong color-brown--jpm"}):
            print(title_link.get_text())
#Inside every "div" tag we look for all the "p" tags, where a brief description of the title is written            
        for content_link in link.find_all("p"):
            print(content_link.get_text())
        print("____________________________________________")


jpm_our_insight()
