# Given a sorted array, A, with possibly duplicated elements, find the indices of the the first and last occurences of the target elemen,t x. Return -1 if the ttarget is not found 
A1 = [1,3,3,5,7,8,9,9,9,15] # target=9,  output = 9 
A2 = [100,150,150,150,153] # target=150, output = [1,2]
A3 = [1,2,3,4,5,6,10] # target = 9, output [-1,-1]

class Solution:
    def get_range(self, arr, target):
        indices=[-1,-1]
        arr_size= len(arr)
        first_index =  True 
        for i in range(0, arr_size):
            if  first_index and  target ==arr[i]:
                indices[0]=i
                print("found once")
                first_index = False 
            if arr[i] == target:
                indices[1]=i
        if target != arr[indices[1]] :
            return [-1,-1]
        return indices 



arr = [1,2,2,2,2,3,4,7,8,8]
x = 2 
print(Solution().get_range(arr,x))
