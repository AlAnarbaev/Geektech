# линейный поиск

name = ['бека', 'beka', 'erf', 'нурислам', 'adahan']

search_for = 'нурислам'  # что ищем


def linear_search(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]  # возвращаем индекс

    return None


print('искомый элемент', search_for, 'найден под индексом',
      linear_search(name, search_for))

# o(5)


# сортировка выборкой
# o(n2)
nums = [2, 3, 1, 3, 1, 5, 7, 85, 5, 3, 44, 9, 9]
print(sorted(nums))
print('было', nums)

for i in range(len(nums)):
    lowest = i  # первый элемент за наименьший

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j

    nums[i],nums[lowest]=nums[lowest],nums[i]
n=1
m=2
n,m=m,n
print('стало',nums)
