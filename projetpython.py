import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#os.chdir('C:\\Users\\22bla\\Documents\\Damien Ecole\\Info') chemin d'accès

df=pd.read_csv('EIVP_KM.csv', sep=';', index_col='sent_at', parse_dates=True)



unites={ 'temp':'°C', 'noise':'dBA' , 'lum':'lux', 'co2':'ppm' , 'humidity':'%' }
variable_dico={'temp':'température','noise':'bruit','lum':'luminosité','co2':'CO_2','humidity':'humidité relative'}

##Statistiques

def minimum():
    M=[]#on crée la liste des minimums pour chaque capteur sélectioné
    i_mini=0 #on initialise l'indice de la valeur minimale
    I=[]#on crée la liste des indices des minimums pour chaque capteur sélectioné

    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')
    L=[int(el) for el in input('choix des capteurs de 1 à 6 (ex: 1 3 5):').split()]  #on choisit la combinaison de capteurs souhaités.
        
        
    for capteur in range(len(L)):  #on parcourt la liste des capteurs sélectionnés
        
        df[df['id']==L[capteur]][variable][d:f].plot(label=f' capteur {L[capteur]}') #on affiche la courbe de la variable sélectionnée
        
        Min=df[df['id']==L[capteur]][variable][0] #Initialisation
        
        for k in range(len(df[df['id']==L[capteur]][d:f].index)-1):#on parcourt toutes les valeurs de la Serie dans la plage temporelle sélectionnée.
            
            if df[df['id']==L[capteur]][variable][d:f][k+1] < Min: #comparaison des valeurs au minimum en cours.
                i_mini = k+1 #on stocke l'indice de la valeur minimale en cours.
                Min = df[df['id']==L[capteur]][variable][d:f][k+1] #on actualise la valeur du minimum
        
        M.append(Min) #on stocke la valeur minimale du capteur qu'on est en train de parcourir.
        I.append(i_mini)  #on stocke également son indice
     
    
    Minimum = min(M)   #Ici on s'autorise à utiliser la bibliothèque python pour calculer le minimum de la liste et éviter à faire une boucle for en plus.
    Indice_du_minimum = I[M.index(Minimum)] #Identification de l'indice correspondant
    
    #on relève les caractétistiques (date précisément indexée sous le format Timestamp)de la valeur minimale pour pouvoir afficher le point avec .index:
    A = df[df['id']==L[M.index(Minimum)]][variable][d:f].index[Indice_du_minimum]           
    
    df[df['id']==L[M.index(Minimum)]][variable][A._repr_base:A._repr_base].plot(label='minimum',marker='o',color='r') #affiche la valeur minimum
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title(f'Le minimum est de {Minimum} ' + unites[f'{variable}'])
    plt.legend()   
    plt.show()

def maximum():  #exactement le même prcoédé que la fonction précédente
    M=[]#on crée la liste des maximum pour chaque capteur sélectioné
    i_maxi=0 #on initialise l'indice de la valeur maximale
    I=[]#on crée la liste des indices des maximum pour chaque capteur sélectioné

    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')
    L=[int(el) for el in input('choix des capteurs de 1 à 6 (ex: 1 3 5):').split()]  #on choisit la combinaison de capteurs souhaités.
        
        
    for capteur in range(len(L)):  #on parcourt la liste des capteurs sélectionnés
        
        df[df['id']==L[capteur]][variable][d:f].plot(label=f' capteur {L[capteur]}') #on affiche la courbe de la variable sélectionnée
        
        Max=df[df['id']==L[capteur]][variable][0] #Initialisation
        
        for k in range(len(df[df['id']==L[capteur]][d:f].index)-1):#on parcourt toutes les valeurs de la Serie dans la plage temporelle sélectionnée.
            
            if df[df['id']==L[capteur]][variable][d:f][k+1] > Max: #comparaison des valeurs au maximum en cours.
                i_maxi = k+1 #on stocke l'indice de la valeur maximale en cours.
                Max = df[df['id']==L[capteur]][variable][d:f][k+1] #on actualise la valeur du maximum
        
        M.append(Max) #on stocke la valeur maximale du capteur qu'on est en train de parcourir.
        I.append(i_maxi)  #on stocke également son indice
     
    
    Maximum = max(M)   #Ici on s'autorise à utiliser la bibliothèque python pour calculer le maximum de la liste et éviter à faire une boucle for en plus.
    Indice_du_maximum = I[M.index(Maximum)] #Identification de l'indice correspondant
    
    #on relève les caractétistiques (date précisément indexée sous le format Timestamp)de la valeur minimale pour pouvoir afficher le point avec .index:
    A = df[df['id']==L[M.index(Maximum)]][variable][d:f].index[Indice_du_maximum]           
    
    df[df['id']==L[M.index(Maximum)]][variable][A._repr_base:A._repr_base].plot(label='maximum',marker='o',color='r') #affiche la valeur maximum
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title(f'Le maximum est de {Maximum} ' + unites[f'{variable}'])
    plt.legend()   
    plt.show()
    
