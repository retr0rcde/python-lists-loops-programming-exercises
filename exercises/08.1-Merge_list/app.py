chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    merged = []
    for item in list1:
        merged.append(item)
    for item in list2:
        merged.append(item)
    return merged
    
print(merge_list(chunk_one, chunk_two))
