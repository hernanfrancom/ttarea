# Clase base
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base

    # Getter para nombre
    @property
    def nombre(self):
        return self.__nombre

    # Getter para sueldo_base
    @property
    def sueldo_base(self):
        return self.__sueldo_base

    # Setter para sueldo_base (validamos que no sea negativo)
    @sueldo_base.setter
    def sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo_base = nuevo_sueldo
        else:
            print("El sueldo base no puede ser negativo.")

    # Método a ser sobrescrito
    def calcular_salario(self):
        return self.__sueldo_base

# Clase hija: EmpleadoFijo
class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        # Salario fijo es simplemente el sueldo base
        return self.sueldo_base

# Clase hija: EmpleadoPorHoras
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

# Clase hija: EmpleadoTemporal
class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, sueldo_base, dias_trabajados, pago_por_dia):
        super().__init__(nombre, sueldo_base)
        self.dias_trabajados = dias_trabajados
        self.pago_por_dia = pago_por_dia

    def calcular_salario(self):
        return self.dias_trabajados * self.pago_por_dia

# Crear empleados de diferentes tipos
empleado1 = EmpleadoFijo("Ana", 3000)
empleado2 = EmpleadoPorHoras("Luis", 0, horas_trabajadas=120, pago_por_hora=15)
empleado3 = EmpleadoTemporal("Carlos", 0, dias_trabajados=20, pago_por_dia=100)

# Lista de empleados
empleados = [empleado1, empleado2, empleado3]

# Calcular salarios usando polimorfismo
for emp in empleados:
    print(f"Empleado: {emp.nombre} - Salario: ${emp.calcular_salario()}")