def min_max(): #on calcule les min et max journaliers
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    df.loc[d:f,variable].resample('D').min().plot(label='min')
    df.loc[d:f,variable].resample('D').max().plot(label='max')
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title('Minimum et Maximum journaliers')
    plt.legend() 
    plt.show()
    
def moyenne():   #on calcule la moyenne journalière
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    df[variable][d:f].resample('D').mean().plot(label='',ls=':')
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title('Moyenne journalière')
    plt.show()

def min_max_moy(): #on projette les min et max plus la moyenne par jour, on utilise ici .aggreagate pour regrouper facilement les valeurs statistiques
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    d=df[variable][d:f].resample('D').agg(['mean','min','max'])
    
    
    d['mean'].plot(label='Moyenne',ls=':')#on affiche la moyenne
    d['max'].plot(label='',ls='-',color='r')
    d['min'].plot(label='',ls='-',color='r')
    plt.fill_between(d.index, d['min'],d['max'],alpha=0.2,label='Ecart Min-Max par jour') #on affiche min et max
    
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title('Minimum Maximum et Moyennes journaliers')
    plt.legend() 
    plt.show()

def ecart_type():
    capteur=int(input("entrer un id du capteur:"))
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')

    fig, ax1 = plt.subplots(figsize=(10,4))                 #on paramètres les deux axes ordonnées, un pour la moyenne, l'autre pour l'ecart-type
    ax2 = ax1.twinx()
    
    ax1.plot(df[df["id"]==capteur][variable][d:f].resample('D').mean().index , df[df['id']==capteur][variable][d:f].resample('D').mean(),color='r',label='Moyenne')
    ax1.set_ylabel(unites[f'{variable}'])
    
    ax2.bar(df[df["id"]==capteur][variable][d:f].resample('D').std().index , df[df['id']==capteur][variable][d:f].resample('D').std(),color='b',alpha=0.2,label='Ecart-type')

    plt.title( 'Evolution de la moyenne de la variable ' + variable_dico[f'{variable}'] + " et son ecart-type" )
    plt.legend()
    plt.show()
 
def mediane():  

    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    return (df[variable][d:f].median())

def variance(): #sur le même principe que l'ecart-type
    capteur=int(input("entrer un id du capteur:"))
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')

    fig, ax1 = plt.subplots(figsize=(10,4))
    ax2 = ax1.twinx()
    
    ax1.plot(df[df["id"]==capteur][variable][d:f].resample('D').mean().index , df[df['id']==capteur][variable][d:f].resample('D').mean(),color='r',label='Moyenne')
    ax1.set_ylabel(unites[f'{variable}'])
    
    ax2.bar(df[df["id"]==capteur][variable][d:f].resample('D').var().index , df[df['id']==capteur][variable][d:f].resample('D').var(),color='b',alpha=0.2,label='variance')

    plt.title( 'Evolution de la moyenne de la variable ' + variable_dico[f'{variable}'] + " et sa variance" )
    plt.legend()
    plt.show()

