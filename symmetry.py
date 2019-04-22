# Проверка выборки на симметричность

def symmetry(median, average, deviation, n):                
	if abs(average - median) <= 3*deviation/(n**0.5):
		return(True)
	else:
		return(False)
