class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 




    def agregarpr(self, Producto):
        if Producto.id not in self.carrito.keys():
            self.carrito[Producto.id]={
                "producto_id":Producto.id, 
                "nombre": Producto.nombre,
                "precio": str (Producto.precio),
                "cantidad": 1,
                "total": Producto.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key==Producto.id:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = Producto.precio
                    value["total"]= value["total"] + Producto.precio
                    break
        self.guardar_carrito()

    def agregar(self, Producto):
        if Producto.id not in self.carrito.keys():
            self.carrito[Producto.id]={
                "producto_id":Producto.id, 
                "nombre": Producto.nombre,
                "precio": str (Producto.precio),
                "cantidad": 1,
                "total": Producto.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key==Producto.id:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = Producto.precio
                    value["total"]= value["total"] + Producto.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, Producto):
        id = Producto.id
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()

    def restar (self,Producto):
        for key, value in self.carrito.items():
            if key == Producto.id:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- Producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(Producto)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True