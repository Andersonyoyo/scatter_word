import csv
import cv2
from datetime import datetime
import os

abs_work_space = os.getcwd()
filename1 = abs_work_space + "\\" + '50100.csv'
filename2 = abs_work_space + "\\" + '50100C.csv'
filename3 = abs_work_space + "\\" + '50100L.csv'
wordinline = []
def sahpe_to_line(file):
    filename = file
    with open(filename, 'r', encoding='UTF-8') as file_obj:
        # csv.reader将文件作为阅读对象传递给reader
        reader = csv.reader(file_obj)
        cout = 0
        for row in reader:
            for num in row:
                if(num == '1'):
                    wordinline.append(cout)
                cout += 1
        file_obj.close()
    return wordinline
