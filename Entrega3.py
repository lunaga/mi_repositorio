def año_bisiesto(anio):
    if type(anio) != int:
        print('eror, por favor ingrese un numero: ')
    elif anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print(f'el año {anio} es bisiesto.')
    else:
        print(f'el año {anio} no es bisiesto.')
año_bisiesto(2012)
año_bisiesto(1900)
año_bisiesto(2010)
año_bisiesto(2000)
año_bisiesto(400)
año_bisiesto('alan') 
       