class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = [[] for _ in range(len(searchWord))]
        for product in products:
            i = 0
            while i < min(len(product), len(searchWord)) and product[i] == searchWord[i]:
                if len(res[i]) < 3: res[i].append(product)
                i += 1
        return res
        