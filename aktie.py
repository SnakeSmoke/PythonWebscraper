from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from decimal import Decimal
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# --ALLA TICKERS TILL AFFARSVARDEN.SE--
#
# Ericsson:     772
# Electrolux:   2193
# AstraZeneca:  1295
# Volvo:        1146

# --ALL TICKERS FÖR YAHOO FINANCE--
#
# Ericsson:     ERIC
# Electrolux:   ELUX-B.ST
# AstraZeneca:  AZN
# Volvo:        VOLV-B.ST

# --ALL TICKERS FÖR NORDENET--
#
# Ericsson:     100
# Electrolux:   81
# AstraZeneca:  3524
# Volvo:        365

#Globala variabler för att identifiera företagen på hemsidan
#ericsson = "772"
#electrolux = "2193"
#astraZeneca = "1295"
#volvo = "1146"
 
#Klass med variabler och metoder
class Aktie:
    def __init__(self, namn, beta):
        self.namn = namn
        self.beta = beta

#Funktionen som hämtar alla aktiekurser

# --ALL TICKERS--
#
# Ericsson:     772
# Electrolux:   2193
# AstraZeneca:  1295
# Volvo:        https://www.affarsvarlden.se/bors/stock-details/1146/

def get_stock_solidity(ticker):

    my_url = "https://www.affarsvarlden.se/bors/stock-details/%s"%(ticker)
    #Hämtar hemsidan
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    finder = page_soup.find_all("span",{"class":"pull-right"})

    item_list = []
    for find in finder:
        item_list.append(find.text)
        #print(find.text)

    return item_list[3]

#kursutveckling för en månad
def get_stock_develop(ticker):

    my_url = "https://www.nordnet.se/mux/web/marknaden/aktiehemsidan/historik.html?identifier=%s&marketplace=11&inhibitTrade=1"%(ticker)
    #Hämtar hemsidan
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    finder = page_soup.find_all("td")
    
    item_list = []
    for find in finder:
        item_list.append(find.text)

    return str(item_list[24])

def get_stock_high(ticker):

    my_url = "https://www.nordnet.se/mux/web/marknaden/aktiehemsidan/historik.html?identifier=%s&marketplace=11&inhibitTrade=1"%(ticker)
    #Hämtar hemsidan
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    finder = page_soup.find_all("td")
    
    item_list = []
    for find in finder:
        item_list.append(find.text)

    return str(item_list[25])

def get_stock_low(ticker):

    my_url = "https://www.nordnet.se/mux/web/marknaden/aktiehemsidan/historik.html?identifier=%s&marketplace=11&inhibitTrade=1"%(ticker)
    #Hämtar hemsidan
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    finder = page_soup.find_all("td")
    
    item_list = []
    for find in finder:
        item_list.append(find.text)

    return str(item_list[26])

def get_stock_PE(ticker):

    my_url = "https://www.affarsvarlden.se/bors/stock-details/%s"%(ticker)
    #Hämtar hemsidan
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    finder = page_soup.find_all("span",{"class":"pull-right"})

    item_list = []
    for find in finder:
        item_list.append(find.text)
        #print(find.text)

    return item_list[9]


def get_stock_PS(ticker):

    my_url = "https://www.affarsvarlden.se/bors/stock-details/%s"%(ticker)
    #Hämtar hemsidan
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    finder = page_soup.find_all("span",{"class":"pull-right"})

    item_list = []
    for find in finder:
        item_list.append(find.text)
        #print(find.text)

    return item_list[8]

def get_stock_name(ticker):
    my_url = "https://www.affarsvarlden.se/bors/stock-details/%s"%(ticker)
    #Hämtar hemsidan
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    return page_soup.h2.text

def get_stock_beta(ticker):
    my_url = "http://finance.yahoo.com/quote/%s?p=%s"%(ticker,ticker)
    
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    
    spans = page_soup.find_all("td",{"data-test":"BETA_3Y-value"})
    for span in spans:
        beta_value = span.text
    return float(beta_value)
 

