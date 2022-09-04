#xndir 1
"""b = [2, 5, 4, 9]
a = []
def xnd1():
    for i in b:
        if i==b[0]:
            i=b[-1]
            a.append(i)
        elif i==b[-1]:
            i=b[0]
            a.append(i)
        else:
            a.append(i)
    return a
print(xnd1())"""
#xndir 5
"""file = open("xnd3.txt")
c = file.read().split()
maxLen = c[0]
for i in c:
 if len(i) > len(maxLen):
  maxLen=i
print("amenaerkar bary = ",maxLen)
print("tareri qanaky=", len(maxLen))"""