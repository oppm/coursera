# python3
import sys
from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.q = [0] * (size+1)
        self.read_idx = 0
        self.write_idx = 0
        self.n = 0

    def insert(self, i):
        self.q[self.read_idx] = i
        self.read_idx = (self.read_idx+1) % (self.size+1)
        self.n = self.n+1

    def peek_back(self):
        return self.q[self.write_idx]

    def peek_front(self):
        idx = self.read_idx + (self.size+1) - 1
        idx %= (self.size+1)
        return self.q[idx]

    def pop(self):
        self.write_idx = (self.write_idx+1) % (self.size+1)
        self.n = self.n-1

    def empty(self):
        return self.read_idx == self.write_idx

    def full(self):
        return self.n == self.size

    def process(self, request):

        while not self.empty():
            time = self.peek_back()
            if time <= request.arrived_at:
                self.pop()
            else:
                break

        if self.empty():
            finish_time = request.arrived_at + request.time_to_process
            self.insert(finish_time)
            return Response(False, request.arrived_at)
        elif self.full():
            return Response(True, -1)
        else:
            finish_time_last_in = self.peek_front()
            self.insert(finish_time_last_in + request.time_to_process)
            return Response(False, finish_time_last_in)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

def test1():
    requests = []
    requests.append(Request(0, 5))
    requests.append(Request(1, 5))
    requests.append(Request(2, 5))
    requests.append(Request(3, 1))
    requests.append(Request(4, 1))
    requests.append(Request(100, 1))
    requests.append(Request(101, 1))
    requests.append(Request(102, 1))

    responses = process_requests(requests, Buffer(5))
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)   

def unit_test():
    test1()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        unit_test()
    else:
        main()
