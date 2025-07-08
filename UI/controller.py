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
        anno = self._view._ddyear.value
        if anno is None:
            self._view.create_alert("Selezionare un anno!")
            self._view.update_page()
            return
        colore = self._view._ddcolor.value
        if colore is None:
            self._view.create_alert("Selezionare un colore!")
            self._view.update_page()
            return
        self._model.buildGraph(colore, anno)
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text(f"Il grafo è stato creato correttamente."))
        self._view.txtOut.controls.append(ft.Text(f"Il grafo creato contiene {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi."))
        self._view.txtOut.controls.append(ft.Text(f"Di seguito gli archi con peso maggiore: "))
        archi = self._model.getArchiPesoMaggiore()
        for arco in archi:
            self._view.txtOut.controls.append(ft.Text(f"{arco[0]} e {arco[1]}, peso: {arco[2]["weight"]}"))
        nodi = self._model.getProdottiPiùPresenti()
        if nodi != []:
            self._view.txtOut.controls.append(ft.Text(f"Di seguito i prodotti presenti in più di un arco: "))
            for nodo in nodi:
                self._view.txtOut.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()

    def fillDDProduct(self):
        pass

    def handle_search(self, e):
        pass
