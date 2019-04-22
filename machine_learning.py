#вычисление среднего арифметичекого вектора признаков

def average(P):                                           
    P_average = sum(P)/len(P)
    return(P_average)

# Вычисление среднего отклонения

def deviation(P, P_average):                    
    Ssq = 0
    for i in P:
        Ssq += (1/(len(P)-1))*((i-P_average)**2)   
    S = Ssq**0.5
    return(S)

# Рассчет метрики как меры близости объектов друг к другу

def evklid(vec1, vec2):                                                       # Евклидова метрика
    Sum = 0
    for i in range(len(vec1)):
        Sum += (vec1[i]-vec2[i])**2
    p = Sum**0.5
    return(round(p, 2))

def manhetten(vec1, vec2):                                                    # Метрика Манхеттен
    p = 0
    for i in range(len(vec1)):
        p += abs(vec1[i]-vec2[i])
    return(p)

def maxmetric(vec1, vec2):                                                    # Max-метрика
    list = []
    for i in range(len(vec1)):
        list.append(abs(vec1[i]-vec2[i]))
    p = max(list)
    return(p)
# функция для нормирования вектора значений признака,
# используя максимальное и минимальное значение признака

def norm_max_min(P):  
    P_normalized = [(i - min(P))/(max(P)-min(P)) for i in P]
    return(P_normalized)

# функция для нормирования вектора значений признака,
# используя среднее значение признака и среднеквадратичное отклонение

def norm_average(P):
    P_average = sum(P)/len(P)                                                 #вычисление среднего арифметичекого вектора признаков
    Ssq = 0
    for i in P:                                                               # Вычисление среднего отклонения
        Ssq += (1/(len(P)-1))*((i-P_average)**2)   
    S = Ssq**0.5
    P_normalized = [(i-P_average)/S for i in P]                               #Рассчет по формуле 
    return(P_normalized)

# Проверка выборки на симметричность

def symmetry(median, average, deviation, n):                
	if abs(average - median) <= 3*deviation/(n**0.5):
		return(True)
	else:
		return(False)

# Определение выбросов, используя простой метод анализа ондого признака

def exception_simple(x, average, deviation, symmetry):
	exception_list = []
	if symmetry:                                                              #проверка на симетричность
		for i in x:
			if i < (average - 3*deviation) or i > (average + 3*deviation):    # является ли значение из вектора х выбросом
				exception_list.append(i)
	else:
		for i in x:
			if i < (average - 5*deviation) or i > (average + 5*deviation):    # является ли значение из вектора х выбросом
				exception_list.append(i)
	return(exception_list)