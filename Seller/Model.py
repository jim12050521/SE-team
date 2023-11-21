#!C:\Users\jim11\anaconda3\python.exe
# -*- coding: utf-8 -*-
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




class SellerModel:
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
        
    def list_products(self):                                                # change json in controller
        try:
            self.cur.execute("SELECT * FROM seller;")   #When you execute a SQL query using the execute function, the results are stored in the cursor object
            result = self.cur.fetchall()

            prds = []                                #direct return products?
            for data in result:
                prds.append(data)
            return prds

        except Exception as e:
            print(f"Error listing products: {e}")            





    def add_product(self, prdN, prdD, prdP):
        try:
            '''
            DBnames = []  # [row[0] for row in self.cur.fetchall()]
            for row in self.cur.fetchall(): # Assume that the query results are as follows: [(name1, ...), (name2, ...), ...]
                DBnames.append(row[0])
            '''
            self.cur.execute("SELECT name FROM seller;")
            sqlname = self.cur.fetchall()
            DBnames = [n[0] for n in sqlname]  #In the results returned by fetchall(), each row is a tuple, and the elements of the tuple correspond to the columns in the query results.
            
            if prdN in DBnames:
                return f'the prduction {prdN} already exists!'
            else:
                sql = "INSERT INTO `seller`(name,  description, price) VALUES(%s, %s, %s);"
                self.cur.execute(sql, (prdN, prdD, prdP))
                self.conn.commit()
                return True
                
        except Exception as e:
            print(f"Error adding product: {e}")
            self.conn.rollback()
            return False





    def edit_product(self, prdID, prdN, prdD, prdP):
        try:
            sql = "UPDATE `seller` SET `name` = %s, `description` = %s, `price` = %s  WHERE `id` = %s;"
            self.cur.execute(sql, (prdN, prdD, prdP, prdID))
            self.conn.commit()
            return True
            
        except Exception as e:
            print(f"Error editing product: {e}")
            self.conn.rollback()
            return False





    def delete_product(self, product_id):
        try:
            sql = "DELETE FROM `seller` WHERE `id` = %s;"
            self.cur.execute(sql, (product_id,))
            self.conn.commit()
            return True

        except Exception as e:
            print(f"Error deleting product: {e}")
            self.conn.rollback()
            return False






















'''
題目: 以MVC架構開發簡易線上購物網站
商家角色:假設只有一個商家
view要用ajax跟vue寫，controller是後台程式

mode名稱是production大致分為method跟DB兩組成。資料庫名為seller，primary key是商品id
，此外的column是name、description、price。

1. 需要增加(add)/修改(edit)/刪除商品(delete)/列出(list)，這四項是method，用sql從資
料庫讀取修改。
2. list moethod要從資料庫抓產品資料放進array在打包成json回傳給請求者(controller)。
3. add method接收一包傳遞過來的json在判斷true or flase，然後在改動資料庫，最後把更新
資料回傳給controller。
4. delete method接收前端藉由controller傳遞過來的id(商品在DB裡的id)，然後在改動資料
庫，最後把更新資料回傳給controller。
5. edit method也是從view.js接收一個修改的表單，應該是js裡的dataform，在由controller
傳遞指令model，model接收後再做修改，結果回傳給controller。

根據以上資料，請給我model的模板。用python跟sql寫。注意，sql程式碼一部分是融入到python
裡(edit、delete、list、add功能)，另一部分是創建資料庫等資訊的程式碼(seller，primary 
key是商品id，此外的column是name、description、price)這個初期創建table我會直接到
mysql中去執行，然後假設我有一個py腳本db.py已經連接資料庫了，所以只要在新的腳本引入
from db import conn, cur就可使用。
'''

