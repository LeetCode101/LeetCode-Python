# Time Limit Exceeded!
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        sums = set()
        sum_so_far = 0
        count = 0

        for i in range(1, n + 1):
            sum_so_far += i

            if sum_so_far == n:
                count += 1
            elif (sum_so_far - n) in sums:
                count += 1

            if sum_so_far not in sums:
                sums.add(sum_so_far)

        return count
