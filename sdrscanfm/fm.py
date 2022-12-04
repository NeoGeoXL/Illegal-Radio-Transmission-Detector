from sdrscanfm import *



def primera_iteracion_fm():

    f_min = 88e6
    f_max = 92e6
    
    
    canales ={
        'canal 1': [88.0000,88.19000,'usado'],
        'canal 2': [88.2000,88.36000,'libre'],
        'canal 3': [88.4000,88.59000,'usado'],
        'canal 4': [88.6250,88.79000,'libre'],
        'canal 5': [88.8000,88.99000,'libre'],
        'canal 6': [89.0000,89.19000,'libre'],
        'canal 7': [89.2500,89.39000,'libre'],
        'canal 8': [89.4000,89.59000,'libre'],
        'canal 9': [89.6000,89.79000,'usado'],
        'canal 10': [89.8500,89.99990,'libre'],
        'canal 11': [90.0000,90.19000,'usado'],
        'canal 12': [90.2000,90.39000,'libre'],
        'canal 13': [90.4000,90.59000,'usado'],
        'canal 14': [90.6000,90.79000,'libre'],
        'canal 15': [90.8000,90.99000,'usado'],
        'canal 16': [91.0000,91.19000,'libre'],
        'canal 17': [91.2000,91.39000,'usado'],
        'canal 18': [91.4000,91.59000,'libre'],
        'canal 19': [91.6000,91.79000,'usado'],
        'canal 20': [91.8000,91.95000,'libre'],
    
        }
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    idx=1
    datos, espuria , descision =procesamiento(f_min,f_max,canales,idx)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espuria)
    return espectro, espuria, descision
            

def segunda_iteracion_fm():

    f_min = 92e6
    f_max = 96e6

    canales ={
        'canal 21': [92.0000,92.19000,'usado'],
        'canal 22': [92.2500,92.39000,'usado'],
        'canal 23': [92.4000,92.59000,'usado'],
        'canal 24': [92.6900,92.79000,'libre'],
        'canal 25': [92.8000,92.99000,'libre'],
        'canal 26': [93.0000,93.15000,'libre'],
        'canal 27': [93.2000,93.39000,'usado'],
        'canal 28': [93.4500,93.59000,'libre'],
        'canal 29': [93.6000,93.79000,'usado'],
        'canal 30': [93.8000,93.95000,'libre'],
        'canal 31': [94.0000,94.19000,'usado'],
        'canal 32': [94.2000,94.39000,'libre'],
        'canal 33': [94.4000,94.59000,'usado'],
        'canal 34': [94.6000,94.77000,'libre'],
        'canal 35': [94.8000,94.5000,'usado'],
        'canal 36': [95.100,95.19000,'libre'],
        'canal 37': [95.2000,95.39000,'usado'],
        'canal 38': [95.4000,95.59000,'libre'],
        'canal 39': [95.6000,95.79000,'usado'],
        'canal 40': [95.8000,95.99000,'libre'],
        } 
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    idx=2
    datos, espuria , descision =procesamiento(f_min,f_max,canales,idx)   #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision

def tercera_iteracion_fm():

    f_min = 96e6
    f_max = 100e6

    
    canales ={
        'canal 41': [96.0000,96.19000,'usado'],
        'canal 42': [96.2700,96.39000,'libre'],
        'canal 43': [96.4000,96.59000,'usado'],
        'canal 44': [96.6000,96.79000,'libre'],
        'canal 45': [96.8000,96.99000,'usado'],
        'canal 46': [97.0000,97.19000,'libre'],
        'canal 47': [97.2000,97.39000,'usado'],
        'canal 48': [97.4000,97.59000,'libre'],
        'canal 49': [97.6000,97.79000,'usado'],
        'canal 50': [97.8000,97.94000,'libre'],
        'canal 51': [98.0000,98.19000,'usado'],
        'canal 52': [98.22500,98.39000,'libre'],
        'canal 53': [98.4000,98.59000,'usado'],
        'canal 54': [98.6000,98.79000,'libre'],
        'canal 55': [98.8000,98.99000,'usado'],
        'canal 56': [99.0250,99.19000,'libre'],
        'canal 57': [99.2000,99.39000,'usado'],
        'canal 58': [99.4250,99.59000,'libre'],
        'canal 59': [99.6000,99.79000,'usado'],
        'canal 60': [99.8000,99.99000,'libre'],
        }  
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    idx=3
    datos, espuria , descision =procesamiento(f_min,f_max,canales,idx)    #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision

def cuarta_iteracion_fm():

    f_min = 100e6
    f_max = 104e6
    
    
    canales ={
        'canal 61': [100.0000,100.19000,'usado'],
        'canal 62': [100.2000,100.39000,'libre'],
        'canal 63': [100.4000,100.59000,'usado'],
        'canal 64': [100.6500,100.79000,'libre'],
        'canal 65': [100.8000,100.99000,'libre'],
        'canal 66': [101.0000,101.19000,'libre'],
        'canal 67': [101.2000,101.39000,'usado'],
        'canal 68': [101.4000,101.59000,'libre'],
        'canal 69': [101.6000,101.79000,'usado'],
        'canal 70': [101.8000,101.99000,'libre'],
        'canal 71': [102.0000,102.19000,'usado'],
        'canal 72': [102.2000,102.39000,'libre'],
        'canal 73': [102.4000,102.59000,'usado'],
        'canal 74': [102.6000,102.79000,'libre'],
        'canal 75': [102.8000,102.99000,'usado'],
        'canal 76': [103.0000,103.19000,'libre'],
        'canal 77': [103.2000,103.39000,'usado'],
        'canal 78': [103.4100,103.59000,'libre'],
        'canal 79': [103.6000,103.79000,'usado'],
        'canal 80': [103.8000,103.99000,'libre'],
        }  
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    idx=4
    datos, espuria , descision =procesamiento(f_min,f_max,canales,idx)     #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision

def quinta_iteracion_fm():

    f_min = 104e6
    f_max = 108e6
   
    
    canales ={
        'canal 81': [104.0000,104.19000,'usado'],
        'canal 82': [104.2000,104.39000,'libre'],
        'canal 83': [104.4000,104.59000,'usado'],
        'canal 84': [104.6500,104.79000,'libre'],
        'canal 85': [104.8000,104.99000,'usado'],
        'canal 86': [105.0000,105.19000,'libre'],
        'canal 87': [105.2000,105.39000,'usado'],
        'canal 88': [105.4000,105.59000,'libre'],
        'canal 89': [105.6000,105.79000,'usado'],
        'canal 90': [105.8000,105.99000,'libre'],
        'canal 91': [106.0000,106.19000,'usado'],
        'canal 92': [106.2000,106.39000,'libre'],
        'canal 93': [106.4000,106.59000,'usado'],
        'canal 94': [106.6000,106.79000,'libre'],
        'canal 95': [106.8000,106.99000,'usado'],
        'canal 96': [107.0000,107.19000,'libre'],
        'canal 97': [107.2000,107.39000,'usado'],
        'canal 98': [107.4000,107.59000,'libre'],
        'canal 99': [107.6000,107.79000,'usado'],
        'canal 100': [107.8000,107.99000,'libre'],
        }  
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    idx=5
    datos, espuria , descision =procesamiento(f_min,f_max,canales,idx)    #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espuria)
    return espectro, espuria, descision

