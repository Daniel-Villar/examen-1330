class Venta1330:
    id_venta1330 = 0
    precios_vent1330 = 0
    stock_venta1330 = 0
    descuento1330 = ""
    vendedor1330 = ""
    fecha1330 = ""
    hora_venta1330 = ""

    def mostrar_datos(self):
        print(f"id venta: {self.id_venta1330}, precio de la venta: {self.precios_vent1330}, "
              f"stock de la venta: {self.stock_venta1330}, descuento: {self.descuento1330}, "
              f"vendedor: {self.vendedor1330}, fecha: {self.fecha1330}, hora: {self.hora_venta1330}")

    def lista_ventas(self):
        list_ventas = [
            "id Venta: 4895", "precio: 400", "fecha de venta: 23/09/2000",
            "hora de venta: 6:00 pm", "descuento: 45%", "vendedor: Ailin", "stock: 400 piezas"
        ]
        for z in list_ventas:
            print(z)

    def tupla_venta1330(self):
        vent_tupla = (
            "id Venta: 7575", "precio: 5600", "fecha de venta: 28/10/2007",
            "hora de venta: 9:00 pm", "descuento: 5%", "vendedor: Renata", "stock: 120 piezas"
        )
        for y in vent_tupla:
            print(y)

    def diccionario_venta(self):
        dicc_vent = {
            "id venta": 1367,
            "precio": "$2000",
            "fecha de venta": "14/03/2022",
            "hora de venta": "4:50 pm",
            "descuento": "6%",
            "vendedor": "Juan",
            "stock": 433
        }
        for c, v in dicc_vent.items():
            print(f"{c}: {v}")

    def altas1330(self):
        print("La venta se dio de alta")
    
    def bajas1330(self):
        print("La venta no se dio de alta")

# Crear una instancia de la clase
venta = Venta1330()
venta.id_venta1330 = 1330
venta.precios_vent1330 = 400
venta.stock_venta1330 = 1090
venta.descuento1330 = "20%"
venta.vendedor1330 = "Bangchan"
venta.fecha1330 = "15/09/2024"
venta.hora_venta1330 = "12:30 am"

# Mostrar datos de la venta
venta.mostrar_datos()

# Mostrar listas, tuplas y diccionarios
venta.lista_ventas()
venta.tupla_venta1330()
venta.diccionario_venta()
