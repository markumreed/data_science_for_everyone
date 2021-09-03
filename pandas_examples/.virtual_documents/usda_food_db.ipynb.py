get_ipython().run_line_magic("config", " Completer.use_jedi = True")


import pandas as pd
import numpy as np
import json


#get_ipython().getoutput("head data/usda_food_database.json")


temp = pd.read_json("data/usda_food_database.json")


temp.head()


db = json.load(open("data/usda_food_database.json"))


db[0].keys()


db[0]['nutrients'][0]


nutrients = pd.DataFrame(db[0]['nutrients'])


nutrients.head()


cols = ['description', 'group', 'id', 'manufacturer']


info = pd.DataFrame(db, columns=cols)


info.head()


info['manufacturer'].value_counts()


info.info()


info['group'].value_counts()



