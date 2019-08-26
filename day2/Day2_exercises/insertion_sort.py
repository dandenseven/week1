our_list = [1, 2, 0, 8, 6, 23]

def insetion_sort(a_lists):
    n = len(a_lists)
    total = 0

    for i in range(1, n):
        key = a_list[i] 
        j = i-1

        while j >= 0 and key > a_list[j]:
            a_list[j + 1] = a_list[j]
            j -= 1
        total +=

        a_list[j + 1] = key
        #print("Total:  (), List:;'.format(total), a_list)
        #input()
    return a_list, total