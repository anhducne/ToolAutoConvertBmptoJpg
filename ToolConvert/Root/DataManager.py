import os
import json
from Root.Utility import GlobalFunction
from Root.Utility import StringHelper
from Root.Utility import GlobalVarible 
from Root.Utility.StringHelper import JsonUpdateType as jsType
from datetime import datetime
RootDir = os.getcwd()
JsonPath = RootDir + "\Root\Data\Data.json"
dataPath = RootDir + '\Root\Data'

dataParentPath = RootDir + '\Root'
new_folder_name = "Data"

stock_target_Path = RootDir

new_Stockfolder_name = "Folder_Import"
new_Targetfolder_name = "Folder_Export"

# Json Time CRUD by Bee

# Hàm check có tồn tại jsonFile không 
def check_json_file(file_path):
  return os.path.exists(file_path)

# Nếu không tồn tại Json/ Tạo Json Default
def create_json(JsonPathPara):
    now = datetime.now()
    current_time = now.isoformat()
    data = {
    "tittle": "Json Create by beeJsonDefault",
    "time_Create": current_time,
    "stock_PATH": RootDir + StringHelper.stockPath,
    "target_PATH": RootDir + StringHelper.target_PATH,
    "resolution_now" : StringHelper.resolution_Now,
    "resolution_all": StringHelper.resolution,
    "ratio_now" : StringHelper.ratio_Now,
    "ratio_defaut": StringHelper.ratio_Defaut,
    "ratio_temp": StringHelper.ratio_Temp,
    "autoRun_1S" : StringHelper.autoRun1s,
    "autoRun_Always" : StringHelper.autoRunAlways,
    "another_ext" : StringHelper.another_ext
    }
    # Ghi dữ liệu vào file JSON
    GlobalFunction.tool_status(StringHelper.createJson)
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    with open(JsonPathPara, 'w', encoding='utf-8') as f:
       f.write(json_data)

