#class introduction
#include all modules
''' this class extracts data from database bases on existing user mobile number. new items are being added
to bill of existing customer'''

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import random
import os

#class invoice which contain billing system for existing customer and creation of new customer
class NewInvoice:
    itemCode = ""
    quantity = 0
    unitPrice = list()

    #costructor which inputs existing customer number and directs to newBill method
    def __init__(self):
            number = int(input("enter mobile number\n"))
            self.newBill(number)
            

    #this method defines input of items for new bill for a existing customer and new registered customers
    def existingCustomer(self,name,number):
        try:
            mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "admin",database = "invoice")
            cursor2= mydb.cursor()
            sales_refno = list()
            r = random.randint(1,100)
            cursor2.execute("select sales_refno from sales_desc")
            check = cursor2.fetchall()
            for i in check:
                checklist = i
                if r not in sales_refno or r not in checklist:
                    sales_refno.append(r)
                    sales = r
                    break
            print("\n............WELCOME " + name + "............\n")
            print("what do you want to buy? Here are some options for you :- \n")
            while True:
                ch = int(input("1. parleg" + "\n2. milk-bikis" + "\n3. ponds face cream 20g" + "\n4. dettol hand wash" + "\n5. levis jeans 38-40" + "\n6. octave set of 3 t-shirts(red blue green)\n" + "7. generate bill\n"))
                if ch == 1:
                    quantity = int(input("enter you required quantity\n"))
                    itemCode = "b01"
                    cursor2.execute("select unit_price from item_desc where icode = '" + itemCode + "'")
                    unitPrice = cursor2.fetchone()
                    total_price = int(unitPrice[0])*quantity
                    sql = "INSERT INTO sales_desc values(%s,%s,%s,%s)"
                    val = (str(sales),itemCode,str(quantity),str(total_price))
                    cursor2.execute(sql,val)
                    mydb.commit()
                    del unitPrice
                elif ch == 2:
                    quantity = int(input("enter you required quantity\n"))
                    itemCode = "b02"
                    cursor2.execute("select unit_price from item_desc where icode = '" + itemCode + "'")
                    unitPrice = cursor2.fetchone()
                    total_price = int(unitPrice[0])*quantity
                    sql = "INSERT INTO sales_desc values(%s,%s,%s,%s)"
                    val = (str(sales),itemCode,str(quantity),str(total_price))
                    cursor2.execute(sql,val)
                    mydb.commit()
                    del unitPrice
                elif ch == 3:
                    quantity = int(input("enter you required quantity\n"))
                    itemCode = "cr01"
                    cursor2.execute("select unit_price from item_desc where icode = '" + itemCode + "'")
                    unitPrice = cursor2.fetchone()
                    total_price = int(unitPrice[0])*quantity
                    sql = "INSERT INTO sales_desc values(%s,%s,%s,%s)"
                    val = (str(sales),itemCode,str(quantity),str(total_price))
                    cursor2.execute(sql,val)
                    mydb.commit()
                    del unitPrice
                elif ch == 4:
                    quantity = int(input("enter you required quantity\n"))
                    itemCode = "hw01"
                    cursor2.execute("select unit_price from item_desc where icode = '" + itemCode + "'")
                    unitPrice = cursor2.fetchone()
                    total_price = int(unitPrice[0])*quantity
                    sql = "INSERT INTO sales_desc values(%s,%s,%s,%s)"
                    val = (str(sales),itemCode,str(quantity),str(total_price))
                    cursor2.execute(sql,val)
                    mydb.commit()
                    del unitPrice
                elif ch == 5:
                    quantity = int(input("enter you required quantity\n"))
                    itemCode = "j01"
                    cursor2.execute("select unit_price from item_desc where icode = '" + itemCode + "'")
                    unitPrice = cursor2.fetchone()
                    total_price = int(unitPrice[0])*quantity
                    sql = "INSERT INTO sales_desc values(%s,%s,%s,%s)"
                    val = (str(sales),itemCode,str(quantity),str(total_price))
                    cursor2.execute(sql,val)
                    mydb.commit()
                    del unitPrice
                elif ch == 6:
                    quantity = int(input("enter you required quantity\n"))
                    itemCode = "ts01"
                    cursor2.execute("select unit_price from item_desc where icode = '" + itemCode + "'")
                    unitPrice = cursor2.fetchone()
                    total_price = int(unitPrice[0])*quantity
                    sql = "INSERT INTO sales_desc values(%s,%s,%s,%s)"
                    val = (str(sales),itemCode,str(quantity),str(total_price))
                    cursor2.execute(sql,val)
                    mydb.commit()
                    del unitPrice
                #generate bill or add more items to bill
                elif ch == 7:
                    ch = input("want to add items to bill again(yes/no)")
                    if ch == 'yes' or ch == 'Yes':
                        self.existingCustomer(name)
                    else:
                        ch1 = input("want to generate bill(yes/no)")
                        if ch1 == 'yes' or ch1 == 'Yes':
                            from invoice import generatePDF
                            gen = generatePDF()
                            gen.genPD(sales,number)
                            break
                        else:
                            print("exitting..............")
                            sys.exit()
                else:
                    print("wrong choice input.........")
                    ch = input("want to add items to bill again(yes/no)")
                    if ch == 'yes' or ch == 'Yes':
                        self.existingCustomer(name)
                        
                    else:
                            print("exitting..............")
                            os._exit(0)
                
            
        except mysql.connector.Error as e:
            print("database not working......currently working on fix.....")
            print(e)

        finally:
            mydb.close()



    #check for existing customer in database
    def newBill(self,number):
        try:
            mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "admin",database = "invoice")
            cursor1 = mydb.cursor()
            sql = "select cmno,cname from customer_detail where cmno=" + "'" +  str(number) + "'"
            cursor1.execute(sql)
            res = cursor1.fetchone()
            if str(number) == res[0]:
                self.existingCustomer(res[1],number)
            else:
                print("number not found")
        except mysql.connector.Error as e:
            print("database not working......currently working on fix.....")
            print(e)
        except TypeError as e:
            print(e)

        finally:
            mydb.close()


