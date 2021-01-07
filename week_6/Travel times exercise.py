model_of_travel = ["walking", "biking", "driving"]

speeds_of_travel = {}

with open("travel_time.txt") as travel_time_file:
    for line in travel_time_file
        mode, speed, get_going, park = line.split(",")
        speeds_of_travel[mode] = (float(speed), float(get_going), float(park))



for mode in modes_of_travel:
    if mode not in speeds_of_travel:
        speed = float(input("Please provide the speed of travel for " + mode + " ."))
        get_going = float(input("Please provide the needed to get going with " + mode + " ."))
        park = float(input("Please provide the time needed to park " + mode + " ."))
        speeds_of_travel[mode] = (speed, get_going, park)


with open("travel_time.txt", "w") as travel_time_file:
    print(speeds_of_travel)
    for mode in speeds_of_travel:
        speed, get_going, park = speeds_of_travel[mode]
        travel_time_file.write(mode + "," + str(speed) + "," + str(get_going) + "," + str(park) + "\n")


distance = float(input("Please provide the distance you would like to travel."))


for mode in speeds_of_travel
    speed, get_going, park = speeds_of_travel[mode]
    travel_time = distance / speed + get_going / 60 + park / 60
    print("{} will take {:.2f} hours to get there.".format(mode, travel_time))