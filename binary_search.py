def binary_search(list, answer):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == answer:
            return mid
        if guess > answer:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9]