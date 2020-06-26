def common_factors(*numbers):
    factors = []
    min_num = min(numbers)
    for n in range(2, min_num // 2 + 1):
        for num in numbers:
            if num % n != 0:
                break
        else:
            factors.append(n)

    return factors


print(common_factors(10, 20, 30))
print(common_factors(20,40,60,80))
