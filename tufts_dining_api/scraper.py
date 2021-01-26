import datetime
import requests
from bs4 import BeautifulSoup

from locations import locations

class Dining():
    def __init__(self):
        self.location = None
        self.locationId = None
        self.date = None


    # TODO: support querying on the basis of date provided
    """
    Returns the menu of the provided dining location
    """
    def getMenu(self, location, date=None):
        if location not in locations:
            print("Invalid dining location provided. Please provide a valid location.")
        else:
            if date:
                self.date = date # TODO: error checking here
            else: 
                self.date = datetime.date.today() 
            self.location = location
            self.locationId = locations[self.location]

            # TODO: modify url to accommodate the date parameter
            url = f"http://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum={self.locationId}&locationName={self.location}&naFlag=1"
            website = requests.get(url)
            soup = BeautifulSoup(website.text, 'html.parser')

            div_list = soup.findAll("div")
            menu_date = None
            
            response = {}

            for div in div_list:
                try:
                    curr_div_class = div["class"][0]
                    if not menu_date:
                        if curr_div_class == "shortmenutitle":
                            menu_date = "".join(div.text.split(",")[-2:]).strip()
                            response["date"] = menu_date
                    if curr_div_class == "shortmenumeals":
                        menu_type = div.text.strip()
                        if menu_type not in response:
                            response[menu_type] = []
                    elif curr_div_class == "shortmenucats":
                        category = div.text.strip()
                        category_dict = {category : []}
                        response[menu_type].append(category_dict)
                    elif curr_div_class == "shortmenurecipes":
                        food_item = div.text.strip()
                        category_dict[category].append(food_item)
                    # TODO: account for duplicate categories and food_items
                except:
                    continue
    
        return response

tufts_dining = Dining()
res = tufts_dining.getMenu("Kindlevan Cafe")
print(res)
