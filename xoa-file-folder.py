import os
import shutil
import time

folder_path = 'c:\\test1'  # Thay đổi đường dẫn này thành thư mục bạn muốn làm việc với
#so ngay:
setNDay = 2

n_days_ago_time = time.time() - setNDay * 24 * 3600  # n ngày trước

while 1:
    print(" Loop...")

    # Lặp qua tất cả các tệp và thư mục trong thư mục
    for root, dirs, files in os.walk(folder_path):
        print(root, dirs, files)
        for file in files:
            file_path = os.path.join(root, file)
            file_creation_time = os.path.getmtime(file_path)
            
            if file_creation_time < n_days_ago_time:
                print("Xoa file: " + file_path)
                os.remove(file_path)  # Xóa tệp

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_creation_time = os.path.getmtime(dir_path)
            if dir_creation_time < n_days_ago_time:
                print("Xoa file: " + dir_path)
                shutil.rmtree(dir_path)  # Xóa thư mục và nội dung bên trong nó
    
    time.sleep(10)
