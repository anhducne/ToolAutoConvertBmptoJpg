import os
from Root.Utility import GlobalVarible 
import Root.Utility.StringHelper as str_static
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def pushImgToTemp(path):
    GlobalVarible.pathImageBmpNow = path

def convertImage():
    try:
        if GlobalVarible.ratio_Now != GlobalVarible.ratio_Defaut: # nếu mà khác tọa độ gốc thì cắt, ko thì convert bth
            img = Image.open(GlobalVarible.pathImageBmpNow).resize((500, 500))
            cropped_image = img.crop((GlobalVarible.ratio_Now[0], GlobalVarible.ratio_Now[1], GlobalVarible.ratio_Now[2],GlobalVarible.ratio_Now[3]))
            width, height = map(int, GlobalVarible.resolution_Now.split('x'))
            new_image_size = (width, height)
            resized_img = cropped_image.resize(new_image_size)
        else:   
            img = Image.open(GlobalVarible.pathImageBmpNow)
            width, height = map(int, GlobalVarible.resolution_Now.split('x'))
            new_image_size = (width, height)
            resized_img = img.resize(new_image_size)
        #Lưu
        makeCountName(resized_img, GlobalVarible.baseImg_Name, str_static.fileExt)
        os.startfile(GlobalVarible.targetPath_Now)
    except Exception as e:
        print(e)
        
    #Thêm Convert vào tên file, vẫn giữ tên cũ của file 
    # jpg_image_name = os.path.basename(GlobalVarible.pathImageBmpNow).replace('.bmp', '_convert.jpg')
    # #Chuyển ảnh convert sang folder
    # jpg_image_path = os.path.join(GlobalVarible.targetPath_Now, jpg_image_name)
        # Tách chuỗi lấy w vs h
        # if nếu mà ratio default mà != ratio now ==> resize ảnh về 500x500 xong cắt theo ratio, xong bắt đầu resize lại do 

def exportImage():
    try:
        width, height = map(int, GlobalVarible.resolution_Now.split('x'))
        new_image_size = (width, height)
        resized_image = GlobalVarible.imageCropTemp.resize(new_image_size)
        photo = resized_image
        makeCountName(photo, GlobalVarible.baseImg_Name, str_static.fileExt)
        os.startfile(GlobalVarible.targetPath_Now)
    except Exception as e:
        print(e)

def makeCountName(img ,fileName, fileExt):
    new_name_change = os.path.basename(fileName).replace('.bmp', '.jpg')
    counter = 1
    new_file_path = os.path.join(GlobalVarible.targetPath_Now,new_name_change)
    while os.path.exists(new_file_path):
        new_file_path = os.path.join(GlobalVarible.targetPath_Now, f"{new_name_change} ({counter}){fileExt}")
        counter += 1
    img.save(new_file_path, "JPEG")

class ImageCropper:
    # Constructor Python 
    def __init__(self, root, image_path, label_result,var_Global, showImgTemp_button, label_Ratio):
        self.root = root
        self.label_Result = label_result
        self.var_Global = var_Global
        self.showimg = showImgTemp_button
        self.labelRRatio = label_Ratio
        self.image = Image.open(image_path).resize((500, 500))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas = tk.Canvas(root, width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.canvas.pack()

        self.drag_start_x = None
        self.drag_start_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_drag_start)
        self.canvas.bind("<B1-Motion>", self.on_dragging)
        self.canvas.bind("<ButtonRelease-1>", self.on_drag_end)

        # Tạo nút submit ảnh đã được crop 
        self.crop_button = ttk.Button(root, text="Crop", command=self.crop_image)
        self.crop_button.pack()

    def on_drag_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def on_dragging(self, event):
        self.canvas.delete("crop_rect")
        self.canvas.create_rectangle(self.drag_start_x, self.drag_start_y, event.x, event.y, outline="red", tags="crop_rect")

    def on_drag_end(self, event):
        pass

    def crop_image(self):
        try:
            bbox = self.canvas.bbox("crop_rect")
            if bbox:
                GlobalVarible.ImageStatus = str_static.cropDone
                cropped_image = self.image.crop((bbox[0], bbox[1], bbox[2], bbox[3]))
                # print(f"bbox:{bbox[0]}, bbox:{bbox[1]}, bbox:{bbox[2]}, bbox:{bbox[3]}")
                for i in range(4):
                    GlobalVarible.ratio_temp[i] = bbox[i]
                # print(list(GlobalVarible.ratio_temp))
                # cropped_image.show()
                self.var_Global.imageCropTemp = cropped_image
                self.label_ResultCrop = ttk.Label(self.root, text=f"Result:{str_static.cropDone}", foreground="red", font=("Arial",10,"bold") )
                self.label_ResultCrop.pack()
                self.showimg.invoke()
                self.root.after(500, self.close_window)
            else:
                GlobalVarible.ImageStatus = str_static.cropNotDone
                self.label_ResultCrop = ttk.Label(self.root, text=f"Result:{str_static.cropNotDone}", foreground="red", font=("Arial",10,"bold"))
                self.label_ResultCrop.pack()
                self.root.after(1000, self.close_window)
        except Exception as e:
                print(e) 
                GlobalVarible.ImageStatus = str_static.cropError

    def close_window(self):
        self.noti_Window()
        self.root.destroy()  # Đóng cửa sổ sau khi thông báo

    def noti_Window(self):
        clearStringRnow = str(self.var_Global.ratio_Now).replace("'", "")
        clearStringRTemp = str(self.var_Global.ratio_temp).replace("'", "")
        self.labelRRatio.config(text=f"RatioDefautNow: {clearStringRnow} - RatioWillChange: {clearStringRTemp}")   
        self.label_Result.config(text=f"RESULT: {self.var_Global.ImageStatus}-Ratio:{clearStringRTemp}") 

    
    