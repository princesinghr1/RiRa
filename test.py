class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def addNode(head,data):
    temp=head
    while(temp.next!=None):
        temp=temp.next
    newNode=node(data)
    temp.next=newNode
    newNode.prev=temp
def delNode(head,data):
    temp=head
    while(temp.data!=data):
        temp=temp.next
        if (temp==None):
            return "No data"
    temp.prev.next=temp.next
    if temp.next:
        temp.next.prev=temp.prev
def printNode(head):
    while head:
        print(head.data,sep="-->")
        head=head.next
head=node(5)
addNode(head,7)
addNode(head,8)
printNode(head)
delNode(head,7)
printNode(head)
        

