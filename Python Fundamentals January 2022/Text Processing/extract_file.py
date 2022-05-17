filepath = input().split("\\")

file_data = filepath[-1]
file = file_data.split(".")
filename = file[0]
file_extension = file[1]

print(f"File name: {filename}")
print(f"File extension: {file_extension}")
