import os
import re
import Root.Utility.StringHelper as str_static
from Root.Utility import GlobalVarible 
from Root.Utility.StringHelper import JsonUpdateType as jsType
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import Root.DataManager as data
import Root.ConvertController as convert
from Root.ConvertController import ImageCropper
from watchdog.observers import Observer
import Root.AutoMode as auto


# Đây là các hàm quản lý chạy ở UI/UX
def notiToolStatus(label_toolStatus, value1, value2):
    GlobalVarible.ToolStatus = value1
    label_toolStatus.config(text=f"TOOL_STATUS: {GlobalVarible.ToolStatus} {value2}")

def notiToolStatus2(label_toolStatus, value1):
    GlobalVarible.ToolStatus = value1
    label_toolStatus.config(text=f"TOOL_STATUS: {GlobalVarible.ToolStatus}")

def notiToolStatus3(label_toolStatus):
    label_toolStatus.config(text=f"TOOL_STATUS: {GlobalVarible.ToolStatus}")

def resultToolStatus(label_result,value):
    GlobalVarible.ImageStatus = value
    label_result.config(text=f"RESULT: {GlobalVarible.ImageStatus}")    

def resultToolStatus2(label_result):
    label_result.config(text=f"RESULT: {GlobalVarible.ImageStatus}")  

def resultToolStatus3(label_result ,value, value2):
    GlobalVarible.ImageStatus = value
    label_result.config(text=f"RESULT: {GlobalVarible.ImageStatus}, {value2}")    

def autoRunStatus(label_result, value):
    label_result.config(text=f"{value}")  

def chooseImage(image_Path, image_Show, label_result, label_toolStatus):
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            if file_path.lower().endswith('.bmp'):
                image_Path.delete("1.0", tk.END)
                image_Path.insert(tk.END, file_path)
                GlobalVarible.baseImg_Name = file_path
                img = Image.open(file_path)
                img = img.resize((200, 200))  # Resize the image as 
                photo = ImageTk.PhotoImage(img)
                image_Show.config(image=photo)
                image_Show.image = photo
                convert.pushImgToTemp(file_path)
                notiToolStatus2(label_toolStatus,str_static.saveImgTemp)
                resultToolStatus(label_result, str_static.loadbmpDone)
            else:
                resultToolStatus(label_result, str_static.loadbmpNotbmp)
        else:
            resultToolStatus(label_result, str_static.loadbmpNotDone)
    except Exception as e:
        print(e) 
        resultToolStatus(label_result, str_static.loadbmpError)

def imgConvertButton(label_result, label_toolStatus):
    try:
        convert.convertImage()
        resultToolStatus3(label_result ,str_static.convertDone, GlobalVarible.resolution_Now)
    except Exception as e:
        print(e)   
        notiToolStatus2(label_toolStatus, str_static.convertError)
        resultToolStatus(label_result, str_static.convertNotDone)

def changeStockFolder(stockFolder_Path, label_toolStatus):
    try:
        f_path = filedialog.askdirectory()
        if f_path:
            stockFolder_Path.delete("1.0", tk.END)
            stockFolder_Path.insert(tk.END, f_path)
            data.update_json(jsType.stock, f_path)  
            notiToolStatus2(label_toolStatus,str_static.changeFstockDone)
            # print(f"partStockNow: {GlobalVarible.stockPath_Now}")
            reset_WatchdogTarget()
        else:
            notiToolStatus2(label_toolStatus,str_static.notChooseFolder)
    except Exception as e:
        print(e)   
        notiToolStatus2(label_toolStatus,str_static.changeFstockError)

def changeTargetFolder(targetFolder_Path, label_toolStatus):
    try:
        f_path = filedialog.askdirectory()
        if f_path:
            targetFolder_Path.delete("1.0", tk.END)
            targetFolder_Path.insert(tk.END, f_path)
            data.update_json(jsType.target, f_path)
            notiToolStatus2(label_toolStatus,str_static.changeFtargetDone)  
            # print(f"partTargetkNow: {GlobalVarible.targetPath_Now}")
        else:
            notiToolStatus2(label_toolStatus,str_static.notChooseFolder)  
    except Exception as e:  
        print(e) 
        notiToolStatus2(label_toolStatus,str_static.changeFtargetError)  

