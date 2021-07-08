#!/usr/bin/env python3
import math
import bisect
def median(a,b):
    return a[math.ceil(b//2)]




def main():
    post=[]
    meds=[]
    i=0
    for k in range(int(input())):
        bisect.insort(post,int(input()))
        meds.append(str(median(post,i)))
        i+=1
    print("\n".join(meds))
if __name__=='__main__':
    main()
