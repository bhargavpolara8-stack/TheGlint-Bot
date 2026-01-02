import requests
from bs4 import BeautifulSoup
from urllib.parse import quote # આ લાઈન ઉમેરો

# ... બાકીનો કોડ ...

            # payload ને આ રીતે અપડેટ કરો
            params = f"?title={quote(title)}&price={quote(price)}&image_url={quote(img)}&affiliate_link={quote(link)}"
            
            res = requests.get(URL + params) # params ને લિંક સાથે જોડી દીધા
            print(f"Sent: {title} | Status: {res.text}")

