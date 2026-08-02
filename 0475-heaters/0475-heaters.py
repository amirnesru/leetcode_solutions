class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0
        heater_idx = 0

        for house in houses:
            while heater_idx + 1 < len(heaters):
                curr_dist = abs(heaters[heater_idx] - house)
                next_dist = abs(heaters[heater_idx + 1] - house)

                if next_dist <= curr_dist:
                    heater_idx += 1
                else:
                    break
            closest_dist = abs(heaters[heater_idx] - house)
            
            if closest_dist > max_radius:
                max_radius = closest_dist

        return (max_radius)