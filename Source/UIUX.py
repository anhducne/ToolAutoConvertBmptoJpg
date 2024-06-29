import os
import sys
import Root.Utility.StringHelper as str_static
import Root.Utility.GlobalVarible as var_Global
import tkinter as tk
from tkinter import ttk
import Root.ToolController as mainIndex
import atexit
from Root.IconNoti import IconNotiSetting
# Hàm của các phím chức năng
RootDir = os.getcwd()
var_Global.RootDirIndex = RootDir

def chooseImage():
    mainIndex.chooseImage(image_Path, image_Show, label_result, label_toolStatus)

def changeStockFolder():
    mainIndex.changeStockFolder(stockFolder_Path, label_toolStatus)

def openStockFolder():
    os.startfile(var_Global.stockPath_Now)

def openTargetFolder():
    os.startfile(var_Global.targetPath_Now)

def changeTargetFolder():
    mainIndex.changeTargetFolder(targetFolder_Path, label_toolStatus)

def changeTargetImageSize():
    mainIndex.changeTargetImageSize(selected_size, label_toolStatus)

def deleteTargetImageSize():
    mainIndex.deleteTargetImageSize(selected_size, size_dropdown, label_toolStatus)

def addTargetImageSize():
    mainIndex.addTargetImageSize(write_addSize, label_toolStatus, size_dropdown)

def imgConvertButton():
    mainIndex.imgConvertButton(label_result, label_toolStatus)

def openPopupCrop():
    mainIndex.openPopupCrop(root,label_result,var_Global, showImgTemp_button, label_Ratio)

def showCropImage():
    mainIndex.showCropImage(image_ShowResult)

def exportCropImage():
    mainIndex.exportCropImage(label_result,label_toolStatus)

def setRatioCropAuto():
    mainIndex.setRatioCropAuto(label_result, label_toolStatus, label_Ratio)

def resetRatioCropAuto():
    mainIndex.resetRatioCropAuto( label_result, label_toolStatus, label_Ratio)

def setRunBGAuto1Season():
    mainIndex.setRunBGAuto1Season( bgRun1Season_button, label_toolStatus)

def setRunBGAutoAlwaysStart():
    mainIndex.setRunBGAutoAlwaysStart(bgRunAlwaysSeason_button, label_toolStatus, RootDir)
 
def hiddenToNoti():
    # root.withdraw()
    # setup_trayIcon()
    label_toolStatus.config(text="TÍNH NĂNG ĐANG PHÁT TRIỂN ^^")

# hàm init icon
def returnInstance():
    icondir1 = RootDir + str_static.defautIconfile
    icondir2 = RootDir + str_static.defautIconfile4Exe
    if os.path.exists(icondir1):
        #Tạo một instance thì mới gọi được hàm ra
        iconNotiInstance=IconNotiSetting(icondir1)
    else:
        iconNotiInstance=IconNotiSetting(icondir2)
    return iconNotiInstance

def setup_trayIcon():
    iconNotiInstance = returnInstance()
    iconNotiInstance.setup_IconTrayNoti()

def on_close():
        try: 
            sys.exit() 
        except Exception as e:
            print(e)