# Nếu có Json thì đọc dữ liệu có sẵn và lưu vào biến global 
def read_json(JsonPath):
    with open(JsonPath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Tittle
    GlobalVarible.title_Now = data.get("tittle")
    # Trích xuất thời gian hiện tại từ dữ liệu
    timestamp = data.get("time_Create")
    # Chuyển đổi chuỗi thời gian sang đối tượng datetime
    time_obj = datetime.fromisoformat(timestamp)
    # Gán giá trị// thời điểm chạy ban đầu
    GlobalVarible.timeCreate_Now = str(time_obj)
    GlobalVarible.stockPath_Now = data.get("stock_PATH")
    GlobalVarible.targetPath_Now = data.get("target_PATH")
    GlobalVarible.resolution_Now = str(data.get("resolution_now"))
    GlobalVarible.resolution_All = data.get("resolution_all")
    GlobalVarible.ratio_Now = data.get("ratio_now")
    GlobalVarible.ratio_Defaut = data.get("ratio_defaut")
    GlobalVarible.ratio_temp = data.get("ratio_temp")
    GlobalVarible.autoRun_1s = data.get("autoRun_1S")
    GlobalVarible.autoRun_AL = data.get("autoRun_Always")
    GlobalVarible.another_ext = data.get("another_ext")

def update_json(type, value):
    with open(JsonPath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if type == jsType.stock:
        GlobalVarible.stockPath_Now = value
        new_stockPath = value
        data["stock_PATH"] = new_stockPath
    elif type == jsType.target:
        GlobalVarible.targetPath_Now = value
        new_targetPath = value
        data["target_PATH"] = new_targetPath 
    elif type == jsType.resolutionNowChange:
        GlobalVarible.resolution_Now = value
        new_resolution_now = value
        data["resolution_now"] = new_resolution_now
    elif type == jsType.resolutionAdd:
        if value in GlobalVarible.resolution_All:
            # trùng
            GlobalFunction.tool_status(StringHelper.writeSizeLoop)
        else:
            data['resolution_all'].append(value)
            GlobalVarible.resolution_All = data.get("resolution_all")
            GlobalFunction.tool_status(StringHelper.writeSizeDone)
    elif type == jsType.resolutionDelete:
        if value in data['resolution_all']:
            data['resolution_all'].remove(value)
            GlobalVarible.resolution_All = data.get("resolution_all")
            GlobalFunction.tool_status(StringHelper.deleteSizeDone)
        else:
            print("Xóa size thất bại")
            GlobalFunction.tool_status(StringHelper.deleteSizeError)
    elif type == jsType.ratioChange:
        try:
            del data["ratio_now"]
            data['ratio_now'] = value
            GlobalFunction.tool_status(StringHelper.ratioChangeDone)
        except Exception as e:
            print(e)
            GlobalFunction.tool_status(StringHelper.ratioChangeError)
    elif type == jsType.runAutoAl:
        del data["autoRun_Always"]
        data['autoRun_Always'] = value
    elif type == jsType.anotherExt:
        data['another_ext'] = value

    with open(JsonPath, 'w') as file:
        json.dump(data, file, indent=4)


def checkData_Json(JsonPathPara):
    if check_json_file(JsonPathPara):
        GlobalFunction.tool_status(StringHelper.availableJson)
        read_json(JsonPathPara)
    else:
        GlobalFunction.tool_status(StringHelper.notavailableJson)
        create_json(JsonPathPara)
        read_json(JsonPathPara)   

# Hàm check Data chạy vào đầu khi khởi động chương trình 
def checkData_Folder(JsonPathPara):
    try:
        if  os.path.exists(dataPath):
            checkData_Json(JsonPathPara)
        else:
            new_folder_path = os.path.join(dataParentPath, new_folder_name)
            os.makedirs(new_folder_path)
            checkData_Json(JsonPathPara)
    except Exception as e:
            print(e)


# Hàm check đã tồn tại folder đích với gốc chưa, chưa thì tạo default rồi gán lại giá trị
def checkStock_Folder(data):
    # GlobalVarible.stockPath_Now = data.get("stock_PATH")
    try:
        if  os.path.exists(data.get("stock_PATH")):
            # print("stockPath_Availiable")
            print(".......")
        
        elif os.path.exists(os.path.join(stock_target_Path, new_Stockfolder_name)):
            print("case cak")
            new_folder_path = os.path.join(stock_target_Path, new_Stockfolder_name)
            data["stock_PATH"] = new_folder_path
            GlobalVarible.stockPath_Now = data.get("stock_PATH")
        else:
            # print("stockPath_NotAvailiable")
            print(".......")
            new_folder_path = os.path.join(stock_target_Path, new_Stockfolder_name)
            os.makedirs(new_folder_path)
            #cập nhật lại data về default
            data["stock_PATH"] = new_folder_path
            GlobalVarible.stockPath_Now = data.get("stock_PATH")
    except Exception as e:
            print(e)

def checkTarget_Folder(data):
    try:
        if  os.path.exists(data.get("target_PATH")):
            # print("targetPath_Availiable")
            print(".....")
        elif os.path.exists(os.path.join(stock_target_Path, new_Targetfolder_name)):
            print(".....")
            new_folder_path = os.path.join(stock_target_Path, new_Targetfolder_name)
            data["target_PATH"] = new_folder_path
            GlobalVarible.targetPath_Now = data.get("stock_PATH")
        else:
            # print("targetPath_NotAvailiable")
            print(".......")
            new_folder_path = os.path.join(stock_target_Path, new_Targetfolder_name)
            os.makedirs(new_folder_path)
            data["target_PATH"] = new_folder_path 
            GlobalVarible.targetPath_Now = data.get("target_PATH")
    except Exception as e:
            print(e)

def check_target_stock_available():
    with open(JsonPath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    checkStock_Folder(data)
    checkTarget_Folder(data)
    with open(JsonPath, 'w') as file:
        json.dump(data, file, indent=4)


    

def Init_Data():
    checkData_Folder(JsonPath)
    check_target_stock_available()