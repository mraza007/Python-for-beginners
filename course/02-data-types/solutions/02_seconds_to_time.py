"""Solution — Exercise 2: Seconds to hours, minutes, seconds."""

total_seconds = 3661

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds is {hours} h, {minutes} m, {seconds} s.")