# UI/UX Zone
root = tk.Tk()
root.title("Tool bmp to jpg")
root.geometry("1090x700") # size cửa sổ mặc đinh
root.resizable(True,True) # cho người dùng resize cửa sổ ko 
root.protocol("WM_DELETE_WINDOW", on_close)
# Tạo và định vị các widget
label_tittle = ttk.Label(root, text="TOOL COVER BMP TO JPG MAKE BY BEE - Ver 0.1" ,foreground="violet", font=("Arial",17,"bold"))
label_tittle.grid(column=1, row=0, sticky=tk.EW, padx=0, pady=5)
#1
label_tittle_2 = ttk.Label(root, text="ZONE#1: CẤU HÌNH", foreground="green", font=("bold"))
label_tittle_2.grid(column=0, row=1, sticky=tk.EW, padx=0, pady=5)
label_toolStatus = ttk.Label(root, text="TOOL_STATUS:", foreground="red", font=("bold"))
label_toolStatus.grid(column=1, row=1, sticky=tk.EW, padx=0, pady=5)
#2
# label_toolStatus = ttk.Label(root, text="TOOL_STATUS:", foreground="red", font=("bold"))
# label_toolStatus.grid(column=1, row=2, sticky=tk.EW, padx=0, pady=5)
#3 - stock folder 
label_stockFolder = ttk.Label(root, text="Thư mục gốc (StockFolder): ")
label_stockFolder.grid(column=0, row=3, sticky=tk.EW, padx=0, pady=5)
stockFolder_Path = tk.Text(root, height=1, width=30)
stockFolder_Path.grid(column=1, row=3, sticky=tk.EW, padx=0, pady=5)
submit_stockFolder = ttk.Button(root, text="Đổi thư mục gốc", command=changeStockFolder)
submit_stockFolder.grid(column=2, row=3, sticky=tk.EW, padx=10, pady=5)
opend_stockFolder = ttk.Button(root, text="Mở Thư mục gốc", command=openStockFolder)
opend_stockFolder.grid(column=3, row=3, sticky=tk.EW, padx=0, pady=5)
#4 - targetFolder 
label_targetFolder = ttk.Label(root, text="Thư mục đích (TargetFolder):")
label_targetFolder.grid(column=0, row=4, sticky=tk.EW, padx=0, pady=5)
targetFolder_Path = tk.Text(root, height=1, width=30)
targetFolder_Path.grid(column=1, row=4, sticky=tk.EW, padx=0, pady=5)
submit_targetFolder = ttk.Button(root, text="Đổi thư mục đích", command=changeTargetFolder)
submit_targetFolder.grid(column=2, row=4, sticky=tk.EW, padx=10, pady=5)
opend_targetFolder = ttk.Button(root, text="Mở Thư mục đích", command=openTargetFolder)
opend_targetFolder.grid(column=3, row=4, sticky=tk.EW, padx=0, pady=5)
#5 - Dropdown list hiển thị các size ảnh từ file JSON
label_dropdown = ttk.Label(root, text="Size ảnh đầu ra: ")
label_dropdown.grid(column=0, row=5, sticky=tk.EW, padx=0, pady=5)
selected_size = tk.StringVar()
size_dropdown = ttk.Combobox(root, textvariable=selected_size)
size_dropdown.grid(column=1, row=5, sticky=tk.EW, padx=0, pady=5)
Choose_ImageSize = ttk.Button(root, text="Chọn", command=changeTargetImageSize)
Choose_ImageSize.grid(column=2, row=5, sticky=tk.EW,padx=10, pady=5)
Del_ImageSize = ttk.Button(root, text="Xóa", command=deleteTargetImageSize)
Del_ImageSize.grid(column=3, row=5, sticky=tk.EW ,padx =0, pady=5)
#6 - box thêm size từ file JSON
label_addSize = ttk.Label(root, text="Thêm size mới (VD:200x200): ")
label_addSize.grid(column=0, row=6, sticky=tk.EW, padx=0, pady=5)
write_addSize = tk.Entry(root)
write_addSize.grid(column=1, row=6, sticky=tk.EW, padx=0, pady=5)
Add_ImageSize = ttk.Button(root, text="Thêm size", command=addTargetImageSize)
Add_ImageSize.grid(column=2, row=6, sticky=tk.EW, padx=10, pady=5)
#7 - Chooseimage Zone
label_ConvertImgNow = ttk.Label(root, text="ZONE#2: THỦ CÔNG", foreground="Blue", font=("bold"))
label_ConvertImgNow.grid(column=0, row=7, sticky=tk.EW, padx=0, pady=5)
#8
image_Show =  ttk.Label(root)
image_Show.grid(column=0, row=8, sticky=tk.EW, padx=0, pady=5)
label_result = ttk.Label(root, text="RESULT: ",  foreground="red", font=("Arial",10,"bold"))
label_result.grid(column=1, row=8, sticky=tk.EW, padx=0, pady=5)
image_ShowResult =  ttk.Label(root)
image_ShowResult.grid(column=2, row=8, sticky=tk.EW, padx=0, pady=5)
#9 - Submit button Zone
button_ChooseImage = ttk.Button(root, text="Chọn ảnh", command=chooseImage)
button_ChooseImage.grid(column=0, row=9, sticky=tk.EW, padx=0, pady=5)
image_Path =  tk.Text(root, height=1, width=30)
image_Path.grid(column=1, row=9, sticky=tk.EW, padx=0, pady=5)
#10
label_option1 = ttk.Label(root, text=f"Chỉ chỉnh size và đổi sang \nfile JPG thì bấm Convert")
label_option1.grid(column=0, row=10, sticky=tk.EW, padx=0, pady=5)
submit_button = ttk.Button(root, text="Convert", command=imgConvertButton)
submit_button.grid(column=1, row=10, sticky=tk.EW, padx=0, pady=5)
showImgTemp_button = ttk.Button(root, text="NonClick", command=showCropImage)
#11
label_option2 = ttk.Label(root, text=f"B1: Crop ảnh thì bấm Crop\nB2: Crop xong xuất thì bấm Export")
label_option2.grid(column=0, row=11, sticky=tk.EW, padx=0, pady=5)
openCrop_button = ttk.Button(root, text="Crop", command=openPopupCrop)
openCrop_button.grid(column=1, row=11, sticky=tk.EW, padx=0, pady=5)
exportCrop_button = ttk.Button(root, text="Export", command=exportCropImage)
exportCrop_button.grid(column=2, row=11, sticky=tk.EW, padx=0, pady=5)
#12
label_tittle_2 = ttk.Label(root, text="ZONE#3:CONFIG AUTO", foreground="brown", font=("bold"))
label_tittle_2.grid(column=0, row=12, sticky=tk.EW, padx=0, pady=5)
#13
label_option2 = ttk.Label(root, text=f"Tự động crop với vùng mặc định")
label_option2.grid(column=0, row=13, sticky=tk.EW, padx=0, pady=5)
label_Ratio = ttk.Label(root, text="RatioDefautNow:", font=("bold"))
label_Ratio.grid(column=1, row=13, sticky=tk.EW, padx=0, pady=5)
setRatio_button = ttk.Button(root, text="Thay đổi", command=setRatioCropAuto)
setRatio_button.grid(column=2, row=13, sticky=tk.EW, padx=0, pady=5)
setRatio_button = ttk.Button(root, text="Đặt lại", command=resetRatioCropAuto)
setRatio_button.grid(column=3, row=13, sticky=tk.EW, padx=0, pady=5)
#14
label_Auto = ttk.Label(root, text="Chế độ chạy nền")
label_Auto.grid(column=0, row=14, sticky=tk.EW, padx=0, pady=5)
bgRunAlwaysSeason_button = ttk.Button(root, text="Tự động chạy ngầm khi khởi động máy - Trạng thái: Đang tắt", command=setRunBGAutoAlwaysStart)
bgRunAlwaysSeason_button.grid(column=1, row=14, sticky=tk.EW, padx=0, pady=5)
bgRun1Season_button = ttk.Button(root, text="Chạy ngầm chỉ phiên này", command=setRunBGAuto1Season)
bgRun1Season_button.grid(column=2, row=14, sticky=tk.EW, padx=0, pady=5)
hiddent_button = ttk.Button(root, text="Ẩn cửa sổ", command=hiddenToNoti)
hiddent_button.grid(column=3, row=14, sticky=tk.EW, padx=0, pady=5)
# EndUI

def update_StatusUI():
    label_toolStatus.config(text=f"TOOL_STATUS: {str(var_Global.ToolStatus)}")

def init_trayicon():
    if var_Global.autoRun_AL:   
        setup_trayIcon()

def Init_UI():
    mainIndex.init_Image(RootDir, image_Path, image_Show, image_ShowResult)
    mainIndex.init_StockFolder(var_Global.stockPath_Now ,stockFolder_Path, label_toolStatus)
    mainIndex.init_TargetFolder(var_Global.targetPath_Now, targetFolder_Path, label_toolStatus)
    mainIndex.init_ResolutionSize(selected_size, size_dropdown)
    mainIndex.init_Ratio(label_Ratio)
    mainIndex.init_Auto1s(bgRun1Season_button)
    mainIndex.init_AutoAL(bgRunAlwaysSeason_button)
    init_trayicon()

def Init_Main():
    mainIndex.Init_Main()
    Init_UI()

if __name__ == "__main__":
  Init_Main()

# Vòng lặp chính của Tkinterx
root.after(1000, update_StatusUI)
root.mainloop()

#Khi nào mà build ra mà popup lỗi để sửa lỗi thì để dòng phía dưới
# os.system("pause") 