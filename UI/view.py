import flet as ft

class View(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        # Page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # Controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # Graphical elements
        self._title = None
        self._ddyear = None
        self._ddcolor = None
        self.btn_graph = None
        self.txtOut = None
        self.txt_container = None
        self._ddnode = None
        self.btn_search = None
        self.txtOut2 = None

    def load_interface(self):
        # Title
        self._title = ft.Text("TdP 2024 - Lab11: Prova tema d'esame", color="blue", size=24)
        self._page.controls.append(self._title)
        # Row with some controls
        # Text field for the name
        self._ddyear = ft.Dropdown(label="Anno")
        self._controller.fillDDAnno()
        self._ddcolor = ft.Dropdown(label="Colore")
        self._controller.fillDDColor()
        # Button for the "creat graph" reply
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self._ddyear,self._ddcolor, self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        # List view where the reply is printed
        self.txtOut = ft.ListView(expand=1, spacing=10, padding=10, auto_scroll=True)
        self._page.controls.append(self.txtOut)
        self._ddnode = ft.Dropdown(label="Product")
        self.btn_search = ft.ElevatedButton(text="Cerca Percorso", on_click=self._controller.handle_search)
        row2 = ft.Row([self._ddnode, self.btn_search],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self.txtOut2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txtOut2)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()