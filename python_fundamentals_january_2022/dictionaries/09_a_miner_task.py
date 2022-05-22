resources = {}

counter = 1
temp_resource = ''
line = input()
while not line == 'stop':
    if counter > 2:
        temp_resource = ''
        counter = 1
    if counter % 2 != 0:
        temp_resource = line
    else:
        resource_value = int(line)
        if temp_resource in resources:
            resources[temp_resource] += resource_value
        else:
            resources[temp_resource] = resource_value
    counter += 1

    line = input()

for resource, value in resources.items():
    print(f"{resource} -> {value}")
