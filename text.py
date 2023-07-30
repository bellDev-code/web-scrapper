def say_hello(name, age):
    print(f"hello {name}, my age is {age} years old")

say_hello("jongho", 12)
# 순서를 상관없이 arg 할당해도 된다.
say_hello(age=13, name="youngdo")