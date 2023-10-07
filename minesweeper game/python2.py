from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False,False)

top_frame=Frame(root,bg='black',width=settings.WIDTH,height=utils.h_p(25))
top_frame.place(x=0,y=0)
game_title=Label(top_frame,
                 bg='black',
                 fg='white',
                 text='Minesweeper Game',
                 font=('',48)
                 )

game_title.place(
    x=utils.w_p(25),
    y=0
)
left_frame=Frame(root,bg='black',width=utils.w_p(25),height=utils.h_p(75))
left_frame.place(x=0,y=180)
center_frame=Frame(root,bg='black',width=utils.w_p(75),height=utils.h_p(75))
center_frame.place(x=utils.w_p(25),y=utils.h_p(25))
for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c=Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x,row=y)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,y=0
)
Cell.randomize_mines()


root.mainloop()