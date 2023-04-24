from pydexcom import Dexcom
from status import Status

class Camper:
    def __init__(self, username, password, low, high, fname, lname, fake_bgvs):
        self.dexcom = None
        #self.create_assign_dexcom(username, password) #Skip until actual credentials are passed in
        self.low = low
        self.high = high
        self.fname = fname
        self.lname = lname
        self.fake_bgvs = fake_bgvs
        self.fw = .25
        self.sw = .25
        self.tw = .50

    def create_assign_dexcom(self, username, password):
        new_dexcom = Dexcom(username, password)
        self.dexcom = new_dexcom

    def check_status(self): #This function will need to be heavily edited to use real data instead of the real data
        #bgvs = self.dexcom.get_glucose_readings(minutes=20, max_count= 4)
        bgvs = self.fake_bgvs
        if bgvs == [-99, -99, -99, -99]:
            stat = Status(5, f"{self.fname} {self.lname} has no data for the last 20 minutes")
            self.status = stat
        elif -99 in bgvs:
            bgvs_list = []
            for num in bgvs:
                if num == -99:
                    bgvs_list.append("-")
                else:
                    bgvs_list.append(num)
            stat = Status(4, f"{self.fname} {self.lname} has incomplete data -> {bgvs_list}")
            self.status = stat
        else:
            stat = self.calc_slopes(bgvs)
            self.status = stat

    def calc_slopes(self, bgvs): #Again, Change this to set the data_1, data_2, etc. to use the .value function from the bg dexcom obj
        # data_1 = bgvs[3]#.value
        # data_2 = bgvs[2]#.value
        # data_3 = bgvs[1]#.value
        # data_4 = bgvs[0]#.value
        data_1 = bgvs[0]
        data_2 = bgvs[1]
        data_3 = bgvs[2]
        data_4 = bgvs[3]
        numerical_values = [data_1,data_2,data_3,data_4]

        first_slope = data_2 - data_1
        second_slope = data_3 - data_2 
        third_slope = data_4 - data_3
        # Calculate the weighted average of the three slopes
        average_slope = (first_slope * self.fw) + (second_slope * self.sw) + (third_slope * self.tw)
        last_bg = data_3
        cur_bg = data_4
        status = self.evaluate_threshold(cur_bg, last_bg, average_slope, numerical_values)
        return status

    def evaluate_threshold(self, cur_bg, last_bg, slope, bgvs):
        pred_bg = cur_bg + (slope * 3)
        if pred_bg <= self.low:
            message_str = f"{self.fname} {self.lname} -- bgvs: {bgvs} -- prediction: {pred_bg}"
            status = Status(2, message_str)
            return status
        elif pred_bg >= self.high:
            message_str = f"{self.fname} {self.lname} -- bgvs: {bgvs} -- prediction: {pred_bg}"
            status = Status(3, message_str)
            return status
        else:
            status = Status(1, f"{self.fname} {self.lname} is stable")
            return status
        
    def __str__(self):
        out_str = f"{self.fname} {self.lname} = {self.fake_bgvs}"
        return out_str
        
            

