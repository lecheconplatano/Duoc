             #modelo :[marca,pantalla,Ram,disco,GB de DD,procesador,    video]
             # cambio 1
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
            }

        # modelo :[precio,stock]
        #cambio 2
stock = {'8475HD': [387990,10],
         '2175HD': [327990,4],
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21],
         '123FHD': [290890,32],
         '342FHD': [444990,7],
         'GF75HD': [749990,2],
         'UWU131HD': [349990,1],
         'FS1230HD': [249990,0],
        }

#Funciones
def stock_marca(marca):
    for mod,info in productos.items():
        if marca == info[0].lower():
            for modelo,datos in stock.items():
                if mod.lower() == modelo.lower():
                    print(f"Modelo: {modelo} || Stock: {datos[1]}")

def salir():
    print("Programa Finalizado.")
    exit()

def búsqueda_precio(p_min,p_max):
    lista_rango = []
    lista = []
    for modelo,datos in stock.items():
        encontrados = False
        if datos[0] in range(p_min,p_max):
            lista_rango.append(datos[0])
            encontrados = True
            for mod,info in productos.items():
                if modelo == mod:
                    marca=info[0]
                    lista.append(marca)
                    lista.append(mod)
    if not encontrados:
            print("No hay notebooks en ese rango de precios.")
    if encontrados:
        print(f"Los notebooks entre los precios de consultas son: {lista}")

def ordenar_productos():
    #[marca-modelo-RAM-Disco-GB]
    if productos == {}:
        print("No hay notebook disponibles para mostrar")
    else:
        print("------Listado de Notebooks Ordenados------")
        for modelo,data in productos.items():
            print(f"{data[0]} - {modelo} - {data[2]} - {data[4]}")
        print("------------------------------------------")



while True:
    print("***MENU PRINCIPAL***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Listado de productos.")
    print("4. Salir.")
    opc = input("Ingrese la opcion: ")
    if opc == "1":
        marca = input("Ingrese marca a consultar: ").lower()
        stock_marca(marca)
    elif opc == "2":
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                if p_min > 0:
                    break
            except:
                print("Debe ingresar valores enteros!!")
        while True:
            try:
                p_max = int(input("Ingrese precio máximo: "))
                if p_max > 0:
                    break
            except:
                print("Debe ingresar valores enteros!!")                
        búsqueda_precio(p_min,p_max)
    elif opc == "3":
        ordenar_productos()
    elif opc == "4":
        salir()
    else:
        print("Debe seleccionar una opción valida!!")
        #fin del codigo