import sys
import requests
from bs4 import BeautifulSoup as bs

def getCurrencies():
    r = requests.get("https://www.x-rates.com/table/?from=USD&amount=1")

    #print("Now printing")
    #print(r.text[0:100])

    soup = bs(r.text, "html.parser")
    #res = soup.find_all('td', attrs={'class':'rtRates'})
    res = soup.find_all('tr')
    #print(res)

    currencyMap = {}

    
    for e in res:
        #print(e.text)
        #print("------------------------------------------------------------------------------------")
        textArray = e.text
        textArray = textArray.split('\n')
        if textArray[2] == "1.00 USD":
            #print(textArray[1])
            currencyMap[textArray[1]] = 1.00
            continue
       
        currencyMap[textArray[1]] = textArray[2]
   
    return currencyMap

#if __name__ == "__main__":
#    currencyMap = getCurrencies()

