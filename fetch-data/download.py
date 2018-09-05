# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Version 
#   Author: WildfootW
#   GitHub: github.com/Wildfoot
#   Copyright (C) 2018 WildfootW All rights reserved.
#

from ftplib import FTP
import re
import os

FTP_SERVER_DOMAIN = "ftp.ntu.edu.tw"
FTP_SERVER_DIRECTORY = "NTU/course/"
SAVE_FILE_LOCATION = "./file/"

if __name__ == "__main__":

    if not os.path.exists(SAVE_FILE_LOCATION):
        os.makedirs(SAVE_FILE_LOCATION)

    ftp = FTP(FTP_SERVER_DOMAIN)
    ftp.login()
    ftp.getwelcome()
    ftp.cwd(FTP_SERVER_DIRECTORY)
    file_list = []
    ftp.retrlines("LIST", file_list.append)
    for i in range(len(file_list)):
        try:
            print(file_list[i])
            file_name = re.search("COURSE.*(X|x)(L|l)(S|s)", file_list[i]).group(0)
            print("Downloading " + file_name + "...")
            ftp.retrbinary("RETR " + file_name, open(SAVE_FILE_LOCATION + file_name, "wb").write)
        except AttributeError:
            continue
    ftp.close()

# https://shades-of-orange.com/post/How-to-Convert-an-XSLX-File-to-CSV-with-UTF-8-Encoding-Using-LibreOffice-OpenOffice
