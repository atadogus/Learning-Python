
def all_subsets(array: list) -> list:
    result = []
    for i in range(len(array)):
        result.append(i)

    return result


sample_array = [1, 2, 3]
print(all_subsets(sample_array))
