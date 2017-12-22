from Tkinter import *
import Tkinter as tkinter
import time
from PIL import Image, ImageTk

root = Tk()
root.title("GendBR Generator")
root.geometry("360x150")
root.config(relief=SOLID, bg='#252525', bd=1)
root.option_add("*Font", "FOT-RodinBokutoh 8")

def GENDBR(event):

    x1=res_gendbr_entry1.get()
    x2=res_gendbr_entry2.get()
    
    global x1_len
    global x2_len
    global max_len
    global min_len
    global x1_ismax
    global x2_ismax
    global x1x2_ismax

    max_len=0
    min_len=0
    x1_ismax=0
    x2_ismax=0
    x1x2_ismax=0    
    diff_start=None
    pre=None
    post1=None
    post2=None
    remi=None
    remi_pos=None
    generated=0

    if x1 == '':
        res_gendbr_entry3.delete(1.0, END)
        res_gendbr_entry3.insert(1.0, "You didn't insert the 1st value.")
        if x2 == '':
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, "You didn't insert any value...")
        return

    if x2 == '':
        res_gendbr_entry3.delete(1.0, END)
        res_gendbr_entry3.insert(1.0, "You didn't insert the 2nd value.")
        return
    if x1 == x2:
        res_gendbr_entry3.delete(1.0, END)
        res_gendbr_entry3.insert(1.0, "These two entries are identical...")
        return

    def getvar_console(x):
        if x == 1:
            z = 'Getting entry values = x1: %s | x2: %s' %(x1, x2)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x == 2:
            z = 'Determining entry length = x1_len: %s | x2_len: %s' %(x1_len, x2_len)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x == 3:
            if x1_ismax == 1:
                z='Determining maximum entry: x1'
            if x2_ismax == 1:
                z='Determining maximum entry: x2'
            if x1x2_ismax == 1:
                z='Determining maximum entry: x1 equals x2'
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()    
        if x == 4:
            z= 'Checking max/min length = Maximum length: %s, Minimum length: %s' %(max_len, min_len)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x == 5:
            z='Difference starts at %s position' %(diff_start)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x == 6:
            z='Setting prefix: %s' %(pre)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x == 7:
            z = 'Removing prefix'
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            z = 'Getting new values = x1: %s | x2: %s' %(x1, x2)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            z = 'Getting new values = x1_len: %s | x2_len: %s' %(x1_len, x2_len)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            if x1_ismax == 1:
                z='Getting new maximum entry: x1'
            if x2_ismax == 1:
                z='Getting new maximum entry: x2'
            if x1x2_ismax == 1:
                z='Getting new maximum entry: x1 equals x2'
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            z= 'Getting new max/min length = Maximum length: %s, Minimum length: %s' %(max_len, min_len)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x == 8:
            z='Reminescent = %s, Position 1: %s, Position 2: %s' %(remi, remi_pos1, remi_pos2)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x == 9:
            z='Removing reminescents'
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            z = 'Getting new values = x1: %s | x2: %s' %(x1, x2)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            z = 'Getting new values = x1_len: %s | x2_len: %s' %(x1_len, x2_len)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            if x1_ismax == 1:
                z='Getting new maximum entry: x1'
            if x2_ismax == 1:
                z='Getting new maximum entry: x2'
            if x1x2_ismax == 1:
                z='Getting new maximum entry: x1 equals x2'
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            z= 'Getting new max/min length = Maximum length: %s, Minimum length: %s' %(max_len, min_len)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x==10:
            z='Setting posts = Post1: %s, Post2: %s' %(post1, post2)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
        if x==11:
            z = 'First case: %s%s%s' %(pre, post1, remi)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()
            z = 'First case: %s%s%s' %(pre, post1, remi)
            res_gendbr_entry3.delete(1.0, END)
            res_gendbr_entry3.insert(1.0, z)
            time.sleep(0.05)
            root.update()

    #Getting len and maxmin
    def get_maxmin():
        global x1_len
        global x2_len
        global max_len
        global min_len
        global x1_ismax
        global x2_ismax
        global x1x2_ismax

        x1_len=len(x1)
        x2_len=len(x2)
        max_len=0
        min_len=0
        x1_ismax=0
        x2_ismax=0
        x1x2_ismax=0

        if x1_len-x2_len > 0:
            x1_ismax=1
            max_len=int(x1_len)
            min_len=int(x2_len)
        if x2_len-x1_len > 0:
            x2_ismax=1
            max_len=int(x2_len)
            min_len=int(x1_len)
        if x1_len-x2_len == 0:
            x1x2_ismax=1
            max_len=int(x1_len)
            min_len=int(x2_len)
    get_maxmin()
    getvar_console(1)
    getvar_console(2)
    getvar_console(3)
    getvar_console(4)

    #Checking where the diff starts
    for i in range(min_len):
        if x1[i] != x2[i]:
            diff_start=i
            break
    if diff_start==None:
        diff_start=min_len
    getvar_console(5)

    #Setting prefix 
    pre=x1[:diff_start]
    getvar_console(6)

    #Updating values (Taking prefix out, minmax)
    x1=x1[diff_start:]
    x2=x2[diff_start:]
    get_maxmin()
    getvar_console(7)

    #Setting remi
    for i in reversed(range(0,max_len)):
        if x1=='':
            remi=''
            remi_pos1=0
            remi_pos2=max_len
            break
        if x2=='':
            remi=''
            remi_pos1=max_len
            remi_pos2=0
            break
        if x1_ismax == 1:
            if x1[i] != x2[min_len-1]:
                remi=x1[i+1:]
                remi_pos1=i+1
                remi_pos2=min_len
                break
        if x2_ismax == 1:
            if x1[min_len-1] != x2[i]:
                remi=x2[i+1:]
                remi_pos1=min_len
                remi_pos2=i+1
                break
        if x1x2_ismax == 1:
            if x1[i] != x2[i]:
                remi=x1[i+1:]
                remi_pos1=i+1
                remi_pos2=min_len
                break
        min_len=min_len-1
    getvar_console(8)

    #Setting Post (Just taking remi out) and post_len
    post1=x1[:remi_pos1]
    post2=x2[:remi_pos2]
    post1_len=len(post1)
    post1_len='{:02X}'.format(post1_len)
    post2_len=len(post2)
    post2_len='{:02X}'.format(post2_len)
    getvar_console(9)
    getvar_console(10)
    getvar_console(11)

    #Final
    generated='%s[VAR GENDBR(00FF,%s%s)]%s%s%s' % (pre, post2_len, post1_len, post1, post2, remi)
    res_gendbr_entry3.delete(1.0, END)
    res_gendbr_entry3.insert(1.0, generated)
    

    def gendbr_get_position(x):
        len_pre=0
        len_pre = len(pre); len_pre=float(len_pre); len_pre=len_pre/100
        len_post1 = len(post1); len_post1=float(len_post1); len_post1=len_post1/100
        len_post2 = len(post2); len_post2=float(len_post2); len_post2=len_post2/100
        len_remi = len(remi); len_remi=float(len_remi); len_remi=len_remi/100

        pre_start = 1.0
        pre_end = pre_start + len_pre
        post1_start = pre_end+0.23
        post1_end = post1_start+len_post1
        post2_start = post1_end
        post2_end = post2_start + len_post2
        remi_start = post2_end
        remi_end = remi_start + len_remi

        if x == 'pre_start':
            z=str(pre_start)        
            return z
        if x == 'pre_end':
            z=str(pre_end); z=z.replace('.0', '.')
            if pre_end == 1:
                z    = 1.0
            return z
        if x == 'post1_start':
            z=str(post1_start); z=z.replace('.0', '.')
            z=float(z) 
            return '%.2f' % z
        if x == 'post1_end':
            z=str(post1_end); z=z.replace('.0', '.')
            z=float(z)
            return '%.2f' % z
        if x == 'post2_start':
            return '%.2f' %post2_start
        if x == 'post2_end':
            return '%.2f' %post2_end
        if x == 'remi_start':
            return '%.2f' %remi_start
        if x == 'remi_end':
            return '%.2f' %remi_end

    def gendbr_tags():
        res_gendbr_entry3.tag_configure("gendbr_tag_pre", foreground='#FFFF00')
        res_gendbr_entry3.tag_add("gendbr_tag_pre", gendbr_get_position('pre_start'), gendbr_get_position('pre_end'))
        res_gendbr_entry3.tag_configure("gendbr_tag_post1", foreground='#00FFD4')
        res_gendbr_entry3.tag_add("gendbr_tag_post1", gendbr_get_position('post1_start'), gendbr_get_position('post1_end'))
        res_gendbr_entry3.tag_configure("gendbr_tag_post2", foreground='#FF00D4')
        res_gendbr_entry3.tag_add("gendbr_tag_post2", gendbr_get_position('post2_start'), gendbr_get_position('post2_end'))
        res_gendbr_entry3.tag_configure("gendbr_tag_remi", foreground='#FFFF00')
        res_gendbr_entry3.tag_add("gendbr_tag_remi", gendbr_get_position('remi_start'), gendbr_get_position('remi_end'))
    gendbr_tags()

