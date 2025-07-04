import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDDAnno(self):
        for i in range(2015, 2019):
            self._view._ddyear.options.append(ft.dropdown.Option(str(i)))

    def fillDDColor(self):
        colori = self._model._colours
        for colore in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(colore))

    def handle_graph(self, e):
        pass



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
