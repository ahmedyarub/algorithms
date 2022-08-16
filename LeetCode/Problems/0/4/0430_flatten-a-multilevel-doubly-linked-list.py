class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def flatten(h: Node) -> Tuple:
            cur, t = h, h

            while cur:
                t = cur

                if cur.child:
                    ch, ct = flatten(cur.child)
                    ct.next = cur.next

                    if cur.next:
                        cur.next.prev = ct
                    else:
                        t = ct

                    cur.next = ch
                    ch.prev = cur

                    cur.child = None
                    cur = ct.next
                else:
                    cur = cur.next

            return h, t

        return flatten(head)[0]
