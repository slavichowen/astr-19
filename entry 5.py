import math

def main():
    amt = 1000
    start = 0
    end = 2 * math.pi
    delta = (end - start) / (amt - 1)
    
    for i in range(amt):
        x = start + i * delta
        print(str(round(x,5)) + "\t" + str(round(math.sin(x),5)))
        
main()