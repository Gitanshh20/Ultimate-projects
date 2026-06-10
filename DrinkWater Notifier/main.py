from plyer import notification
import time 

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "Daily water requirements vary based on climate, activity level, and body size. The Mayo Clinic recommends an average daily total fluid intake of about 15.5 cups (3.7 liters) for men and 11.5 cups (2.7 liters) for women.",
            app_icon = "E:\Gitansh_Codes\Project\DrinkWater\icon.ico",
            timeout = 10
        )
        time.sleep(18000)