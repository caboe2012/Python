def remove_duplicates(numbers):
    s = []
    i = 0
    while i < len(numbers):
        if numbers[i] not in s:
            s.append(numbers[i])
            i += 1
        else:
            i += 1
    return s

data = [1, 1, 2, 2, 3, 3, 4, 4, 5, 1, 2, 3, 4, 5, 6]
print data

print remove_duplicates(data)
