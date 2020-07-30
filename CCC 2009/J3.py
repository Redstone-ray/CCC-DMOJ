# Hanson
x = int(input())
print(x, "in Ottawa")
print((x - 300) % 2400, "in Victoria")
print((x - 200) % 2400, "in Edmonton")
print((x - 100) % 2400, "in Winnipeg")
print(x, "in Toronto")
print((x + 100) % 2400, "in Halifax")
if ((x + 130) % 2400) % 100 >= 60:
   print((x + 130) % 2400 - 60 + 100, "in St. John's")
else:
   print(((x + 130) % 2400), "in St. John's")

