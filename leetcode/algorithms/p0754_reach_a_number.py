class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = 1

        while True:
            sum_so_far = step * (1 + step) // 2

            if sum_so_far >= target and (sum_so_far - target) % 2 == 0:
                break

            step += 1

        return step
