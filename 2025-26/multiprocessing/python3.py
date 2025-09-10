import multiprocessing
import time
def producer(q):
    for i in range(10):
        print("Adding:",i)
        q.put(i)
        time.sleep(1)


def consume(q):
    while True:
        item=q.get()
        if item is None:
            break
        print(item)
        time.sleep(1)


if __name__=='__main__':
    queue=multiprocessing.Queue()
    m1=multiprocessing.Process(target=producer,args=(queue,))
    m2=multiprocessing.Process(target=consume,args=(queue,))
    m1.start()
    m2.start()
    # queue.put("Aakash ")
    m1.join()
    m2.join()