def correlation():
 
    variable1=input('entrer une variable (temp,humidity,co2,noise,lum):')
    variable2=input('entrer une deuxieme variable (temp,humidity,co2,noise,lum):')
    
    f = plt.figure()
    ax = f.add_subplot(111)

    df[variable1].plot(label='evolution de la variable ' +variable_dico[f'{variable1}'] )
    df[variable2].plot(label='evolution de la variable ' +variable_dico[f'{variable2}'] )#Affichage des deux courbes représentant les deux variables en fonction du temps.
    
    indice = df[variable1].corr(df[ variable2]) #indice de corrélation entre les deux variables

    
    plt.text(0.5,0.5,f"l'indice de correlation est {indice}",horizontalalignment='center',
     verticalalignment='center', transform = ax.transAxes, fontsize=7, color='r')#Indication dans la console de la valeur de l’indice de corrélation

    plt.legend()
    plt.show() 


def humidex():
    
    d=input('date debut:')
    f=input('date fin:')
    
    df['alpha']=((17.27*df['temp'])/(237.7+df['temp']))+np.log(df['humidity']/100)
    df['temp_rosée']=(237.7*df['alpha'])/(17.27-df['alpha'])
    df['humidex']= df['temp']+0.555*(6.11*np.exp(5417.7530*((1/273.16)-1/(273.15+df['temp_rosée'])))-10)
    
    
    df['humidex'][d:f].plot()

    plt.ylabel('°C')
    plt.title('Indice humidex au cours du temps')
    plt.show()

    
##L’évolution d’une variable en fonction du temps

def evolution():
        variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
        d=input('entrer date début (exemple 2020-09):')
        f=input('entrer date fin:')
        L=[int(el) for el in input('choix des capteurs de 1 à 6 (ex: 1 3 5):').split()]
        
        
        for k in range(len(L)):  #on parcourt la liste des capteurs sélectionnés
                df[df['id']==L[k]][variable][d:f].plot(label=f' capteur {L[k]}') # et on dessine le graphique correspondant au capteur 'id' pour la variable et la plage horaire choisies
        plt.title( 'Evolution de la ' + variable_dico[f'{variable}'])
        plt.ylabel(unites[f'{variable}'])
        plt.legend()               
        plt.show()
        
     
 ##Anomalies   
    


def anomalie_arret():
    V=['temp','noise','lum','co2','humidity'] # on crée la liste des variables pour pouvoir la parcourir.
    capteur_defiant=0   # on initialise la variable qui va nous permettre d'identifier le capteur défiant.
    
    for variable in V:
        
        for capteur in range(1,7):
            
            for k in range(len(df[df['id']==capteur].index)-1):    #on parcourt toutes les données du capteur, choisi avec la boucle for précédente.
                
                T = df[df['id']==capteur].index[k+1] - df[df['id']==capteur].index[k] #on calcule la différence de temps écoulé entre deux prises de mesures. Il s'agit d'un Timedelta.
                
                if T.components.days!=0:   #si le temps entre deux mesures dépasse un jour on considère qu'il s'agit d'une anomalie d'interruption du capteur.
                    
                    indice=k
                    A=df[df['id']==capteur].index[indice]  # on relève les caractétistiques des deux valeurs entre lesquelles le temps écoulé dépasse un jour. Il s'agit d'un Timestamp
                    B=df[df['id']==capteur].index[indice+1]
                    
                    capteur_defiant=capteur
                    
                    df[df['id']==capteur][variable][A._repr_base:B._repr_base].plot(label=f'Arrêt du capteur {capteur}',ls=":",lw=5,color='r')   
                    #on représente alors toutes les valeurs qui ont présentées cette anomalie. Le module ._repr_base donne la date exacte
                    
            if capteur_defiant==capteur:   #Si un capteur défiant a été détecté alors on représente la courbe de la variable et du capteur concerné en totalité.
                
                df[df['id']==capteur_defiant][variable].plot(label=f'Capteur {capteur_defiant}')
                plt.title(f'Evolution de la variable "{variable}" en fonction du temps')
                plt.legend()
                plt.show()
    print(f'Le capteur qui présente une anomalie d arrêt est le capteur "{capteur_defiant}"')
    

    
