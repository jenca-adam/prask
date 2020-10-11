#!/usr/bin/python
dlska=[int(i) for i in input().split(' ')][1]
kuski=[int(I)for I in input().split(' ')]
maxi=0
for i in kuski:
    maxi=max(maxi,sum(kuski[kuski.index(i):kuski.index(i)+3]))
print(maxi)
