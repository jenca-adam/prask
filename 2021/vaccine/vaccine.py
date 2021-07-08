#!/usr/bin/env python3.9
import bisect
E="prazdna"
class WaitingRoom:
    def __init__(self):
        self.maxpr=-1
        self.stav=E
        self.ludia=[]
        self.stavy=[]
    def buildout(self):
        return '\n'.join([str(x) for x in self.stavy])
    def conf(self):
        if not self.ludia :
            self.stav=E
        else:
            self.stav=self.ludia[-1]
    def add(self,p):
        bisect.insort(self.ludia,p)
    def rem(self):
        self.ludia.pop()
    def _feed(self,t,x):
        if int(t)==0:
            self.rem()
        else:
            self.add(int(x))
        self.conf()
        self.stavy.append(self.stav)
    
    def feed(self,line):
        t,x=line.split(' ')
        self._feed(t,x)
def main():
    cn=int(input())
    wr=WaitingRoom()
    for i in range(cn):
        wr.feed(input())
    print(wr.buildout())
if __name__=='__main__':
    main()
