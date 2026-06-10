import calendar

year = int(input("Enter Your Year: ")) 
month = int(input("Enter Your Month in Number: "))

print(f"\n{calendar.month(year, month)}")