
class Table:
    def __init__(self, tableNo, waiterName, status):
        self.tableNo=tableNo
        self.waiterName=waiterName
        self.status=status

def findWaiterWiseTotalNoOfTables(tc):
    l=dict()
    mm=[]
    for j in tc:
        mm.append(j.waiterName)
    for i in tc:
        if i.waiterName not in l.keys():
            l.update({i.waiterName: mm.count(i.waiterName)})
    sorted(l.keys())
    return(l)
        

def findWaiterByNameByTableNo(tc,tno):
    for i in tc:
        if i.tableNo==tno:
            return(i.waiterName)
    return "No Table Found"



if __name__=="__main__":
    n=int(input())
    tc=[]
    for i in range(n):
        tableNo=int(input())
        waiterName=input()
        status=input()
        tc.append(Table(tableNo,waiterName,status))
    tno=int(input())
    x=findWaiterWiseTotalNoOfTables(tc)
    y=findWaiterByNameByTableNo(tc,tno)
    for key,value in sorted(x.items()):
        print("{0}-{1}".format(key,value))
    print(y)