def common_elements(list1,list2):
    return list(set(list1) & set(list2))
list1 = [1, 2, 3, "nesli", "alfa", "beta", 158, ]
list2 = [5, 2,"nesli", "forever", 45, "eskisehir", 148]
#setler içinde başka set olamaz
common= common_elements(list1,list2)
print(common)






    
