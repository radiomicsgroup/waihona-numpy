---
title: waihonanumpy
date: February 4, 2022
---

## Install

Run

```bash
pip install waihonanumpy
```  
## Use

```python
from waihonanumpy import RedisStorage
import numpy as np
# setup connection to redis database
redis = RedisStorage(host='172.27.0.75', password='password123')
# store a numpy array 
redis["p1","r1"] = np.arange(21).reshape(3, 7)
redis["p1","r2"] = np.arange(21).reshape(21, 1)
# if the result is an only value return a tuple (key,value)
a_prime_key, a_prime_value = redis["p1","r1"] 
# get a list of tuples (key,value)
list_items = redis["p1","*"]
```