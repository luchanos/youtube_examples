class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: "ListNode"):
        cur_self = self
        cur_other = other

        while True:
            if cur_self is None and cur_other is None:
                return True
            if cur_self is not None and cur_other is not None and cur_self.val == cur_other.val:
                cur_self = cur_self.next
                cur_other = cur_other.next
                continue
            return False
