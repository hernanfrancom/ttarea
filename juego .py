class Personaje:
    def __init__(self, vida, ataque, defensa):
        self._vida = 0
        self._ataque = 0
        self._defensa = 0
        self.set_vida(vida)
        self.set_ataque(ataque)
        self.set_defensa(defensa)
    
    # Getters y setters con validación
    def get_vida(self):
        return self._vida
    
    def set_vida(self, vida):
        if vida < 0:
            self._vida = 0
        elif vida > 100:
            self._vida = 100
        else:
            self._vida = vida
    
    def get_ataque(self):
        return self._ataque
    
    def set_ataque(self, ataque):
        self._ataque = max(0, ataque)
    
    def get_defensa(self):
        return self._defensa
    
    def set_defensa(self, defensa):
        self._defensa = max(0, defensa)
    
    def atacar(self, objetivo):
        # Método base que será sobrescrito por las subclases
        danio = max(0, self._ataque - objetivo.get_defensa())
        objetivo.set_vida(objetivo.get_vida() - danio)
        return danio
    
    def esta_vivo(self):
        return self._vida > 0
    
    def __str__(self):
        return f"{self.__class__.__name__}: Vida={self._vida}, Ataque={self._ataque}, Defensa={self._defensa}"


class Guerrero(Personaje):
    def atacar(self, objetivo):
        # Guerrero: 20% más de daño
        danio = max(0, (self.get_ataque() * 1.2) - objetivo.get_defensa())
        objetivo.set_vida(objetivo.get_vida() - danio)
        return danio


class Mago(Personaje):
    def atacar(self, objetivo):
        # Mago: ignora la defensa
        danio = self.get_ataque()
        objetivo.set_vida(objetivo.get_vida() - danio)
        return danio


class Arquero(Personaje):
    def atacar(self, objetivo):
        # Arquero: si ataque > defensa, doble daño
        if self.get_ataque() > objetivo.get_defensa():
            danio = self.get_ataque() * 2
        else:
            danio = max(0, self.get_ataque() - objetivo.get_defensa())
        objetivo.set_vida(objetivo.get_vida() - danio)
        return danio


def batalla(jugador1, jugador2):
    print("¡Comienza la batalla!")
    print(jugador1)
    print(jugador2)
    print()
    
    turno = 1
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print(f"Turno {turno}")
        
        # Jugador 1 ataca a Jugador 2
        danio = jugador1.atacar(jugador2)
        print(f"{jugador1.__class__.__name__} ataca a {jugador2.__class__.__name__} y causa {danio:.1f} de daño")
        print(f"Vida de {jugador2.__class__.__name__}: {jugador2.get_vida():.1f}")
        
        if not jugador2.esta_vivo():
            print(f"\n{jugador2.__class__.__name__} ha sido derrotado!")
            break
        
        # Jugador 2 ataca a Jugador 1
        danio = jugador2.atacar(jugador1)
        print(f"{jugador2.__class__.__name__} ataca a {jugador1.__class__.__name__} y causa {danio:.1f} de daño")
        print(f"Vida de {jugador1.__class__.__name__}: {jugador1.get_vida():.1f}")
        
        if not jugador1.esta_vivo():
            print(f"\n{jugador1.__class__.__name__} ha sido derrotado!")
            break
        
        print()
        turno += 1
    
    print("\n¡Batalla terminada!")
    if jugador1.esta_vivo():
        print(f"¡{jugador1.__class__.__name__} es el ganador!")
    else:
        print(f"¡{jugador2.__class__.__name__} es el ganador!")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear personajes según el ejemplo
    guerrero = Guerrero(vida=100, ataque=30, defensa=20)
    mago = Mago(vida=80, ataque=40, defensa=10)
    
    # Iniciar batalla
    batalla(guerrero, mago)