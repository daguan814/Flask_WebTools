"""
@author shuijing
@date 2023-10-20 16:47
@version 1.0 
@description 
"""

import requests

res = requests.get('http://127.0.0.1:9000/learn/rep', data={'name': '12412', 'age': '14'})
print(res.text)
