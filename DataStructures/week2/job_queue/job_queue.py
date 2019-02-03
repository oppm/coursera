# python3
import sys
from random import randint

class Worker:
    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.end_time = 0

    def __gt__(self, other):
        if self.end_time > other.end_time:
            return False
        elif self.end_time < other.end_time:
            return True
        else:
            return self.thread_id < other.thread_id

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def is_complete(self, i):

        n = len(self.workers)
        
        if i >= n-1:
            return True

        l = (i*2+1)
        r = (i*2+2)
        
        if l <= n-1:
            if self.workers[i] < self.workers[l]:
                return False
        if r <= n-1:
            if self.workers[i] < self.workers[r]:
                return False

        return self.is_complete(l) and self.is_complete(r)

    def assert_complete(self):
        complete = self.is_complete(0)

        if not complete:
            pass
        else:
            pass

    def sift_up(self, i):
        if i > 0:
            j = (i-1)//2
            worker_i = self.workers[i]
            worker_parent = self.workers[j]

            if worker_i > worker_parent:
                self.workers[i], self.workers[j] = self.workers[j], self.workers[i]
                self.sift_up(j)

    def sift_down(self, i):

        n = len(self.workers)
        l = (i*2+1)
        r = (i*2+2)
        max_i, max = i, self.workers[i]
        if l <= n-1:
            if self.workers[l] > max:
                max_i, max = l, self.workers[l]
        if r <= n-1:
            if self.workers[r] > max:
                max_i, max = r, self.workers[r]
        
        if max_i != i:
            self.workers[max_i], self.workers[i] = self.workers[i], self.workers[max_i]
            self.sift_down(max_i)        

    def insert(self, worker):
        self.workers.append(worker)
        self.sift_up(len(self.workers)-1)
        #self.assert_complete()

    def extract_max(self):
        max = self.workers[0]

        self.workers[0] = self.workers[len(self.workers)-1]
        self.workers.pop()

        if len(self.workers) > 0:
            self.sift_down(0)

        #self.assert_complete()
        return max

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        self.workers = []
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        for thread_id in range(self.num_workers):
            self.insert(Worker(thread_id))

        for i in range(len(self.jobs)):
            next_job = self.jobs[i]
            worker = self.extract_max()
            self.assigned_workers[i] = worker.thread_id
            self.start_times[i] = worker.end_time
            worker.end_time += next_job
            self.insert(worker)

    def assign_jobs_naive(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
        pass

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

def cmp(a, b):
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
    else:
        return False
    
def test(num_workers, jobs):
    job_queue = JobQueue()
    job_queue.num_workers = num_workers
    job_queue.jobs = jobs
    job_queue.assign_jobs()
    assigned_workers_0 = job_queue.assigned_workers
    start_times_0 = job_queue.start_times
    job_queue.assign_jobs_naive()
    eq_0 = cmp(assigned_workers_0, job_queue.assigned_workers)
    eq_1 = cmp(start_times_0, job_queue.start_times)
    print("passed" if eq_0 and eq_1 else "failed")

def stress_testing():
    while True:
        num_workers = randint(1, 10)
        num_jobs = randint(1, 10)
        jobs = [0] * num_jobs
        for i in range(num_jobs):
            jobs[i] = randint(0, 1000)
        test(num_workers, jobs)

def unit_test():
    test(4, [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
    test(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    test(4, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    test(1, [9,8,7,6,5,4,3,2,1])
    test(4, [9,8,7,6,5,4,3,2,1])
    test(4, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    test(2, [1, 2, 3, 4, 5])
    test(5, [43, 23, 5])
    #test(100000, [1])
    test(2, [9, 9, 9])
    test(4, [1, 1, 0, 0, 2, 2])
    test(3, [1, 1, 9, 1])
    test(9, [824, 692, 349, 0, 100, 112, 17, 189, 794, 140])

def main():
    job_queue = JobQueue()
    job_queue.solve()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
        stress_testing()
    else:
        main()      
