with open("birthday_card.txt") as in_file:
    text = in_file.read()

text = text.replace("[name]", "Tarçın")  # need to assign the new version of the text to a container

with open("tarçın_birthday_card.txt", mode="w") as out_file:
    out_file.write(text)

