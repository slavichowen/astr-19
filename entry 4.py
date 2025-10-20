class dog:
    def __init__(self, armlen, leglen, eyes, tail, furry):
        self.armlength = armlen
        self.leglength = leglen
        self.eyes = eyes
        self.tail = tail
        self.furry = furry
    def describe(self):
        print(f"This dog has {self.eyes} eyes", (self.tail and "a tail" or "no tail"),"and is",(self.furry and "furry" or "not furry"))
        
        
buster = dog(1,2,3,True, False) #my dogs name
buster.describe()