from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = defaultdict(int)
        n1 = len(nums1)
        n2 = len(nums2)
        n3 = len(nums3)
        n4 = len(nums4)
        count = 0
        for a in range(n1):
            for b in range(n2):
                hashmap[nums1[a] + nums2[b]] += 1
        for c in range(n3):
            for d in range(n4):
                target = -(nums3[c] + nums4[d])
                if target in hashmap:
                    count += hashmap[target]

        return count

  # so here its basically 4 pointers approach in which the pointer traverse in a 4 different arrays with different pointers.
  # nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2] , target = 0
  # From the above arrays . target = 0, so, nums1[a] + nums2[b] + nums3[c] + nums4[d] = target= 0 ; so we can write simply w + x + y + z = 0 ==> w + x = -(y + z)
  # so lets say if (w + x) is in hashmap .so if w + x is in hashmap,so -(y + z) which is equals to w + x, so the hashmap[target] == -(y + z) == w + x, so we return count of the target in which we found w + x or -(y +z)
  # from the above example w + x count will be the same as -(y + z) will be the same so we return count which give us the target = 0 by adding w + x + y + z
