import collections
from typing import List


class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) \
            -> List[str]:
        counter = collections.Counter(features)
        feature_set = set(features)
        positions = {x: i for i, x in enumerate(features)}

        for response in responses:
            visited = set()

            for feature in response.split(' '):
                if feature in feature_set and feature not in visited:
                    counter[feature] += 1
                    visited.add(feature)

        sorted_features = [(-c, positions[f], f) for f, c in counter.items()]
        sorted_features.sort()

        return [x[2] for x in sorted_features]
