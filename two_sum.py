"""   
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def two_sum(nums,target):
    index_m = []
    check_sum = 0
    for i in range(len(nums)) : #points to the finst item in the list
       #print('>>>>'+str(nums[i]))
       #for each item, lets add with items left to it
       for j in range(i-1,-1,-1):
          #print('#######Item:'+str(nums[i])+'----: other item'+str(nums[j]))
           check_sum = nums[i] + nums[j]
           if check_sum == target :
               if nums.index(nums[i]) not in index_m :
                   index_m.append(nums.index(nums[i]) )
               
          
      #for each item, lets add with items Right to it  
       for j in range(i+1,len(nums),1):
           #print('Item:'+str(nums[i])+'----: other item'+str(nums[j]))
           check_sum = nums[i] + nums[j]
           if check_sum == target :
            
              if nums.index(nums[i]) not in index_m :
                   index_m.append(nums.index(nums[i]) )
    return index_m

