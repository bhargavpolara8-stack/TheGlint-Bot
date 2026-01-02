import requests

# ધ્યાન રાખજો: http જ રાખવું, https નહીં
URL = "http://theglint.rf.gd/add_product.php"

# પ્રોડક્ટનો ડેટા
data = {
    "title": "Gold Plated Necklace",
    "price": "₹499",
    "image_url": "https://m.media-amazon.com/images/I/719n9mKID6L._AC_UY1100_.jpg",
    "affiliate_link": "https://www.amazon.in/"
}

# verify=False અને headers ઉમેરવાથી SSL વગર પણ ડેટા જશે
try:
    response = requests.post(URL, data=data, timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
except Exception as e:
    print(f"Error: {e}")
