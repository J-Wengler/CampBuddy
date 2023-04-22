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

    def create_assign_dexcom(self, username, password):
        new_dexcom = Dexcom(username, password)
        self.dexcom = new_dexcom

    def check_status(self):
        bgvs = self.dexcom.get_glucose_readings(minutes=20, max_count= 4)
        if bgvs == None:
            status = Status(5, "missing data from last 20 mins")
            return status
        elif len(bgvs) < 4:
            numerical_bgvs = []
            for bg in bgvs:
                if bg == None:
                    numerical_bgvs.append("NA")
                else:
                    numerical_bgvs.append(str(bg.value))
            message = str(numerical_bgvs)
            status = Status(4, message)
            return status
        elif self.check_bgvs(bgvs):
            status = self.calc_slopes(bgvs)
            return status

    def calc_slopes(self, bgvs):
        data_1 = bgvs[3].value
        data_2 = bgvs[2].value
        data_3 = bgvs[1].value
        data_4 = bgvs[0].value
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
            message_str = f"15 Min Prediction: {pred_bg} Last 4 bgvs = {bgvs}"
            status = Status(2, message_str)
            return status
        elif pred_bg >= self.high:
            message_str = f"15 Min Prediction: {pred_bg} Last 4 bgvs = {bgvs}"
            status = Status(3, message_str)
            return status
        else:
            status = Status(1, "Stable")
            return status
        
    def __str__(self):
        out_str = f"{self.fname} {self.lname} = {self.fake_bgvs}"
        return out_str
        
            

