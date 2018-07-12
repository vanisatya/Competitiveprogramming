global g
g={
"A" :".-",
"B":"-...",
"C" :"-.-.",
"D" :"-..",
"E" :".",
"F":"..-.",
"G" :"--.",
"H" :"....",
"I":"..",
"J":".---",
"K":"-.-",
"L":".-..",
"M":"--",	
"N":"-.",
"O":"---",
"P":".--.",
"Q":"--.-",
"R":".-.",
"S":"...",
"T":"-",
"U":"..-",
"V":"...-",
"W":".--",
"X":"-..-",
"Y":"-.--",
"Z":"--.."
}
def words(li):
    lst1=[]
    for j in li:
        k=mors(j)
        lst1.append(k)
    strng=set(lst1)
    c=len(strng)
    return c
        
def mors(s):
    global g
    str=s.upper()
    li=list(str)
    strng=""
    for i in li:
        strng=strng+g[i]
    return strng


        

print(words(["gin", "zen", "gig", "msg"]))
print(words(["a", "z", "g", "m"]))
print(words(["bhi", "vsv", "sgh", "vbi"]  ))
print(words(["a","b","c","d"]))
print(words(["hig", "sip", "pot"]  ))
