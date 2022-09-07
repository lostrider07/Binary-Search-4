#Time complexity: O(m + n)
#Space complexity: O(n)

#Hashmap
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #None check
        if len(nums2) > len(nums1):
            return self.intersect(nums2, nums1)
        hashmap = {}
        
        for i in nums1:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                
        result = []
        for i in nums2:
            if i in hashmap:
                if hashmap[i] > 0:
                    hashmap[i] -= 1
                    result.append(i)
        return result
      
      
      
#Two Pointer
#Time complexity: O(mlogm) or O(nlogn)  #The largest one
#Space compelxity: O(m +n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        nums1.sort()
        nums2.sort()

        result = []
        
        #None check
        if n2 > n1:
            return self.intersect(nums2, nums1)
        p1 = 0
        p2 = 0
       
        while p1 < n1 and p2 < n2:
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
                
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return result

      
#Binary Search
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        nums1.sort()
        nums2.sort()

        result = []
        
        #None check
        if n2 > n1:
            return self.intersect(nums2, nums1)
       
    
        low = 0
        high = n2 - 1
        
        for i in range(n1):
            high = n2 - 1
            while low <= high:
                mid = (low + high)//2
                if nums2[mid] == nums1[i]:
                    if low < mid and nums2[mid - 1] == nums2[mid]:
                        high = mid - 1

                    else:
                        result.append(nums2[mid])
                        low = mid + 1
                        break

                elif nums2[mid] > nums1[i]:
                    high = mid - 1
                else:
                    low = mid + 1

        return result
                    
                    
