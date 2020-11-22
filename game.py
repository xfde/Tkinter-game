import tkinter
from tkinter import *

import time
import os

#CREATE WINDOW
window = Tk()
paused = False
start = False
canvas = None
pause_Lable = None
pause_Text = None
pause_Quit_Lable = None
pause_Quit_Text = None

#player variables
health = 4

def configure_window():
    window.geometry("1280x720")
    window.configure(background="#21182c")
    window.title("Lightning in a botle")


#CONFIGURE WINDOW
configure_window()

def key(event):
    global paused
    if not paused:
        if event.char == 'd':
            canvas.move(character_sprite,10,0)
        elif event.char == 'a':
            canvas.move(character_sprite,-10,0)
        elif event.char == 'w':
            canvas.move(character_sprite,0,-10)
        elif event.char == 's':
            canvas.move(character_sprite,0,10)

def isIn():
#    [0][0]
#        [64][64]
    canvas.coords(character_sprite)

def pause_game(event):
    global paused
    if paused:
        print("unpaused")
        paused = False
        canvas.itemconfig(pause_Lable,state= HIDDEN)
        canvas.itemconfig(pause_Text,state= HIDDEN)
        canvas.itemconfig(pause_Quit_Lable,state= HIDDEN)
        canvas.itemconfig(pause_Quit_Text,state= HIDDEN)
    else:
        print("paused")
        paused = True
        canvas.itemconfig(pause_Lable,state= NORMAL)
        canvas.itemconfig(pause_Text,state= NORMAL)
        canvas.itemconfig(pause_Quit_Lable,state= NORMAL)
        canvas.itemconfig(pause_Quit_Text,state= NORMAL)

def callback(event):
    canvas.focus_set()
    print("clicked at", event.x, event.y)

def quit_game():
    window.destroy()
def quit_game_fromin(event):
    window.destroy()
def new_game():
    global start
    start = True

def leaderboards(event):
    leaderboard = True

def update(ind):
    if not paused:
        frame = goblinframes[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        canvas.itemconfig(goblin_sprite, image=frame)
        window.after(100, update, ind)

lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
total_rows = len(lst)
total_columns = len(lst[0])
def leaderboards():
    unpack_menu()
    canvasldb = Canvas(width=1280, height=720, bg= '#120338')
    canvasldb.pack()
    title = canvasldb.create_text((640,50),text="Lederboards",fill="white")
    for i in range(total_rows):
        for j in range(total_columns):
            qe = Entry(window, width=20, fg='white',bg='#9254de', font=('Arial', 16, 'bold'))
            qe.grid(row=i, column=j)
            qe.insert(END, lst[i][j])

def unpack_menu():
    bg_label.pack_forget()
    newgButton.pack_forget()
    loadButton.pack_forget()
    leaderboardButton.pack_forget()
    quitButton.pack_forget()

def new_game():
    global pause_Lable
    global pause_Text
    global pause_Quit_Lable
    global pause_Quit_Text
    global canvas
    global goblin_sprite
    canvas = Canvas(width=1280, height=720, bg= '#21182c')
    canvas.pack()
    unpack_menu()
    canvas.bind("<Key>", key)
    canvas.bind("<Escape>", pause_game)
    canvas.bind("<Button-1>", callback)
    goblin_sprite = canvas.create_image(100,100)
    character_sprite = canvas.create_image(width_sprite/2,height_sprite/2,image=frames)
    potion_sprite = canvas.create_image(500,500,image=potion_sprite_asset)
    tooltip = canvas.create_text((640,280),text="press E to interact",fill="white",state= HIDDEN)
    score = canvas.create_text((30,15),text="Score: 0",fill="white")
    health_bar = []
    x = 70
    y = 20
    for i in range(health):
        health_bar.append(canvas.create_image(x,y, image=hearth_sprite))
        x = x + 25
    #put pause lable on top of the stack
    pause_Lable = canvas.create_rectangle(540, 260, 740, 440, fill="#dfe9d7",state= HIDDEN)
    pause_Text = canvas.create_text((640,280),text="Game paused",state= HIDDEN)
    pause_Quit_Lable = canvas.create_rectangle(550, 400, 730, 420, fill="#21182c",state= HIDDEN)
    pause_Quit_Text = canvas.create_text((640,410),text="Quit",fill="white",state= HIDDEN)
    canvas.tag_bind(pause_Quit_Lable, "<Button-1>", quit_game_fromin)
    canvas.tag_bind(pause_Quit_Text, "<Button-1>", quit_game_fromin)
    window.after(0, update, 0)

#sprites import
frames = PhotoImage(file='./assets/idle.gif')
hearth_sprite = PhotoImage(file='./assets/hearth.gif')
frames = frames.zoom(2)
potion_sprite_asset = PhotoImage(file='./assets/health_potion.gif')
potion_sprite_asset = potion_sprite_asset.zoom(2)
width_sprite = frames.width()
height_sprite = frames.height()
frameCnt = 6
goblinframes = [PhotoImage(file='./assets/goblin.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
goblin_sprite = None
#initialise canvas
bg_image_menu = PhotoImage("./assets/menu.gif")
bg_label = Label(window,image= bg_image_menu)
bg_label.pack()
newgButton = Button(bg_label, font= ('Arial', 15), foreground='#21182c', background="white", text="New Game", command=new_game)
newgButton.pack(pady = 20, padx = 15)
loadButton = Button(bg_label, font= ('Arial', 15),state= DISABLED, foreground='#21182c', background="white", text="Load Game", command=callback)
loadButton.pack(pady = 15, padx = 15)
leaderboardButton = Button(bg_label, font= ('Arial', 15), foreground='#21182c', background="white", text="Leaderboard", command=leaderboards)
leaderboardButton.pack(pady = 15, padx = 15)
quitButton = Button(bg_label, font= ('Arial', 15), foreground='#21182c', background="white", text="Quit", command=quit_game)
quitButton.pack(pady = 15, padx = 15)
window.mainloop()
