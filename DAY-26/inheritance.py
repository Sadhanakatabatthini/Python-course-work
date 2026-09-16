'''
#single Inheritance
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

sadhana = whatsappv1()
sadhana.message()

usharani = whatsappv2()
usharani.message()
usharani.status()


#Multilevel Inheritance
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3(whatsappv2):
    def calls(self):
        print("You can call")

sadhana = whatsappv1()
sadhana.message()

usharani = whatsappv2()
usharani.message()
usharani.status()

laxmi = whatsappv3()
laxmi.calls()
laxmi.status()
laxmi.message()


# Multiple Inheritance
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2:
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3(whatsappv1,whatsappv2):
    def calls(self):
        print("You can call")

sadhana = whatsappv1()
sadhana.message()

usharani = whatsappv2()
usharani.status()

laxmi = whatsappv3()
laxmi.calls()
laxmi.status()
laxmi.message()


#Hybrid Inheritance 
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2:
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3:
    def calls(self):
        print("You can call")

class whatsappv4:
    def community(self):
        print("You can create multiple groups")

class whatsappv5(whatsappv2,whatsappv4,whatsappv3):
    def channels(self):
        print("You can post with huge crowd")

sadhana = whatsappv1()
sadhana.message()

usharani = whatsappv2()
usharani.status()

laxmi = whatsappv5()
laxmi.calls()
laxmi.status()
laxmi.community()
laxmi.channels()


'''
#Hierarchical Inheritance
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3(whatsappv1):
    def calls(self):
        print("You can call")

class whatsappv4(whatsappv1):
    def community(self):
        print("You can create multiple groups")



sadhana = whatsappv1()
sadhana.message()

usharani = whatsappv2()
usharani.status()
usharani.message()

laxmi = whatsappv4()
laxmi.community()
laxmi.message()