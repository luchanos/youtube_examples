"""
https://leetcode.com/problems/capitalize-the-title/
"""

import pytest


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res_lst = []
        for x in title.split():
            res_lst.append(x.lower()) if len(x) < 3 else res_lst.append(x.title())
        return " ".join(res_lst)


@pytest.mark.parametrize("input_data, expected", [
    ("capiTalIze tHe titLe", "Capitalize The Title"),
    ("First leTTeR of EACH Word", "First Letter of Each Word"),
    ("i lOve leetcode", "i Love Leetcode"),
    ("L hV", "l hv")
])
def test_remove_element(input_data, expected):
    sol = Solution()
    assert sol.capitalizeTitle(input_data) == expected
