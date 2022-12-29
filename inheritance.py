class product:
    def __init__(self,name,price,dealprice,rating):
        self.name=name
        self.price=price
        self.dealprice=dealprice
        self.rating=rating


    def displayproductdetails(self):
        print(self.name)
        print(self.price)
        print(self.dealprice)
        print(self.rating)

class electronic:
    def __init__(self,warranty):
        self.warranty=warranty
    def getwarranty(self):
        print(self.warranty)

x1= product("rocky",2500,300,4.5)
x1.displayproductdetails()
x2=electronic(5)
x2.getwarranty()

class grocery:
    def __init__(self,expirydate,package):
        self.expirydate=expirydate
        self.package=package
    def getexpirydate(self):
        print(self.expirydate)
x1=product("rockybhai",2345,34,4)
x1.displayproductdetails()
x2=grocery(2023,2345)
x2.getexpirydate()


