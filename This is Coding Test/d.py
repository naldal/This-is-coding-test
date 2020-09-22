n = input()
top = 0


def check(n, top):
    for i in range(len(n)):
        if n[i] == ')' and top <= 0:
            return False
        elif n[i] == '(':
            top += 1
        elif n[i] == ')' and top >= 1:
            top -= 1
        if i == len(n) - 1:
            if top == 0:
                return True
            else:
                return False


result = check(n, top)

print("good" if result else "bad")
