class Solution:
    def frequencySort(self, s: str) -> str:
        dic_let = {}
        dic_freq = {}
        
        for i in s:
            if i in dic_let:
                dic_freq[dic_let[i]].remove(i)
                if len(dic_freq[dic_let[i]]) == 0:
                    dic_freq.pop(dic_let[i])
                dic_let[i] += 1
                dic_freq.setdefault(dic_let[i], [])
                dic_freq[dic_let[i]].append(i)
            else:
                dic_freq.setdefault(1, [])
                dic_let[i] = 1
                dic_freq[1].append(i)
        ret_string = ""
        for i in sorted(dic_freq.keys()):
            for e in dic_freq[i]:
                for h in range(0, i):
                    ret_string = e + ret_string
        return ret_string