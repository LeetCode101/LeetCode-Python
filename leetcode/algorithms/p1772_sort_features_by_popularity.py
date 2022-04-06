import collections
from typing import List


class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) \
            -> List[str]:
        counter = collections.Counter(features)
        feature_set = set(features)
        positions = {x: i for i, x in enumerate(features)}

        for response in responses:
            for feature in set(response.split(' ')):
                if feature in feature_set:
                    counter[feature] += 1

        sorted_features = [(-c, positions[f], f) for f, c in counter.items()]
        sorted_features.sort()

        return [x[2] for x in sorted_features]
