from Parish import Parish

class World:

    parish_names_trasdeza = ["Ansemil","Breixa","Chapa","Margaride","Martixe","Negreiros","Ponte","Silleda"]
    parishes = []

    def __init__(self):

        for parish_name in self.parish_names_trasdeza:
            self.parishes.append(Parish(parish_name))
