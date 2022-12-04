with open('input.txt', 'r') as input_file:
    input_data = input_file.read().splitlines()

results = []

acc = 0
for element in input_data:
    if element != '':
        acc += int(element)
    else:
        results.append(acc)
        acc = 0

results.sort(reverse=True)
print(sum(results[:3]))
