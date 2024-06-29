from PIL import Image, ImageTk
import pystray
from pystray import MenuItem as item


class IconNotiSetting:
    # Constructor Python 
    def __init__(self, iconPath):
        self.icon_Path = iconPath
        self.icon = Image.open(self.icon_Path)
        self.menu = (item('Mở cửa sổ', self.on_back),)
        self.noti = pystray.Icon("DuxBee_Tool", self.icon, "Duxbee_bmpConvert", self.menu)
        self.isActive = False

    def setup_IconTrayNoti(self):
        self.noti.run()
        self.isActive = True

    def on_back(self):
        try:
            # self.noti.stop()
            # icon.stop(icon)
            # self.root.deiconify()
            # # cập nhật lại giao diện UI - fix trắng màn
            # self.root.update()
            # # cập nhật lại giao diện UI - fix lỗi luồng- lag
            # self.root.mainloop()
            # self.noti.stop()
            self.noti.stop()
            self.isActive = False
        except Exception as e:
            print(e)

    def isActive(self):
        return self.isActive