from sdrscantv import *



def primera_iteracion_tv():

    f_min = 54e6
    f_max = 88e6

    canales ={
        'canal 2': [54.00,60.00,'usado'],
        'canal 3': [60.00,66.00,'libre'],
        'canal 4': [66.00,72.00,'usado'],
        'canal 5': [76.00,82.00,'usado'],
        'canal 6': [82.00,88.00,'libre'],
        }

    datos, espuria , descision =procesamiento1(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision


def segunda_iteracion_tv():
    f_min = 174e6
    f_max = 216e6

    canales ={
        'canal 7': [174.00,180.00,'libre'],
        'canal 8': [180.00,186.00,'usado'],
        'canal 9': [186.00,192.00,'usado'],
        'canal 10': [192.00,198.00,'libre'],
        'canal 11': [198.00,204.00,'usado'],
        'canal 12': [204.00,210.00,'libre'],
        'canal 13': [210.00,216.00,'usado'],
    }

    datos, espuria , descision =procesamiento2(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision

def tercera_iteracion_tv():

    f_min = 500e6
    f_max = 572e6

    
    canales ={
        'canal 19': [500.00,506.00,'libre'],
        'canal 20': [506.00,512.00,'libre'],
        'canal 21': [512.00,518.00,'libre'],
        'canal 22': [518.00,524.00,'usado'],
        'canal 23': [524.00,530.00,'usado'],
        'canal 24': [530.00,536.00,'libre'],
        'canal 25': [536.00,542.00,'usado'],
        'canal 26': [542.00,548.00,'libre'],
        'canal 27': [548.00,554.00,'usado'],
        'canal 28': [554.00,560.00,'libre'],
        'canal 29': [560.00,566.00,'usado'],
        'canal 30': [566.00,572.00,'libre'],
    }

    datos, espuria , descision =procesamiento3(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision

def cuarta_iteracion_tv():

    f_min = 572e6
    f_max = 632e6
    
    canales ={
        'canal 31': [572.00,578.00,'usado'],
        'canal 32': [578.00,584.00,'libre'],
        'canal 33': [584.00,590.00,'usado'],
        'canal 34': [590.00,596.00,'libre'],
        'canal 35': [596.00,602.00,'usado'],
        'canal 36': [602.00,608.00,'libre'],
        'canal 37': [608.00,614.00,'libre'],
        'canal 38': [614.00,620.00,'libre'],
        'canal 39': [620.00,626.00,'libre'],
        'canal 40': [626.00,632.00,'libre'],
    }
    datos, espuria , descision =procesamiento4(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision

def quinta_iteracion_tv():

    f_min = 626e6
    f_max = 686e6

    canales ={
        'canal 41': [632.00,638.00,'libre'],
        'canal 42': [638.00,644.00,'libre'],
        'canal 43': [644.00,650.00,'libre'],
        'canal 44': [650.00,656.00,'libre'],
        'canal 45': [656.00,662.00,'libre'],
        'canal 46': [662.00,668.00,'libre'],
        'canal 47': [668.00,674.00,'libre'],
        'canal 48': [674.00,680.00,'libre'],
        'canal 49': [680.00,686.00,'libre'],
    }

    datos, espuria , descision =procesamiento5(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision