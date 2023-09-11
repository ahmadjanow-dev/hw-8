import requests
from bs4 import BeautifulSoup
import os
import time
import sqlite3
import random

def parssing_supak_laptops():
    n = 0
    connection = sqlite3.connect('laptop.db')
    cursor = connection.cursor()

    for page in range(1, 9):
        url = f'https://www.sulpak.kg/f/noutbuki?page={page}'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')

        laptops_name = soup.find_all('div', class_='product__item-name')
        laptops_price = soup.find_all('div', class_='product__item-price')

        cursor.execute(f"""CREATE TABLE IF NOT EXISTS page{page} (
            id INTEGER ,
            name VARCHAR(100),
            price VARCHAR(100)
        );""")

        for name, price in zip(laptops_name, laptops_price):
            n += 1
            current_price = "".join(price.text.split())
            rand_ints = random.randint(111111, 9999999999)
            cursor.execute(f"""INSERT INTO page{page}(id,name,price) VALUES ({rand_ints},'{name.text}','{current_price}')""")
            connection.commit()

    connection.close()

parssing_supak_laptops()
