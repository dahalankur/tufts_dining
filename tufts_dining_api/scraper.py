import os
import sys
import datetime, json
import requests
from bs4 import BeautifulSoup

from tufts_dining_api.locations import locations


def main():  
    # TODO: add a lookup by date functionality
    location = 'Kindlevan Cafe'
    url = f"http://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum={locations[location]}&locationName={location}&naFlag=1"
    website = requests.get(url)
    soup = BeautifulSoup(website.text, 'html.parser')

    div_list = soup.findAll("div")
    menu_date = None

    for div in div_list:
        try:
            curr_div_class = div["class"][0]
            if not menu_date:
                if curr_div_class == "shortmenutitle":
                    menu_date = "".join(div.text.split(",")[-2:]).strip()

            menu_type = div.text if curr_div_class == "shortmenumeals" else None
            category = div.text if curr_div_class == "shortmenucats" else None
            food_item = div.text if curr_div_class == "shortmenurecipes" else None
            if menu_type:
                print(f"xxxxxxxxxxxxxxxxx{menu_type}xxxxxxxxxxxxxxxxx")
            if category:
                print(f"---------{category}---------")
            if food_item:
                print(food_item)
        except:
            continue

    print(menu_date)



if __name__ == "__main__":
    main()