total_secs = int(input("How many seconds, in total?"))

#days
days = (total_secs // 86400)
days_still_remaining = total_secs % 86400

#hours
hours = (days_still_remaining // 3600)
hours_still_remaining = total_secs % 3600

#minutes
minutes = (hours_still_remaining // 60)
minutes_still_remaining = total_secs % 60

#seconds
final_seconds_remaining = minutes_still_remaining % 60


print("Days=", days, "Hrs=", hours, " mins=", minutes,
"secs=", final_seconds_remaining)