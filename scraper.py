import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

URL = "http://theglint.rf.gd/add_product.php"
AMAZON_URL = "https://www.amazon.in/s?k=jewelry"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_amazon_products():
    try:
        page = requests.get(AMAZON_URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        products = soup.find_all("div", {"data-component-type": "s-search-result"}, limit=5)
        
        for product in products:
            try:
                title = product.h2.text.strip()[:50]
                price_tag = product.find("span", "a-price-whole")
                price = price_tag.text if price_tag else "Check Price"
                img = product.find("img", "s-image")['src']
                link = "https://www.amazon.in" + product.h2.a['href']
                
                # બધી વિગતોને સુરક્ષિત રીતે લિંકમાં જોડવા માટે
                final_url = f"{URL}?title={quote(title)}&price={quote(price)}&image_url={quote(img)}&affiliate_link={quote(link)}"
                
                res = requests.get(final_url)
                print(f"Sent: {title} | Status: {res.text}")
            except Exception as e:
                print(f"Product Error: {e}")
    except Exception as e:
        print(f"Main Error: {e}")

get_amazon_products()

