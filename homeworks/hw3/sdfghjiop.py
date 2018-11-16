import os
inp = "input_texts"
lst = os.listdir(inp)
for fl in lst:
    os.system(r"C:\Users\Пользователь\Downloads\mystem-3.1-win-64bit.zip " + inp + os.sep + fl + " output_texts" + os.sep + fl)
