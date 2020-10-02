def solution(citations):
    citations.sort(reverse=True)
    for index, citation in enumerate(citations):
        if citation <= index:
            return index
    else:
        return len(citations)

print(solution([4,4,4]))