def deviation(P, P_average):         # Вычисление среднего отклонения
    Ssq = 0
    for i in P:                                    
        Ssq += (1/(len(P)-1))*((i-P_average)**2)   
    S = Ssq**0.5
    return(S)
