class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        for i in range(len(score)):
            arr.append(score[i][k])
        arr.sort(reverse=True)
        result=[]                                            
        for i in range(len (score)):
            for j in range (len(score)):
                if arr[i]==score[j][k]:
                    result.append(score[j])
        return result

            
