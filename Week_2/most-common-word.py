class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_split = paragraph.lower().split(" ")
        punct = ["!","?",",",";","."]
        # paragraph_split = "".join(ch for ch in paragraph if ch not in punct).split(" ")
        dic = {}
        max_ocurrence = ""
        times = 0
        for words in paragraph_split:
            ws = "".join(words.split("'"))
            for i in range(0,len(ws)):
                if ws[i] in punct:
                    ws = ws[:i] + " " + ws[i+1:]
            splits = ws.split(" ")
            for w in splits:
                if w not in banned and w != "":
                    dic.setdefault(w, 0)
                    dic[w] += 1
                    if dic[w] > times:
                        times = dic[w]
                        max_ocurrence = w
        return max_ocurrence