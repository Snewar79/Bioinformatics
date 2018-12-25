def mass_in_answer(_pep, _mas):
	
	#print _mas;
	Mass = 0
	
	for amin in _pep:
		Mass += MasArrayHardCode.get(amin)
	_mas += [Mass]



# Захардкодим табличку
MasArrayHardCode = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137,  'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 'Y' : 163, 'V' : 99 
}


peptyde_input_str = input()
peptyde_size = len(peptyde_input_str)

answer = [0]

for i in range(1, peptyde_size):
	for j in range(0, peptyde_size):
		subpeptyde = ""
		tail = i if i <= peptyde_size - j else peptyde_size - j
		
		stump = i - tail
		
		
		subpeptyde += peptyde_input_str[j:j+tail]
		
		subpeptyde += peptyde_input_str[0:stump]
		mass_in_answer(subpeptyde, answer)
		
		
		
#Отсортируем
answer.sort()

#Добавим последнюю
mass_in_answer(peptyde_input_str, answer)


for mass in answer:
	print(mass, end=" ")
