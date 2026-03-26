from FEATURE_CUSTOMER_REGISTER import register_client
from FEATURE_PRODUCTS_REGISTER import register_products
from FEATURE_ORDER_CREATION import crear_pedido

accumulated_customers =()
accumulated_customers = register_client(accumulated_customers)  

accumulated_products =()
accumulated_products = register_products(accumulated_products)  

accumulated_orders = ()
accumulated_orders = crear_pedido (accumulated_customers, accumulated_products, accumulated_orders)




for interant in accumulated_orders:
    print("ORDER INFORMATION".center(50, "-"))
    print()
    print("ID:".ljust(30), interant["id order"])
    print("Name:".ljust(30), interant["customer"])
    print("E-mail:".ljust(30), interant["product"])
    print("price:".ljust(30), interant["price"])
    print("quantity:".ljust(30), interant["quantity"])
    print("total:".ljust(30), interant["Subtotal"])
    print()





































#ESTO ES PARA PROBAR SI SE GUARDARON LOS DATOS EN LA TUPLA
# for interant in accumulated_tuple:
#     print("CUSTOMER INFORMATION".center(50, "-"))
#     print()
#     print("ID:".ljust(30), interant["id"])
#     print("Name:".ljust(30), interant["name"])
#     print("E-mail:".ljust(30), interant["email"])
#     print()

# for interant in products:
#     print("PRODUCT INFORMATION".center(50, "-"))
#     print()
#     print("name".ljust(30), interant["name"])
#     print("id".ljust(30), interant["id"])
#     print("price".ljust(30), interant["price"])
#     print()