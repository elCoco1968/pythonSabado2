#Represa Hidroituango

#ENTRADAS
nivelAgua=float(input('Digite el nivel de agua: '))

#PROCESO
if nivelAgua>=0 and nivelAgua <= 250:
    print(f'El sensor marca {nivelAgua}, muy bajo... ') 
elif nivelAgua>250:
    print(f'El sensor marca {nivelAgua}, operando normal') 
else:
    print(f'El sensor marca {nivelAgua}, muy alto') 

    

