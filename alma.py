
import numpy as np
import requests
import json
import pandas as pd
import csv

API_HOST = "http://api-cahosted.exlibrisgroup.com/almaws/v1/analytics/reports/?apikey= l8xx36b6d50422ba49c2973064fa3b7a96b0"

request = requests.get(API_HOST)
requesttool = request.json()
