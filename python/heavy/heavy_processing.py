
import os

import multiprocessing as mps

NO_PROCS = os.cpu_count()


def do_stuff():
    for i in range(1_000_000_000_000):
        nums = [x for x in range(i)]
        s = sum(nums)
        print(f"[{os.getpid()}] WOOT: {s}")


if __name__ == "__main__":
    procs = []

    for n in range(NO_PROCS):
        procs.append(mps.Process(target=do_stuff))

    for p in procs:
        p.start()

    for p in procs:
        p.join()

    print("-------- DONE ---------")
