def solution(bridge_length, weight, truck_weights):
    answer = 0
    for i in range(len(truck_weights)):
        print(i)
        total_weight = truck_weights[i]
        truck_count = 1
        reduce = 0
        if total_weight < weight:
            for j in range(i+1, len(truck_weights)):
                total_weight += truck_weights[j]
                if total_weight > weight:
                    total_weight -= truck_weights[j]
                    break
                elif total_weight <= weight:
                    total_weight += truck_weights[j]
                    truck_count += 1

                    reduce += bridge_length
            answer += bridge_length + (truck_count - 1) - reduce
    answer += 1
    print(answer)
    return answer



# solution(2, 10, [7, 4, 5, 6])
# solution(100, 100, [10])
solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
