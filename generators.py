# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i * i)
#     return result


def square_numbers(nums):
    for i in nums:
        yield i * i


# my_nums = square_numbers([1, 2, 3, 4, 5])

my_nums = (i * i for i in [1, 2, 3, 4, 5])

print(list(my_nums))

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# for num in my_nums:
#     print(num)
