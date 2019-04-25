# Рассчет метрики как меры близости объектов друг к другу
# Новый коментарий

def evklid(vec1, vec2):                     # Евклидова метрика
    Sum = 0
    for i in range(len(vec1)):
        Sum += (vec1[i]-vec2[i])**2
    p = Sum**0.5
    return(round(p, 2))

def manhetten(vec1, vec2):                  # Метрика Манхеттен
    p = 0
    for i in range(len(vec1)):
        p += abs(vec1[i]-vec2[i])
    return(p)

def maxmetric(vec1, vec2):                  # Max-метрика
    list = []
    for i in range(len(vec1)):
        list.append(abs(vec1[i]-vec2[i]))
    p = max(list)
    return(p)