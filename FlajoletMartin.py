from numpy import median
import mmh3


class FlajoletMartin:
    def __init__(self, L=20, hashes_count=1, hash_group_count=1):
        self.L = L  # Is corresponded to maximum length of binary-strings
        self.__hashes_count = hashes_count
        self.__hashes_group_count = hash_group_count
        self.results = [0] * hash_group_count

    def run(self, string):
        """ Starts Flajolet-Martin algorithm on single input string.
        :param string: Input string
        :type string: str
        :return: nothing
        :rtype: None
        Example:
        >>> fm = FlajoletMartin(L=100)
        >>> for string in stream:
        >>>     fm.run(string)
        """
        __seed = 0
        for __i in range(self.__hashes_group_count):
            __max_tail_0_count = 0
            for __j in range(self.__hashes_count):
                __seed += 1
                __hash_func = lambda x: (mmh3.hash(x, __seed, signed=False) % 2**self.L)
                __hash_num = __hash_func(string)
                __tail_0_count = self.countTrailingZeros(__hash_num)
                if __tail_0_count > __max_tail_0_count:
                    __max_tail_0_count = __tail_0_count
                self.results[__i] += 2 ** __max_tail_0_count
            self.results[__i] /= __j

    def getResult(self):
        """ Returns estimated value for counting distinct strings.
        :return: Estimated count
        :rtype: int
        Example:
        >>> fm = FlajoletMartin(L=100)
        >>> for string in stream:
        >>>     fm.run(string)
        >>> print fm.getResult()    # prints estimated count
        """
        return int(median(self.results))

    def countTrailingZeros(self, hash_num):
        """ Counts trainling zeros of hash_num bits-string.
        :param hash_num: Output value of hashing process.
        :type hash_num: int
        :return: Number of trailing zeros.
        :rtype: int
        Example:
        >>> fm = FlajoletMartin(L=100)
        >>> print fm.countTrailingZeros(7)      # 0
        >>> print fm.countTrailingZeros(6)      # 1
        >>> print fm.countTrailingZeros(4)      # 2
        """
        if hash_num == 0:
            return self.L
        __c = 0
        __hash_num = hash_num
        while __hash_num % 2 == 0:
            __c += 1
            __hash_num /= 2
        return __c
