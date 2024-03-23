from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():  
        # BeautifulSoup Object     
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs=("class", "wikitable"))
    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        print(table_cols)
        
        temp_list=[]
        for col_data in table_cols:
            print(col_data.text)

            data = col_data.text.strip()
            print(data)

            temp_list.append(data)
        scraped_data.append(temp_list)


        
    

# Calling Method    
scrape()

star_data=[]

for i in range(0, len(scraped_data)):
    Star_name = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Luminosity = scraped_data[i][7]

    required_data = [Star_name, Distance, Mass, Radius, Luminosity]
    star_data.append(required_data)

# Define Header
headers = ["Star_name", "Distance", "Mass", "Radius", "Luminosity"]

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(star_data, columns=headers)

# Convert to CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")