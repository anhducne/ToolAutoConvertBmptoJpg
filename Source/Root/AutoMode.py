import os
import winreg as reg

from Root.Utility import GlobalVarible 
from Root.Utility import StringHelper
from tkinter import messagebox
from PIL import Image
from watchdog.events import FileSystemEventHandler

RootDir = os.getcwd()

#AutoStartUp_Config
keyRegname = "BeeTool"
exeNameConfig = "/DuxBee_tool.exe"

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(".bmp") and GlobalVarible.autoRun_1s:
            convert(event.src_path)
        if not event.is_directory and event.src_path.lower().endswith(".bmp") and GlobalVarible.autoRun_AL:
            convert(event.src_path)

def convert(file_path):
    try:
        if GlobalVarible.ratio_Now != GlobalVarible.ratio_Defaut:           
            # đây có 1 phần kiểu move ảnh thì oke, còn copy ảnh thì bị lỗi quyền, đã bắt ngoại lệ
            # if not os.path.splitext(file_path)[1]:  # Kiểm tra xem file có phần mở rộng hay không
            #     new_file_path = file_path + ".bmp"  # Thêm phần mở rộng vào tên file
            #     os.rename(file_path, new_file_path)  # Đổi tên file thành tên mới với phần mở rộng
            #     print(f"Đã thêm phần mở rộng 'bmp' cho file.")
            img = Image.open(file_path).resize((500, 500))
            cropped_image = img.crop((GlobalVarible.ratio_Now[0], GlobalVarible.ratio_Now[1], GlobalVarible.ratio_Now[2],GlobalVarible.ratio_Now[3]))
            width, height = map(int, GlobalVarible.resolution_Now.split('x'))
            new_image_size = (width, height)
            resized_img = cropped_image.resize(new_image_size)
            img = resized_img     
            change_file_name(img, file_path)    
        else:
            img = Image.open(file_path)
            width, height = map(int, GlobalVarible.resolution_Now.split('x'))
            new_image_size = (width, height)
            resized_img = img.resize(new_image_size)
            img = resized_img
            change_file_name(img, file_path)
    except Exception as e:
        print("(Error)-Auto-Convert")
        print(e)

def change_file_name(img, file_path):
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))
    file_ext = StringHelper.fileExt
    # Kiểm tra và thay đổi tên file nếu trùng
    new_file_path = os.path.join(GlobalVarible.targetPath_Now, file_name + file_ext)
    counter = 1
    while os.path.exists(new_file_path):
        new_file_path = os.path.join(GlobalVarible.targetPath_Now, f"{file_name} ({counter}){file_ext}")
        counter += 1 
    img.save(new_file_path, "JPEG")           

def toggle_auto_convert_1s():
    if GlobalVarible.autoRun_1s:
        messagebox.showinfo("Thông báo", "Tự động convert chạy trong 1 phiên đã được bật.")
    else:
        messagebox.showinfo("Thông báo", "Tự động convert chạy trong 1 phiên đã được tắt.")

def toggle_auto_convert_AL(RootDir):
    if GlobalVarible.autoRun_AL:
        make_auto_startup_AL(RootDir)
    else:
        make_auto_startup_AL(RootDir)

def make_auto_startup_AL(rootDir):
    optionSaveReg1(rootDir)
    optionSaveReg2(rootDir)    

def optionSaveReg1(rootDir):
    key = reg.HKEY_CURRENT_USER
    key_path = "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    key_name = keyRegname
    exe_path = os.path.abspath(rootDir+exeNameConfig)
    if GlobalVarible.autoRun_AL:
        try:
            #Đây là case mà khi mở lên key này không tồn tại ==> viết ngay 1 key mới
            key = reg.CreateKey(key, key_path)
            reg.SetValueEx(key, key_name, 0, reg.REG_SZ, exe_path)
            # Đóng khóa registry tránh tốn tài nguyên 
            reg.CloseKey(key)
        except FileNotFoundError:
            # Đây là case mà khi mở lên key đã tồn tại không viết đc key mới ==> xóa key cũ viết key mới
            with reg.OpenKey(key, key_path, 0, reg.KEY_ALL_ACCESS) as reg_key:
                reg.DeleteValue(reg_key, key_name)
            key = reg.CreateKey(key, key_path)
            reg.SetValueEx(key, key_name, 0, reg.REG_SZ, exe_path)
            reg.CloseKey(key)
            print("Lỗi OP1")
    else:
        try:
            with reg.OpenKey(key, key_path, 0, reg.KEY_ALL_ACCESS) as reg_key:
                reg.DeleteValue(reg_key, key_name)
            reg.CloseKey(key)
        except FileNotFoundError:
            print("Lỗi Reg OP1")

def optionSaveReg2(rootDir):
    key = reg.HKEY_CURRENT_USER
    key_path = r"SoftwareMicrosoftWindowsCurrentVersionRun"
    key_name = keyRegname
    exe_path = os.path.abspath(rootDir+exeNameConfig)
    if GlobalVarible.autoRun_AL:
        try:
            #Đây là case mà khi mở lên key này không tồn tại ==> viết ngay 1 key mới
            key = reg.CreateKey(key, key_path)
            reg.SetValueEx(key, key_name, 0, reg.REG_SZ, exe_path)
            messagebox.showinfo("Thông báo", "Tự động convert khi khởi động máy tính đã được bật.")
            # Đóng khóa registry tránh tốn tài nguyên 
            reg.CloseKey(key)
        except FileNotFoundError:
            # Đây là case mà khi mở lên key đã tồn tại không viết đc key mới ==> xóa key cũ viết key mới
            with reg.OpenKey(key, key_path, 0, reg.KEY_ALL_ACCESS) as reg_key:
                reg.DeleteValue(reg_key, key_name)
            key = reg.CreateKey(key, key_path)
            reg.SetValueEx(key, key_name, 0, reg.REG_SZ, exe_path)
            messagebox.showinfo("Thông báo", "Tự động convert khi khởi động máy tính đã được bật.")
            print("Lỗi OP2")
            reg.CloseKey(key)
    else:
        try:
            with reg.OpenKey(key, key_path, 0, reg.KEY_ALL_ACCESS) as reg_key:
                reg.DeleteValue(reg_key, key_name)
            reg.CloseKey(key)
            messagebox.showinfo("Thông báo", "Tự động convert khi khởi động máy tính đã được tắt.")
        except FileNotFoundError:
            print("Lỗi Reg OP2")
