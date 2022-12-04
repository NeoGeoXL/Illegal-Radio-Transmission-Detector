from sdrscantv import *



def primera_iteracion_tv():

    f_min = 54e6
    f_max = 88e6
    
    
    canales ={
        'canal 2 - Libre 1': [54.0000,54.249,'libre'],
        'canal 2 - Video': [54.250,56.250,'usado'],
        'canal 2 - Libre 2': [56.251,58.490,'libre'],
        'canal 2 - Armonicos': [58.50,59.250,'usado'],
        'canal 2 - Libre 3': [59.251,59.680,'libre'],
        'canal 2 - Audio': [59.69,59.81,'usado'],
        'canal 2 - Libre 4': [59.82,60.000,'libre'],
        
        'canal 3 - Libre 1': [60.001,61.149,'libre'],
        'canal 3 - Armonicos': [61.150,61.50,'usado'],
        'canal 3 - Libre 2': [61.51,66.000,'libre'],


        'canal 4 - Libre 1': [66.001,66.7490,'libre'],
        'canal 4 - Video': [66.750,68.750,'usado'],
        'canal 4 - Libre 2': [68.751,70.749,'libre'],
        'canal 4 - Armonicos': [70.750,71.01,'usado'],
        'canal 4 - Libre 3': [71.02,71.70,'libre'],
        'canal 4 - Audio': [71.71,71.77,'usado'],
        'canal 4 - Libre 4':[71.78,72.00,'libre'],

        'canal 5 - Libre 1': [76.000,76.249,'libre'],
        'canal 5 - Video': [76.250,78.750,'usado'],
        'canal 5 - Libre 2': [78.751,80.249,'libre'],
        'canal 5 - Armonicos': [80.250,81.250,'usado'],
        'canal 5 - Libre 3': [81.251,81.68,'libre'],
        'canal 5 - Audio': [81.69,81.81,'usado'],
        'canal 5 - Libre 4': [81.82,82.00,'libre'],

        'canal 6 - Libre 1': [82.01,85.39,'libre'],
        'canal 6 - Armonicos': [85.40,85.60,'usado'],
        'canal 6 - Libre 2': [85.70,88.000,'libre'],
        }
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    datos, espuria , descision =procesamiento1(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision
            

def segunda_iteracion_tv():

    f_min = 174e6
    f_max = 216e6

    canales ={

        'canal 7 - Libre 1': [174.00,180.00,'usado'],   #Probelmas con este canal rmse>1000

        'canal 8 - Libre 1': [180.01,180.49,'libre'],
        'canal 8 - Video': [180.50,182.250,'usado'],
        'canal 8 - Libre 2': [182.26,184.49,'libre'],
        'canal 8 - Armonicos': [184.50,185.250,'usado'],
        'canal 8 - Libre 3': [185.26,185.68,'libre'],
        'canal 8 - Audio': [185.69,185.81,'usado'],
        'canal 8 - Libre 4': [185.82,186.00,'libre'],

        'canal 9 - Libre 1': [186.01,186.99,'libre'],
        'canal 9 - Video': [187.00,187.50,'usado'],
        'canal 9 - Libre 2': [187.60,190.5,'libre'],
        'canal 9 - Armonicos': [190.60,191.00,'usado'],
        'canal 9 - Libre 3': [191.01,191.68,'libre'],
        'canal 9 - Audio': [191.69,191.81,'usado'],
        'canal 9 - Libre 4': [191.82,192.00,'libre'],
    
        'canal 10 - Libre 1': [192.01,198.00,'libre'],

        'canal 11 - Libre 1': [198.01,198.99,'libre'],
        'canal 11 - Video': [199.00,199.750,'usado'],
        'canal 11 - Libre 2': [199.76,202.74,'libre'],
        'canal 11 - Armonicos': [202.75,203.00,'usado'],
        'canal 11 - Libre 3': [203.01,203.68,'libre'],
        'canal 11 - Audio': [203.69,203.81,'usado'],
        'canal 11 - Libre 4': [203.82,204.00,'libre'],

        'canal 12 - Libre 1': [204.01,210.00,'libre'],

        'canal 13 - Libre 1': [210.01,210.749,'usado'],
        'canal 13 - Video': [210.75,212.00,'usado'],
        'canal 13 - Libre 2': [212.01,214.6,'usado'],
        'canal 13 - Armonicos': [214.7,215.10,'usado'],
        'canal 13 - Libre 3': [215.20,215.67,'usado'],
        'canal 13 - Audio': [215.68,215.81,'usado'],
        'canal 13 - Libre 4': [215.82,216.00,'usado'],

        } 
    
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    datos, espuria , descision =procesamiento2(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision

def tercera_iteracion_tv():

    f_min = 500e6
    f_max = 572e6

    
    canales ={

        'canal 19 - Libre 1': [500.00,500.04,'libre'],
        'canal 19 - Armonicos': [500.05,500.25,'usado'],
        'canal 19 - Libre 2': [500.26,506.000,'libre'],

        'canal 20 - Libre 1': [506.01,512.00,'libre'],

        'canal 21 - Libre 1': [512.01,512.49,'libre'],
        'canal 21 - Armonicos': [512.5,513.75,'usado'],
        'canal 21 - Libre 2': [513.76,518.000,'libre'],

        'canal 22 - Libre 1': [518.01,518.349,'libre'],
        'canal 22 - Armonicos': [518.35,518.45,'usado'],
        'canal 22 - Libre 2': [518.46,524.000,'libre'],

        'canal 23 - Libre 1': [524.01,524.49,'libre'],
        'canal 23 - Video': [524.5,526.50,'usado'],
        'canal 23 - Libre 2': [526.6,528.49,'libre'],
        'canal 23 - Armonicos': [528.5,529.125,'usado'],
        'canal 23 - Libre 3': [529.13,529.6,'libre'],
        'canal 23 - Audio': [529.625,529.85,'usado'],
        'canal 23 - Libre 4': [529.86,530.00,'libre'],

        'canal 24 - Libre 1': [530.01,532.774,'libre'],
        'canal 24 - Armonicos': [532.775,532.85,'usado'],
        'canal 24 - Libre 2': [532.86,536.000,'libre'],
    
        'canal 25 - Libre 1': [536.01,536.249,'libre'],
        'canal 25 - Video': [536.250,538.250,'usado'],
        'canal 25 - Libre 2': [538.26,540.49,'libre'],
        'canal 25 - Armonicos': [540.5,541.250,'usado'],
        'canal 25 - Libre 3': [541.260,541.64,'libre'],
        'canal 25 - Audio': [541.65,541.825,'usado'],
        'canal 25 - Libre 4': [541.83,542.00,'libre'],

        'canal 26 - Libre 1': [542.01,547.174,'libre'],
        'canal 26 - Armonicos': [547.175,547.225,'usado'],
        'canal 26 - Libre 2': [547.226,548.000,'libre'],

        'canal 27 - Libre 1': [548.01,548.249,'libre'],
        'canal 27 - Video': [548.250,550.50,'usado'],
        'canal 27 - Libre 2': [550.60,552.49,'libre'],
        'canal 27 - Armonicos': [552.5,553.250,'usado'],
        'canal 27 - Libre 3': [553.260,553.64,'libre'],
        'canal 27 - Audio': [553.65,553.875,'usado'],
        'canal 27 - Libre 4': [553.88,554.00,'libre'],

        'canal 28 - Libre 1': [554.01,560.00,'libre'],

        'canal 29 - Libre 1': [560.01,560.249,'libre'],
        'canal 29 - Video': [560.250,562.00,'usado'],
        'canal 29 - Libre 2': [562.01,564.49,'libre'],
        'canal 29 - Armonicos': [564.5,565.05,'usado'],
        'canal 29 - Libre 3': [565.06,565.67,'libre'],
        'canal 29 - Audio': [565.68,565.81,'usado'],
        'canal 29 - Libre 4': [565.82,566.00,'libre'],

        'canal 30 - Libre 1': [566.01,572.00,'libre'],
        }  
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    datos, espuria , descision =procesamiento3(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro) 
    return espectro, espuria, descision

def cuarta_iteracion_tv():

    f_min = 572e6
    f_max = 632e6
    
    
    canales ={

        'canal 31 - Libre 1': [572.01,572.49,'libre'],
        'canal 31 - Video': [572.50,574.00,'usado'],
        'canal 31 - Libre 2': [574.01,575.920,'libre'],
        'canal 31 - Armonicos': [575.925,577.25,'usado'],
        'canal 31 - Libre 3': [575.3,577.69,'libre'],
        'canal 31 - Audio': [577.7,577.81,'usado'],
        'canal 31 - Libre 4': [577.82,578.00,'libre'],

        'canal 32 - Libre 1': [578.01,584.00,'libre'],

        'canal 33 - Libre 1': [584.01,584.49,'libre'],
        'canal 33 - Video': [584.50,586.00,'usado'],
        'canal 33 - Libre 2': [586.01,588.649,'libre'],
        'canal 33 - Armonicos': [588.65,589.10,'usado'],
        'canal 33 - Libre 3': [589.2,589.68,'libre'],
        'canal 33 - Audio': [589.69,589.88750,'usado'],
        'canal 33 - Libre 4': [589.9,590.00,'libre'],

        'canal 34 - Libre 1': [590.01,590.34,'libre'],
        'canal 34 - Armonicos': [590.35,590.45,'usado'],
        'canal 34 - Libre 2': [590.46,596.000,'libre'],

        'canal 35 - Libre 1': [596.01,596.24,'libre'],
        'canal 35 - Video': [596.25,598.55,'usado'],
        'canal 35 - Libre 2': [598.56,599.95,'libre'],
        'canal 35 - Armonicos': [599.96,601.10,'usado'],
        'canal 35 - Libre 3': [601.2,601.68,'libre'],
        'canal 35 - Audio': [601.69,601.8250,'usado'],
        'canal 35 - Libre 4': [601.9,602.00,'libre'],

        'canal 36 - Libre 1': [602.01,608.00,'libre'],

        'canal 37 - Libre 1': [608.01,614.00,'libre'],

        'canal 38 - Libre 1': [614.01,620.00,'libre'],

        'canal 39 - Libre 1': [620.01,623.69,'libre'],
        'canal 39 - Armonicos': [623.7,623.9,'usado'],
        #'canal 39 - Libre 2': [624.00,624.00,'libre'],


        }  
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    datos, espuria , descision =procesamiento4(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision

def quinta_iteracion_tv():

    f_min = 626e6
    f_max = 686e6
   
    
    canales ={

        'canal 40 - Libre 1': [626.01,632.00,'libre'],
        'canal 41 - Libre 1': [632.01,638.00,'libre'],
        'canal 42 - Libre 1': [638.01,644.00,'libre'],
        'canal 43 - Libre 1': [644.01,650.00,'libre'],
        'canal 44 - Libre 1': [650.01,656.00,'libre'],
        'canal 45 - Libre 1': [656.01,662.00,'libre'],
        'canal 46 - Libre 1': [662.01,668.00,'libre'],
        'canal 47 - Libre 1': [668.01,674.00,'libre'],
        'canal 48 - Libre 1': [674.01,680.00,'libre'],
        'canal 49 - Libre 1': [680.01,686.00,'libre'],

        }  
    

    #Espectro: Diccionario con los datos de las frecuencias y sus Potencias
    datos, espuria , descision =procesamiento5(f_min,f_max,canales)      #descion = 1 hay espuria, 0 no hay espuria
    espectro = procesamiento_diccionarios(datos)
    #print (espectro)
    return espectro, espuria, descision