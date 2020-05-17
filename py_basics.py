# 0_Hello World
# print("DSP is everywhere")
# print("Sine is the great great grandmother of all signals")
# v = 12
# w = 11
# x = 0.000008

# if v == (w+1):
#     # indented 4 spaces
#     print("Statement is true    `")


# 1_Variables
# num_int = 10
# num_float = 8.0

# print(num_int, num_float)

# num_float2 = float(9)
# print(num_float2)

# greeting = 'hello'
# print(greeting)

# response = "hi"

# concat = greeting + response

# print(concat)

# 2_Lists
# my_list = []
# my_list.append(56)
# my_list.append(4)
# my_list.append(67)

# # print(my_list[2])

# for x in my_list:
#     print(x)

# 3_Operators

# num = 1 + 3

# print(num)

# num *= 2

# print(num)

# remainder = 10 % 4

# print("Remainder = " + str(remainder))

# squared = 12**2
# cubed = 12**3

# print(squared, cubed)

# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 11, 12, 13, 14]

# complete_list = list1 + list2

# print(complete_list)

# print("The number is ", 2)

# amount = 0.75
# print("The amount is", amount)

# second_amount = 0.0000089

# print("The amount %f is very very small." % second_amount)

# 5_Conditions

# city = "London"
# temp = 35

# if city == "London" and temp == 35:
#     print("It is hot in London today")
# else:
#     print("It's balmy")

# city = "Mumbai"

# if city in ["NYC", "Accra", "Istanbul", "London", "Mumbai"]:
#     print("city found!")
# else:
#     print("not in there!")

# countries = ["Turkey", "Ghana", "China", "India"]
# country = "Turkey"

# if country in countries:
#     print("country found!")
# else:
#     print("not found!")

# 6_For Loops

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# for num in numbers:
#     print(num)

# print("--------------")

# for x in range(5):
#     if x > 2:
#         print(x)
#     else:
#         print("not high enough!")


# print("--------------")

# for x in range(3, 8, 2):
#     print(x)

# 7_While Loops

# num = 0
# while num < 5:
#     print(num)
#     num += 1

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

# for x in range(10):
#     if x % 2 == 0:
#         continue
#     print(x)

# 8_Functions

# def simple_function():
#     print("This is simple")


# simple_function()


# # def country_info(country, capital):
# #     print("The capital of %s is %s" % (country, capital))


# def country_info(country, capital):
#     print(f"The capital of {country} is {capital}")


# country_info("Belgium", "Brussels")


# def add_this(a, b):
#     return a + b


# print(add_this(56, 4))

# 9_Dictionary

# ages = {
#     "Bill": 45,
#     "Ken": 33
# }

# ages["Tom"] = 29
# ages["Dale"] = 30
# ages["Phil"] = 19

# print(ages)

# postcodes = {
#     "Mechanicsburg": 17055,
#     "Philly": 19123,
#     "Lanco": 17602
# }

# print(postcodes["Philly"])
# print(postcodes)

# for key, value in postcodes.items():
#     print(f"This key is {key}, and the value is {value}")

# del postcodes["Mechanicsburg"]
# print(postcodes)

# 10_Objects and Classes

class SimpleClass:
    greeting = "Hello"

    def funct1(self):
        print("This is a simple class")
        print(self.greeting)


simple_object = SimpleClass()

print(simple_object.greeting)
simple_object.funct1()


class Computer:
    name = ""
    kind = "Laptop"
    color = ""
    cost = 500

    def description(self):
        desc_str = f"This is a {self.color} {self.name} worth {self.cost}"
        print(desc_str)


my_comp = Computer()

my_comp.name = "Lappy"
my_comp.color = "Sanguid"
my_comp.cost = 750

my_comp.description()
