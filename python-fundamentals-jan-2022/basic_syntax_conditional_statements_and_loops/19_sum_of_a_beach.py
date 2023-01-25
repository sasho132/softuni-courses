text = input()
text_filtered = text.lower()

counter = text_filtered.count('sand') + text_filtered.count('water') + text_filtered.count('fish') + \
          text_filtered.count('sun')

print(counter)
