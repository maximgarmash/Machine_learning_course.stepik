# Определение выбросов, используя простой метод анализа ондого признака

def exception_simple(x, average, deviation, symmetry):
	exception_list = []
	if symmetry:                       #проверка на симетричность
		for i in x:
			if i < (average - 3*deviation) or i > (average + 3*deviation): # является ли значение из вектора х выбросом
				exception_list.append(i)
	else:
		for i in x:
			if i < (average - 5*deviation) or i > (average + 5*deviation): # является ли значение из вектора х выбросом
				exception_list.append(i)
	return(exception_list)
