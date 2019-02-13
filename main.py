''' this is python main class which ask user
to input wether to generate old or new invoice
based on which we check if it is an existing user or not through his mobile
number which is linked to database'''

class main1:
    ch = 0
    #contructor initialization
    def __init__(self):
        #ask if customer is existing or not
        print("--------------welcome to python billing system--------------")
        ch = input("are u a existing customer(yes/no)\n")
        if ch == 'yes' or ch == 'Yes':
        #redirects to newinvoice class/package
            from newinvoice import NewInvoice
            NewInvoice()
        else:
            #register new customer
            from registerCustomer import RegisterCustomer
            RegisterCustomer()

obj = main1()


