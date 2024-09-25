def solution(arr, divisor):
    result = []
    remainder = [num for num in arr if num % divisor == 0]

    if not remainder:
        result.append(-1)
    else:
        result = sorted(remainder)

    return print(result)


while True:
    arr = [int(x) for x in input('Input arrays: ').split()]
    fl_same = False

    for x in arr:
        if x <= 0:
            print('Please input positive number.')
            fl_same = True

    if len(set(arr)) != len(arr):
        print('please Input all integers differently.')
    elif not arr:
        print('The array can\'t not empty.')
    elif len(set(arr)) == len(arr) and fl_same is False:
        break


while True:
    divisor = int(input('Input divisor: '))

    if divisor <= 0:
        print('Please input positive number.')
    else:
        break

solution(arr, divisor)