class Answer:
    def __init__(self, picture: str = "", notice: str = ""):
        self.pictures: list = list() if not picture else [picture]
        self.notice: str = notice


if __name__ == "__main__":
    a = Answer()
    a.pictures.append("sfewgsdbv")
    print(a.pictures)
