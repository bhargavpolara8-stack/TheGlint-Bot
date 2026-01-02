import requests
from bs4 import BeautifulSoup

# તમારી વેબસાઈટની લિંક
WEB_URL = "http://theglint.rf.gd/add_product.php"

def add_to_website(title, price, img, link):
    data = {
        "title": title,
        "price": price,
        "image_url": img,
        "affiliate_link": link
    }
    r = requests.post(WEB_URL, data=data)
    return r.text

# અત્યારે આપણે ટેસ્ટિંગ માટે એક સેમ્પલ ડેટા મોકલીએ છીએ
# પછી તમે Amazon ની લિંક માંથી સ્ક્રૅપિંગ કરી શકશો
success = add_to_website(
    "Traditional Gold Plated Jhumka", 
    "₹399", 
    "https://m.media-amazon.com/images/I/719n9mKID6L._AC_UY1100_.jpg", 
    "https://www.amazon.in/"
)

print(f"Status: {success}")
