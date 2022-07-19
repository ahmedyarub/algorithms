class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        if self.iter.hasNext():
            self.nxt = self.iter.next()
        else:
            self.nxt = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nxt

    def next(self):
        """
        :rtype: int
        """
        result = self.nxt
        if self.iter.hasNext():
            self.nxt = self.iter.next()
        else:
            self.nxt = None

        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nxt is not None
