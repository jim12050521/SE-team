#!C:\Users\jim11\anaconda3\python.exe
# -*- coding: utf-8 -*-
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from Model import SellerModel
from db import conn, cur
import cgi
import json





print("Content-type: application/json\n")
# 建立 CGI 基於 FieldStorage 對象, 用於處理 URL 中的查詢字符串和表單數據
form = cgi.FieldStorage()  #FieldStorage object: The cgi.FieldStorage() object can handle both the query string and form data in the URL
# 獲取操作類型
act = form.getvalue('act')

seller_model = SellerModel(conn, cur)

def list_products():
    # 獲取資料庫中的所有產品, 並返回 JSON 格式的響應
    ###verify
    products = seller_model.list_products()
    return json.dumps(products)





import json

def add_product():
    """
    將一個新的產品添加到系統中。

    此函數從表單數據中獲取產品名稱、描述和價格。
    然後調用`seller_model`模塊中的`add_product`函數將產品添加到系統中。
    如果產品成功添加，則返回一個帶有成功消息的JSON響應。
    否則，返回一個帶有錯誤消息的JSON響應。

    返回：
        str：指示添加產品成功或失敗的JSON響應。
    """
    prdN = form.getvalue('prd_name')
    prdD = form.getvalue('prd_description')
    prdP = form.getvalue('prd_price')

    result = seller_model.add_product(prdN, prdD, prdP)
    if result:
        return json.dumps({"message": "產品添加成功"})
    else:
        return json.dumps({"error": "無法添加產品"})




def edit_product():
    """
    編輯現有產品。
    獲取產品ID、產品名稱、產品描述和產品價格。
    然後調用`seller_model`模塊中的`edit_product`函數編輯產品。
    """
    prdID = form.getvalue('prd_id')
    prdN = form.getvalue('prd_name')
    prdD = form.getvalue('prd_description')
    prdP = form.getvalue('prd_price')
    ###verify
    seller_model.edit_product(prdID, prdN, prdD, prdP)
    return True





def delete_product():
    """
    從系統中刪除產品。
    獲取要刪除的產品的ID。
    然後調用`seller_model`模塊中的`delete_product`函數刪除產品。
    """              
    product_id = form.getvalue('id')
    ###verify
    seller_model.delete_product(product_id)
    return True





if act == 'list':
    response = list_products()
elif act == 'add':
    response = add_product()
elif act == 'edit':
    response = edit_product()
elif act == 'delete':
    response = delete_product()
else:
    response = json.dumps({'error': 'Invalid action'})

print(response)















'''
class ProductController:
    def __init__(self):
        # 初始化 ProductModel
        self.product_model = ProductModel(conn, cur)

    def list_products(self):
        products = self.product_model.list_products()
        return json.dumps(products)

    def add_product(self, prdN, prdD, prdP):
        result = self.product_model.add_product(prdN, prdD, prdP)
        return json.dumps(result)

    def edit_product(self, prdID, prdN, prdD, prdP):
        result = self.product_model.edit_product(prdID, prdN, prdD, prdP)
        return json.dumps(result)

    def delete_product(self, product_id):
        result = self.product_model.delete_product(product_id)
        return json.dumps(result)

if __name__ == '__main__':
    # 設定 Content-type 為 JSON
    print("Content-type: application/json\n")

    # 創建 CGI 基於 FieldStorage 對象
    form = cgi.FieldStorage()

    # 實例化 ProductController
    product_controller = ProductController()

    # 從 CGI 參數中獲取操作類型
    act = form.getvalue('act')

    # 根據不同的操作類型調用相應的方法
    if act == 'list_products':
        response = product_controller.list_products()
    elif act == 'add_product':
        prdN = form.getvalue('prdN')
        prdD = form.getvalue('prdD')
        prdP = form.getvalue('prdP')
        response = product_controller.add_product(prdN, prdD, prdP)
    elif act == 'edit_product':
        prdID = form.getvalue('prdID')
        prdN = form.getvalue('prdN')
        prdD = form.getvalue('prdD')
        prdP = form.getvalue('prdP')
        response = product_controller.edit_product(prdID, prdN, prdD, prdP)
    elif act == 'delete_product':
        product_id = form.getvalue('product_id')
        response = product_controller.delete_product(product_id)
    else:
        response = json.dumps({'error': 'Invalid action'})

    # 返回 JSON 響應
    print(response)
'''

