class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split('.'), 
                                  version2.split('.'), 
                                  fillvalue='0'):
            d1, d2 = int(v1), int(v2)
            if d1 < d2:
                return -1
            elif d1 > d2:
                return 1
        return 0