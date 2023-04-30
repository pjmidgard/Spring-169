# Spring-169
Spring-169

Spring compression algorithm:

Spring compression algorithm:

Add "1" If number divide by two we it and if again it divide by two after minus 1 if not divide by two or it not divide by two two times minus 1. Times compression 6 bytes and Size of file 4 bytes. Can compress 4GB. Compress while we get N<=(2**256)-1. Add 1 and zeros.

Example:
N=int(C,2)
N2=N
N=N//2
N1=N%2
if N1==0:
    N3=N%2
    if N3==0:
        N=N-1
    else:
        N=N2-1
else:
    N=N2-1






