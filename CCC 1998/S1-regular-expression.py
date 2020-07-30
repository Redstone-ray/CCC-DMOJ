import re

for i in range(int(input())):
       print(re.sub(r"\b\w{4}\b", "****", input()))


