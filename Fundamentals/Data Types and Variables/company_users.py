companies_dict = {}

command = input()
while command != 'End':
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies_dict:
        companies_dict[company_name] = []
    if employee_id not in companies_dict[company_name]:
        companies_dict[company_name].append(employee_id)

    command = input()

for key, values in companies_dict.items():
    print(f"{key}")
    temp_ids = '\n-- '.join(values)
    print(f"-- {temp_ids}")
