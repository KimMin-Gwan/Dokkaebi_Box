from typing import Any
from flask import Flask, request
import numpy as np
from pymongo import MongoClient# pymongo 임포트
from PIL import Image





client=MongoClient('mongodb+srv://sunjuwhan:ans693200@sunjuwhan.soaegl1.mongodb.net/')
db=client['IOT']
collection=db['image']

#db=client['test_sun']
#collection=db['test']



query={'date':20231029,'category':'지갑'}
data={'date':20221023,'category':'에어팟'}
collection.insert_one(data)
result=collection.find(query)

list_result=[]
for doc in result:
    list_result.append(doc)
    
for i in range(len(list_result)):
    print(list_result[i])