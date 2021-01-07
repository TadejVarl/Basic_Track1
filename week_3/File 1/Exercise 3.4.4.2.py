today = 4
sleeping = 137

which_day = (today + sleeping) % 7

if which_day == 0:
    print("Monday")
elif which_day == 1:
    print("Tuesday")
elif which_day == 2:
    print ("Wednesday")
elif which_day == 3:
    print ("Thursday")
elif which_day == 4:
    print ("Friday")
elif which_day == 5:
    print ("Saturday")
elif which_day == 6:
    print ("Sunday")


# second version of the same exercise

week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

today = 3
sleeps = 137

print("You will wake up on a ", week_days[(today + sleeps) % len(week_days)])


