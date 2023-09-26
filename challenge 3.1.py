def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices
products = ["Apple", "Banana", "Orange", "Apple", "Grapes"]
target_product = "Apple"
result = linear_search_product(products, target_product)
print(result)  # This will print [0, 3] because "Apple" is found at indices 0 and 3 in the list. 