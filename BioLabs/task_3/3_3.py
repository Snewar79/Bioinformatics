import functools as ft

HardCodeTable = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}



def add_mass(_pep, _mas):
	out_mass = 0
	for i in _pep:
		out_mass += i
	_mas += [out_mass]




def mass(peptide):
	out = 0
	
	for i in peptide:
		out += i
		
	return out


	
def parent_mass(spectrum, length):
	return spectrum[ len(spectrum) - 1 ]

		
def linear_scoring(peptide, spectrum):

	if not peptide:
		return 0

	
	
	
	# Линейно
	
	tmp = [0]

	for i in range(1, len(peptide)):
		for j in range(0, len(peptide) - i + 1):
			add_mass(peptide[j:j + i], tmp)
			
			
			
    
	tmp.sort()
	
	
	add_mass(peptide, tmp)

	pep_spectrum = tmp.copy()

	
	copy_of_spec = spectrum.copy()
	
	
	balls = 0
	
	for mass in pep_spectrum:
		if mass in copy_of_spec:
			copy_of_spec.remove(mass)
			balls = balls +  1

	return balls
		


def score_cmp(first, second, spectrum):
	return linear_scoring(second, spectrum) - linear_scoring(first, spectrum)
	
	
	

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

	
	

def cmp_to_key(cmp, spectrum):
	
	
	class cmp_cl:
		def __init__(self, obj, *args):
			self.obj = obj
		def __lt__(self, other):
			return cmp(self.obj, other.obj, spectrum) < 0
		def __gt__(self, other):
			return cmp(self.obj, other.obj, spectrum) > 0
		def __eq__(self, other):
			return cmp(self.obj, other.obj, spectrum) == 0
		def __le__(self, other):
			return cmp(self.obj, other.obj, spectrum) <= 0
		def __ge__(self, other):
			return cmp(self.obj, other.obj, spectrum) >= 0
		def __ne__(self, other):
			return cmp(self.obj, other.obj, spectrum) != 0
        
        
        
	return cmp_cl	
	
	


#run
pep_len = int(input())


inp_data = input()
#print(inp_data)

list = inp_data.split(' ')
#aaagrhhhh
spectrum = []
for i in range(len(list)):
    spectrum.append(int(list[i]))
#print(spectrum)


dict_sort_list = sorted(set(HardCodeTable.values()))




active_list = []


active_list = fill(active_list)


first_pep = []



	
while active_list:	
    
    
    to_delete = []
		
    for peptide in active_list:
        
        
        
        if mass(peptide) == parent_mass(spectrum, 0):
            
            
            if linear_scoring(peptide, spectrum) > linear_scoring(first_pep, spectrum):
                first_pep = peptide

        elif mass(peptide) > parent_mass(spectrum, 0):
            to_delete.append(peptide)
						
						
						
    for i in to_delete:
        active_list.remove(i)
    
    n = pep_len
    
    sorted_leaderboard = sorted(active_list, key=cmp_to_key(score_cmp, spectrum))
    trimmed_s_l = sorted_leaderboard[:n]
    
    
    
    for pep in sorted_leaderboard[n:]:
        if linear_scoring(pep, spectrum) == linear_scoring(trimmed_s_l[-1], spectrum):
            trimmed_s_l.append(pep)
        else:
            break
			
			
    active_list = trimmed_s_l
       
    
    
		
    if active_list:
        active_list = fill(active_list)
		
#print(first_pep)



for i in range(len(first_pep)):
    print(first_pep[i], end = "-" if i < len(first_pep) - 1 else " ")
















