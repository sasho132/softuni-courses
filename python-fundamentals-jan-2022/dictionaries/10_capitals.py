country_names = input().split(", ")
capital_cities = input().split(", ")

res = {country: city for country, city in zip(country_names, capital_cities)}

for key, value in res.items():
    print(f"{key} -> {value}")
