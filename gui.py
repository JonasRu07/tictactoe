import tkinter as tk
from tkinter import PhotoImage


class GUI(object):
    def __init__(self):
        self.controller = None

        self.window = tk.Tk()
        self.window.geometry('330x220')
        self.window.title('Tic Tac Toe')
        self.window.config(background='#e8d5b5')
        self.images = {
            'field' : None,
            'board_frame' : tk.PhotoImage(file='./images/board_frame.png'),
            'X' : PhotoImage(file='./images/x.png'),
            'O' : PhotoImage(file='./images/o.png'),
            'player_vs_player' : PhotoImage(file='./images/player_vs_player.png'),
            'player_vs_engine' : PhotoImage(file='./images/player_vs_engine.png'),
            'engine_vs_engine' : PhotoImage(file='./images/engine_vs_engine.png')
            }

        self.frame_fields = tk.Frame(master=self.window,
                                     background= '#FF00FF',)
        self.frame_fields.place(x=20, y=20, height=180, width=180)
        self.frame_fields_image = tk.Label(self.frame_fields, image= self.images.get('board_frame'))
        self.frame_fields_image.pack()

        self.list_fields = []
        for i in range(9):
            button = tk.Button(master= self.frame_fields,
                               background='#7c7484',
                               activebackground= '#4c8076',
                               relief= 'groove',
                               command= lambda index=i : self.button_field_click(index))
            self.list_fields.append(button)
            button.place(x=i%3*60+5, y=i//3*60+5, height=50, width=50)

        self.label_current_player = tk.Label(master=self.window,
                                             text='X',
                                             background='#5C2CAa',
                                             font= 'Aral, 30')
        self.label_current_player.place(x=220, y=20, width=90, height=40)

        self.button_engine_toggle = tk.Button(master=self.window,
                                              background='green',
                                              command=self.button_engine_toggle_click,
                                              image=self.images.get('player_vs_player'))
        self.button_engine_toggle.place(x=220, y=70, width=90, height=40)

        self.label_game_end = tk.Label(master=self.window,
                                     background='lightblue')
        self.label_game_end.place(x=220, y=120, width=90, height=40)

    def update_game_mode_button(self, state):
        self.button_engine_toggle.config(image=self.images.get(state))

    def update_game_end_label(self, winner: str | None):
        if winner:
            self.label_game_end.config(text=winner)
        else:
            self.label_game_end.config(text='DRAW')

    def show_move(self, index, player):
        self.list_fields[index].config(image=self.images.get(player))
        next_player = ('X', '#5C2CAa')  if player == 'O' else ('O', '#A00000')
        self.label_current_player.config(text=next_player[0],
                                         background=next_player[1])

    def button_field_click(self, index):
        self.controller.field_click(index)

    def button_engine_toggle_click(self):
        self.controller.button_engine_status_toggle()

    def set_controller(self, ref_controller):
        self.controller = ref_controller

    def start(self):
        self.window.mainloop()
