from .models import Product, OrderProduct, Order, Customer


# Bu klass karzinaga produkt qoshishga va udalit qilishga xizmat qiladi

class CartAuthenticatedUser:
    def __init__(self, request, product_id=None, action=None):
        self.user = request.user

        if product_id and action:
            self.add_or_delete(product_id, action)

    # Karzinadagi informasiyani chiqarib
    def get_cart_info(self):
        customer, created = Customer.objects.get_or_create(
            # Sotib oluvchi karzinani yaratvoti narsa sotib olgani xisob
            user=self.user,

        )
        order, created = Order.objects.get_or_create(customer=customer)  # Zakazni yaratish
        order_products = order.orderproduct_set.all()  # Hamma zakaz qilingan produktlani oz ichiga oladi

        cart_total_quantity = order.get_cart_total_quantity  # Hamma produktlani sananb beradi!
        cart_total_price = order.get_cart_total_price  # Hammasini narxini obshiy qoshib beradi!

        return {
            'cart_total_quantity': cart_total_quantity,
            'cart_total_price': cart_total_price,
            'order': order,
            'products': order_products
        }

    def add_or_delete(self, product_id, action):
        order = self.get_cart_info()['order']
        product = Product.objects.get(pk=product_id)
        order_product, created = OrderProduct.objects.get_or_create(order=order, product=product)

        if action == 'add' and product.quantity > 0:
            order_product.quantity += 1  # +1 karzinaga qoshadi!
            product.quantity -= 1  # -1 kazinadan ob tashidi !
        else:
            order_product.quantity -= 1
            product.quantity += 1

        product.save()
        order_product.save()

        if order_product.quantity <= 0:  # Agar 0 dan tushib ketsa polni ochiradi produktni
            order_product.delete()

    def clear(self):
        order = self.get_cart_info()['order']
        order_products = order.orderproduct_set.all()
        for product in order_products:
            product.delete()
        order.save()


# Tepadagi klassni funksiyalari bilan birga ishlatish funksiyasi
def get_cart_data(request):
    cart = CartAuthenticatedUser(request)
    cart_info = cart.get_cart_info()

    return {
        'cart_total_quantity': cart_info['cart_total_quantity'], # produkt sanalvotti
        'cart_total_price': cart_info['cart_total_price'], # produkt narxlari xisoblanvotti
        'order': cart_info['order'], # produkt zakazga tushdi
        'products': cart_info['products'] # produkt zakaz prassesida
    }
