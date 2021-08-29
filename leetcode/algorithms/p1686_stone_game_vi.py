from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        scores = [(aliceValues[i] + bobValues[i], i)
                  for i in range(len(aliceValues))]
        scores.sort(reverse=True)

        alice_score, bob_score = 0, 0

        for i in range(len(scores)):
            _, j = scores[i]

            if i & 1 == 0:
                alice_score += aliceValues[j]
            else:
                bob_score += bobValues[j]

        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0
