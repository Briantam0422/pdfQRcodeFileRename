import sys
import subprocess

print("Setup started")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pdf2image'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyzbar'])
print("Setup Done")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
