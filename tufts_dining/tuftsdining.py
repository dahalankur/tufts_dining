"""
tuftsdining.py
Author: Ankur Dahal
Date:   01-29-2021
A python package that exports the TuftsDining class, used to retrieve Tufts Dining menus.
"""
import re
import datetime
import requests
from bs4 import BeautifulSoup

from constants import *


class TuftsDining():
    """
    __init__
    initialize the instance, set location id if valid location is provided
    """
    def __init__(self, location):
        self.location = location
        self.locations = [location for location, id in LOCATIONS.items()]
        if location in LOCATIONS:
            self._locationId = LOCATIONS[self.location]
        else:
            self.location = None
            self._locationId = None



    """
    menu
    does   :  returns the full menu of the dining location this method is called on
    params :  date (optional) - the required date in "MM-DD-YYYY" format
    returns:  the menu for the provided date as a dictionary
    notes  :  may return a dictionary with a single key, "Error" in cases where
              the supplied date is in the wrong format, or when the 
              object was initialized with an incorrect location
    """
    def menu(self, date=None):
        if self.location:
            # set date = Today if no parameters were supplied
            if not date:
                date = datetime.date.today().strftime('%m-%d-%Y')
            else: 
                if not self._isValidDate(date):
                    return INVALID_DATE
            
            # extract the day, month and year from the date
            month, day, year = date.split("-")

            # construct the url
            url = f"http://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&"
            url += f"locationNum={self._locationId}&locationName={self.location}&naFlag=1"
            url += f"&WeeksMenus=This+Week%27s+Menus&myaction=read&dtdate={month}%2f{day}%2f{year}"
            
            # scrape the website and return the result
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            return self._getResponse(soup)
        else:
            return INVALID_LOCATION
           


    """
    breakfast
    does   :  returns the breakfast menu of the dining location this method is called on
    params :  date (optional) - the required date in "MM-DD-YYYY" format
    returns:  the breakfast menu for the provided date as a dictionary
    notes  :  may return a dictionary with a single key, "Error" in cases where
              the supplied date is in the wrong format, when the 
              object was initialized with an incorrect location, or if there 
              exists no breakfast menu for the location provided
    """
    def breakfast(self, date=None):
        if self.location:
            if not date:
                menu = self.menu()
            else:
                if self._isValidDate(date):
                    menu = self.menu(date)
                else:
                    return INVALID_DATE
            if "Breakfast" in menu:
                return menu["Breakfast"]
            return BREAKFAST_NOT_AVAILABLE
        else:
            return INVALID_LOCATION
    


    """
    dinner
    does   :  returns the dinner menu of the dining location this method is called on
    params :  date (optional) - the required date in "MM-DD-YYYY" format
    returns:  the dinner menu for the provided date as a dictionary
    notes  :  may return a dictionary with a single key, "Error" in cases where
              the supplied date is in the wrong format, when the 
              object was initialized with an incorrect location, or if there 
              exists no dinner menu for the location provided
    """
    def dinner(self, date=None):
        if self.location:
            if not date:
                menu = self.menu()
            else:
                if self._isValidDate(date):
                    menu = self.menu(date)
                else:
                    return INVALID_DATE
            if "Dinner" in menu:
                return menu["Dinner"]
            return DINNER_NOT_AVAILABLE
        else:
            return INVALID_LOCATION
    


    """
    lunch
    does   :  returns the lunch menu of the dining location this method is called on
    params :  date (optional) - the required date in "MM-DD-YYYY" format
    returns:  the lunch menu for the provided date as a dictionary
    notes  :  may return a dictionary with a single key, "Error" in cases where
              the supplied date is in the wrong format, when the 
              object was initialized with an incorrect location, or if there 
              exists no lunch menu for the location provided
    """
    def lunch(self, date=None):
        if self.location:
            if not date:
                menu = self.menu()
            else:
                if self._isValidDate(date):
                    menu = self.menu(date)
                else:
                    return INVALID_DATE
            if "Lunch" in menu:
                return menu["Lunch"]
            return LUNCH_NOT_AVAILABLE
        else:
            return INVALID_LOCATION



    """
    brunch
    does   :  returns the brunch menu of the dining location this method is called on
    params :  date (optional) - the required date in "MM-DD-YYYY" format
    returns:  the brunch menu for the provided date as a dictionary
    notes  :  may return a dictionary with a single key, "Error" in cases where
              the supplied date is in the wrong format, when the 
              object was initialized with an incorrect location, or if there 
              exists no brunch menu for the location provided
    """
    def brunch(self, date=None):
        if self.location:
            if not date:
                menu = self.menu()
            else:
                if self._isValidDate(date):
                    menu = self.menu(date)
                else:
                    return INVALID_DATE
            if "Brunch" in menu:
                return menu["Brunch"]
            return BRUNCH_NOT_AVAILABLE
        else:
            return INVALID_LOCATION
    

    """
    _getResponse
    Helper method for constructing the response dict
    """
    def _getResponse(self, soup):
        response = dict()

        for div in soup.findAll("div"):
            try:
                curr_div_class = div["class"][0]

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
            except:
                continue
        return response


    """
    _isValidDate
    Checks if the supplied date is in mm-dd-yyyy format
    """
    def _isValidDate(self, date):
        rexp = "^((0[1-9])|(1[0-2]))-(0[1-9]|[1-2][0-9]|3[0-1])-20[0-2][0-9]$"
        return True if re.search(rexp, date) else False
