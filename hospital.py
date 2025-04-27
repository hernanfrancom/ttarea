# Clase padre
class Persona:
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre
        self.__edad = edad
        self.__documento = documento

    # Propiedad para nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Propiedad para edad
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

    # Propiedad para documento
    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, nuevo_documento):
        self.__documento = nuevo_documento

# Clase hija Paciente
class Paciente(Persona):
    def __init__(self, nombre, edad, documento, diagnostico):
        super().__init__(nombre, edad, documento)
        self.__diagnostico = diagnostico
        self.__historial = []

    def agregar_historial(self, entrada):
        """Agrega una entrada al historial del paciente"""
        self.__historial.append(entrada)
        print("Entrada agregada al historial.")

    def ver_historial(self):
        """Muestra el historial completo del paciente"""
        print(f"Historial de {self.nombre}:")
        for i, entrada in enumerate(self.__historial, start=1):
            print(f"{i}. {entrada}")

    def ver_diagnostico(self):
        """Muestra el diagnóstico actual del paciente"""
        print(f"Diagnóstico de {self.nombre}: {self.__diagnostico}")

    # Método extra para modificar el diagnóstico (uso interno por Doctor)
    def _modificar_diagnostico(self, nuevo_diagnostico):
        self.__diagnostico = nuevo_diagnostico
        print(f"Diagnóstico actualizado para {self.nombre}.")

# Clase hija Doctor
class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)
        self.__especialidad = especialidad

    def ver_especialidad(self):
        """Muestra la especialidad del doctor"""
        print(f"Especialidad del Dr. {self.nombre}: {self.__especialidad}")

    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        """Modifica el diagnóstico de un paciente si es un objeto Paciente"""
        if isinstance(paciente, Paciente):
            paciente._modificar_diagnostico(nuevo_diagnostico)
        else:
            print("Error: Solo se puede modificar el diagnóstico de un paciente.")

# Creamos un paciente
paciente1 = Paciente("Juan Perez", 30, "12345678", "Gripe común")

# Creamos un doctor
doctor1 = Doctor("Dra. Ana Morales", 45, "87654321", "Medicina General")

# Ver información
paciente1.ver_diagnostico()
paciente1.ver_historial()

# Agregamos entradas al historial
paciente1.agregar_historial("Consulta inicial: síntomas leves.")
paciente1.agregar_historial("Prescripción de medicamento.")

# Ver historial actualizado
paciente1.ver_historial()

# El doctor modifica el diagnóstico
doctor1.modificar_diagnostico(paciente1, "Influenza estacional")

# Ver el nuevo diagnóstico
paciente1.ver_diagnostico()

# Ver especialidad del doctor
doctor1.ver_especialidad()
