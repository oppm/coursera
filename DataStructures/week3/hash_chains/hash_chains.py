# python3
import sys

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.buckets = [None] * bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            chain = self.buckets[query.ind]
            if chain != None:
                self.write_chain(chain)
            else:
                print("")
        else:
            hash_val = self._hash_func(query.s)
            chain = self.buckets[hash_val]
            if chain == None:
                chain = []

            try:
                ind = chain.index(query.s)
            except ValueError:
                ind = -1

            if query.type == 'add':
                if ind == -1:
                    chain.insert(0, query.s)
                    self.buckets[hash_val] = chain                    
            elif query.type == 'find':
                self.write_search_result(ind != -1)
            else: # del
                if ind != -1:
                    chain.pop(ind)

    def process_query_naive(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

def test(bucket_count, queries):
    proc = QueryProcessor(bucket_count)
    for q in queries:
        proc.process_query(q)
    return True

def test_verify(bucket_count, queries):
    print("passed" if test(bucket_count, queries) else "failed")

def unit_test():
#    test(5, [
#        Query(["add", "world"]),
#        Query(["add", "HellO"]),
#        Query(["check", 4]),
#        Query(["find", "World"]),
#        Query(["find", "world"]),
#        Query(["del", "world"]),
#        Query(["check", 4]),
#        Query(["del", "HellO"]),
#        Query(["add", "luck"]),
#        Query(["add", "GooD"]),
#        Query(["check", 2]),
#        Query(["del", "good"])])
#    test(4, [
#        Query(["add", "test"]),
#        Query(["add", "test"]),
#        Query(["find", "test"]),
#        Query(["del", "test"]),
#        Query(["find", "test"]),
#        Query(["find", "Test"]),
#        Query(["add", "Test"]),
#        Query(["find", "Test"])
#    ])
    test(3, [
        Query(["check", 0]),
        Query(["find", "help"]),
        Query(["add", "help"]),
        Query(["add", "del"]),
        Query(["add", "add"]),
        Query(["find", "add"]),
        Query(["find", "del"]),
        Query(["del", "del"]),
        Query(["find", "del"]),
        Query(["check", 0]),
        Query(["check", 1]),
        Query(["check", 2])
    ])

def main():
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:
        main()      