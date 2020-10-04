def solution(name):
    click = 0
    arr = [x for x in name]
    for index, i in enumerate(arr):
        print(ord(i))
        if ord(i) >= 77:
            click += abs(ord("Z")-ord(i))+1
        else:
            click += abs(ord("A")-ord(i))

        if index == len(arr)-1:
            return click

        if i == "A":
            continue

        click += 1
    return click


print(solution("JAN"))