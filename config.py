import configparser
from ctypes import windll

def createConfig(path):

    user32 = windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    config = configparser.ConfigParser()
    config.add_section("Settings")

    config.set("Settings", "resolution_width", str(screensize[0]))
    config.set("Settings", "resolution_height", str(screensize[1]))

    with open(path, "w") as config_file:
        config.write(config_file)