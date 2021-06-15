from EjercicioPOO1 import CuentaCorriente


class CuentaJoven(CuentaCorriente):
    def __init__(self,NumeroCuenta,Titular,Saldo, bonus_promocion=0):
         super().__init__(NumeroCuenta,Titular,Saldo)
         self.Saldo=Saldo+bonus_promocion
         self.bonus_promocion=bonus_promocion
    def getBonus(self):
        return "Bonus: "+str(self.bonus_promocion)

    def ingresar(self, ingreso):
        return super().ingresar(ingreso)
    def retirar(self, retiro):
        return super().retirar(retiro)
    def getDatos(self):
        return super().getDatos()+" Bonus: "+str(self.bonus_promocion)



cuentaj=CuentaJoven("20800182123456789087", "Pablo Vidal", 16000,300 )
cuentaj.ingresar(200)
cuentaj.retirar(275)
cuentaj.getDatos()
print(cuentaj.getBonus())
print(cuentaj.getDatos())
