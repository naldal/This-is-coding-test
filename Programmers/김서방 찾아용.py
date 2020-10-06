def solution(seoul):
    answer = [i for i, v in enumerate(seoul) if v == "Kim"]
    return "김서방은 "+str(answer[0])+"에 있다"

print(solution(["a", "Kim"]))