path = "raw_contact_sheet.csv"
lines = [line for line in open(path)]

print(lines[0])
print(lines[1])

print(lines[0].strip())

print(lines[0].strip().split(','))

dataset = [line.strip().split(',') for line in open(path)]

print(dataset[0])
print(dataset[1])
print(dataset[2])
print(dataset[3])