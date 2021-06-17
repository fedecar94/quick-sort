def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array

    pivot = array[0]

    lo = []
    hi = []
    eq = [pivot]

    for item in array[1:]:
        if item < pivot:
            lo.append(item)
        elif item > pivot:
            hi.append(item)
        else:
            eq.append(item)

    lo = quick_sort(lo)
    hi = quick_sort(hi)

    return lo + eq + hi


if __name__ == '__main__':
    import random

    randomlist = [random.randint(1, 30) for x in range(0, 10)]

    print(randomlist)
    sorted_list = quick_sort(randomlist)
    print(sorted_list)
