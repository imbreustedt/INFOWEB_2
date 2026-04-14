class agua:
    def dados(self):
        self.mes = 0
        self.consumo = 0
        self.ano = 0
    def calculo(self):
        valor10m = 38.00
        if self.consumo > 10:
            if self.consumo <= 20:
                valor10m += (self.consumo - 10) * 5
            else: 
                valor10m += (10 * 5.00) + (self.consumo - 20) * 6.00
        return valor10m
    
m = input("Digite o mês (ex: Março): ")
a = int(input("Digite o ano: "))
c = float(input("Digite o consumo em m³: "))

conta = agua(m, a, c)
valor_pagar = conta.calcular_valor()

print(f"\nConta de {conta.mes}/{conta.ano}")
print(f"Consumo: {conta.consumo} m³")
print(f"Valor a pagar: R$ {valor_pagar:.2f}")