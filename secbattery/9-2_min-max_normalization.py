def min_max_normalize(lst) : 
    normalized = []
    
    for value in lst :
        normalized_num = (value - min(lst)) / (max(lst) - min(lst)) # 일정한 비율로 반환
        normalized.append (normalized_num)
        
    return normalized

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 24, 56, 74, 21, 11, 23, 52]

b = min_max_normalize(a)

print (b)