def anomalie_valeur():
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')  
    L=[int(el) for el in input('choix des capteurs de 1 à 6 (ex: 1 3 5):').split()]
        
        
    for capteur in range(len(L)):  #on parcourt la liste des capteurs
        
        anomalie_1, anomalie_2, anomalie_3, anomalie_4 = 0, 0, 0, 0   # on initialise 4 degrés d'anomalies pour chaque capteur
    
        for k in range(len(df[df['id']==L[capteur]][d:f].index)-1):  #on parcourt les valeurs du tableau du capteur correspondant.
            
            D=np.abs(df[df['id']==L[capteur]][variable][d:f][k] - df[df['id']==L[capteur]][variable][d:f].resample('D').mean()[df[df['id']==L[capteur]][variable][d:f].index[k]._date_repr])
        
            # D est la différence entre la valeur d'une variable (d'indice k) pour un capteur donné( L[capteur] ) et la valeur moyenne de cette variable sur la journée.
            
            s=df[df['id']==L[capteur]][variable][d:f].std()
            
            # s est l'écart-type
            # Une valeur présentant un écart à la moyenne inférieur à l'écart type est banale, compris entre une et deux fois l'écart type est modérément courante, compris entre deux et trois fois l'écart type commence a être remarquable,compris entre trois et quatre fois l'écart type est exceptionnelle, supérieur à quatre fois l'écart type est historique et très rare.
            
            if D>=s and D<2*s:
                            df[df['id']==L[capteur]][variable][d:f][k:k+1].plot(label='',lw=2,color='g',marker='o')   #on affiche les points pour les anomalies détéctées grâce à l'indice k
                            anomalie_1+=1
            
            if D>=2*s and D<3*s:
                            df[df['id']==L[capteur]][variable][d:f][k:k+1].plot(label='',lw=2,color='r',marker='o')
                            anomalie_2+=1
            
            if D>=3*s and D<4*s:
                            df[df['id']==L[capteur]][variable][d:f][k:k+1].plot(label='',lw=2,color='m',marker='o')
                            anomalie_3+=1
            
            if D>=4*s:
                            df[df['id']==L[capteur]][variable][d:f][k:k+1].plot(label='',lw=2,color='k',marker='o')
                            anomalie_4+=1
        if anomalie_4>=1:
            print(f'il existe au moins une anomalie extrême pour le capteur {L[capteur]}') 
        if anomalie_3>1:
            print(f'il existe des anomalies exceptionnelles pour le capteur {L[capteur]}')
        if anomalie_3>1:
            print(f'il existe des anomalies remarquables pour le capteur {L[capteur]}')
        if anomalie_2>1:
            print(f'il existe des anomalies courantes pour le capteur {L[capteur]}')
        
        df[df['id']==L[capteur]][variable][d:f].plot(label=f'capteur {L[capteur]}')
    plt.title('vert : anomalie courante \\ rouge : anomalie courante \\  magenta : anomalie exceptionnelle \\  noire : anomalie rare ')
    plt.figure(figsize=(20,10))
    plt.legend()
    plt.show()
    
    

    
def occupation():
    H,J=[],[] #Deux listes pour les horaires et les journées correspondantes
    capteur=int(input('entrer un id du capteur:'))
    
    for k in range(len(df[df['id']==capteur].index)-1):
    
        if df[df['id']==capteur]['co2'][k]>490 :  #on considère que la salle est occupée à partir de 490ppm, pour ne pas prendre en compte les week-end.
            
            indice=k
            A=df[df['id']==capteur].index[indice]
            
            Jour=A._date_repr    #Donnée du jour
            Horaire=A._time_repr #Donnée de l'horaire
            H.append(Horaire)
            J.append(Jour)
                
            
            
            df[df['id']==capteur]['co2'][A._repr_base:A._repr_base].plot(marker='o',color='r',label='occupation moyenne de la salle')  #on parcourt toutes les données du capteur
    
    #On peut aussi créer un dataframe avec les horaires d'occupation
    data = {'Periode_occupation': H , 'Jour':J}
    Tab = pd.DataFrame(data=data)
    Tab['Jour']=pd.to_datetime(SE.Jour) #on met le format jour en datetime
    
    df[df['id']==capteur]['co2'].plot(label='co2')  #on affiche la courbe co2   
   
    plt.show()
    print("Les horaires d'occupation: ", H,Tab)
