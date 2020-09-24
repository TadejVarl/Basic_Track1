time_now_1 = input('What is the time now?')
time_now = int(time_now_1)

hours_to_wait_1 = input('How long to wait for the alarm? :')
hours_to_wait = int(hours_to_wait_1)

print((hours_to_wait % 24) + time_now)
