nums = (33, 55, 67, 66, 44, 34, 55)
i = 0
find = 67
while i < len(nums):
    print("not found", i)
    
    if nums[i] == find:
     print("number find at", i)
     break
    i += 1


nums = (33, 55, 67, 66, 44, 34, 55)
i = 0
find = 67

while i < len(nums):
    print("checking index:", i)

    if nums[i] == find:
        print("number found at index", i)
        break   # stop the loop when found

    i += 1       # move to next index

    # print the number in for loop.
    num = [1, 2, 4, 66, 55, 78, 34,99]
    for el in num: #el in  means all the value which are present in num
       print(el)

       