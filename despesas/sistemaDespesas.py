from despesas.despesa import Despesa

desp1 = Despesa('Compras do mês', 400)
desp2 = Despesa('Conta de luz', 300)
desp3 = Despesa('Disney+', 17.9)

Despesa.realizarPagamento(desp1)
Despesa.realizarPagamento(desp2)
Despesa.realizarPagamento(desp3)

print(desp1.valor)
print(desp2.valor)
print(desp3.valor)
print(Despesa.totalDespesas)
