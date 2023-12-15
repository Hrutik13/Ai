from collections import defaultdict
jug1=int(input("Enter water level for jug1"))
jug2=int(input("Enter water level for jug2"))
aim=int(input("Enter water level aim"))
visited=defaultdict(lambda:False)
print("Jug1\t Jug2")
def waterJug(amt1,amt2):
    if(amt1==aim and amt2==0)or(amt2==aim and amt1==0):
        print("-"*25)
        print(amt1,"\t",amt2,'->Goal State')
        print("-"*25)
        return True
    if visited[(amt1,amt2)]==False:
      print(amt1,"\t",amt2)
      visited[(amt1,amt2)]=True

      return(waterJug(0,amt2)or
             waterJug(amt1,0)or
             waterJug(jug1,amt2)or
             waterJug(amt1,jug2)or
             waterJug(amt1+min(amt2,(jug1-amt1)),
             amt2-min(amt2,(jug1-amt1)))or
             waterJug(amt1-min(amt1,(jug2-amt2)),
             amt2+min(amt1,(jug2-amt2))))
    else:
        return False
print("Steps:")
waterJug(0,0)
