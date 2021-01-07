# key value pairs
fruit_bowl = {}

fruit_bowl["apple"] = 4
fruit_bowl["banana"] = 2    # each key can only exist once, else it is overwritten

print(fruit_bowl)


# get()

user_input = input("What kind of fruit will you add?")
fruit_bowl[user_input] = fruit_bowl.get(user_input, 0) + 1

print(fruit_bowl)

# iterate over all keys

for fruit, quantity in fruit_bowl.items():
    print(fruit, quantity)


# in tests keys (not values)

if "pineapple" in fruit_bowl:
    print("What an exotic fruitbowl!")
else:
    print("What a mundane fruitbowl...")

if 4 in fruit_bowl.values(4):
    print("There are four different fruits.")

# exercise 3 and 4 require file, we will cover next week, but you can have a look