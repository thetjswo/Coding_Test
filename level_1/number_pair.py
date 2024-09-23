# 두 정수 `X`, `Y`의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다.
# (단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). `X`, `Y`의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. `X`, `Y`의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.
# 예를 들어, `X` = 3403이고 `Y` = 13203이라면, `X`와 `Y`의 짝꿍은 `X`와 `Y`에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다.
# 다른 예시로 `X` = 5525이고 `Y` = 1255이면 `X`와 `Y`의 짝꿍은 `X`와 `Y`에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다.
# (`X`에는 5가 3개, `Y`에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)

# Q: 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

def solution(x, y):
    pair_cnt = [0] * 10
    x_cnt = [0] * 10
    y_cnt = [0] * 10

    num_set = []
    result = ''

    for x_unit in x:
        x_cnt[int(x_unit)] += 1

    for y_unit in y:
        y_cnt[int(y_unit)] += 1

    for i, (x, y) in enumerate(zip(x_cnt, y_cnt)):
        if x == y:
            pair_cnt[i] = x
        elif x > y:
            pair_cnt[i] = y
        elif x < y:
            pair_cnt[i] = x

    for i, unit in enumerate(pair_cnt):
        if unit != 0:
            for x in range(unit):
                num_set.append(i)

    if not num_set:
        result = '-1'
    elif num_set:
        zero_cnt = 0
        for x in num_set:
            if x != 0:
                zero_cnt += 1

        if zero_cnt == 0:
            result = '0'
        else:
            result = ''.join(str(x) for x in num_set[::-1])

    return print(result)


max_length = 3000000
min_length = 3

while True:
    first_num = input("Input first number: ")
    if min_length <= len(first_num) <= max_length:
        break
    elif int(first_num[0]) == 0:
        print('First number can\'t be zero')
    else:
        print('The number\'s length must bigger than 3 or smaller than 3000000')


while True:
    second_num = input("Input second number: ")
    if min_length <= len(first_num) <= max_length:
        break
    elif int(first_num[0]) == 0:
        print('First number can\'t be zero')
    else:
        print('The number\'s length must bigger than 3 or smaller than 3000000')


solution(first_num, second_num)