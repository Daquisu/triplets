def gabarito_cardinalidade(n):
    return round((n+3)**2/12) - (n//2 + 1)


def triplets_rapido(n):
    list_triplets = []
    n_total = gabarito_cardinalidade(n)
    end = False
    for i in range (n-2, 0, -1):
        if end:
            break

        max_k = n-i
        for k in range(1, max_k):
            j = n - i - k
            ordered_triplet = sorted([i, j, k], reverse=True)
            if ordered_triplet not in list_triplets:
                list_triplets.append(ordered_triplet)
                if len(list_triplets) == n_total:
                    end = True
                    break
    
    assert end, 'Logical error'

    return list_triplets

for i in range(7, 20):
    print(f'n = {i}, cardinalidade = {gabarito_cardinalidade(i)}.')
    print('Combinações:')
    print(sorted(triplets_rapido(i)))