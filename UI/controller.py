import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceTeam=None

    def handleCreaGrafo(self, e):
        if self._view._ddAnno.value is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(
                ft.Text("Selezionare prima un anno!", color="red")
            )
            self._view.update_page()
            return

        self._model.creaGrafo(self._view._ddAnno.value)
        n,m= self._model.getGraphDetails()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato! "
                    f"Il grafo è costituito di {n} nodi e {m} archi")
        )
        self._view.update_page()


    def handleDettagli(self, e):
        if self._choiceTeam is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Selezionare prima un team dal menu!", color="red"))
            self._view.update_page()
            return
        viciniTuple=self._model.getVicini(self._choiceTeam)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text(f"Il nodo {self._choiceTeam} ha {len(viciniTuple)} vicini", color="green")
        )

        self._view._txt_result.controls.append(
            ft.Text("Lista ordinata di vicini:", color="green")
        )

        for v in viciniTuple:
            self._view._txt_result.controls.append(
                ft.Text(f"{v[0]} - peso {v[1]}", color="green")
            )

        self._view.update_page()

    def handlePercorso(self, e):
        pass

    def fillDDYears(self, dd: ft.Dropdown()):
        years= self._model.getAllYears()
        for year in years:
            dd.options.append(ft.dropdown.Option(text=year))

    def handleYearSelected(self, e):
        if self._view._ddAnno.value is None:
            self._view._txtOutSquadre.controls.clear()
            self._view._txtOutSquadre.controls.append(ft.Text("Selezionare un anno dal menu!", color="red"))

        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Per il {self._view._ddAnno.value} sono iscritte {len(teams)} squadre.", color="green"))

        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(t))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data=t, text=t.name, on_click=self.readDDTeams))




        self._view.update_page()

    def readDDTeams(self, e):
        if e.control.data is None:
            self._choiceTeam=None
        else:
            self._choiceTeam = e.control.data
        print(f"Selezionato il Team {self._choiceTeam}")

