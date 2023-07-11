"""
La empresa en la que trabajas recibe una gran cantidad de materias primas y otros productos en su inventario, los cuales
son registrados y manejados en hojas de papel que describen nombres, cantidades, precios, tipos y tamaños de cada producto
que entra y sale. Recientemente se perdieron algunas hojas y se tomó la decisión de digitalizar este proceso. Dado lo anterior,
se te pide que desarrolles un programa en Python, en el cual, la persona encargada de registrar entradas y salidas de
inventarios pueda hacer estos registros fácilmente mediante la terminal. La tarea se deberá llevar a cabo utilizando funciones
para añadir nuevos artículos, actualizar cantidades y buscar artículos específicos basándose en varios criterios. Se deberán
utilizar funciones lambda para ordenar el inventario en función de diferentes atributos, como ordenar los artículos por nombre,
cantidad o precio. Además, se deberán emplear funciones anidadas para gestionar operaciones complejas, como generar informes de
inventario o calcular el valor total del inventario. Deberás subir este archivo de Python a un repositorio Github, junto con
un archivo **README.md** que explique cómo utilizar el programa. Se evaluará el uso de funciones y funciones lambda para agregar
(con diferentes datos incluyendo fecha con la paquetería *datetime*), editar, leer, y borrar productos del inventario, que todo
funcione correctamente y que contenga el archivo **README.md**.
"""

from builtins import filter

products = []


def add_product():
    name = input('Enter product name: ')
    description = input('Enter product description: ')
    category = input('Enter product category: ')
    size = input('Enter product size: ')
    price = input('Enter product price: ')
    quantity = input('Enter product quantity: ')
    insertProduct(name, description, price, category, size, quantity)
    print('Customer added')


def insertProduct(name, description, price, category, size, quantity):
    product = {'name': name, 'description': description, 'price': price, 'category': category, 'size': size,
               'quantity': quantity}
    products.append(product)


def update_product():
    name = input('Enter product name to update: ')
    for product in products:
        if product['name'] == name:
            description = input('Enter the new product description: ')
            category = input('Enter the new product category: ')
            size = input('Enter the new product size: ')
            price = input('Enter the new product price: ')
            quantity = input('Enter the new product quantity: ')
            product['description'] = description
            product['price'] = price
            product['category'] = category
            product['size'] = size
            product['quantity'] = quantity
            print('Customer updated.')
            return
    print('Product not found.')


def show_products():
    if len(products) == 0:
        print('No products found ')
        return
    for product in products:
        show_product(product)


def show_product(product):
    print(f"Name: {product['name']}, Description: {product['description']}, Category: {product['category']}, "
          f"Size: {product['size']}, Price: {product['price']}, Quantity: {product['quantity']}")


def sort_products():
    option = int(input('Sort by: \n 1.Name \n 2.Category \n 3.Price \n Select and option: '))
    if option == 1:
        sort_products = sorted(products, key=lambda product: product['name'])
    elif option == 2:
        sort_products = sorted(products, key=lambda product: product['category'])
    elif option == 3:
        sort_products = sorted(products, key=lambda product: product['price'])
    else:
        print('Invalid option. ')
        return
    for product in sort_products:
        show_product(product)


def search_product():
    option = int(input('Search by: \n 1.Name \n 2.Category \n 3.Description \n Select and option: '))
    if option == 1:
        name = input('Enter product name to search : ')
        filtered_products = list(filter(lambda product: name.lower() in product['name'].lower(), products))
    elif option == 2:
        category = input('Enter product category to search: ')
        filtered_products = list(filter(lambda product: category.lower() in product['category'].lower(), products))
    elif option == 3:
        description = input('Enter product description to search : ')
        filtered_products = list(
            filter(lambda product: description.lower() in product['description'].lower(), products))
    else:
        print('option not valid')
        return
    if len(filtered_products) > 0:
        print('Search results: ')
        for product in filtered_products:
            show_product(product)
    else:
        print('No product found.')


def backup_inventory():
    archivoBackup = input("Enter the file name to create the backup: ")
    archivoBackup += ".backup"
    with open(archivoBackup, 'w') as archivo:
        for product in products:
            archivo.write(
                f"{product['name']},{product['description']},{product['category']},{product['price']},{product['size']},{product['quantity']}")


def import_inventory():
    archivoBackup = input("Enter the file name to import the backup: ")
    archivoBackup += ".backup"
    with open(archivoBackup, 'r') as archivo:
        for line in archivo.readlines():
            values = line.split(",")
            name = values[0]
            description = values[1]
            category = values[2]
            price = values[3]
            size = values[4]
            quantity = values[5]
            insertProduct(name, description, price, category, size, quantity)


def inventario_menu():
    while True:
        print('Inventory System')
        print('1. Add Product')
        print('2. Update Product')
        print('3. Show Products')
        print('4. Find a Product')
        print('5. Sort a Products')
        print('6. Create Backup')
        print('7. Import Backup')
        print('8. Exit')
        inputSelected = input('Enter your choice: ')
        if inputSelected.isdigit():
            choice = int(inputSelected)
        else:
            choice = -1

        if choice == 1:
            add_product()
        elif choice == 2:
            update_product()
        elif choice == 3:
            show_products()
        elif choice == 4:
            search_product()
        elif choice == 5:
            sort_products()
        elif choice == 6:
            backup_inventory()
        elif choice == 7:
            import_inventory()
        elif choice == 8:
            print('Existing...')
            break
        else:
            print('Invalida choice. Try again')


inventario_menu()
