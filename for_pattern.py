class for_pattern:
    def __init__(self, name):
        self.name = name

    def print_tri(self):
        for i in self.name:
            print(i)
            
    def print_straightline(self):
        for j in self.name:
            print(j,end="")   
        print()     
                
    def print_straight_backward(self):
        for j in self.name[::-1]:
            print(j,end="")
        print()    
            
    def print_backward(self):
        for k in self.name[::-1]:
            print(k)     
     
    def print_diagonal(self):
        for l in self.name:
            print(l)
        print()           

for_pattern("susith").print_tri()
for_pattern("susith").print_straightline()
"""for_pattern("susith").print_straight_backward()
for_pattern("susith").print_backward()"""
for_pattern("susith").print_diagonal()