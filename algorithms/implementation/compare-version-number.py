class Solution():

    def remove_leading_zeros(self, version):
        arr = version.split('.')
        res = []
        while arr:
            item = arr.pop(0)
            new_str = ""
            for i, e in enumerate(item):
                if i == 0 and e == '0':
                    continue
                else:
                    break
            item = item[i:]
            res.append(item)
        return ".".join(res)

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = self.remove_leading_zeros(version1)
        version2 = self.remove_leading_zeros(version2)
        v1 = [int(e) for e in version1.split('.')]
        v2 = [int(e) for e in version2.split('.')]

        l1 = len(v1) - 1
        l2 = len(v2) - 1
        while l1 >= 0 and v1[l1] == 0:
            v1.pop(l1)
            l1 -= 1
        while l2 >= 0 and v2[l2] == 0:
            v2.pop(l2)
            l2 -= 1

        v1 = tuple(v1)
        v2 = tuple(v2)

        if v1 == v2:
            return 0

        if v1 > v2:
            return 1
        return -1
