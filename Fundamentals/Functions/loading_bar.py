def loading_bar(loading_percent):
    if loading_percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{loading_percent}%\
 [{'%' * (loading_percent // 10)}{'.' * (10 - (loading_percent // 10))}]\nStill loading..."


percent_number = int(input())
print(loading_bar(percent_number))
