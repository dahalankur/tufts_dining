import datetime
import requests
from bs4 import BeautifulSoup

from tufts_dining.locations import locations

class TuftsDining():
    def __init__(self, location):
        self.location = location
        if location in locations:
            self._locationId = locations[self.location]
        else:
            self.location = None
            self._locationId = None


    # TODO: support querying on the basis of date provided
    """
    Returns the full menu of the dining location as a dictionary
    """
    def menu(self, date=None):
        # check if valid location was provided in the constructor
        if self.location:
            if not date:
                date = datetime.date.today()
            else: 
                pass
                # check the supplied date for errors
        
            # TODO: modify url to accommodate the date parameter
            url = f"http://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum={self._locationId}&locationName={self.location}&naFlag=1"
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            menu_date = None  # TODO: modify this to use the supplied date instead    
            return self.__getResponse(soup)
        else:
            return {"Error" : "Invalid location provided"}
           

    def breakfast(self, date=None):
        if self.location:
            menu = self.menu()
            if "Breakfast" in menu:
                return menu["Breakfast"]
            return {"Error" : "Breakfast not available for the selected location"}
        else:
            return {"Error" : "Invalid location provided"}
    

    def dinner(self, date=None):
        if self.location:
            menu = self.menu()
            if "Dinner" in menu:
                return menu["Dinner"]
            return {"Error" : "Dinner not available for the selected location"}
        else:
            return {"Error" : "Invalid location provided"}
    

    def lunch(self, date=None):
        if self.location:
            menu = self.menu()
            if "Lunch" in menu:
                return menu["Lunch"]
            return {"Error" : "Lunch not available for the selected location"}
        else:
            return {"Error" : "Invalid location provided"}

    
    """
    Private helper method for constructing the response dict
    """
    def __getResponse(self, soup):
        response = dict()
        # menu_date = None
        for div in soup.findAll("div"):
            try:
                curr_div_class = div["class"][0]
                # if not menu_date:
                #     if curr_div_class == "shortmenutitle":
                #         menu_date = "".join(div.text.split(",")[-2:]).strip()
                #         response["date"] = menu_date
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


# carm = TuftsDining("Carmichael Dining Center")
# print(carm.menu()