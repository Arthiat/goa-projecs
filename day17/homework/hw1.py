def remove(list,element):
     j=0
     while j < len(list):
         if list[j] ==element:
             del list[j]
             break
         j+=1
     return list

print(remove([1,2,3,4,5],2))