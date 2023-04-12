def fr(n):
    rn = n.lower() ; r = 0
    for i,c in enumerate(rn):
        match c:
            case 'i':
                try: r+=4 if rn[i+1]=='v'else 9 if rn[i+1]=='x'else 1
                except IndexError: pass
                else: continue
            case 'v':
                try:
                    if rn[i-1]=='i'and i-1>=0:continue
                except IndexError:pass
                r+=5
            case 'x':
                try:
                    if rn[i-1]=='i'and i-1>=0:continue
                except IndexError:pass
                try:r+=40 if rn[i+1]=='l'else 90 if rn[i+1]=='c'else 10
                except IndexError: r+=10
            case 'l':
                try:
                    if rn[i-1]=='x'and i-1>=0:continue
                except IndexError:pass
                r+=50
            case 'c':
                try:
                    if rn[i-1]=='x'and i-1>=0:continue
                except IndexError:pass
                try:r+=400 if rn[i+1]=='d'else 900 if rn[i+1]=='m'else 100
                except IndexError:r+=100
            case 'd':
                try:
                    if rn[i-1]=='c'and i-1>=0:continue
                except IndexError:pass
                r+=500
            case 'm':
                try:
                    if rn[i-1]=='c'and i-1>=0:continue
                except IndexError:pass
                r+=1000
            case _: raise ValueError("only numerals IVXLCDM are supported")
    return r
def to(n):
    if n<4000:
        if n>0:
            r=str()
            thou=tuple(("".ljust(x,"M")for x in range(4)))#('', 'M', 'MM', 'MMM')
            h=tuple(("".ljust(x,"C")for x in range(4)))+("CD",)+tuple(("D".ljust(x+1,"C")for x in range(4)))+("CM",)#('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
            t=tuple(("".ljust(x,"X")for x in range(4)))+tuple(("L".rjust(2,"X")if x==0 else "L".ljust(x,"X")for x in range(5)))+("XC",)#('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
            o=tuple(("".ljust(x,"I")for x in range(4)))+tuple(("V".rjust(2,"I")if x==0 else "V".ljust(x,"I")for x in range(5)))+("IX",)#('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
            r+=thou[n//1000]if n>999 else str()
            r+=h[int((n//100).__str__()[-1])]if n>99 else str()
            r+=t[int((n//10).__str__()[-1])]if n>9 else str()
            r+=o[int(n.__str__()[-1])]
            return r
        else:raise ValueError("only positive numbers are supported")
    else:raise ValueError("only numbers up to 3999 are supported")

assert fr(to(the := 900)) == the, "NO it's %d"%fr(to(the))
