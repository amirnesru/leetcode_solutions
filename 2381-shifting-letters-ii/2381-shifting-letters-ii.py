class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        arr = [0]*(len(s)+1)
        for i in shifts:
            if i[2] == 0 :
                arr[i[0]]-=1
                arr[i[1]+1]+=1
            else:
                arr[i[0]]+=1
                arr[i[1]+1]-=1
        for i in range (1,len(arr)):
            arr[i]+=arr[i-1]
            arr[i]= arr[i]
        for i in range(len(s)):
            arr[i]+=ord(s[i])-97
            arr[i] = arr[i] % 26 + 97
        ss= ""
        for i in range(len(s)):
            ss+=chr(arr[i])

        return ss