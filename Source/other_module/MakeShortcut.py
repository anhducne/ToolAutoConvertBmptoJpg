import os
import win32com.client

# Đường dẫn đến phần mềm mà bạn muốn tạo shortcut
target = r"C:\Users\Duxbee\Desktop\DuxBee_tool\DuxBee_tool.exe"

# Lấy đường dẫn đến thư mục ProgramData từ biến môi trường
program_data = os.environ['PROGRAMDATA']

# Tạo đường dẫn đến thư mục Startup
folder = os.path.join(program_data, r"Microsoft\Windows\Start Menu\Programs\StartUp")

# Tên của shortcut
shortcut_name = "MyApp"

# Tạo một đối tượng shell
shell = win32com.client.Dispatch("WScript.Shell")

# Tạo đường dẫn đầy đủ cho file shortcut
shortcut_path = os.path.join(folder, shortcut_name + ".lnk")

# Tạo shortcut
shortcut = shell.CreateShortcut(shortcut_path)
shortcut.TargetPath = target
shortcut.WorkingDirectory = os.path.dirname(target)  # Thư mục làm việc sẽ là thư mục chứa ứng dụng
shortcut.IconLocation = target  # Sử dụng icon của ứng dụng
shortcut.save()

print(f"Shortcut '{shortcut_name}' đã được tạo tại '{folder}'")