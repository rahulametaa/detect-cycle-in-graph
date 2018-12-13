class Graph:
    def __init__(self,N,E):
        self.N=N
        self.E=E
        self.edges=[]
        self.disjoint_set=[]
        self.take_input(N,E)
    
    def take_input(self,N,E):
        print('Enter nodes one by one:')
        for i in range(N):
            self.add_nodes(int(input('enter node:')))
        print('Enter edges one by one:')
        for i in range(E):
            self.add_edges(list(map(int,input('enter edge:').split(' '))))
        
    
    def add_nodes(self,v):
        self.disjoint_set.append([v,-1])
    
    def add_edges(self,E):
        self.edges.append(E)
    
    def search(self,x):
        for i in range(self.N):
            if(self.disjoint_set[i][0]==x):
                return i
    
    def find(self,x):
        i=self.search(x)
        if(self.disjoint_set[i][1]<0):
            return (x,self.disjoint_set[i][1])
        return self.find(self.disjoint_set[i][1])
    
    def union(self,x,y):
        t1=self.find(x)
        t2=self.find(y)
        i=self.search(t1[0])
        j=self.search(t2[0])
        if(t1[1]<=t2[1]):
            self.disjoint_set[i][1]+=t2[1]
            self.disjoint_set[j][1]=t1[0]
        else:
            self.disjoint_set[j][1]+=t1[1]
            self.disjoint_set[i][1]=t2[0]
        
    
    def detect_Cycle(self):
        for i in self.edges:
            if(self.find(i[0])[0]!=self.find(i[1])[0]):
                self.union(i[0],i[1])
            else:
                return True
        return False
                
          

g1=Graph(4,4)
print(g1.detect_Cycle())
