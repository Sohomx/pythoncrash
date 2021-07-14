# Core Modules
import datetime
from datetime import date
import time
from time import time

# Pip Module
from camelcase import CamelCase

import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))


print(timestamp)