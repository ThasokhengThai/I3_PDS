#Compute
total_second=9875
hour=total_second//3600
minute=(total_second%3600)//60
second=total_second%60

print(hour)
print(minute)
print(second)
print(f"{hour} hour {minute} minute {second} second")

check=hour*3600+minute*60+second
print(check)
print(total_second==check)
print(check!=total_second)