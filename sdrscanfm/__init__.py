import matplotlib.pyplot as plt
import rtlsdr
import numpy as np
import time
import pandas as pd
from datetime import datetime
from sklearn.metrics import mean_squared_error
import pathlib
import time



def hacer_potencia(psd_max):
    potencia=10*np.log10(psd_max)
    return potencia


def setup(f_min, f_max,veces):
    #Frecuency range and step
   
    rate_best = 2.4e6
    df = rate_best
    


    # Set up the scan
    freqs = np.arange(f_min + df/2.,f_max,df)
    nfreq = freqs.shape[0]  
    npsd_res = 512  # frequency resolution (number of samples in psd)
    npsd_avg = 256  # number of PSDs to average
    nsamp = npsd_res*npsd_avg
    nfreq_spec = nfreq*npsd_res 
    samples = np.zeros([nsamp,nfreq],dtype='complex128') 

    #Setting the data lists 
    psd_array = np.zeros([npsd_res,nfreq])
    freq_array = np.zeros([npsd_res,nfreq])
    #time_array = np.zeros([npsd_res,nfreq],dtype='datetime64[s]')
    relative_power_array = np.zeros([npsd_res,nfreq])


    #Configuracion de dataframes para el MAXHOLD
    len=freq_array.shape[0]
    
    psd_total=np.empty([len*2,veces])

    return rate_best, freqs, nfreq, npsd_res, npsd_avg, nsamp, nfreq_spec, samples, psd_array, freq_array, relative_power_array, psd_total
#db microvoltio / metro

def readsdr(rate_best, freqs, nfreq, npsd_res, npsd_avg, nsamp, nfreq_spec, samples, 
    psd_array, freq_array, relative_power_array, psd_total,veces):
    #Initializing SDR
    sdr = rtlsdr.RtlSdr()
    sdr.sample_rate = rate_best
    sdr.gain = 2
    samp_rate = sdr.sample_rate 
    for k in range(veces):
        for i,freq in enumerate(freqs):
                sdr.center_freq = freq
                samples[:,i] = sdr.read_samples(nsamp)
    for i,freq in enumerate(freqs):   
        fc_mhz = freq/1e6
        bw_mhz = sdr.sample_rate/1e6  
        psd_array[:,i],freq_array[:,i] = plt.psd(samples[:,i], NFFT=npsd_res, Fs=bw_mhz, Fc=fc_mhz) #NFFT:The number of data points used in each block for the FFT.
    freq_series=np.concatenate(freq_array)
    psd_series=np.concatenate(psd_array)
    psd_total=np.insert(psd_total,k,psd_series,axis=1)
    sdr.close()
    psd_total=pd.DataFrame(psd_total)
    psd_new=psd_total.loc[:,0:veces-1]
    psd_max=psd_new.max(axis=1)
    max_hold=psd_max.apply(hacer_potencia)
    data_array = np.stack((freq_series, max_hold), axis=1)
    df=pd.DataFrame(data_array,columns=['Frecuencia','Potencia'])
    data= df.sort_values('Frecuencia',ascending=True)
    
    return data

def canal_filter(data,f_min_canal,f_max_canal):
    data_canal=data[(data['Frecuencia']>=f_min_canal) & (data['Frecuencia']<=f_max_canal)]
    data_canal=data_canal.reset_index(drop=True)
    return data_canal




def ploteo_senal_comparacion_y_referencia(data_canal,senal_referencia,senal_comparacion,key):
    #print(senal_comparacion) #82,1
    #print(senal_referencia) #82,
    #senal_comparacion = senal_comparacion.squeeze()
    #print(' el shape de senal comparacion: ')
    #print(senal_comparacion.shape)
    #print(senal_comparacion.shape) #82,1
    #print(senal_referencia.shape) #82,

    data_canal_freqs=data_canal['Frecuencia']
    data_canal_freqs = data_canal_freqs.to_numpy()
    referencia_numpy = senal_referencia.to_numpy()
    comparacion_numpy = senal_comparacion.to_numpy()

    referencia_signal = np.stack((data_canal_freqs,  referencia_numpy), axis=1)
    comparacion_signal = np.stack((data_canal_freqs,  comparacion_numpy), axis=1)
    #print(referencia_signal)
    #print(comparacion_signal)

    plt.subplot(2,1,1)
    plt.plot(referencia_signal[:,0],referencia_signal[:,1])
    plt.title('Senal de referencia')
    #plt.xlabel('Frecuencia [MHz]')
    plt.ylabel('Potencia [dB]')
    plt.subplot(2,1,2)
    plt.plot(comparacion_signal[:,0],comparacion_signal[:,1])
    plt.title('Senal de comparacion')
    plt.xlabel('Frecuencia [MHz]')
    plt.ylabel('Potencia [dB]')

    plt.suptitle('Senales de referencia y comparacion del: {}'.format(key))
    plt.show()



