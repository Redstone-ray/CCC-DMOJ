import re
key,message=input(),input()
message=re.sub('[^a-zA-Z]+', '', message)
for i,c in enumerate(message):
    shift=ord(key[i%len(key)])-ord("A")
    r=(ord(c)+shift)
    if r>90:
        r=r-26
    print(chr(r),end="")