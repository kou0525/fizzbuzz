# for number in range(1, 101):
#     print("for文")
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# ---------------------------------------------

# number = 1
#
# while number < 101: #numberが101未満（numberが100）であれば下記のif文を実行
#     print("while文")
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
#     number += 1 #numberに+1する
#


# ---------------------------------------------
# 関数化

def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)


for i in range(1, 101):
    result = fizzbuzz_convert(i)
    print(result)
