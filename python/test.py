class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Node:
    def __init__(self,point,g=0,h=0):
        self.point=point
        self.father=None
        self.g=g
        self.h=h
    def manhattan(self,endNode): #曼哈顿算法计算h值，每一个节点对应终点都有一个h值
        self.h=abs(endNode.point.x-self.Point.x)+abs(endNode.point.y-self.point.y)
    def setG(self,g):
        self.g=g
    def setfather(self,node):
        self.father=node

class Astar:
    def __init__(self,map2d,startNode,endNode):
        self.map2d=map2d
        self.startNode=startNode
        self.endNode=endNode
        self.openlist=[]
        self.closelist=[]
        self.currentNode=startNode
        self.pathlist=[]
    
    def getminFNode(self):
        if self.openlist:
            nodetmp=self.openlist[0]
        for i in self.openlist:
            if i.g+i.h<nodetmp.g+nodetmp.h:
                nodetmp=i
        return nodetmp
    
    def NodeInOpenlist(self,node):
        for i in self.openlist:
            if node.point.x==i.point,x and node.point.y==i.point.y:
                return True
        return False
    
    def NodeInCloselist(self,node):
        for i in self.closelist:
            if node.point.x==i.point,x and node.point.y==i.point.y:
                return True
        return False
    
    def endNodeInOpenlist(self):
        for i in self.openlist:
            if self.endNode.point.x==i.point,x and self.endNode.point.y==i.point.y:
                return True
        return False
    
    def getNodeFromOpenlist(self,node):
        for i in self.openlist:
            if node.point.x==i.point,x and node.point.y==i.point.y:
                return i
        return NULL
    
    def SearchOneNode(self,node):
        if self.map2d.isPass(node.Point)!=True:
            return
        if self.NodeInCloselist(node):
            return
        if abs(self.currentNode.point.x-node.point.x)==1 and abs(self.currentNode.point.y-node.point.y)==1:
            gTemp=14
        else:
            gTemp=10
        
        if self.NodeInOpenlist(node)!=True:
            node.manhattan(self.endNode) #计算h值
            node.g=gTemp
            node.father=self.currentNode
            self.openlist.append(node)
        else:
            nodeTmp=self.getNodeFromOpenlist(node)
            if self.currentNode.g+node.g<nodeTmp.g:
                nodeTmp.g=self.currentNode.g+node.g
                nodeTmp.father=self.currentNode

def searchNear(self):
    """
    (x-1,y-1)(x-1,y)(x-1,y+1)
    (x  ,y-1)(x  ,y)(x  ,y+1)
    (x+1,y-1)(x+1,y)(x+1,y+1)
    """
    if self.map2d.isPass(Point(self.currentNode.point.x-1,self.currentNode.point.y)) and self.map2d.isPass(Point(self.currentNode.point.x,self.currentNode.point.y-1)): #为什么不是or？
        self.SearchOneNode(Node(Point(self.currentNode.point.x-1,self.currentNode.point.y-1)))
    self.SearchOneNode(Point(self.currentNode.point.x-1,self.currentNode.point.y))
    if self.map2d.isPass(Point(self.currentNode.point.x-1,self.currentNode.point.y)) and self.map2d.isPass(Point(self.currentNode.point.x,self.currentNode.point.y+1)):
        self.SearchOneNode(Point(self.currentNode.point.x-1,self.currentNode.point.y+1))
    self.SearchOneNode(Point(self.currentNode.point.x,self.currentNode.point.y-1))
    self.SearchOneNode(Point(self.currentNode.point.x,self.currentNode.point.y+1))
    if self.map2d,isPass(Point(self.currentNode.point.x,self.currentNode.point.y-1)) and self.map2d.isPass(Point(self.currentNode.point.x+1,self.currentNode.point.y)):
        self.SearchOneNode(Point(self.currentNode.point.x+1,self.currentNode.point.y-1))
    self.SearchOneNode(Point(self.currentNode.point.x+1,self.currentNode.point.y))
    if self.map2d.isPass(Point(self.currentNode.point.x,self.currentNode.point.y+1)) and self.map2d.isPass(Point(self.currentNode.point.x+1,self.currentNode.point.y)):
        self.SearchOneNode(Point(self.currentNode.point.x+1,self.currentNode.point.y+1))

def start(self):
    self.startNode.manhattan(self.endNode)
    self.startNode.setG(0)
    self.openlist.append(self.startNode)
    
    while True:
        self.currentNode=self.getminFNode()
        