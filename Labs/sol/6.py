# def zipIt(*lists):
#     print(lists)
#     print(len(lists))
#     max_elements = 0
#     for l in lists:
#         count_of_list_elements = len(l)
#         if(count_of_list_elements > max_elements):
#             max_elements = count_of_list_elements

#     for l in lists:
#         for i in max_elements:


# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# zipIt(l1, l2)
# # zipIt([1, 2, 3])
# # zipIt(['a', 'b', 'c'])

def zipIt(l1, l2):
    result = []
    i = 0
    while (i < len(l1) and i < len(l2)):
        result.append((l1[i], l2[i]))
        i += 1

    return result


l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']
l = zipIt(l1, l2)
print(l)
