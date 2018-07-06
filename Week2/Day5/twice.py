def find_repeat(numbers_list):
    n = len(numbers_list)-1
    first_n_sum= n*(n+1)/2
   sumup = 0
    for i in numbers_list: 
       sumup += i
    return sumup- first_n_sum