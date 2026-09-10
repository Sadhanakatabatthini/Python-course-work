class Flipkart:
    discount = 30

    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print("Updated Discount: ", cls.discount)
    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the flipkart',self.name)

    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% discount is going, grab the product...........")

lohitha = Flipkart()
lohitha.info('lohitha',965234567,'Hyd')
lohitha.updatediscount()
lohitha.banner()

sadhana = Flipkart()
sadhana.info('lohitha',965234567,'Hyd')
sadhana.updatediscount()
sadhana.banner()

vishnu = Flipkart()
vishnu.info('lohitha',965234567,'Hyd')
vishnu.updatediscount()
vishnu.banner()
