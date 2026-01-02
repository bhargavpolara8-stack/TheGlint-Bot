import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# તમારી સાઇટની સાચી લિંક
URL = "http://theglint.rf.gd/add_product.php"
AMAZON_URL = "https://www.amazon.in/s?k=jewelry"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_amazon_products():
    print("Searching for products on Amazon...")
    try:
        page = requests.get(AMAZON_URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        
        # Amazon માંથી 5 પ્રોડક્ટ્સ લેવા માટે
        products = soup.find_all("div", {"data-component-type": "s-search-result"}, limit=5)
        
        if not products:
            print("No products found. Amazon might be blocking the request.")
            return

        for product in products:
            try:
                # વિગતો કાઢવી
                title = product.h2.text.strip()[:60]
                price_tag = product.find("span", "a-price-whole")
                price = "Rs. " + price_tag.text if price_tag else "Check Price"
                img = product.find("img", "s-image")['src']
                link = "https://www.amazon.in" + product.h2.a['href']
                
                # ડેટાને લિંક (URL) માં સુરક્ષિત રીતે પેક કરવો
                final_url = f"{URL}?title={quote(title)}&price={quote(price)}&image_url={quote(img)}&affiliate_link={quote(link)}"
                
                # તમારી વેબસાઇટ પર ડેટા મોકલવો
                res = requests.get(final_url)
                print(f"Sent: {title[:20]}... | Result: {res.text}")
                
            except Exception as e:
                print(f"Inner Error: {e}")
                
    except Exception as e:
        print(f"Outer Error: {e}")

if __name__ == "__main__":
    get_amazon_products()
    