def comparacion(data_canal,senal_referencia,senal_comparacion,key):
    senal_comparacion=senal_comparacion.squeeze()
    #ploteo_senal_comparacion_y_referencia(data_canal,senal_referencia,senal_comparacion,key)

    '''    senal_referencia_numpy = senal_referencia.to_numpy()
    senal_comparacion_numpy = senal_comparacion.to_numpy()
    correlacion_signal = np.stack((senal_referencia_numpy,  senal_comparacion_numpy), axis=1)
    correlacion_df = pd.DataFrame(correlacion_signal,columns=['Referencia','Comparacion'])

    print(correlacion_df)'''

    '''senal_referencia_numpy = senal_referencia.to_numpy()
    senal_comparacion_numpy = senal_comparacion.to_numpy()

    corre = np.corrcoef(senal_referencia_numpy,senal_comparacion_numpy)
    print('La correlacion con numpy es : {}'.format(corre))'''
    
    corr=senal_referencia.corr(senal_comparacion)
    #print(corr)
    corr_validation=np.isnan(corr)
    if corr_validation==True:
        corr=0.2
    rmse=mean_squared_error(senal_referencia,senal_comparacion,squared=True)

    if rmse > 10:
        rmse_list=[]
        for i in range(50):
            rmse=mean_squared_error(senal_referencia,senal_comparacion,squared=True)
            rmse_list.append(rmse)
        rmse=min(rmse_list)
    return corr,rmse

def detection_limit(n,umbral,constante):
    #umbral = constante
    if n <= umbral: 
        return constante
    else:
        return n

def minima_senal_detectable_canal(data,umbral):
    #senal_referencia = data['Potencia'].apply(detection_limit,args=(-29,-29))   #args=-45,-45
    senal_referencia = data['Potencia'].apply(detection_limit,args=(umbral,umbral))
    #plt.plot(senal_referencia)
    return senal_referencia


#Senal referencia = Senal leida con el sdr y con la tranmision no deseada
#Senal comparacion = Senal creada a partir de la longitud del df y con los valores por defecto del umbral

def crear_senal_comparacion(senal_referencia,umbral):
    senal_comparacion=np.empty(senal_referencia.shape[0])
    senal_comparacion[:] = umbral
    '''senal_comparacion = senal_comparacion.squeeze()
    print(' el shape de senal comparacion: ')
    print(senal_comparacion.shape)'''
    senal_comparacion=pd.DataFrame(senal_comparacion)
    #print(senal_comparacion)
    return senal_comparacion
    

def filtrado_canal(data,f_min_canal,f_max_canal):
    data_canal=canal_filter(data,f_min_canal,f_max_canal)
    #umbral=data_canal['Potencia'].max()
    #senal_referencia=data_canal['Potencia'].apply(detection_limit,args=(umbral,umbral))
    return data_canal


def comparacion_senales(data_canal,senal_referencia,senal_comparacion,key):

    if senal_comparacion.shape[0] != senal_referencia.shape[0]:
        senal_comparacion=senal_comparacion[0:senal_referencia.shape[0]]
    corr,rmse = comparacion(data_canal,senal_referencia,senal_comparacion,key)     #compararmos la senal con la misma solo para probar 
    #coherencia = signal_coherence(senal_referencia,senal_comparacion)
    #print('La coherencia es: '+ str(coherencia))
    return corr,rmse


    
    
