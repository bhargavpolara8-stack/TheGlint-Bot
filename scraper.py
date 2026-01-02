import requests
from bs4 import BeautifulSoup

# તમારી લિંક
URL = "http://theglint.rf.gd/add_product.php"
AMAZON_URL = "https://www.amazon.in/s?k=jewelry"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_amazon_products():
    page = requests.get(AMAZON_URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # 5 પ્રોડક્ટ્સ લેવા માટે
    products = soup.find_all("div", {"data-component-type": "s-search-result"}, limit=5)
    
    for product in products:
        try:
            title = product.h2.text.strip()[:50]
            price_tag = product.find("span", "a-price-whole")
            price = price_tag.text if price_tag else "Check Price"
            img = product.find("img", "s-image")['src']
            link = "https://www.amazon.in" + product.h2.a['href']
            
            # ડેટા મોકલવાની રીત બદલી (GET વાપરી છે)
            payload = {
                "title": title,
                "price": price,
                "image_url": img,
                "affiliate_link": link
            }
            
            # અહીં requests.get વાપર્યું છે
            res = requests.get(URL, params=payload)
            print(f"Sent: {title} | Status: {res.text}")
            
        except Exception as e:
            print(f"Error: {e}")

get_amazon_products()

