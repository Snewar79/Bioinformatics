HardCodeTable = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
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

def sum_of_pep_mass(pep):
	out = 0
	
	for i in pep:
		out = out + i
		
	return out



def fill(peptides):	
	out = []

	if peptides:
		for peptide in peptides:
			for i in dict_sort_list:
				
				new_peptide = peptide[:]
				
				new_peptide.append(i)
				
				
				out.append(new_peptide)
				
				
	else:
			for i in dict_sort_list:
				out.append([i])
				
				
				
	return out	




def add_mass(_pep, _mas):
	out_mass = 0
	for i in _pep:
		out_mass += i
	_mas += [out_mass]


def check_includes(peptide, spectrum):
	#Проверим соответствие спектра и пептида
	peptide_spectrum = [0]


	
	for i in range(1, len(peptide)):
		for j in range(len(peptide) - i + 1):
			add_mass(peptide[j:j + i], peptide_spectrum)
						
			
	peptide_spectrum.sort()
	
	
	add_mass(peptide, peptide_spectrum)
	
	tmp = spectrum.copy()
	
	#print(tmp)
	
	
	for i in peptide_spectrum:
		if i in tmp:
			tmp.remove(i)
		else:
			return False
			
			
	#print(tmp)
	if sum_of_pep_mass(peptide) in spectrum:
		return True
	else:
		return False


# 
dict_sort_list = sorted(set(HardCodeTable.values()))


inp_data = input()
#print(inp_data)

list = inp_data.split(' ')
#aaagrhhhh
spectrum = []
for i in range(len(list)):
    spectrum.append(int(list[i]))
#print(spectrum)

# run

peptides = []
		
peptides = fill(peptides)
	
#print(peptides)
while peptides:	
	
	
	delete_elem = []
	for peptide in peptides:
		
		
		if sum_of_pep_mass(peptide) == (spectrum[ len(spectrum) - 1 ]):
		
		
			if RING(peptide) == spectrum:
				for i in range(len(peptide)):
					print(peptide[i], end = "-" if i < len(peptide) - 1 else " ")
					
			delete_elem.append(peptide)
			
			
		elif not check_includes(peptide, spectrum):
		
			delete_elem.append(peptide)
			# Отвегнуть
			
			#Удалим лишние
	for iter in delete_elem:
			peptides.remove(iter)
		
	# Если остались
	if peptides:
			peptides = fill(peptides)
		

