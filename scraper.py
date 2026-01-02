import requests
from bs4 import BeautifulSoup

URL = "http://theglint.rf.gd/add_product.php"

# Amazon પર જ્વેલરી શોધવા માટેની લિંક
AMAZON_URL = "https://www.amazon.in/s?k=jewelry"

# Amazon ને એવું લાગવું જોઈએ કે કોઈ માણસ બ્રાઉઝર ખોલી રહ્યો છે
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

def get_amazon_products():
    page = requests.get(AMAZON_URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # બધી પ્રોડક્ટ્સ શોધવી
    products = soup.find_all("div", {"data-component-type": "s-search-result"}, limit=5)
    
    for product in products:
        try:
            title = product.h2.text.strip()
            # કિંમત શોધવી
            price_tag = product.find("span", "a-price-whole")
            price = "₹" + price_tag.text if price_tag else "N/A"
            
            # ફોટો શોધવો
            img = product.find("img", "s-image")['src']
            
            # લિંક બનાવવી (તમારો Affiliate ID અહીં ઉમેરી શકો છો)
            link = "https://www.amazon.in" + product.h2.a['href']
            
            # તમારી વેબસાઈટ પર મોકલવું
            payload = {
                "title": title[:50] + "...", # નામ ટૂંકું રાખવા
                "price": price,
                "image_url": img,
                "affiliate_link": link
            }
            
            res = requests.post(URL, data=payload)
            print(f"Sent: {title[:20]} | Status: {res.text}")
            
        except Exception as e:
            print(f"Error scraping a product: {e}")

# બોટ ચલાવો
get_amazon_products()
