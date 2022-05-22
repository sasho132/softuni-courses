from collections import deque


material_boxes = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])
presents_dict = {
    150: "Doll", 
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}

while material_boxes and magic_values:
    
    current_box = material_boxes.pop()
    magic_value = magic_values.popleft()
    
    res = current_box * magic_value

    if res in presents_dict:
        toy = presents_dict[res]
        if toy not in crafted_presents:
            crafted_presents[toy] = 0
        crafted_presents[toy] += 1

    elif res < 0:
        material_boxes.append(current_box + magic_value)
    
    elif res > 0:
        material_boxes.append(current_box + 15)

    else: 
        if current_box == 0 and magic_value == 0:
            continue

        elif current_box == 0:
            magic_values.appendleft(magic_value)
        
        elif magic_value == 0:
            material_boxes.append(current_box)
        

if 'Doll' in crafted_presents and 'Wooden train' in crafted_presents \
    or 'Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_boxes:
    print(f"Materials left: {', '.join([str(x) for x in reversed(material_boxes)])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for present, value in sorted(crafted_presents.items()):
    print(f"{present}: {value}")
