s = "sample 'text in quotes' text"
s1 = 'sample "text in quotes" text'
s2 = """
sample "text in quotes" text
sample "text in quotes" text
sample "text in quotes" text
sample "text in quotes" text
sample 'text in quotes' text
sample "text in quotes" text
sample "text in quotes" text
sd
dsf
df
"""


def func():
    """Функция, которая ничего не делает"""
    pass


# print(s)
# print(s1)
# print(s2)

# print(s[5000000])
# s4 = s + s1 + s2
# print(s4)

# name = input("Enter you name, please: ")
# score = input("Enter your score, please: ")

name = "Nikolai"
score = "100"
# print("Hello", name, "!")
# print(f"Hello {name}! Your score is {score}")

very_big_dict_with_data = {
    "name": "Nikolai",
    "score": "100"
}
template = "Hello %d! Your score is %s"
# print(template.format("Nik", "100"))
print(template % ("1dfvsdfvsdfv", 2))

print()
