# Tufts Dining
[![PyPI](https://img.shields.io/badge/tufts--dining-v%200.1.0-green)](https://pypi.org/project/tufts-dining/)
![PyPI - Python Version](https://img.shields.io/badge/python-3.6-orange)


A Python package for retrieving dining menu data for Tufts University Dining.

### Installation
Install `tufts_dining` using pip (or pip3)
```bash
pip install tufts_dining
```

### Usage
This package exports the `TuftsDining` class, so the way to use it now is to instantiate a `TuftsDining` object
```python
from tufts_dining import TuftsDining
carm = TuftsDining("Carmichael Dining Center")
```
#### Note: importing the package as `tufts-dining` will not work, make sure to use `tufts_dining` while importing the class.

To view a list of available dining locations, you can view the `locations` attribute of the previously instantiated `TuftsDining` object
```bash
$ carm.locations
['Carmichael Dining Center', 'Dewick Dining Center', 'The Commons Marketplace', 'Hodgdon Food On-the-Run', 'Pax et Lox Glatt Kosher Deli', 'Kindlevan Cafe']
```
#### Note: The locations supplied to the constructor are case-sensitive

After an object of `TuftsDining` has been instantiated, you can use a number of methods to extract dining menu data. The following methods are available:
```python
# get the entire menu
full_menu = carm.menu()

# get the breakfast, lunch, brunch and dinner menu
carm_breakfast = carm.breakfast()
carm_brunch = carm.brunch()
carm_lunch = carm.lunch()
carm_dinner = carm.dinner()
```

If no arguments are passed to the aforementioned methods, the date is set to "Today" by default. If you want to extract the menu for a different date, you can pass it to the respective methods as a string in `MM-DD-YYYY` format
```python
hodge = TuftsDining("Hodgdon Food On-the-Run")

# get the menu for 23rd February, 2021
hodge_menu = hodge.menu("02-23-2021")

```

### Changelog
#### 0.1.0 - 01/29/2021
Initial release, version 0.1.0.
