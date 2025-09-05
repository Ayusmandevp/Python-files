# Object Count Tracker: Design a class that tracks how many objects have been created from it and has a method to display this count.


class countTracker:
    count=0
    def __init__(self):
        countTracker.count+=1
        print("hello")
    @staticmethod
    def show_count():
        print(f"count is {countTracker.count}")
c1=countTracker()
c2=countTracker()
c3=countTracker()
c4=countTracker()
print(countTracker.count)