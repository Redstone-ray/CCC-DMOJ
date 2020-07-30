a=input()
while a!="quit!":
    if len(a)>4:
            if a.endswith("or"):
                if a[-3] not in "aeiouy":
                    print(a.replace("or","our"))
                else:
                    print(a)
            else:
                print(a)
    else:
        print(a)
    a=input()