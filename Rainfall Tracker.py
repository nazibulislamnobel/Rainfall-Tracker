num_years = int(input("Enter the number of years: "))
total_rainfall = 0

for year in range(1, num_years + 1):
    print(f"For year {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for month {month}: "))
        total_rainfall += rainfall

num_months = num_years * 12
average_rainfall = total_rainfall / num_months

print(f"For {num_months} months")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")