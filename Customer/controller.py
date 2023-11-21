#!C:\Users\jim11\anaconda3\python.exe
# -*- coding: utf-8 -*-
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from model import CustomerModel
from db import conn, cur
import cgi
import json



 

print("Content-type: application/json\n")

form = cgi.FieldStorage()  
act = form.getvalue('act')

customer_model = CustomerModel(conn, cur)

def browse_products():
    """
    獲取資料庫中(商品)的所有產品, 並返回 JSON 格式的響應
    """
    ###verify
    objects = customer_model.Browse_product()
    return json.dumps(objects)





def show_cart():
    """
    獲取資料庫(購物車)中的所有產品, 並返回 JSON 格式的響應
    """                                
    ###verify
    contents = customer_model.shopping_cart()
    return json.dumps(contents)





def plus_product():
    """
    將一個新的產品添加到購物車中。
    
    """
    prdID = int(form.getvalue('id'))   #Wrap the id in the url
    ###verify
    customer_model.plus_to_cart(prdID)
    return True





def subtract_product():
    """
    將一個新的產品從購物車中減去。
        
    """
    prdID = int(form.getvalue('id'))
    ###verify
    customer_model.subtract_from_cart(prdID)
    return True

 



def close_account():          
    """
    計算購物車中的所有產品的總價格。
    """                      
    ###verify
    lst = customer_model.settlement()
    return json.dumps(lst)





if act == 'browse':
    response = browse_products()
elif act == 'cart':
    response = show_cart()
elif act == 'plus':
    response = plus_product()
elif act == 'subtract':
    response = subtract_product()
elif act == 'settlement':
    response = close_account()
else:
    response = json.dumps({'error': 'Invalid action'})

print(response)















