# #TODO:
# # 1. Make a list of campers from a given file containing dexcom usernames and passwords
# # 2. Every 5 minutes run through all the campers and check their status
# #     1 = stable BG
# #     2 = low predicted
# #     3 = high predicted
# #     4 = between 1 - 3 datapoints over last 20 minutes (not continous so can't run algorithm)
# #     5 = no data for the last 20 minutes

from campbuddy import CampBuddy


cb = CampBuddy("/Users/jameswengler/test_users.csv")
cb.day_report()

# #### FIXME 
# from PyQt5.QtWidgets import QMainWindow, QApplication
# import sys


# class MainWidget(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Drag and Drop")
#         self.resize(720, 480)
#         self.setAcceptDrops(True)

#     def dragEnterEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.accept()
#         else:
#             event.ignore()

#     def dropEvent(self, event):
#         files = [u.toLocalFile() for u in event.mimeData().urls()]
#         for f in files:
#             print(f)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = MainWidget()
#     ui.show()
#     app.exec()