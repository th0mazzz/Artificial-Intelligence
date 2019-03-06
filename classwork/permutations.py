def perm(input_list):
    perm_help(input_list, 0)

def perm_help(input_list, current):
    if current == len(input_list) - 1:
        print input_list
    
    input_list[current], input_list[len(input_list) - 1] = (input_list[len(input_list) - 1], input_list[current])
    perm_help(input_list, current + 1)
    input_list[current], input_list[len(input_list) - 1] = (input_list[len(input_list) - 1], input_list[current])


#Test
#perm([0, 1, 2])

#this is Joan's code:
def permutation(L):
    if len(L) == 1:
        yield L
    else:
        for i in range(len(L)):
            for sp in permutation(L[:i] + L[i+1:]):
                yield [L[i]] + sp


permutation([0])
