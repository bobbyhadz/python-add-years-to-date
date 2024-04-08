# Add year(s) to a date in Python

from datetime import datetime, date


def add_years(start_date, years):
    try:
        return start_date.replace(year=start_date.year + years)
    except ValueError:
        # 👇️ Preserve calendar day (if Feb 29th doesn't exist, set to 28th)
        return start_date.replace(year=start_date.year + years, day=28)


# ✅ Add years to a date
my_str = '09-14-2023'  # 👉️ (mm-dd-yyyy)
date_1 = datetime.strptime(my_str, '%m-%d-%Y')
print(date_1)  # 👉️ 2023-09-14 00:00:00

result_1 = add_years(date_1, 3)
print(result_1)  # 👉️ 2026-09-14 00:00:00

# -----------------------------------------------

# ✅ Add years to the current date

current_date = datetime.today()
print(current_date)  # 👉️ 2023-02-18 18:57:28.484966

result_2 = add_years(current_date, 2)
print(result_2)  # 👉️ 2025-02-18 18:57:28.484966