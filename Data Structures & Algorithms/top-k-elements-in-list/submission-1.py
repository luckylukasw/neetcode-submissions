class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements = {}
        buckets = [[] for i in range(len(nums))]
        for num in nums:
            if num not in frequent_elements:
                frequent_elements[num] = 1
            else:
                frequent_elements[num] = frequent_elements[num] + 1
        for num, frequency in frequent_elements.items():
            buckets[frequency-1].append(num)
        buckets.reverse()
        output = []
        for bucket in buckets:
            for num in bucket:
                output.append(num)
                if (len(output) >= k):
                    return output