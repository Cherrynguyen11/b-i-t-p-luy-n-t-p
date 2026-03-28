import time

nam_sinh = int(input("Nhập năm sinh: "))
nam_hien_tai = time.localtime().tm_year

tuoi = nam_hien_tai - nam_sinh

print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi")
