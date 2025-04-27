# Clase padre
class Transporte:
    def tipo_transporte(self):
        print("Tipo de transporte no especificado.")

# Clase hija Coche
class Coche(Transporte):
    def tipo_transporte(self):
        print("Este es un transporte terrestre.")

# Clase hija Avion
class Avion(Transporte):
    def tipo_transporte(self):
        print("Este es un transporte aéreo.")

# Clase hija Barco
class Barco(Transporte):
    def tipo_transporte(self):
        print("Este es un transporte marítimo.")

# -----------------------
# PRUEBA DEL CÓDIGO:
# -----------------------

# Creamos objetos de cada clase
coche = Coche()
avion = Avion()
barco = Barco()

# Llamamos al método tipo_transporte() de cada objeto
coche.tipo_transporte()   # Debe decir: Este es un transporte terrestre
avion.tipo_transporte()   # Debe decir: Este es un transporte aéreo
barco.tipo_transporte()   # Debe decir: Este es un transporte marítimo
