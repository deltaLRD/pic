import os

for root, dirs, files in os.walk(os.getcwd()):
    
    if root != "D:\\pic":
        continue
    pics = []
    for pic in files:
        if pic.find(".cmd")!=-1:
            continue
        if pic.find(".py")!=-1:
            continue
        if pic.find(".html")!=-1:
            continue
        pics.append(pic)
        print(os.path.getctime(pic))

    pics.sort(key=lambda x: os.path.getctime(x))

    print(pics)
    index = 1
    pics_next = []
    for i in pics:
        os.rename(i, "img"+str(index).rjust(5,"0")+".jpg")
        pics_next.append("img"+str(index).rjust(5,"0")+".jpg")
        index += 1
    index = 1
    for i in pics_next:
        os.rename(i, str(index).rjust(5,"0")+'.jpg')
        index += 1
