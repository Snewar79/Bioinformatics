# Ну как всегда
HardCodeTable = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}


def RING(_peptide):	
	out = [0]

	for i in range(1, len(_peptide)):
	
		length = len(_peptide)		

		for j in range(length):
		
			subpep = []
			
			
			ost = i if i <= len(_peptide) - j else len(_peptide) - j
			
			stump = i - ost
			
			subpep += _peptide[j:j + ost]
			subpep += _peptide[0:stump]
			
			add_mass(subpep, out)



	out.sort()
	add_mass(peptide, out)
	#print(out)
	return out


def add_mass(_pep, _mas):
	out_mass = 0
	for i in _pep:
		out_mass += HardCodeTable.get(i)
	_mas += [out_mass]



#run
peptide = input()

inp_data = input()
#print(inp_data)

list = inp_data.split(' ')

spectrum = []
for i in range(len(list)):
    spectrum.append(int(list[i]))
	
	
#Ввели данные

dict_sort_list = sorted(set(HardCodeTable.values()))


pep_spectrum = RING(peptide)

tmp = spectrum
	
balls = 0
	
for mass in pep_spectrum:
	if mass in tmp:
		tmp.remove(mass)
		balls += 1


print(balls)

#изи лаба
