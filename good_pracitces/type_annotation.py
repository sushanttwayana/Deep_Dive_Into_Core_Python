def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]


lst1 : list[str] = upper_everything(['May', 'June', 'july'])
# print(lst1)

# lst2 : list[int] = upper_everything([1, 2, 3])
# print(lst2)

# sample : list[int] = [1, 2, 'a', 'b']
sample : list[int] = ['a', 1, 2 , 'b']
# print(sample)

sample = [1, 2, "abc"]


names : list[str] = ['James', 'Cindrella', 'Bakayuga', 'Midoriya', 'Luffy']


long_names: list[str] = []

# for name in names:
#     if len(name) >= 7:
#         long_names.append(name)
        
        
        
long_names : list[str] = [name for name in names if len(name) >= 7 ]

print(f'Long names: {long_names}')    