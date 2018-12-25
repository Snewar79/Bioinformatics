MasArrayHardCode  = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


pep_mass = int(input())

#Список под динамическое программирование
arr_for_dynamyc = []


arr_for_dynamyc.append(1)


for i in range(pep_mass + 1):
    arr_for_dynamyc.append(0)
	
	#Пройдем все ячейки до новой
    length = len(MasArrayHardCode)
    for j in range(length):
		
		
        if (i >= MasArrayHardCode [j]):
			#Рассчитаем нужный нам индекс
            index = i - MasArrayHardCode[j]
			#print(index)
			
            arr_for_dynamyc[i] += arr_for_dynamyc[index]
            
			
			
			
#print(arr_for_dynamyc[pep_mass])
print(arr_for_dynamyc[pep_mass])
