# This is string help, u can find any thing path or string in here !!!! yeah create by bee
from enum import Enum
class JsonUpdateType(Enum):
    stock = 1
    target = 2
    resolutionNowChange = 3
    resolutionDelete =4,
    resolutionAdd = 5,
    ratioChange = 6,
    runAutoAl = 7,
    anotherExt = 8

#AutoStartUp_Config


# UI/UX
defautAvaImage = "\Root\Image\Ava.jpg"
defautAvaImage4Exe = "\_internal\Image\Ava.jpg"
defautIconfile = "\Root\Image\ico.ico"
defautIconfile4Exe = "\_internal\Image\ico.ico"
# json Data Defaut Value
stockPath = "\Folder_Import"
target_PATH = "\Folder_Export"
resolution_Now = '200x200'
resolution =  ['200x200','960x640', '1024x1024', '2048x2048']
ratio_Now = ['0','0','0','0']
ratio_Defaut = ['0','0','0','0']
ratio_Temp = ['0','0','0','0']
autoRun1s = False
autoRunAlways = False
another_ext = False

#Tool Status
availableJson = "(Init)-Load xong: Data.json"
notavailableJson = "(Init)-Không có: Data.json"
createJson = "(Init)-Đã tạo mới: Data.json"
changeFstockDone = "(HoànThành)-Đã thay đổi folder gốc"
changeFstockError = "(Error)-Không thay đổi được folder gốc"
changeFtargetDone = "(HoànThành)-Đã thay đổi folder đích"
changeFtargetError = "(Error)-Không thay đổi được folder đích"
notChooseFolder = "(Cảnhbáo)-Chưa chọn folder !"
deleteSizeDone = "(HoànThành)-Xóa size thành công"
deleteSizeError = "(Error)-Xóa size thành công"
changeSizeDone = "(HoànThành)-Đã thay đổi size mặc định:"
changeSizeLoop = "(Cảnhbáo)-Size mặc định đã là:"
writeSizeDone ="(HoànThành)-Đã thêm size "
writeSizeLoop ="(Cảnhbáo)-Size này đã có sẵn trong data "
writeSizeNotDone = "(Cảnhbáo)-Nhập lại(sốxsố - không có dấu cách)"
writeSizeError = "(Error)-Không thêm được size mới"
saveImgTemp = "(HoànThành)-Lưu Path bmp vào temp"

#Convert Status
loadbmpDone ="(HoànThành)-Load ảnh Bmp thành công"
loadbmpNotDone = "(Cảnhbáo)-Chưa chọn ảnh"
loadbmpNotbmp = "(Cảnhbáo)-Ảnh đã chọn không phải file.bmp"
loadbmpError = "(Error)-Loadbmp"
convertDone ="(HoànThành)-Convert Bmp sang Jpg thành công"
convertNotDone ="(Cảnhbáo)-Chọn ảnh trước khi Convert"
convertError = "(Error)-Convert"
#Crop
cropDone = "(HoànThành)-Crop ảnh thành công"
cropNotDonee = "(Cảnhbáo)-Chọn ảnh trước khi Crop"
cropNotDone = "(Cảnhbáo)-Vui lòng chọn vùng cần crop"
cropError = "(Error)-Crop"
cropExportDone = "(HoànThành)-Xuất ảnh crop thành công"
cropExportNotDone = "(Cảnhbáo)-Nhập ảnh hoặc chọn vùng crop trước khi xuất"
cropExportNotDonee = "(Cảnhbáo)-Phát hiện lỗi không mong muốn"
cropExportError = "(Error)-ExportCrop"
#Ratio
ratioChangeDone = "(HoànThành)-Thay đổi ratio thành công"
ratioChangeNotDone = "(Cảnhbáo)-Đã là ratio hiện tại"
ratioChangeNotDonee = "(Cảnhbáo)-Phát hiện lỗi không mong muốn"
ratioChangeError = "(Error)-RatioChange"
#AutoRun

AutoRun1sOn = "Chạy ngầm chỉ phiên này: Bật"
AutoRun1sOff = "Chạy ngầm chỉ phiên này: Tắt"

AutoR1sStatus = "(HoànThành)-AutoRun1s: "
AutoR1sStatus_waring = "(Cảnhbáo)-AutoRun1s: Lỗi không mong muốn "
AutoR1sStatus_waring2 = "(Cảnhbáo)-AutoRun1s: Tắt luôn chạy cùng hệ thống"
AutoRun1sError = "(Error)-AutoRun1s"

AutoRunAlwaysOn = "Tự động chạy ngầm khi khởi động máy - Trạng thái: Bật"
AutoRunAlwaysOff = "Tự động chạy ngầm khi khởi động máy - Trạng thái: Tắt"

AutoRALStatus = "(HoànThành)-AutoRunAlways: "
AutoRALStatus_waring = "(Cảnhbáo)-AutoRunAlways: Lỗi không mong muốn "
AutoRALStatus_waring2 = "(Cảnhbáo)-AutoRunAlways: Tắt chỉ chạy 1 phiên"
AutoRunAlwaysError = "(Error)-AutoRunAlways"




#FileName
fileNameConvert = "Duxbei_Convert"
fileNameCrop = "Duxbei_Crop"
fileExt =".jpg"
#AnotherFile
anotherfileDone = "(HoànThành)- another ext: "

#MessengerBox



#Contact
devContact= "DuxBee - Alo me !"


