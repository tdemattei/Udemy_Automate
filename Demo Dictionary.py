# Dictionary count

import pprint

message = "A practical programming course for office workers, academics, and administrators who want to improve their productivity."

count = {}

for letter in message.upper():
    count.setdefault(letter, 0)
    count[letter] = count[letter] + 1

pprint.pprint(count)
