
import re

message = "Phone1 555-444-1234 Phone2 666-123-4567"

phone_num = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
print(phone_num.findall(message))