def procesamiento(f_min,f_max,canales,idx):
    veces=1
    rate_best, freqs, nfreq, npsd_res, npsd_avg, nsamp, nfreq_spec, samples, psd_array, freq_array, relative_power_array, psd_total= setup(f_min, f_max,veces)
    data=readsdr(rate_best, freqs, nfreq, npsd_res, npsd_avg, nsamp, nfreq_spec, samples, psd_array, freq_array, relative_power_array, psd_total,veces)
    #umbral,senal_referencia=minimun_signal_detectable(canales,data)

    for key in canales:
        values=canales[key]
        condicicon=values[2]
        if condicicon=='libre':
            
            f_min_canal=values[0]
            f_max_canal=values[1]

            data_canal=filtrado_canal(data,f_min_canal,f_max_canal)
            umbral = -48
            senal_referencia=minima_senal_detectable_canal(data_canal,umbral)
            senal_comparacion = crear_senal_comparacion(senal_referencia,umbral) 
            corr, rmse = comparacion_senales(data_canal,senal_referencia,senal_comparacion,key)
            #data_canal.to_csv(r'C:\Users\ggarc\Desktop\Tesis\matrizfm')
            CURRENT_DIR = pathlib.Path().resolve()  
            IMAGE_DIR=CURRENT_DIR.joinpath("app","static","images","fm")
            IMAGE_DIR = str(IMAGE_DIR)
            date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
            espectro = 'FM'


            if corr < 0.25 and rmse > 0.01 :
                maxim=data_canal['Potencia'].max()
                idmax=data_canal['Potencia'].idxmax()

                #print(rmse)
                if maxim > -200 and maxim < 200:
                    parasita = data_canal.loc[idmax]
                    max_freq=parasita['Frecuencia']
                    max_pot=parasita['Potencia']

                    

                    espuria={
                        'Fecha':date,
                        'Espectro':espectro,
                        'Potencia':max_pot,
                        'Frecuencia':max_freq,  
                    }

                    descision = 1 

                    '''plt.subplot(3,1,1)
                    plt.plot(data_canal['Frecuencia'],data_canal['Potencia'])
                    plt.title('Senal Electromagnetica de '+str(key))
                    plt.subplot(3,1,2)
                    plt.plot(senal_referencia)
                    plt.title('Senal Referencia')
                    plt.subplot(3,1,3)
                    plt.plot(senal_comparacion)
                    plt.title('Senal Comparacion')
                    plt.show()'''
                            
                    print('La transmision no deseada se encuentra en {} con una potencia de: {}'.format(max_freq,max_pot))


                    data_numpy=data.to_numpy() 
                    plt.switch_backend('agg')                 
                    plt.clf()                 
                    plt.plot(data_numpy[:,0],data_numpy[:,1])
                    plt.plot(espuria['Frecuencia'],espuria['Potencia'],marker='o',color='r',markersize=10)
                    plt.grid()
                    #plt.title('Grafica de la iteracion {} del espectro de Radio FM de: {} a {} [MHz]'.format(idx,f_min/1e6,f_max/1e6))
                    plt.xlabel('Frecuencia [MHZ]')
                    plt.ylabel('Potencia [dB]')
                    plt.savefig(IMAGE_DIR+'\espectro_iteracion_{}.png'.format(idx))
                    
                    #plt.show()


                    return data,espuria,descision

                    #Para la app web mandas un diccionario con 1 si hay una frecuencia parasita y el valor de la frecuencia y 0 si no hay frecuencia parasita
            else:
                print('No hay interferencia en el ' + str(key))
                print('El rmse es: '+ str(rmse))
                print('La correlacion es ' + str(corr))
                print('*'*50)
                espuria={
                        'Espectro':espectro,
                        'Fecha': date,
                        'Potencia':0,
                        'Frecuencia':0,
                    }
                descision = 0

    data_numpy=data.to_numpy()                  
    plt.switch_backend('agg')                 
    plt.clf()
    plt.plot(data_numpy[:,0],data_numpy[:,1])
    plt.grid()
    #plt.title('Grafica de la iteracion {} del espectro de Radio FM de: {} a {} [MHz]'.format(idx,f_min/1e6,f_max/1e6))
    plt.xlabel('Frecuencia [MHZ]')
    plt.ylabel('Potencia [dB]')
    plt.savefig(IMAGE_DIR+'\espectro_iteracion_{}.png'.format(idx))
    
    #plt.show()
    return data,espuria,descision
    




def procesamiento_diccionarios(datos):
    datos.set_index('Frecuencia',inplace=True)
    datos=datos.rename_axis('Frecuencia')
    datos_potencia = datos['Potencia'].tolist()
    datos=datos.to_dict(orient='split')
    del datos['columns']
    espectro = {
        'Frecuencia': datos['index'],
        'Potencia': datos_potencia,
    }
    return espectro
    
