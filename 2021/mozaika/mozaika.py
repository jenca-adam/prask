#!/usr/bin/env python3.9
gtr=[chr(i) for i in range(ord('A'),ord('z')+1)]+['-']
gstr=gtr+['.']


def check(a):
    if a not in gstr:
        raise ValueError("invalid char")
def onmain(a,n='__main__'):
    if __name__==n:
        a()
def firstc(d):
    for ca in gtr:
        try:
            return d.index(ca)
        except:
            pass
    raise IndexError
def lastc(d):
    uras=''.join(d)
    res=-1
    for car in gtr:
        ix=uras.rfind(car)
        res=max(res,ix)

    assert res>0 ,'not found'
    return res
def contc(a):
    for car in gtr:
        if car in a:
            return True
    return False
class Infinity:
    def __lt__(self,a):
        return False
    def __gt__(self,a):
        return True
def main():
    table=[]
    r,s = [int(i) for i in input().split(' ')]
    for k in range(r):
        g=(input())
        assert len(g)==s

        f=[]
        for char in g:
            check(char)
            f.append(char)
        table.append(f)
    gal=Infinity()
    lal=-1
    vrch=0
    spod=-1
    lix=0
    for line in table:
        try:
            gal2=firstc(line)
            gal=min(gal,gal2)
        except:
            pass
        try:
            lal2=lastc(line)
            lal=max(lal,lal2)
        except:pass
        if contc(line):
            spod=lix
            if vrch==0:
                vrch=lix
        lix+=1

    if lal>s-2 or gal==0 or vrch==0 or spod>r-2:
        print("Neda sa")
        exit()
    ss=lal-gal+3
    table[vrch-1]=['.']*(gal-1)+["#"]*ss+["."]*(s-ss-(gal-1))
    table[spod+1]=['.']*(gal-1)+["#"]*ss+["."]*(s-ss-(gal-1))
    for asa in range(vrch,spod+1):
        table[asa][gal-1]="#"
        table[asa][lal+1]="#"
    print()
    print('\n'.join([''.join(i) for i in table]))
        
        
onmain(main)
