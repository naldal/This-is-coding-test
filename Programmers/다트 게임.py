import math

def solution(dartResult):
    score = []
    sdt = ['S', 'D', 'T']
    spc = ['*', '#']
    tmp = ""
    for i in dartResult:
        if i.isdigit():
            tmp += i
            # score.append(int(i))
        elif i in sdt:
            # print(tmp)
            score.append(int(tmp))
            tmp = ""
            if i == 'S':
                score[len(score)-1] = math.pow(score[len(score)-1], 1)
            elif i == 'D':
                score[len(score)-1] = math.pow(score[len(score)-1], 2)
            elif i == 'T':
                score[len(score)-1] = math.pow(score[len(score)-1], 3)
        elif i in spc:
            if i == '*':
                if len(score) >= 2:
                    score[len(score)-2] *= 2
                    score[len(score)-1] *= 2
                else:
                    score[len(score) - 1] *= 2
            elif i == '#':
                score[len(score) - 1] *= -1
    return int(sum(score))





solution("1S2D*3T")
solution("1D2S#10S")
solution("1D2S0T")
solution("1S*2T*3S")
solution("1T2D3D#")
