class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for d in cpdomains:
            visits = int(d.split(" ")[0])
            domain = d.split(" ")[1].split(".")
            for i in range(len(domain)-1,-1,-1):
                sub_domain = ".".join(domain[i:])
                if sub_domain in dic:
                    dic[sub_domain] += visits
                else:
                    dic[sub_domain] = visits
        
        ret_list = []
        for key, value in dic.items():
            ret_list.append(str(value)+" "+key)
        
        return ret_list