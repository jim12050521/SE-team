#!C:\Users\jim11\anaconda3\python.exe
# -*- coding: utf-8 -*-
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





class CustomerModel:
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
         
    def Browse_product(self):                                                
        try:
            self.cur.execute("SELECT * FROM seller;")  
            result = self.cur.fetchall()

            prds = []                             
            for data in result:
                prds.append(data)
            return prds

        except Exception as e:
            print(f"Error listing products: {e}")            





    def shopping_cart(self):
        try:
            self.cur.execute("SELECT * FROM customer;")  
            result = self.cur.fetchall()

            cart = []                                
            for data in result:
                cart.append(data)
            return cart

        except Exception as e:
            print(f"Error generating cart: {e}")





    def plus_to_cart(self, prdID):
        try:
            self.cur.execute("SELECT * FROM customer;")
            sqlid = self.cur.fetchall()
            DBc_id = [i[0] for i in sqlid]  
            
            if prdID in DBc_id:
                sql = "UPDATE `customer` SET `unit_quantity` = `unit_quantity` + 1 WHERE `c_id` = %s;"
                self.cur.execute(sql, (prdID, ))
                self.conn.commit()
                return True
                
            else:
                sql = "SELECT name, price FROM seller WHERE id = %s"
                self.cur.execute(sql, (prdID, ))
                sqldata = self.cur.fetchone()

                prdN = sqldata[0]
                prdP = sqldata[1]

                sql = "INSERT INTO `customer`(c_id, c_name,  one_price, unit_quantity) VALUES(%s, %s, %s, 1);"
                self.cur.execute(sql, (prdID, prdN, prdP))
                self.conn.commit()
                return True
                
        except Exception as e:
            print(f"Error adding to cart: {e}")
 




    def subtract_from_cart(self, prdID): #modify + and - after
        try:
            sql = "SELECT unit_quantity FROM customer WHERE c_id = %s;"
            self.cur.execute(sql, (prdID, ))
            sqlquantity = self.cur.fetchone()  #fetchone() returns a tuple containing the results, not a list
            DBquantity = sqlquantity[0]
            
            if DBquantity > 1:
                sql = "UPDATE `customer` SET `unit_quantity` = `unit_quantity` - 1 WHERE `c_id` = %s;"
                self.cur.execute(sql, (prdID,))
                self.conn.commit()
                return True
                
            elif DBquantity == 1:
                self.cur.execute("SET SQL_SAFE_UPDATES = 0;")
                sql = "DELETE FROM customer WHERE c_id = %s"
                self.cur.execute(sql, (prdID,))
                self.cur.execute("SET SQL_SAFE_UPDATES = 1;")
                self.conn.commit()
                return True
            
        except Exception as e:
            print(f"Error deleting from cart: {e}")
        




    def settlement(self):
        try:
            self.cur.execute("SELECT `unit_quantity`, `one_price` FROM customer;")
            result = self.cur.fetchall()

            if len(result) < 1:
                return [0, 0]
            
            else:
                '''
                quantity = sum(row[0] for row in result)
                price = sum(row[0] * row[1] for row in result)
                buycar = [quantity, price]
                return buycar
                '''
                quantity = 0
                price = 0
                buycar = []
                
                for row in result:
                    quantity += row[0] 
                    price += (row[0] * row[1])
                buycar.extend([quantity, price])

                return buycar


        except Exception as e:
            print(f"Error fetching settlement: {e}")
            


'''#use for debug
from db import conn, cur
c = CustomerModel(conn, cur)
r = c.shopping_cart()

a = CustomerModel(conn, cur)
r2 = a.subtract_from_cart(1)
print(r2)
'''










'''
            self.cur.execute("SET SQL_SAFE_UPDATES = 0;")
            self.cur.execute("DELETE FROM settlement;")
            self.cur.execute("SET SQL_SAFE_UPDATES = 1;")

            self.cur.execute("SELECT `unit_quantity`, `one_price` FROM customer;")
            result = self.cur.fetchall()

            sql = "INSERT INTO `customer` (quantity, price) VALUES(%s, %s);"   #It won't actually be used here, maybe for inspection.
            values = (quantity, price)
            self.cur.execute(sql, values)
            self.conn.commit()
'''





'''
在 add_to_cart 和 delete_from_cart 方法中，可以使用 ON DUPLICATE KEY UPDATE 來實現一個 SQL 查詢，這樣可以更有效地處理相同商品的添加和刪除。這需要在 customer 表上添加一個唯一索引（Unique Key）。


def add_to_cart(self, prdID):
    try:
        sql = "INSERT INTO `customer` (c_id, c_name, one_price, unit_quantity) VALUES (%s, %s, %s, 1) ON DUPLICATE KEY UPDATE unit_quantity = unit_quantity + 1;"
        self.cur.execute(sql, (prdID, prdN, prdP))
        self.conn.commit()
        return True
    except Exception as e:
        print(f"Error adding to cart: {e}")

def delete_from_cart(self, prdID):
    try:
        sql = "UPDATE `customer` SET `unit_quantity` = `unit_quantity` - 1 WHERE `c_id` = %s AND `unit_quantity` > 1;"
        self.cur.execute(sql, (prdID,))
        self.conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting from cart: {e}")

'''













