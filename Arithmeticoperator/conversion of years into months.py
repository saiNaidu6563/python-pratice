#conversion of no.of years into no.of months into no.of days
y=float(input("enter the year y:"))
m=float(input("enter the months m:"))
d=float(input("enter the days d:"))
my = y * 12
dm = m * 30
td = (my+ m) * 30 + dm

print(f"conversion of years into months into days {y} {m} {d} {my} {dm}={td}")