string = "sajjid"
no_of_char = len(string)

for char in set(string):
    count = string.count(char)
    print("Character",char, "occurs",count, "time")