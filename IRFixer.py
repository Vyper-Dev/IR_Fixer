import re

IRfile = str(input("Enter filename with extension: "))
f = open(IRfile, 'r')
Lines = f.readlines()
f.close()
AllLines = []
Terms = ["Version:","type:","protocol:","address:","command:"]

def SplitTerm(x):
    global Words
    global Position
    for element in Line:
        if element.find(Terms[x]) != -1:
            Words = element.split(Terms[x])
            Words.remove("")
            Words.append("\n")
            Words.append(Terms[x])
            Position = Line.index(element)
            Line.remove(element)
    Line.insert(Position, Words[2])
    Line.insert(Position, Words[1])
    Line.insert(Position, Words[0])

for i in range(len(Lines)):
    Line = Lines[i]
    Line = re.split(r'(\ )', Line)
    if i == 0:
        SplitTerm(0)
        Terms.remove("Version:")
    else:
        Line.remove(" ")
        Line.insert(1, "\n")
        for x in range(len(Terms)): 
            SplitTerm(x)
    Line = "".join(Line)
    AllLines.append(Line)

f = open(IRfile, 'w')
for i in range(len(AllLines)):
    f.write(AllLines[i])
f.close()