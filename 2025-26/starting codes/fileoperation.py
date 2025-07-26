def check_word():
    f=open("practice.txt","r")
    data=f.read()
    if(data.find("learning")!=-1):
        print("found")
    else:
        print("not found")

def check_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if (word in data):
                print(line_no)
                return
            line_no+=1
    return -1

check_line()