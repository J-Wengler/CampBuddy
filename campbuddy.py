from camper import Camper


class CampBuddy:
    def __init__(self, filepath):
        self.camper_file = filepath
        self.low = 65
        self.high = 300
        self.alert_string = "NOTHING"
        self.campers = []
        self.num_campers = 0
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
                self.num_campers += 1
                self.campers.append(new_camper)

    def day_report(self):
        lows = []
        highs = []
        missing_some = []
        missing_all = []
        stable = []
        for camper in self.campers:
            camper.check_status()
        for camper in self.campers:
            if camper.status.get_status() == 1:
                stable.append(camper)
            elif camper.status.get_status() == 2:
                lows.append(camper)
            elif camper.status.get_status() == 3:
                highs.append(camper)
            elif camper.status.get_status() == 4:
                missing_some.append(camper)
            elif camper.status.get_status() == 5:
                missing_all.append(camper)

        report = self.generate_report(lows, highs, missing_some, missing_all, stable)
        print(report)
    
    def generate_report(self, lows, highs, missing_some, missing_all, stable):
        str_report = f"Report generated for {self.num_campers} campers. {len(stable)} are stable.\n\n"

        low_str = f"LOWS ({len(lows)} campers)\n"
        for camper in lows:
            low_str += f"{camper.status}\n"
        str_report += low_str

        high_str = f"\nHIGHS ({len(highs)} campers)\n"
        for camper in highs:
            high_str += f"{camper.status}\n"
        str_report += high_str

        some_str = f"\nMissing SOME data ({len(missing_some)} campers)\n"
        for camper in missing_some:
            some_str += f"{camper.status}\n"
        str_report += some_str

        all_str = f"\nMissing ALL data ({len(missing_all)} campers)\n"
        for camper in missing_all:
            all_str += f"{camper.status}\n"
        str_report += all_str


        return str_report
        
    



