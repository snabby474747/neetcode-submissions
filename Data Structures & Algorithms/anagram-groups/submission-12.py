class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # res = defaultdict(list)

        # for i in strs:
        #     count = [0]*26

        #     for j in i:
        #         count[ord(j) - ord("a")] +=1

        #     res[tuple(count)].append(i)

        # return list(res.values())

        res = defaultdict(list)

        for i in strs:
            count = [0]*26

            for j in i:
                count[ord(j)-ord("a")]+=1

            res[tuple(count)].append(i)

        return list(res.values())

        
        # res = defaultdict(list)

        # for word in strs:
        #     key = tuple(sorted(Counter(word).items()))
        #     res[key].append(word)

        # return list(res.values())

        # res = defaultdict(list)

        # for i in strs:
        #     key = tuple(sorted())
