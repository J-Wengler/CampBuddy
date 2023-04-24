#TODO:
# 1. Make a list of campers from a given file containing dexcom usernames and passwords
# 2. Every 5 minutes run through all the campers and check their status
#     1 = stable BG
#     2 = low predicted
#     3 = high predicted
#     4 = between 1 - 3 datapoints over last 20 minutes (not continous so can't run algorithm)
#     5 = no data for the last 20 minutes

from campbuddy import CampBuddy


cb = CampBuddy("/Users/jameswengler/test_users.csv")
cb.day_report()