import statistics as stat
import random as rdm
from typing import List

def simulation(days_to_simulate : int, mct : str, days):
    """
    Basic class to simulate the dolar value
    
    Parameters
    ----------
    (str) path_file_old_values: direccion con los valores del USd de dias anteriores
    (int) days_to_simulate: cantidad de dias q se quiere simular el comportamiento del dolar
    (str) mct : medida de tendencia central a utilizar
    (int) days : representa los dias anteriores que se van a tener en cuenta para predecir el valor del dolar
    """
    for x in range(days_to_simulate):
        path_file_old_values = 'values.txt'
        value_last_days = read_script_values(path_file_old_values, mct,days)
        generate_values(int(value_last_days),10)
        recopilated_values = read_script_values('generated_values.txt',mct,days)
        usd_value = (int(value_last_days) + int(recopilated_values)) // 2
        temp = event_arbitrarial_value(usd_value)
        if temp > 0:
            usd_value = temp
        add_new_dolar_price(path_file_old_values,usd_value)
        print(f'El valor del dolar al dia {x + 1} de la simulacion fue: {usd_value}')
        


def add_new_dolar_price(path, value):
    file = open(path,'a')
    file.write(str(value) + '\n')
    file.close()


def read_script_values(path_file,mct : str, days):
    fl = open(path_file)
    lines = fl.readlines()
    values : List = []
    for item in lines:
        if days == 0:
            break
        temp = item.replace('\n','')
        values.append(int(float(temp)))
        days -= 1
    fl.close()
    if mct == 'moda':
        return calculate_mode(values)
    elif mct == 'media':
        return calculate_mean(values)
    elif mct == 'mediana':
        return calculate_median(values)
    else :
        raise Exception('Por favor elija calcular moda media o mediana')

def calculate_mode(values):
    return stat.mode(values)

def calculate_mean(values):
    return stat.mean(values)

def calculate_median(values):
    return stat.median(values)

def generate_values(usd_value, variance):
    fl = open('generated_values.txt','w')
    rdm_value = rdm.randint(300,400)
    v_a = stat.NormalDist(usd_value,variance)
    list_samples = v_a.samples(rdm_value)
    for elem in list_samples:
        fl.write(str(elem) + '\n')
    fl.close()

def event_arbitrarial_value(usd_value):
    """
    Funcion para simular generar un valor arbitrario del dolar con intencion de elevar
    su valor
    Args:
    (int) usd_value: valor real del usd del dia

    Returns:
        _type_: _description_
    """
    r = rdm.randint(0,100)
    if r < 7:
        return usd_value + usd_value//20
    return - 1


simulation(30,'mediana',1)

