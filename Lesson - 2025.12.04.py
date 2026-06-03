# This is a comment line
print("Hello world")

inflation_rate = 0.35

# ! Data Types
# Integers - whole numbers
# Strings - text, objects, varchar()
# Floats, decimal
# Date, datetime
# Boolean - True/False

a = 10
name = "Jack"
b = True
c = 10.5
d = "10"

print("My name is:", name)
print(a + a)  # 20
print(d + d)  # 1010

# Entering variables
username = input("Please enter your name: ")
print(f"Welcome {username}")


# %%
# ! IF ELSE Opeators
lesson_mark = 90

if lesson_mark > 60:
    print("Congratulations you passed the exam")
else:
    print("You failed")

if lesson_mark > 90:
    print("Congratulations, you passed the test with AA grade")
elif lesson_mark > 80:
    print("Congratulations, you passed the test with BB grade")
elif lesson_mark > 70:
    print("Congratulations, you passed the test with CC grade")
elif lesson_mark > 60:
    print("Congratulations, you passed the test with DD grade")
else:
    print("You failed the exam")

# %%
#! For Loops
list = ["John", "Jack", "Jill", "Jim", "James"]

for name in list:
    print(name)


#! While Loops
count = 5

while count < 10:
    print(count)
    count += 1
