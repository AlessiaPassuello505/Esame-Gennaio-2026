import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceAnnoF=None
        self._choiceAnnoI=None

    def fillDDYears(self):
        anni = self._model.getYears()
        anniDDI = list(map(lambda x: ft.dropdown.Option(x, on_click=self._choiceAnnoI), anni))
        anniDDF = list(map(lambda x: ft.dropdown.Option(x, on_click=self._choiceAnnoF), anni))
        self._view._ddAnno1.options = anniDDI
        self._view._ddAnno2.options = anniDDF
        self._view.update_page()

    def _choiceAnnoI(self, e):
        self._annoI = e.control.data

    def _choiceAnnoF(self, e):
        self._annoF = e.control.data


    def handleCreaGrafo(self,e):
        annoI = self._view._ddAnno1.value
        annoF = self._view._ddAnno2.value

        if annoI is None or annoF is None:
            self._view.txt_result.controls.append(
                ft.Text("Attenzione, selezionare un range di votazioni"))
            self._view.update_page()
            return
        self._model.creaGrafo(annoI, annoF)
        n, m = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato! ", color="red"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {n}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {m}"))

        self._view.update_page()

    def handleDettagli(self, e):
        pass

    def handleCerca(self, e):
        pass