def changeTargetImageSize(selected_size, label_toolStatus):
    selectedSizeTemp = selected_size.get()
    if selectedSizeTemp != GlobalVarible.resolution_Now :
        data.update_json(jsType.resolutionNowChange, selectedSizeTemp)
        selected_size.set(GlobalVarible.resolution_Now)
        notiToolStatus(label_toolStatus, str_static.changeSizeDone, GlobalVarible.resolution_Now)  
    else:
        notiToolStatus(label_toolStatus, str_static.changeSizeLoop, GlobalVarible.resolution_Now)  

def deleteTargetImageSize(selected_size, size_dropdown, label_toolStatus):
    selectedSizeTemp = selected_size.get()
    if selectedSizeTemp != GlobalVarible.resolution_Now :
        data.update_json(jsType.resolutionDelete, selectedSizeTemp)
        selected_size.set(GlobalVarible.resolution_Now)
        size_dropdown['values'] = GlobalVarible.resolution_All
    else:
        # trùng
        data.update_json(jsType.resolutionDelete, selectedSizeTemp)
        GlobalVarible.resolution_Now = GlobalVarible.resolution_All[0]
        data.update_json(jsType.resolutionNowChange, GlobalVarible.resolution_Now)
        selected_size.set(GlobalVarible.resolution_Now)
        size_dropdown['values'] = GlobalVarible.resolution_All  
    notiToolStatus3(label_toolStatus)  

def check_format_imageSize(input_str):
    pattern = r'^\d+x\d+$'  # Biểu thức chính quy để kiểm tra định dạng 'số x số'
    if re.match(pattern, input_str):
        return True
    else:
        return False

def addTargetImageSize(write_addSize, label_toolStatus, size_dropdown):
    try:
        inputData = write_addSize.get()
        if check_format_imageSize(inputData):
            data.update_json(jsType.resolutionAdd, inputData)
            notiToolStatus3(label_toolStatus)
            size_dropdown['values'] = GlobalVarible.resolution_All  
        else:
            notiToolStatus2(label_toolStatus, str_static.writeSizeNotDone)
    except Exception as e:  
        print(e)
        notiToolStatus2(label_toolStatus,str_static.writeSizeError)   

def openPopupCrop(root,label_result,var_Global, showImgTemp_button, label_Ratio):
    try: 
        new_window = tk.Toplevel(root)  # Tạo một cửa sổ con mới
        new_window.title("Crop Windows")
        # gọi hàm, truyền vào đối để tượng tạo canvas hiện tại là một cái root cửa sổ con
        # đồng thời truyền vào đường dẫn ảnh cần crop 
        ImageCropper(new_window, GlobalVarible.pathImageBmpNow, label_result,var_Global,showImgTemp_button, label_Ratio)
        # lắng nghe kết quả
    except Exception as e: 
        print(e)
        resultToolStatus(label_result, str_static.cropNotDonee)

def showCropImage(image_ShowResult):
    resized_image = GlobalVarible.imageCropTemp.resize((200, 200))
    photo = ImageTk.PhotoImage(resized_image)
    image_ShowResult.config(image=photo)
    image_ShowResult.image = photo

def exportCropImage(label_result,label_toolStatus):
    try:
        if GlobalVarible.imageCropTemp != None:
            convert.exportImage()
            notiToolStatus2(label_toolStatus, str_static.cropExportDone)
            resultToolStatus3(label_result, str_static.cropExportDone,"Size:"+str(GlobalVarible.resolution_Now)+" Ratio:"+str(GlobalVarible.ratio_temp))
        else:
            print(GlobalVarible.imageCropTemp)
            resultToolStatus(label_result, str_static.cropExportNotDone)
    except Exception as e:
        print(e)
        notiToolStatus2(label_toolStatus, str_static.cropExportError)
        resultToolStatus(label_result, str_static.cropExportNotDonee)

