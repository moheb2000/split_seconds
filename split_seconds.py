all_seconds = int(input('please enter seconds -> '))

second = all_seconds % 60

all_minutes = all_seconds // 60

minute = all_minutes % 60

all_hours = all_minutes // 60

hour = all_hours % 24

all_days = all_hours // 24

print(f'{all_days} days {hour} hours {minute} minutes {second} seconds')


