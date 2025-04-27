class Empleado:
    def __init__(self, nombre, rol, clave_acceso):
        self.__nombre = nombre
        self.__rol = rol
        # Guardamos la clave de forma básica cifrada (reversa)
        self.__clave_acceso = self.__cifrar_clave(clave_acceso)

    # Método privado para cifrar (revertir) la clave
    def __cifrar_clave(self, clave):
        return clave[::-1]

    # Método privado para descifrar la clave
    def __descifrar_clave(self, clave_cifrada):
        return clave_cifrada[::-1]

    # Propiedad para ver el nombre (solo lectura)
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para ver el rol (solo lectura)
    @property
    def rol(self):
        return self.__rol

    # Método para verificar si la clave ingresada es correcta
    def verificar_clave(self, clave_ingresada):
        clave_real = self.__descifrar_clave(self.__clave_acceso)
        if clave_ingresada == clave_real:
            print(" Acceso concedido.")
            return True
        else:
            print(" Clave incorrecta.")
            return False

    # Método para cambiar la clave (solo si se proporciona la clave antigua correcta)
    def cambiar_clave(self, clave_antigua, nueva_clave):
        if self.verificar_clave(clave_antigua):
            self.__clave_acceso = self.__cifrar_clave(nueva_clave)
            print(" Clave cambiada exitosamente.")
        else:
            print(" No se pudo cambiar la clave: la clave antigua es incorrecta.")

    # Método opcional para mostrar información básica
    def mostrar_info(self):
        print(f"Empleado: {self.__nombre}")
        print(f"Rol: {self.__rol}")



# Creamos un empleado
empleado1 = Empleado("Carlos", "Analista", "miClave123")

# Mostramos la información
empleado1.mostrar_info()

# Consultamos el nombre y rol usando @property
print(empleado1.nombre)  # Carlos
print(empleado1.rol)     # Analista

# Intentamos verificar la clave correcta
empleado1.verificar_clave("miClave123")

# Intentamos cambiar la clave con una clave antigua incorrecta
empleado1.cambiar_clave("clave_incorrecta", "nuevaClave456")

# Cambiamos la clave con la clave antigua correcta
empleado1.cambiar_clave("miClave123", "nuevaClave456")

# Verificamos ahora con la nueva clave
empleado1.verificar_clave("nuevaClave456")
