#Online Shopping System (Multilevel Inheritance) 
'''An e-commerce company organizes products using multiple levels. Create classes 
Product → ElectronicProduct → MobilePhone using multilevel inheritance and 
display product details.
'''
class Product:
    def product_details(self):
        print("Product: Mobile phone")


class Electronicproduct(Product):
    def electronic_details(self):
        print("category: Electronics")

class Mobilephone(Electronicproduct):
    def mobile_details(self):
        print("brand: samsung")
        print("price: 25000")

m = Mobilephone()

m.product_details()
m.electronic_details()
m.mobile_details()
