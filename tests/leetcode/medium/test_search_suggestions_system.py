"""
https://leetcode.com/problems/search-suggestions-system/
"""

import pytest
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        combination = ""
        total_res = []
        for let in searchWord:
            res = []
            combination += let
            for word in products:
                if len(res) == 3:
                    break
                if word.startswith(combination):
                    res.append(word)
            total_res.append(res)
        return total_res


@pytest.mark.parametrize("input_data, search_word, expected", [
(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse", [
["mobile", "moneypot", "monitor"],
["mobile", "moneypot", "monitor"],
["mouse", "mousepad"],
["mouse", "mousepad"],
["mouse", "mousepad"]
]),
    (["havana"], "havana", [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]),
    (["bags","baggage","banner","box","cloths"], "bags", [["baggage","bags","banner"],["baggage","bags","banner"],
                                                          ["baggage","bags"],["bags"]])
])
def test_remove_element(input_data, search_word, expected):
    sol = Solution()
    assert sol.suggestedProducts(input_data, search_word) == expected
