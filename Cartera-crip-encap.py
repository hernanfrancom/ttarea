# Definimos la clase CarteraCripto
class CarteraCripto:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__saldo_btc = 0.0

    def consultar_saldo(self):
        """Muestra el saldo actual de BTC"""
        print(f"Hola {self.__usuario}, tu saldo es de {self.__saldo_btc:.8f} BTC.")

    def comprar_btc(self, monto_usd, precio_actual_btc):
        """Compra BTC usando dólares"""
        if monto_usd > 0 and precio_actual_btc > 0:
            cantidad_btc = monto_usd / precio_actual_btc
            self.__saldo_btc += cantidad_btc
            print(f"¡Compra realizada! Has comprado {cantidad_btc:.8f} BTC.")
        else:
            print("El monto en dólares y el precio del BTC deben ser mayores a 0.")

    def vender_btc(self, monto_btc, precio_actual_btc):
        """Vende una cantidad de BTC"""
        if monto_btc <= 0:
            print("La cantidad de BTC a vender debe ser mayor que 0.")
        elif monto_btc > self.__saldo_btc:
            print("No tienes suficiente BTC para vender esa cantidad.")
        elif precio_actual_btc <= 0:
            print("El precio actual del BTC debe ser mayor que 0.")
        else:
            monto_usd = monto_btc * precio_actual_btc
            self.__saldo_btc -= monto_btc
            print(f"¡Venta realizada! Recibirás ${monto_usd:.2f} USD.")

    def obtener_saldo_btc(self):
        """Devuelve el saldo de BTC (para uso interno si es necesario)"""
        return self.__saldo_btc



# 1. Crear una cartera para el usuario "carlos "
cartera_carlos  = CarteraCripto("carlos ")

# 2. Consultar el saldo inicial
cartera_carlos.consultar_saldo()

# 3. Comprar BTC con 500 dólares, si el precio del BTC es 25000 USD
cartera_carlos.comprar_btc(monto_usd=500, precio_actual_btc=25000)

# 4. Consultar saldo después de la compra
cartera_carlos.consultar_saldo()

# 5. Vender 0.01 BTC, si el precio actual del BTC es 27000 USD
cartera_carlos.vender_btc(monto_btc=0.01, precio_actual_btc=27000)

# 6. Consultar saldo final después de la venta
cartera_carlos.consultar_saldo()
