from collections import defaultdict 
   
class Graph: 
   
    def __init__(self,V): 
        self.V=V  
        self.graph=defaultdict(list)  
        self.comp=0
   
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
          
    def SCCUtil(self, u, low, disc, stackMember, st): 
        disc[u]=self.comp
        low[u]=self.comp
        self.comp+=1
        stackMember[u]=True
        st.append(u) 
  
        for v in self.graph[u]:
            if disc[v] == -1 : 
                self.SCCUtil(v, low, disc, stackMember, st) 
                low[u] = min(low[u], low[v]) 
            elif stackMember[v] == True:  
                low[u] = min(low[u], disc[v]) 
        if low[u] == disc[u]: 
            while w != u: 
                w = st.pop() 
                print(w, end=' ')
                stackMember[w] = False
            print()
              
    def SCC(self):
        disc = [-1] * (self.V) 
        low = [-1] * (self.V) 
        stackMember = [False] * (self.V) 
        st =[]
        for i in range(self.V): 
            if disc[i] == -1: 
                self.SCCUtil(i, low, disc, stackMember, st) 



# Tarjan's Algorithm in Python3 using SIngle-DFS
