import sys
from Classes import *

"""
ATENÇÃO: VOCÊ NÃO DEVE ALTERAR ESSA PARTE DO CÓDIGO!
"""

case = int(sys.stdin.readline())

conta_corrente = ContaCorrente(1, 2.50)
conta_poupanca = ContaPoupanca(1, 0.15)

if case == 0:
    print("%.2f" % conta_corrente.saldo)
elif case == 1:
    conta_corrente.depositar(5)
    print("%.2f" % conta_corrente.saldo)
elif case == 2:
    conta_corrente.depositar(5)
    conta_corrente.cobrar_taxa()
    print("%.2f" % conta_corrente.saldo)
elif case == 3:  
    conta_corrente.depositar(5)
    conta_corrente.cobrar_taxa()    
    conta_corrente.cobrar_taxa()
    print("%.2f" % conta_corrente.saldo)
elif case == 4:
    conta_corrente.depositar(5)
    conta_corrente.cobrar_taxa()    
    conta_corrente.cobrar_taxa()    
    conta_corrente.depositar(3.5)
    print("%.2f" % conta_corrente.saldo)
elif case == 5:
    conta_corrente.depositar(5)
    conta_corrente.cobrar_taxa()    
    conta_corrente.cobrar_taxa()    
    conta_corrente.depositar(3.5)    
    conta_corrente.sacar(0.5)
    print("%.2f" % conta_corrente.saldo)    
elif case == 6:
    print(conta_poupanca.saldo)
elif case == 7:
    conta_poupanca.depositar(10)
    print("%.2f" % conta_poupanca.saldo)
elif case == 8:   
    conta_poupanca.depositar(10)
    conta_poupanca.aplicar_juros()
    print("%.2f" % conta_poupanca.saldo)
elif case == 9:
    conta_poupanca.depositar(10)
    conta_poupanca.aplicar_juros()    
    conta_poupanca.aplicar_juros()
    print("%.2f" % conta_poupanca.saldo)
elif case == 10:
    conta_poupanca.depositar(10)
    conta_poupanca.aplicar_juros()    
    conta_poupanca.aplicar_juros()    
    conta_poupanca.sacar(0.5)
    print("%.2f" % conta_poupanca.saldo) 
elif case == 11:
    conta_poupanca.depositar(10)
    conta_poupanca.aplicar_juros()    
    conta_poupanca.aplicar_juros()    
    conta_poupanca.sacar(0.5)    
    conta_poupanca.sacar(1.5)
    print("%.2f" % conta_poupanca.saldo) 
else:
    print("Unknown case: ", case)    