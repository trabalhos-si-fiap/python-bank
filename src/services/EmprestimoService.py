from src.Menu import Menu


class Emprestimo:
    def __init__(self, menu: Menu):
        self.menu = menu

    def run(self):
        self.menu.emprestimo()
