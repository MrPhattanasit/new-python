work = int(input("Enter the number of hours worked: "))
hour = int(input("Enter the hourly pay rate: "))

if work <= 40:
    pay= work * hour
else:
    pay = (work - 40) * hour * 1.5 +(40 * hour)
print("Total pay for the week: $", format(pay,".2f"))