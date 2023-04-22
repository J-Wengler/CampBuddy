from camper import Camper


class CampBuddy:
    def __init__(self, filepath):
        self.camper_file = filepath
        self.low = 65
        self.high = 300
        self.alert_string = "NOTHING"
        self.campers = []
        self.create_campers()

    def create_campers(self):
        path = self.camper_file
        with open(path, "r+") as in_file:
            header = in_file.readline()
            lines = in_file.readlines()
            for line in lines:
                sep_line = line.split(",")
                fname = sep_line[0]
                lname = sep_line[1]
                dusername = sep_line[2]
                dpassword = sep_line[3]
                str_bgvs = sep_line[4].split("/")
                bgvs = []
                for bg in str_bgvs:
                    bgvs.append(int(bg))
                new_camper = Camper(dusername, dpassword, self.low, self.high, fname, lname, bgvs)
                self.campers.append(new_camper)

        for camper in self.campers:
            print(camper)
