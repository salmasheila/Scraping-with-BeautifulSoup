import requests
from bs4 import BeautifulSoup
import pandas as pd

result = requests.get("https://www.bhinneka.com/jual?cari=iphone")
# print(result.status_code)
# print(result.headers)

src = result.content
# print(src)

soup = BeautifulSoup(src, 'html.parser')
# print (type(soup))

products = soup.find_all("div", "o_wsale_product_grid_wrapper position-relative h-100")
# print(products)

product_name = []
price = []

for product in products :
    nama = product.find('a', 'text-primary text-decoration-none').get_text().encode("utf-8")
    harga = product.find('span','oe_currency_value').get_text().replace("Rp", "").replace(".", "").replace(" ", "").encode("utf-8")
    product_name.append(nama)
    price.append(harga)

product_dict = {
    'nama' : product_name,
    'harga' : price
}
df = pd.DataFrame(product_dict, columns=['nama', 'harga'])
df.sort_values('harga', ascending=True)
print(df)
# df.to_csv('bhinneka.csv', sep = ',')