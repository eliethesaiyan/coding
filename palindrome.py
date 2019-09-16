''' A palindrome is a sequence of characters that reads the same backwards and forwards.  Given a string s, find the longerst palindromic substring in s.
Example :
Input : banana
output :"anana"

Input : million
output : illi
'''
class Solution:
    def longest_palindrome(self,s):
        is_palindrome= False
        offset=[0,0]
        z = len(s)
        for i in range(0,int(z/2)):
            for j in reversed(range(int(z/2),z)):
                start = i 
                end =  j
                print(i,j)
                print(s[i:j+1])
                if s[start]==s[end] and not is_palindrome:
                   offset[0] = start
                   offset[1] = end + 1
                   print("this is the palindrome")
                   print(s[start:end+1])
                   is_palindrome = True
                   sub_len = len(s[start:end+1])
                   
                   for a  in range(0,sub_len//2):
                       if s[i+a] != s[j-a]:
                           print(s[i+a],s[j-a])
                           print("subtring dont  match") #is_palindrome= False
                           is_palindrome=False
                           continue 
                else: 
                    continue
        

        print(len(s[offset[0]:offset[1]]))
        return s[offset[0]:offset[1]]

s = "abracadabra"
print(str(Solution().longest_palindrome(s)))




