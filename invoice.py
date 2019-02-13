from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice
import random
import mysql.connector
import os
''' to generate pdf from data extraction from database'''

class generatePDF:

    #this method generate pdf from data from database    
    def genPD(self,sales_refno,number):
        amount = 0
        try:
            doc = SimpleInvoice('invoice2.pdf')

            # Paid stamp, optional
            doc.is_paid = True
            mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "admin",database = "invoice")
            cursor2= mydb.cursor()
            invoice_refno = list()
            r = random.randint(100,1000)
            cursor2.execute("select invoice_refno from bill_info")
            check = cursor2.fetchall()
            for i in check:
                checklist = i
                if r not in invoice_refno or r not in checklist:
                    invoice_refno.append(r)
                    break
            invoiceNumber = r
            doc.invoice_info = InvoiceInfo(invoiceNumber, datetime.now(), datetime.now())  # Invoice info, optional

            # Service Provider Info, optional
            doc.service_provider_info = ServiceProviderInfo(
                name='Python shop',
                street='23, Bakers Street, Dehradun',
                city='Dehradun',
                state='Uttarakhand',
                country='India',
                post_code='248009',
                #vat_tax_number='Vat/Tax number'
            )

            # Client info, optional
            doc.client_info = ClientInfo(email='python_billingSystem@gmail.com')
            cursor2.execute("select * from sales_desc where sales_refno = "+ str(sales_refno))
            details = cursor2.fetchall()
            #add items in pdf
            for iterate in details:
                if iterate[1] == "b01":
                    name = "parle-g"
                    desc = "glucose biscuit 50g"
                    doc.add_item(Item(name,desc,iterate[2],str(iterate[3]/iterate[2])))
                    amount += int(iterate[3])
                    
                elif iterate[1] == "b02":
                    name = "milk-bikis"
                    desc = "glucose biscuit 50g"
                    doc.add_item(Item(name,desc,iterate[2],str(iterate[3]/iterate[2])))
                    amount += int(iterate[3])
                    
                elif iterate[1] == "cr01":
                    name = "ponds face cream"
                    desc = "face cream 100g"
                    doc.add_item(Item(name,desc,iterate[2],str(iterate[3]/iterate[2])))
                    amount += int(iterate[3])
                        
                elif iterate[1] == "hw01":
                    name = "dettol hand wash"
                    desc = "anti-bacterial hand wash"
                    doc.add_item(Item(name,desc,iterate[2],str(iterate[3]/iterate[2])))
                    amount += int(iterate[3])
                        
                elif iterate[1] == "j01":
                    name = "levis jeans"
                    desc = "levis jeans indigo colour waist:- 38 height:- 40"
                    doc.add_item(Item(name,desc,iterate[2],str(iterate[3]/iterate[2])))
                    amount += int(iterate[3])
                        
                elif iterate[1] == "ts01":
                    name = "octave tshirts"
                    desc = "pack of 3 tshirts(red/green/blue)"
                    doc.add_item(Item(name,desc,iterate[2],str(iterate[3]/iterate[2])))
                    amount += int(iterate[3])
                        
                else:
                    print("item will be added to database soon......")

                    
            # Tax rate, optional
            doc.set_item_tax_rate(5.25)  # 5.25%
            total_amount = (amount*(5.25/100)) + amount
            print(total_amount)

            #store bill info in database
            cursor2.execute("select cid from customer_detail where cmno = " + str(number))
            getCustomerId = cursor2.fetchone()
            sql = "insert into bill_info(sales_refno,total_amount,cid,date,invoice_refno) values(%s,%s,%s,%s,%s)"
            val = (sales_refno,total_amount,getCustomerId[0],str(datetime.now()),invoiceNumber)
            cursor2.execute(sql,val)
            mydb.commit()

            #Transactions detail, optional
            doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
            doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

            # Optional
            doc.set_bottom_tip("Email: help_pythonBilling@hotmail.com<br />Feel Free to contact us for any queries.")



        except mysql.connector.Error as e:
            print("database not working......currently working on fix.....")
            print(e)
#to display flash message set 1
        finally:
            
            import requests
            url = "https://www.fast2sms.com/dev/bulk"
            querystring = {"authorization":"n0BJ1r8yP2hOapZUmHcNFEgbvAuxeQXiG5Y3CS7MI9qLdjfok4gRtoI36EPh97QXUm0x2L85dkrzVwnf",
                           "sender_id":"FSTSMS",
                           "message":"Bill Generated!",
                           "language":"english",
                           "route":"p",
                           "numbers":number,
                           "flash":"1"
                           }

            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            doc.finish()
            mydb.close()
            os._exit(0)



