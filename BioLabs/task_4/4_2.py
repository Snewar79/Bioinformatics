global_dict = ["A", "T", "G", "C"]


def everyPatternsK(_dict, _k): #В прошлый раз хватило различных для четырех, тут все же нужно для k
    my_patterns = _dict
	
    my_patterns = appender(my_patterns, _dict, _k - 1)

    return my_patterns
	
	
	
def appender(prew , _dict, how_more):
    if how_more == 0:
        return prew
    
    tmp = []
    # К каждому прикрепляем новую букву и рекурсивно добавляем следующие n - 1
    for i in prew:
        for j in _dict:
            tmp.append(i + j)
    return appender(tmp, _dict, how_more - 1)



def defference(pat1, pat2, out):  #Find the differing in two patterns # Просто возьмем из предыдущей лабы

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



k = int(input())


DNA = []



#while True:
 #   line = input()
#    if line == '':
 #       break
    # обработка
 #   print(line)



for i in range(10):
    DNA.append(input())




#Вводим данные


#Получаем все паттерны длины k    
patterns = everyPatternsK(global_dict, k)
    
    
#Нужно что-то для выбора ответа, как начальное условие. Возьмем первый попавшийся - нулевой


first_diff = 0

for iterator in DNA:
    tmp = []
    local_minimum = defference(patterns[0], iterator[0:k], tmp)
    
    right_border = len(iterator) - k + 1
    for i in range(0, right_border):
        right_pat_border = i + k
        #print(right_pat_border)
        local_diff = defference(patterns[0], iterator[i:right_pat_border], tmp)
        
        if local_diff < local_minimum:
            local_minimum = local_diff
        
    first_diff = first_diff + local_minimum

        
delta = first_diff

cur_ans = patterns[0]
    
    
    
count = len(patterns)


for it_pattern in range(1, count): # Проверим оставшиеся, вдруг они больше?
    
    
    next_diff = 0
    for iterator in DNA:
        tmp = []
        local_minimum = defference(patterns[it_pattern], iterator[0:k], tmp)
    
    
        right_border = len(iterator) - k + 1
        for i in range(0, right_border):
            right_pat_border = i + k
            #print(right_pat_border)
            local_diff = defference(patterns[it_pattern], iterator[i:right_pat_border], tmp)
        
            if local_diff < local_minimum:
                local_minimum = local_diff
        
        next_diff = next_diff + local_minimum

    
    if delta > next_diff:
        delta = next_diff
        cur_ans = patterns[it_pattern]
        
        
print(cur_ans)
