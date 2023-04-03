class Date:
    def __init__(self, date_str:str) -> None:
        self.day = int(date_str[0] + date_str[1])
        self.month = int(date_str[2:4])
        self.year = int(date_str[4:9])
    def __str__(self) -> str:
        return str(self.day) + "." + str(self.month) + "." + str(self.year)


