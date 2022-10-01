'''
    to register new customer in database
'''

import mysql.connector
import os

#class with logic of registration form of customer
class RegisterCustomer:

    #initialize constructor and send entries to database
    def __init__(self):
        try:
            mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "admin",database = "invoice")
            cursor1 = mydb.cursor()
            print("---------------------welcome to python billing system---------------------\n")
            customerName = input("enter your Full Name\n")
            mobileNumber = input("enter you Mobile Number\n")
            sql = "insert into customer_detail(cname,cmno) values(%s,%s)"
            val = (customerName,mobileNumber)
            cursor1.execute(sql,val)
            mydb.commit()
            
            
        except mysql.connector.Error as e:
            print("database not working......currently working on fix.....")
            print(e)

        #send an sms to number that registration successful
        finally:
            import requests
            url = "https://www.fast2sms.com/dev/bulk"
            querystring = {"authorization":"n0BJ1r8yP2hOapZUmHcNFEgbvAuxeQXiG5Y3CS7MI9qLdjfok4gRtoI36EPh97QXUm0x2L85dkrzVwnf",
                           "sender_id":"FSTSMS",
                           "message":"successfully registered",
                           "language":"english",
                           "route":"p",
                           "numbers":mobileNumber,
                           "flash":"0"
                           '''to display flash message set 1'''}

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
                
            choice = input("want to buy from python billing system(yes/no)\n")
            if choice == "yes" or choice == "Yes":
                from newinvoice import NewInvoice
                new = NewInvoice()
                new.existingCustomer(customerName,mobileNumber)
            else:
                print("Registered Successfully\nThank You for Registering. please enjoy shopping with us!")
                os._exit(0)
            mydb.close()
            
