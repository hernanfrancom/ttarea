class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.__notas = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if not codigo.isalnum():
            raise ValueError("El código debe ser alfanumérico.")
        self.__codigo = codigo

    def agregar_nota(self, nota):
        if 0.0 <= nota <= 5.0:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0

    def obtener_notas(self):
        return self.__notas  # Método para acceder a las notas de manera controlada


# Ejemplo de uso
if __name__ == "__main__":
    try:
        estudiante1 = Estudiante("Ana Pérez", "AP123")
        estudiante1.agregar_nota(4.5)
        estudiante1.agregar_nota(3.8)
        estudiante1.agregar_nota(2.9)

        print(f"Nombre: {estudiante1.nombre}")
        print(f"Código: {estudiante1.codigo}")
        print(f"Notas: {estudiante1.obtener_notas()}")
        print(f"Promedio: {estudiante1.calcular_promedio()}")
        print(f"¿Aprobado?: {estudiante1.es_aprobado()}")

        print("\n--- Probando validaciones ---")
        try:
            estudiante2 = Estudiante("", "XYZ45")
        except ValueError as e:
            print(f"Error al crear estudiante 2: {e}")

        try:
            estudiante3 = Estudiante("Carlos López", "ABC DEF")
        except ValueError as e:
            print(f"Error al crear estudiante 3: {e}")

        try:
            estudiante1.agregar_nota(6.0)
        except ValueError as e:
            print(f"Error al agregar nota inválida: {e}")
    except ValueError as e:
        print(f"Error general: {e}")
