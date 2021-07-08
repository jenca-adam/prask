def najblizsiNasobok(y,x):
    return y * x//y
class Adam:
    def __init__(self,k,n,m,debug=False):
        self.k=k
        self.m=m
        self.n=n
        self.wintop=m+n-1
        self.winbott=m
        self.moving=True
        self.aval=range(self.winbott,self.wintop+2)
    def move(self):
        if self.moving :
            if  self.n<=self.k<self.m :
                print(self.k,flush=True)
                exit()
            else :
                for item in self.aval :
                    result=self.k-najblizsiNasobok(item,self.k)
                    if self.n<=result<self.m:
                        break
                else:
                    result=self.n
                self.k-=result
                print(result,flush=True)
        else :
            try:
                self.k-=int(input().strip())
            except:
                exit() 
                    
        self.moving=not self.moving
if __name__=='__main__':
    fd=[int(i) for i in input().split()]
    adam=Adam(*fd,debug=True)
    while True:
        adam.move()

        
        
