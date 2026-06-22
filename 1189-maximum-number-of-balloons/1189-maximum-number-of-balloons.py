class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = Counter(text)
        s= "balloon"
        d =Counter(s)
        arr =[]
        for i in dic :
            if i in d :
                arr.append(dic[i]//d[i])
        if len(arr) == 5:
            return min(arr)
        else: 
            return 0      


        # we ca also solve like this 
        # d = Counter(text)
        # return min(d['b'],d['a'],d['l'] // 2,d['o'] // 2,d['n'] )       
