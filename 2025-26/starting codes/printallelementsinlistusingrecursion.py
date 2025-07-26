def listelement(list,index=0):
    if(len(list)==index):
        return
    print(list[index])
    listelement(list,index+1)

a=[1,2,3,4,5,6]
b=["a",'b',"c","d","e"]
listelement(b)