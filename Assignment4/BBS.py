from math import *
from Euclidean import gcd

def PseudorandomBits(p, q):
    B = []
    dupX0 = []
    xiList = []
    bits = {}
    cycle = {}
    n = p * q
    a = [i for i in range(1, int((n-1)/2) + 1)]
    s = set()
    x0 = set()
    y = set()	
    l = 1
    seed = []
 
    f = open("result.txt", 'w+')
    
    print("p = ", p, " q = ", q, " n = ", n)
    text = "p = " + str(p) + " ; q = " + str(q) + " ; n = " + str(n) + "\r\n"
    f.write(text)
	
    for i in a: # initialize s set
        if gcd(i, n) == 1:
            s.add(i)
    print("s = ", s) 
    f.write("s = ")
    f.write(str(s))
    f.write("\r\n")

	
    for j in s:       # initialize x0 set
        i = int(pow(j, 2)) % n		
        x0.add(i) # deduped set of x0 
        dupX0.append(i) # list of x0 with duplication
    print("List of distinct x0 = ", sorted(x0), "\n")
    f.write("List of distinct x0 = ")
    f.write(str(sorted(x0)))
    f.write("\r\n")

    for x in sorted(x0):
        foundT = False
        temp = []
        xi = x
        while l < n:
            xi = int(pow(xi, 2)) % n  
            temp.append(xi)			
            b = xi % 2
            B.append(b)
            y.add(xi)
            if foundT == False:
                if x == xi:
                    foundT = True
                    T = l
                    print("x0 = ", x, "; integers in the cycle are ", y, "; cycle length T = ", T)
                    text = "x0 = " + str(x) + "; integers in the cycle are " + str(y) + "; cycle length T = " + str(T) + "\n"
                    f.write(text)                					
                    cycle.update({x:y})
            l = l + 1
        if foundT == False:
            print("x0 = ", x, " ; cycle is not found within bit length ", l-1)
            text = "x0 = " + str(x) + " ; cycle is not found within bit length " + str(l-1) + "\n"
            f.write(text)
        print("20 bits of bit-sequence = ", B[0:20], "\n")
        text = "20 bits of bit-sequence = " + str(B[0:20]) + "\r\n"
        f.write(text)
        bits.update({x:B})
        xiList.append(temp)
        l = 1
        y = set()
        B = []
    #print("cycle = ", cycle)
    

    dedupCycle = []
    for k, v in cycle.items():
        dup = False
        if len(dedupCycle) == 0:
            dedupCycle.append(v)
        else:
            for j in dedupCycle:
                if ((v <= j) & (j <= v)) == True:
                    dup = True
                    break					
            if dup == False:			
                dedupCycle.append(v)
    print("Number of distinct cycle = ", len(dedupCycle), "; Distinct cycle = ", dedupCycle)
    text = "Number of distinct cycle = " + str(len(dedupCycle)) + " ; Distinct cycle = " + str(dedupCycle) + "\r\n"
    f.write(text)


	
#PseudorandomBits(3, 7)
#PseudorandomBits(7, 11)
PseudorandomBits(19, 23)
        