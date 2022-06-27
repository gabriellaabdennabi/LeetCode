class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0 
        hi = len(nums)-1 

        while lo < hi:
            mid = (lo+hi) // 2

            if nums[mid] == nums[mid-1]:
                if ((mid-1) - lo) %2 != 0:
                    hi = mid - 2 
                else:
                    lo = mid + 1


            elif nums[mid] == nums[mid+1]:
                if (hi - (mid+1)) % 2 != 0:
                    lo = mid + 2 

                else:
                    hi = mid - 1

            else:
                return nums[mid]

        return nums[lo]



