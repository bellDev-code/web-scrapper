"""
def say_hello(name, age):
    print(f"hello {name}, my age is {age} years old")

say_hello("jongho", 12)
# 순서를 상관없이 arg 할당해도 된다.
say_hello(age=13, name="youngdo")
"""

lits_of_numbers = [1, 2, 3]

# 단, lists의 길이를 알고 있을때만 사용할 수 있다.
first, second, third = lits_of_numbers

print(first, second, third)