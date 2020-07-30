import itertools
def populate (subjectc, verbc, objectc):
    for i in range (subjectc):
        sub.append(input())
    for i in range (verbc):
        ver.append(input())
    for i in range (objectc):
        obj.append(input())
for i in range(int(input())):
    subjectc, verbc, objectc = int(input()), int(input()), int(input())
    sub,ver,obj=[],[],[]
    populate(subjectc, verbc, objectc)
    for j, k,e in itertools.product(range(subjectc), range(verbc),range(objectc)):
        print(sub[j],ver[k],obj[e]+".")