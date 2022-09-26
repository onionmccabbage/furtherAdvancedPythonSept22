# threads and processing are related
# a multi-processor computer can run many threads on each processor
import multiprocessing
# each thread will run in the SAME python instance (on ONE CPU) - threads are CPU-bound
# each process can run on SEPARATE Python instances, on separate CPUs

print(multiprocessing.cpu_count())

