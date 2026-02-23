import datetime
import time

seconds_since_epoch = int(time.time())

formatted_with_commas = f"{seconds_since_epoch:,}"

formatted_scientific = f"{seconds_since_epoch:.2e}"

print("Seconds since January 1, 1970:", formatted_with_commas, "or",
      formatted_scientific, "in scientific notation")

today = datetime.date.today()

formatted_date = today.strftime("%b %d %Y")
print(formatted_date)
