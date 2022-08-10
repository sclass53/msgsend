import os
w,tmp=os.path.split(__file__)
def sendsth(name,message,title):
    with open("msg/"+title+".md","w+") as f:
        f.write("### Msg_from: "+name+"\n\n")
        f.write("## Title: "+title+"\n\n")
        f.write(message[:-2])
    os.system("cd "+w+"msg")
    os.system("git init")
    os.system("git remote add origin https://github.com/sclass53/msgsend.git")
    os.system("git add .")
    os.system('git commit -m "init project"')
    os.system("git config --unset http.proxy")
    os.system("git config --unset https.proxy")
    os.system('git config credential.username "ginoblog"')
    os.system('git config credential.useremail "gino_redlight@163.com"')
    os.system('git config --global user.name "ginoblog"')
    os.system('git config --global user.email "gino_redlight@163.com"')
    os.system('git branch -M master')
    os.system('git push -u origin master')
wl=''
while 1:
    wl=''
    com=input("FTP::>")
    if com=="send":
        fname=input("Author: ")
        ftitle=input("Title: ")
        fr=input("Content (Type '~' at any blank line to end): ")
        wl+=(fr+'\n')
        while fr!='~':
            fr=input()
            wl+=(fr+'\n')
        sendsth(fname,wl,ftitle)
        print("Msg sended successfully.\n")
        