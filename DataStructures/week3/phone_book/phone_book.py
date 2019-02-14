# python3
import sys

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

    def create_instance(obj):
        if obj.type == 'add':
            return Query([obj.type, obj.number, obj.name])
        else:
            return Query([obj.type, obj.number])

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [None] * 10000000
    for cur_query in queries:
        if cur_query.type == 'add':            
            contacts[cur_query.number] = cur_query
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
        else:
            contact = contacts[cur_query.number]
            if contact != None:
                response = contact.name
            else:
                response = 'not found'
            result.append(response)
    return result

def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

def test_single(queries):
    queries_naive = []
    for q in queries:
        queries_naive.append(Query.create_instance(q))
    res_fast = process_queries(queries)
    res_naive = process_queries_naive(queries_naive)
    if len(res_fast) != len(res_naive):
        return False
    for i in range(len(res_fast)):
        if res_fast[i] != res_naive[i]:
            return False
    return True

def test(queries):
    print("passed" if test_single(queries) else "failed")

def unit_test():
    test([
        Query(['add', 911, 'police']),
        Query(['add', 76213, 'Mom']),
        Query(['add', 17239, 'Bob']),
        Query(['find', 76213]),
        Query(['find', 910]),
        Query(['find', 911]),
        Query(['del', 910]),
        Query(['del', 911]),
        Query(['find', 911]),
        Query(['find', 76213]),
        Query(['add', 76213, 'daddy']),
        Query(['find', 76213])])

def main():
    write_responses(process_queries(read_queries()))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:
        main()      
