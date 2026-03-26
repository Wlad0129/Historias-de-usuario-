def crear_pedido(accumulated_customers, accumulated_products, accumulated_orders):
    print()
    registro = input("¿Would you like to register an order? yes/no: ")

    while registro == "yes":
        print("="*60)
        print("ORDER REGISTRATION".center(60, "="))
        print("="*60)
        print()
        
        #mostrar clientes disponibles
        print("REGISTERED CUSTOMERS".center(60))
        contador = 1
        for cliente in accumulated_customers:
            print()
            print("ID:  ".ljust(30), cliente['id'])
            print("Name:".ljust(30), cliente['name'])
            print("-" * 50)
            print()
            contador = contador + 1   

        #mostrar productos disponibles
        print("PRODUCTS AVAILABLE".center(60))
        contador = 1
        for producto in accumulated_products:
            print()
            print("ID:   ".ljust(30), producto['id'])
            print("Name: ".ljust(30), producto['name'])
            print("Price:".ljust(30), producto['price'])
            print("-" * 50)
            contador = contador + 1

        print("-" * 50)

        #El usuario escoge por número
        customer_option  = int(input("Select the customer ID: "))
        product_option = int(input("Select the product ID: "))
        quantity        = int(input("Product quantity: "))

        #obtenemos cliente y producto por posición 
        selected_customer  = accumulated_customers[customer_option - 1]
        selected_product = accumulated_products[product_option - 1]

        #calculamos total
        total = selected_product["price"] * quantity

        # Creamos el diccionario del pedido
        order_dictionary = {
            "id order" : len(accumulated_orders) + 1,
            "customer"   : selected_customer["name"],
            "product"  : selected_product["name"],
            "price"    : selected_product["price"],
            "quantity"  : quantity,
            "Subtotall"     : total
        }

        #guardamos en la tupla acumulada
        accumulated_orders = accumulated_orders + (order_dictionary,)

        print()
        print("-" * 50)
        print("ORDER SUCCESFULLY REGISTERED ".center(50, "="))
        print("-" * 50)
        registro = input("¿Would you like to register another order? yes/no: ")
        print()

    return accumulated_orders