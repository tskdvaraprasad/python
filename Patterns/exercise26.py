n = 5

for i in range(n):
    ch = chr(65 + i)
    
    for j in range(i + 1):
        print(ch, end=" ")
    
    print()
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 