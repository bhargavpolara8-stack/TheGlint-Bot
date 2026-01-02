import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# સાચી લિંક
URL = "http://theglint.rf.gd/add_product.php"
AMAZON_URL = "https://www.amazon.in/s?k=jewelry"

# આ હેડર્સ સર્વરને છેતરશે કે ડેટા બ્રાઉઝરથી આવે છે
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

def get_amazon_products():
    print("Fetching Amazon data...")
    session = requests.Session() # સેસનનો ઉપયોગ
    try:
        page = session.get(AMAZON_URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        products = soup.find_all("div", {"data-component-type": "s-search-result"}, limit=5)
        
        for product in products:
            try:
                title = product.h2.text.strip()[:60]
                price_tag = product.find("span", "a-price-whole")
                price = "Rs. " + price_tag.text if price_tag else "Check Price"
                img = product.find("img", "s-image")['src']
                link = "https://www.amazon.in" + product.h2.a['href']
                
                # ડેટા મોકલવો
                params = {
                    "title": title,
                    "price": price,
                    "image_url": img,
                    "affiliate_link": link
                }
                
                # અહીં GET રિક્વેસ્ટ સેસન સાથે મોકલવી
                res = session.get(URL, params=params, headers=headers)
                print(f"Product: {title[:20]}... | Server Response: {res.text}")
                
            except Exception as e:
                print(f"Error: {e}")
                
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    get_amazon_products()
    
