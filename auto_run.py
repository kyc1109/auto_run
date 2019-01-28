#!python3
# -*- coding: UTF-8 -*-
import sys, os, time, datetime, ctypes, subprocess
def auto_run():
    filename=os.path.basename(__file__).replace(".py", ".exe")
    filefullpathname=os.getcwd()+"\\"+filename#sys.argv[0] is not stable
    regkey="HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    print("cwd:", os.getcwd())
    #os.chdir(os.environ['USERPROFILE']+"\\Desktop") #Change the current working directory to Desktop
    #print("cwd: ", os.getcwd())
    #print("regkey: ", regkey)
    print("filename:",filename)
    print("filefullpathname:",filefullpathname)
    
    for root, dirs, files in os.walk("C:\\"): #https://stackoverflow.com/questions/1124810/how-can-i-find-path-to-given-file
        for file in files:
            if file == filename:
                os.chdir(root)
                #print(os.path.abspath(os.path.join(file)))
                filefullpathname=os.path.abspath(os.path.join(root,file))
                print(filefullpathname)     
    try:
        #print("regkey: ","reg add "+regkey+" /v stress_"+filename.replace(".exe","")+" /t REG_SZ /d "+filefullpathname+" /f")
        os.system("reg add "+regkey+" /v stress_"+filename.replace(".exe","")+" /t REG_SZ /d "+filefullpathname+" /f")
        print("auto run reg ok")
        os.system("timeout /t 10")
    except:
        print("auto run reg failed !!!")
        os.system("timeout /t 30")

if __name__ == "__main__":  # Start from here
    auto_run()
