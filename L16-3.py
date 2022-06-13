class Product:

    def __init__(self, TYPE, name, price):
        self.price = price
        self.name = name
        self.type = TYPE


class ProductStore:
    PROFIT = 0

    def __init__(self):
        self.COUNT = 0
        self.SHOP_PRICE = 0

    def add(self, product, amount):
        try:
            self.COUNT += amount
            self.SHOP_PRICE = product.price + product.price * 0.3

        except ValueError:
            pass

    # def set_discount(self, identifier, percent, identifier_type='name'):
    #     try:
    #         pass
    # 
    #     except ValueError:
    #         pass

    def sell_product(self, product_name, amount):
        try:
            product_name.COUNT -= amount
            if product_name.COUNT < 0:
                product_name.COUNT += amount
                raise ValueError

            dirt_profit = product_name.SHOP_PRICE * amount
            ProductStore.PROFIT += dirt_profit - product_name.price * amount

        except ValueError:
            print('валю ерор')

    def get_income(self, ):
        try:
            return ProductStore.PROFIT

        except ValueError:
            pass

    def get_all_products(self):
        try:
            return ProductStore.__dict__

        except ValueError:
            pass

    def get_product_info(self, product_name):
        try:
            return product_name.__dict__

        except ValueError:
            pass


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p, 10)

s.add(p2, 300)

print(s.get_all_products())

s.sell_product('Ramen', 10)
 
# assert s.get_product_info('Ramen') == ('Ramen', 290)
