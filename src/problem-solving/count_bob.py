def count_bob(bobStr):
    if not bobStr:
        return 0

    total = 0

    for x in range(len(bobStr)):
        y = x + 3
        subsStr = bobStr[x:y]

        if subsStr.lower() == 'bob':
            total = total + 1

    return total
