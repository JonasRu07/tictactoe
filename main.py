from controller import Controller
from board import Board
from gui import GUI
from engine import Engine


board = Board()
controller = Controller()
engine = Engine()
gui = GUI()

controller.set_board(board)
controller.set_gui(gui)
controller.set_engine(engine)
engine.set_board(board)
engine.set_controller(controller)
gui.set_controller(controller)

controller.start_gui()