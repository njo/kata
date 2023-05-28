def split_sum(n):
    total = 0
    while n >= 10:
        total += int((n % 10)) ** 2
        n = int(n / 10)
    return total + n ** 2

def is_happy_number(n):
    slow = n
    fast = split_sum(n)
    max_iter = 999
    while max_iter > 0:

        if fast == 1:
            return True
        if fast == slow:
            return False

        slow = split_sum(slow)
        fast = split_sum(split_sum(fast))
        max_iter -= 1

    return False

print(is_happy_number(19))
print(is_happy_number(2147483646))
print(is_happy_number(7))
print(is_happy_number(1012))
print(is_happy_number(2))
print(is_happy_number(2023))