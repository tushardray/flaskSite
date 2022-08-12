def solution(year):
    strYear = str(year)
    century = ""

    if len(strYear) == 2:
        century = year/10

    elif len(strYear) == 3:
        century = year/100

    elif len(strYear) == 4:
        oneBeforeCentury = year/100
        century = oneBeforeCentury + 1

    return int(century)


print(solution(1700))
