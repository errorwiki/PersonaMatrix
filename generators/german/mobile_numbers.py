import random

# Network prefixes
prefix = ['151', '160', '170', '171', '175', '152', '162', '172', '173',
          '174', '157', '159', '163', '176', '177', '178', '179']

# Generate mobile numbers
mobile_numbers = []
for i in range(500_000):
    mobile_numbers.append(f'+49 {random.choice(prefix)} {"".join([str(random.randint(0, 9)) for _ in range(7)])}')

# Write to file
with open('data/german/mobile-numbers.txt', 'w') as file:
    for number in mobile_numbers:
        file.write(f'{number}\n')
