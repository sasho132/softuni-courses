notes = [0] * 11

command = input()
while command != "End":
    notes_list = command.split("-")
    note_priority = int(notes_list[0])
    note = notes_list[1]
    notes.pop(note_priority)
    notes.insert(note_priority, note)
    command = input()

filtered_notes = [x for x in notes if x != 0]
print(filtered_notes)
