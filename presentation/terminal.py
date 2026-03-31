
from __future__ import annotations
from typing import TYPE_CHECKING




if TYPE_CHECKING:
    from presentation.menu import Menu


class Terminal:
    def __init__(self):
        from presentation.menu import MainMenu
        self.current_menu = MainMenu(self)
        self.running = True
       


    def navigate(self, menu: Menu):
        
        self.current_menu = menu

    def quit(self):
        self.running = False
        print("Quitting...")

