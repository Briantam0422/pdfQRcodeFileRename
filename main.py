import os
import tempfile
import glob
from datetime import datetime
from os.path import join, basename
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode


def cihan():
    same_name_count = 0
    file_folder = os.path.join(os.path.abspath(os.getcwd()), 'files')
    if len(os.listdir(file_folder)) == 0:
        print("No pdf found")
        print("Please put all the pdf documents to the 'files' folder")
    else:
        for file in glob.glob(join(file_folder, '*.pdf')):
            # convert pdf file to png
            # scan the image
            file_name = basename(file)
            print("Get File: " + file_name)
            with tempfile.TemporaryDirectory() as path:
                poppler_path = os.path.join(os.path.abspath(os.getcwd()), r'poppler-0.68.0\bin')
                images_from_path = convert_from_path(file, 500, poppler_path=poppler_path)
                new_name = []
                for image in images_from_path:
                    decoded = decode(image)
                    for d in decoded:
                        new_name.append(d.data.decode("utf-8"))
            new_name_joined = '{}.pdf'.format(','.join(new_name))
            print('New name: ' + new_name_joined)
            old_name_path = os.path.join(file_folder, file_name)
            new_name_path = os.path.join(file_folder, new_name_joined)
            try:
                os.rename(old_name_path, new_name_path)
            except:
                new_name.append(str(same_name_count))
                new_name_joined = '{}.pdf'.format('_copy'.join(new_name))
                new_name_path = os.path.join(file_folder, new_name_joined)
                os.rename(old_name_path, new_name_path)
                same_name_count = same_name_count + 1
            print("Renamed: " + file_name + " to " + new_name_joined)
            print("----------------------------------------------------------------------------------------")


if __name__ == '__main__':
    # python main.py
    print("Scan Started")
    print("---------------------------------------SCANNING-------------------------------------------")
    cihan()
    print("------------------------------------------END----------------------------------------------")
    print()
    k = input("press enter to exit")