def setRatioCropAuto(label_result, label_toolStatus, label_Ratio):
    try:
        if GlobalVarible.ratio_Now != GlobalVarible.ratio_temp:
            GlobalVarible.ratio_Now = GlobalVarible.ratio_temp
            data.update_json(jsType.ratioChange, GlobalVarible.ratio_Now)
            init_Ratio(label_Ratio)
            resultToolStatus3(label_result ,str_static.ratioChangeDone, GlobalVarible.ratio_Now)
        else:
            resultToolStatus(label_result ,str_static.ratioChangeNotDone)
    except Exception as e: 
        print(e)
        resultToolStatus(label_result ,str_static.ratioChangeNotDonee)
        notiToolStatus2(label_toolStatus, str_static.ratioChangeError)

def resetRatioCropAuto(label_result, label_toolStatus, label_Ratio):
    try:
        if GlobalVarible.ratio_Now != GlobalVarible.ratio_Defaut:
            GlobalVarible.ratio_Now = GlobalVarible.ratio_Defaut
            data.update_json(jsType.ratioChange, GlobalVarible.ratio_Now)
            init_Ratio(label_Ratio)
            resultToolStatus3(label_result ,str_static.ratioChangeDone, GlobalVarible.ratio_Now)
        else:
            resultToolStatus(label_result ,str_static.ratioChangeNotDone)
    except Exception as e: 
        print(e)
        resultToolStatus(label_result ,str_static.ratioChangeNotDonee)
        notiToolStatus2(label_toolStatus, str_static.ratioChangeError)

#AutoRun
def setRunBGAuto1Season(bgRun1Season_button, label_toolStatus):
    try:     
        if GlobalVarible.autoRun_AL:
            notiToolStatus2(label_toolStatus, str_static.AutoR1sStatus_waring2)
        else:
            if GlobalVarible.autoRun_1s:
                GlobalVarible.autoRun_1s = False
                auto.toggle_auto_convert_1s()
                autoRunStatus(bgRun1Season_button, str_static.AutoRun1sOff)
            else:
                GlobalVarible.autoRun_1s = True
                auto.toggle_auto_convert_1s()
                autoRunStatus(bgRun1Season_button,str_static.AutoRun1sOn)
            notiToolStatus(label_toolStatus, str_static.AutoR1sStatus, GlobalVarible.autoRun_1s)      
    except Exception as e:
        print(e)
        notiToolStatus2(label_toolStatus, str_static.AutoRun1sError)

def setRunBGAutoAlwaysStart( bgRunAlwaysSeason_button, label_toolStatus, RootDir):
    try:
        if GlobalVarible.autoRun_1s:
            notiToolStatus2(label_toolStatus, str_static.AutoRALStatus_waring2)
        else:
            if GlobalVarible.autoRun_AL:
                GlobalVarible.autoRun_AL = False
                auto.toggle_auto_convert_AL(RootDir)
                autoRunStatus(bgRunAlwaysSeason_button, str_static.AutoRunAlwaysOff)
                data.update_json(jsType.runAutoAl, GlobalVarible.autoRun_AL)
            else:
                GlobalVarible.autoRun_AL = True
                auto.toggle_auto_convert_AL(RootDir)
                autoRunStatus(bgRunAlwaysSeason_button, str_static.AutoRunAlwaysOn)
                data.update_json(jsType.runAutoAl, GlobalVarible.autoRun_AL)
            notiToolStatus(label_toolStatus, str_static.AutoRALStatus, GlobalVarible.autoRun_AL)
    except Exception as e:
        print(e)
        notiToolStatus2(label_toolStatus, str_static.AutoRunAlwaysError)

def reset_WatchdogTarget():
    try:
        event_handler = auto.FileHandler()
        observer = Observer()
        observer.unschedule_all()
        observer.schedule(event_handler, GlobalVarible.stockPath_Now, recursive=False)
        observer.start()
    except Exception as e:
        print(e)
        print(GlobalVarible.stockPath_Now)



