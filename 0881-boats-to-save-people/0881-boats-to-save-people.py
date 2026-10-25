class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        slow = 0
        fast = len(people) - 1
        ans = 0
        people.sort()
        while slow <= fast:
            if people[slow] + people[fast] <= limit:
                slow += 1
            fast -= 1
            ans += 1

        return ans