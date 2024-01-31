import os
import glob
import stat

list_of_files = glob.glob(r'C:\Users\rynej\Documents\dataset examples\*')
latest_file = max(list_of_files, key=os.path.getctime)

File = r"C:\Users\rynej\Documents\dataset examples\example.txt"
choice = input("1: Enable Read-Only\n2: Disable Read Only\n")
if choice == "1":
    print("The file is now read only!")
    os.chmod(latest_file, stat.S_IREAD)
elif choice == "2":
    print("The file is now NOT read only!")
    os.chmod(latest_file, stat.S_IWRITE)