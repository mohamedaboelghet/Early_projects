class CollegeClass:
    def __init__(self, names: str, ids: int, _Year: int):
        self.names = names
        self.ids = ids
        self._Year = _Year

    def main_interface(self):

        if self._Year == 1:
            return f"Hi {self.names}! \nyour id is: {self.ids}\nYour Classess are\nAhmed Elashry's Infromation system\nMai Kassab's History of engineering\nOsama's elhelw's HTML"


        elif self._Year == 2:
            return f"Hi {self.names}! \nyour id is: {self.ids}\nYour Classess are\nAhmed Elashry's Infromation system 2\nNwal Sadawi's Algebra\nOsama's elhelw's Css"

        elif self._Year == 3:
            return f"Hi {self.names}! \nyour id is: {self.ids}\nYour Classess are\nAhmed Elashry's Infromation system3\nMai Kassab's OOP\nOsama's elhelw's Javascript"


        elif self._Year == 4:
            return f"Hi {self.names}! \nyour id is: {self.ids}\nYour Classess are\nAhmed Elashry's Computing\nMai Kassab's Statistics\nOsama's elhelw's Java2"

        return "just a personal advise, study, so you do not fail!"


# Small database:

Student1 = CollegeClass("mohamed Abouelght", 123443656, 1)
print(Student1.main_interface())
