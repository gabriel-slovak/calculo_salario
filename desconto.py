#INSS = 11%
#VA = 6%
#VT = 5%
#Auxilio creche = 15%

from regras import *

salario_bruto = float(input("Digite o salario bruto: R$"))


INSS = calcular_INSS(salario_bruto)
VA = calcular_VA(salario_bruto)
VT = calcular_VT(salario_bruto)
AUX_CRECHE = 0.0


#VALIDAÇÂO DE APENAS SIM OU NÂO
tem_filhos = ''
while tem_filhos != 'S' and tem_filhos != 'N':
    tem_filhos = input('Possui filho(s)? (S) Sim | (N) Não: ').upper()
    
    if tem_filhos != 'N' and tem_filhos != 'S':
        print('Você só pode digitar (S) ou (N)')


if tem_filhos == 'S':
    AUX_CRECHE = calcular_CRECHE(salario_bruto)
    
salario_liquido = calcular_salario_liquido(salario_bruto, INSS, VA, VT,AUX_CRECHE)

print(f'Seu salario liquido é R$ {salario_liquido}')

print(f'total de descontos R$: {calcular_total_descontos(INSS, VA, VT, AUX_CRECHE)}')