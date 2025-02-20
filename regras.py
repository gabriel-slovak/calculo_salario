def calcular_INSS(sal_bruto):
    return sal_bruto * 0.11

def calcular_VA(sal_bruto):
    return sal_bruto *0.06

def calcular_VT(sal_bruto):
    return sal_bruto * 0.05

def calcular_CRECHE(sal_bruto):
    return sal_bruto * 0.15 

def calcular_salario_liquido(sal_bruto, val_inss, val_va, val_vt, val_creche):
    return sal_bruto - (val_inss + val_va + val_vt + val_creche)

def calcular_total_descontos(val_inss, val_va, val_vt, val_creche):
    return val_inss + val_va + val_vt + val_creche