res_gendbr_entry1 = Entry(root, bg='#292b3a', fg='#FFFFFF', relief=SOLID, borderwidth=2) #GENDBR
res_gendbr_entry2 = Entry(root, bg='#292b3a', fg='#FFFFFF', relief=SOLID, borderwidth=2)
res_gendbr_entry3 = Text(root, bg='#292b3a', fg='green', relief=SOLID, borderwidth=2)

res_gendbr_btn1 = Button(root, text='GENERATE', bg='#242424', fg='#FFFFFF', relief=SOLID, borderwidth=3)

image_female = Image.open("./icons/female.png")
image_male = Image.open("./icons/male.png")

female = ImageTk.PhotoImage(image_female)
male = ImageTk.PhotoImage(image_male)


res_gendbr_lab1 = Label(root, text='Insert texts here:', fg='#FFFFFF', bg='#242424')
res_gendbr_lab2 = Label(root, text='Generated text:', fg='#FFFFFF', bg='#242424')

res_gendbr_ico1 = Label(root, image=male, bg='#252525')
res_gendbr_ico2 = Label(root, image=female, bg='#252525')

res_gendbr_entry1.place(x=25, y=30, width=145)
res_gendbr_entry2.place(x=195, y=30, width=145)
res_gendbr_entry3.place(x=10, y=110, width=331, height=20)
res_gendbr_btn1.place(x=129, y=60, width=90, height=30)
res_gendbr_lab1.place(x=10, y=10)
res_gendbr_lab2.place(x=10, y=90)
res_gendbr_ico1.place(x=5, y=32)
res_gendbr_ico2.place(x=176, y=32)

res_gendbr_entry1.bind('<Return>', GENDBR)
res_gendbr_entry2.bind('<Return>', GENDBR)
res_gendbr_btn1.bind('<Button-1>', GENDBR)

img = tkinter.PhotoImage(file = r'./icons/icon.gif')
root.tk.call('wm', 'iconphoto', root._w, img)

root.mainloop()