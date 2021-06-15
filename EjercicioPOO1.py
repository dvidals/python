class CuentaCorriente():
    NumeroCuenta=""
    Titular=""
    Saldo=0

    def __init__(self,NumeroCuenta,Titular,Saldo):
        self.NumeroCuenta=NumeroCuenta
        self.Titular=Titular
        self.Saldo=Saldo
    def getDatos(self):
        return "Nº de cuenta: "+self.NumeroCuenta+ ", Titular: "+self.Titular+\
            ", Saldo: "+str(self.Saldo)
    def ingresar(self, ingreso):
        self.Saldo=self.Saldo+ingreso
    def retirar(self, retiro):
        self.Saldo=self.Saldo-retiro
cuenta=CuentaCorriente("20800182123456789012", "David Vidal", 4700)
cuenta.ingresar(1050)
cuenta.retirar(450)
print(cuenta.getDatos())
