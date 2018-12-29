
global_dict = ["A", "T", "G", "C"]


def everyPatternsK(dict, _k): #fix #Find all variants of words by char in dict
    my_patterns = []
	
    for i in dict:
        for j in dict:
            for k in dict:
                for m in dict:
                    my_patterns.append(i + j + k + m)

    return my_patterns
	
	
	
	
	

def defference(pat1, pat2, out):  #Find the differing in two patterns

    diff_count = 0
	
    count = len(pat1)
	
    iterator = 0
	
    for i in range(0, count): # first pattern iterator
        if pat1[i] == pat2[iterator]:
            iterator = iterator + 1 #all is ok. Nothing to do
        else:
            diff_count = diff_count + 1 #not equal! Adding +1 in defference
            iterator = iterator + 1		

    out = diff_count
    return diff_count




def shorter(pat, ref): # func del equal. Not use
    
    print("pat-----------\n")
    print(pat)
    print("pat_e-----------\n")
    pat_len = len(pat)
    ref_len = len(ref)
	
    for i in range(0, pat_len):
        flag = False
        for j in range(0, ref_len):
            if pat[i] == ref[j]:
                flag = True
		
        if (flag == False):
            ref.append(pat[i])
			
    ref = ' '.join(ref)
	
    return ref

inp = input()

tmp_list = inp.split(" ")

k = tmp_list[0];
d = tmp_list[1];

k = int(k)
d = int(d)
DNA = []




for i in range(k):
    DNA.append(input())

#input data block is end


patterns = []
count = 0

DNA_pat_count = len(DNA)

for iterator in range(0, DNA_pat_count):

    gr  = len(DNA[iterator]) - k + 1
	
	
    for i in range(gr):
	
	
        all_pat = everyPatternsK(global_dict, k) 
        
        all_pat_len = len(all_pat)
		
		#for each k patterns in dna
        for g in range(0, all_pat_len):
            tmp_pat = all_pat[g]
            tmp_out = []
			
			#finde string to check on equal
            pat_to_check_1 = DNA[iterator][i:i + k]
           
			#chek the difference		
            if defference(tmp_pat, pat_to_check_1, tmp_out) > d:
                count = 0
            else:
                count = 0				
				#for each differing from Pattern by at mos d mismatches
                for iterator_2 in range(0, DNA_pat_count):
                    gr_2 = len(DNA[iterator_2]) - k + 1
                    for j in range(0, gr_2):
						
                        gr_3 = j + k
						#print(gr_3)
                        pat_to_check = DNA[iterator_2][j:gr_3]
						
						
                        local_dif = defference(tmp_pat, pat_to_check, tmp_out)
                        local_dif = abs(local_dif)
                        if  local_dif <= d:
                            count = count +  1
                            break
							
				#add pattern' to patterns
                if count == DNA_pat_count:
                    patterns.append(tmp_pat)
    
	
	
	
	
	

	
	
	
	
	# Del not diff patterns
ans = []
length = len(patterns)
	
for i in range(0, length):
    flag = False
    for j in ans:
        if (patterns[i] == j):
            flag = True
    if flag == False:
        ans.append(patterns[i])

ans = " ".join(ans)
	
print(ans)

