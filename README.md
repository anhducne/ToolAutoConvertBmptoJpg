- Thư viện:
  
1. pip install Pillow (GUI)
2. pip install event-dispatching (Event)
3. pip install watchdog (EventHandle bắt skien có file mới vào folder)
4. pip install pyinstaller (gói code lại thành packet)
5. pip install pywin32 (bắt sự kiện thu nhỏ chương trình xuống khay)
6. pip install pystray (tạo thu nhỏ ở notificationbar)

- Build ra exe:

1. Lệnh build 
pyinstaller --windowed --onefile UIUX.py
2. Lệnh build kèm icon
pyinstaller --icon my_icon.ico main.py
3. Build file spec - cấu hình trong file và chúng ta sẽ build theo cấu hình file
pyinstaller UIUX.spec ==> UIUX ở đây thì thay bằng tên file py mình muốn build

- Dành cho file exe 

1. Tự động khởi động
- Tạo Shortcut cho vào C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
2. Khi bật tự động chạy khi khởi động máy
- UI sẽ không chạy trước mà ở noti sẽ có icon của tool
3. Đối với bản full - tool bắt buộc phải có file _internal đi kèm
4. Đối với bản Portable - tool chạy đơn lẻ không cần file kèm theo
