'''
Authour=Ibin Siby
Discription=Input two lists from the user. Merge these lists into a third list such that in the merged list, all even numbers occur first followed by odd numbers. Both the even numbers and odd numbers should be in sorted order.
'''
list1=[25,12,2,56,7,6]
list2=[98,45,43,57]
combined_list=list1+list2

even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list=even_list+odd_list
print("list1=",list1)
print("list2=",list2)

print("Merged_list=",merged_list)
