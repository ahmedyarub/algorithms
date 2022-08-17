class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        return not len(set(pairwise(nums)).difference(set([t for sequence in sequences for t in pairwise(sequence)])))
