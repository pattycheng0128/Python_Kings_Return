import subprocess

# 3個獨立的子行程，記憶體是各別獨立的
calcPro = subprocess.Popen('calc.exe')
notePro = subprocess.Popen('notepad.exe')
writePro = subprocess.Popen('write.exe')
print(calcPro,notePro,writePro)