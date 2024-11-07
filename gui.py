import tkinter as tk

class GUI(object):
    def __init__(self):
        self.controller = None

        self.window = tk.Tk()
        self.window.geometry('512x512')
        self.window.title('Tic Tac Toe')

        self.images = {
            'X' : tk.PhotoImage(file='./images/x.png'),
            'O' : tk.PhotoImage(file='./images/o.png')
        }

        self.frame_fields = tk.Frame(master=self.window,
                                     background= '#4b4453')
        self.frame_fields.place(x=20, y=20, height=180, width=180)

        self.list_fields = []
        for i in range(9):
            button = tk.Button(master= self.frame_fields,
                               background='#005bd3',
                               activebackground= '#00aec4',
                               command= lambda index=i : self.button_field_click(index))
            self.list_fields.append(button)
            button.place(x=i%3*60+5, y=i//3*60+5, height=50, width=50)

        self.label_current_player = tk.Label(master=self.window,
                                             text='X',
                                             background='#c11a94')
        self.label_current_player.place(x=220, y=20, width=60, height=40)

        self.button_engine_toggle = tk.Button(master=self.window,
                                              background='green',
                                              command=self.button_engine_toggle_click)
        self.button_engine_toggle.place(x=220, y=70, width=60, height=40)

    def show_move(self, index, player):
        self.list_fields[index].config(image=self.images.get(player))
        self.label_current_player.config(text=player,
                                         background= '#c11a94' if player == 'X' else '#ffbe4e')

    def button_field_click(self, index):
        self.controller.field_click(index)

    def button_engine_toggle_click(self):
        self.controller.button_engine_status_toggle()

    def set_controller(self, ref_controller):
        self.controller = ref_controller

    def start(self):
        self.window.mainloop()

