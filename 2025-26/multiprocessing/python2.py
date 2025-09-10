import multiprocessing
import sys
def test():
    print("This is my function1")
if __name__=='__main__':
    m=multiprocessing.Process(target=test)
    print("This is my main prog")
    m.start()
    m.join()