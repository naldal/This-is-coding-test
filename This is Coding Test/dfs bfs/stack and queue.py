stack = [2, 5, 3, 7, 1, 9]
print(stack)
stack.reverse()
print(stack)
print(sorted(stack))
stack.sort()
print(stack)
print(sorted(stack, reverse=True))
print(stack)

from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.popleft()
queue.append(1)
queue.append(2)
queue.append(7)
queue.append(9)
print(queue)

queue.remove(2)
print(queue)

queue.reverse()
print(queue)


def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return
    return n * factorial_recursive(n - 1)