#AnotherExt - chưa hoàn thiện
def another_Ext(label_toolStatus):
    data.update_json(jsType.anotherExt, GlobalVarible.another_ext)
    notiToolStatus(label_toolStatus, str_static.anotherfileDone, GlobalVarible.another_ext)

# Init UI/UX 

def init_StockFolder(f_path, stockFolder_Path, label_toolStatus):
    try:
        stockFolder_Path.delete("1.0", tk.END)
        stockFolder_Path.insert(tk.END, f_path)
    except Exception as e:   
        print(e)
        notiToolStatus2(label_toolStatus,str_static.changeFstockNotDone)  

def init_TargetFolder(f_path,targetFolder_Path, label_toolStatus):
    try:
        targetFolder_Path.delete("1.0", tk.END)
        targetFolder_Path.insert(tk.END, f_path)
    except Exception as e:  
        print(e)
        notiToolStatus2(label_toolStatus,str_static.changeFtargetNotDone)   

def init_ResolutionSize(selected_size, size_dropdown):
    selected_size.set(GlobalVarible.resolution_Now)
    # cleaned_string = var_Global.resolution_All.replace("'", "").replace(",", "").replace("]", "").replace("[", "") // cái ni là cho chuỗi string
    size_dropdown['values'] = GlobalVarible.resolution_All

def check_Available_Image(file_path):
  return os.path.exists(file_path)

def init_Image(file_path, image_Path, image_Show, image_ShowResult):
    try:
        temp1 = file_path + str_static.defautAvaImage
        temp2 = file_path + str_static.defautAvaImage4Exe
        if check_Available_Image(temp1):
            image_Path.delete("1.0", tk.END)
            image_Path.insert(tk.END, temp1)
    # Hiển thị ảnh cần convert 
            img = Image.open(temp1)
            img = img.resize((200, 200))  # Resize the image as 
            photo = ImageTk.PhotoImage(img)
            image_Show.config(image=photo)
            image_Show.image = photo
            image_ShowResult.config(image=photo)
            image_ShowResult.image = photo
        else:
            image_Path.delete("1.0", tk.END)
            image_Path.insert(tk.END, temp2)
            img = Image.open(temp2)
            img = img.resize((200, 200))  # Resize the image as 
            photo = ImageTk.PhotoImage(img)
            image_Show.config(image=photo)
            image_Show.image = photo
            image_ShowResult.config(image=photo)
            image_ShowResult.image = photo
    except Exception as e:
        print(e)
        image_Path.insert(tk.END, "Bấm chọn ảnh để hiện ảnh và đường dẫn")

def init_Ratio(label_Ratio):
    clearStringRnow = str(GlobalVarible.ratio_Now).replace("'", "")
    clearStringRTemp = str(GlobalVarible.ratio_temp).replace("'", "")
    label_Ratio.config(text=f"RatioDefautNow: {clearStringRnow} - RatioWillChange: {clearStringRTemp}")  

def init_Auto1s( bgRun1Season_button):
    if GlobalVarible.autoRun_1s:
        autoRunStatus(bgRun1Season_button,str_static.AutoRun1sOn)
    else:
        autoRunStatus(bgRun1Season_button, str_static.AutoRun1sOff)

def init_AutoAL( bgRunAlwaysSeason_button):
    if GlobalVarible.autoRun_AL:
        autoRunStatus(bgRunAlwaysSeason_button, str_static.AutoRunAlwaysOn)
    else:
        autoRunStatus(bgRunAlwaysSeason_button, str_static.AutoRunAlwaysOff)

def init_WatchDog():
    try:
        event_handler = auto.FileHandler()
        observer = Observer()
        observer.schedule(event_handler, GlobalVarible.stockPath_Now, recursive=False)
        observer.start()
    except Exception as e:
        print(e)
        print(GlobalVarible.stockPath_Now)

# Init tổng - Chạy Tất cả vào timeLine

def Init_Main():
    GlobalVarible.imageCropTemp = None
    data.Init_Data()
    init_WatchDog()
