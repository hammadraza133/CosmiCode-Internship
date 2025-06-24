# Task 5: Convert seconds to hours, minutes, and seconds

total_seconds = int(input("Enter time in seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{total_seconds} seconds is equal to {hours} hour(s), {minutes} minute(s), and {seconds} second(s).")
