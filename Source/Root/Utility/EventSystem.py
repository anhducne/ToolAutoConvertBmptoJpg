class Event:
    def __init__(self, name):
        self.name = name

class EventManager:
    def __init__(self):
        self.events = {}

    def subscribe(self, event_name, callback):
        print(f"---đăng ký sự kiện: {event_name}")
        if event_name not in self.events:
            self.events[event_name] = []
            print(f"---đăng ký sự kiện: {self.events[event_name]}")

        self.events[event_name].append(callback)
        print(f"---đăng ký hàm: {callback}")

    def publish(self, event):
        print(f"---bắn sự kiện: {event.name}")
        event_name = event.name
        if event_name in self.events:
            print(f"---check sự kiện đến hàm: {event_name}")
            for callback in self.events[event_name]:
                print(f"---bắn sự kiện đến hàm: {callback(event)}")
                callback(event)


        
# def event_NotiFunx(Event):   # Sự kiện được bắn
#     print("+++nhận sự kiện không ? ")
#     label_toolStatus.config(text=f"Tool Status: Nhận sự kiện nef")
#     # print(f"Tool Status: {var_static.ToolStatus}")
#     print(f"Event {Event.name} fired in file_a!")

# event_manager.subscribe(str_static.event_Noti, event_NotiFunx) # Đăng ký sự kiện



# from Utility import GlobalVarible
# from Utility import StringHelper
# from Utility.EventSystem import EventManager
# from Utility.EventSystem import Event

# # OnEnable
# event_manager = EventManager()


# def tool_status(str):
#     GlobalVarible.ToolStatus = str
#     print(f"in GLobal Func: { GlobalVarible.ToolStatus}")
#     event_1 = Event(StringHelper.event_Noti)
#     event_manager.publish(event_1)