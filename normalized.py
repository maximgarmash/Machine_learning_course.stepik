# функция для нормирования вектора значений признака, используя максимальное и минимальное значение признака

def norm_max_min(P):  
    P_normalized = [(i - min(P))/(max(P)-min(P)) for i in P]
    return(P_normalized)

# функция для нормирования вектора значений признака, используя среднее значение признака и среднеквадратичное отклонение

def norm_average(P):
    P_average = sum(P)/len(P)                      #вычисление среднего арифметичекого вектора признаков
    Ssq = 0
    for i in P:                                    # Вычисление среднего отклонения
        Ssq += (1/(len(P)-1))*((i-P_average)**2)   
    S = Ssq**0.5
    P_normalized = [(i-P_average)/S for i in P]    #Рассчет по формуле 
    return(P_normalized)