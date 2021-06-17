def quick_sort(array: list):
    if len(array) < 2:
        return

    pivot = array[0]

    lo = []
    eq = [pivot]
    hi = []

    for item in array[1:]:
        if item < pivot:
            lo.append(item)
        elif item > pivot:
            hi.append(item)
        else:
            eq.append(item)

    quick_sort(lo)
    quick_sort(hi)

    size_lo = len(lo)
    if size_lo:
        array[:size_lo] = lo

    size_eq = len(eq)
    if size_eq:
        array[size_lo: size_lo + size_eq] = eq

    size_hi = len(hi)
    if size_hi:
        array[size_lo + size_eq:] = hi


if __name__ == '__main__':
    import random

    randomlist = [random.randint(1, 30) for x in range(0, 10)]

    print(randomlist)
    quick_sort(randomlist)
    print(randomlist)
