import os
import subprocess
import nmap
import httpx
main_while = True
op_while = True
clone_path = ''

os.system('clear')


class mode():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style(code):
        return "\33[{code}m".format(code=code)

    def color(code):
        return "\33[{code}m".format(code=code)


def validateIPAddress (x):
    parts = x.split(".")
    if len(parts) !=4:
        print("IP address {} is not valid".format(x))
        return False
    for part in parts:
        if not isinstance(int(part), int):
            print("IP address {} is not valid".format(x))
            return False
        if int(part)<0 or int(part)>255:
            print("IP address {} is not valid".format(x))
            return False

    print("IP address {} is valid".format(x))
    return True


def check_directory(base_url, directory):
    url = f"{base_url}/{directory}"
    response = httpx.get(url)
    if response.status_code == 200:
        print(f"Found: {url}")

def dir_bruteforce(base_url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            directory = line.strip()
            check_directory(base_url, directory)

wordlist_file = "/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt"  # Replace with the path to your wordlist



print(mode.color(36) + """

                                                          ███╗   ██╗ █████╗ ███╗   ██╗ ██████╗     ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
                                                          ████╗  ██║██╔══██╗████╗  ██║██╔═══██╗    ██╔════╝████╗  ██║██║   ██║████╗ ████║
                                                          ██╔██╗ ██║███████║██╔██╗ ██║██║   ██║    █████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
                                                          ██║╚██╗██║██╔══██║██║╚██╗██║██║   ██║    ██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
                                                          ██║ ╚████║██║  ██║██║ ╚████║╚██████╔╝    ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
                                                          ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝


                                                         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                         $                                                                              $
                                                         $          Developed by: MHD Nazar, Khalid Atatreh, Firas Orfal                $
                                                         $                                                                              $
                                                         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
\n""")

while main_while:
    main_choice = input(str(mode.color(32) + mode.style(1) + """Please select a number that you wish to process
1) Do the enumueration
2) Exit\n""" + mode.color(31) + mode.style(1)))

    if main_choice == '1':
        ip_address = str(input(mode.style(1) + mode.color(32) + "Please enter the IP Address: \n " + mode.color(33) + mode.style(1)))
        gg =validateIPAddress(ip_address)
        if gg==True:
            # os.environ["VAR1"] = ip_address
            # os.system("./IIPP.sh")

            ping_result = subprocess.run(['./IIPP.sh', ip_address],  capture_output=True, text=True)

            if ping_result.returncode == 0:
                print("Host is alive")
                while op_while:
                    options = input(str(mode.color(35) + mode.style(1) + """Please select a number that you wish to process
                1) full enumueration
                2) custom
                3) Exit\n""" + mode.color(31) + mode.style(1)))

                    if options == '1':
                        nm = nmap.PortScanner()
                        # Perform a TCP port scan on all ports with service version detection
                        nm.scan(hosts=ip_address, arguments='-p- -T4 -A')
                        print("hello")
                        # Check the scan results
                        for host in nm.all_hosts():
                            print(f"Host: {host}")
                            for proto in nm[host].all_protocols():
                                print(f"Protocol: {proto}")
                                port_list = nm[host][proto].keys()
                                for port in port_list:
                                    print(f"Port: {port}")
                                    print(f"  State: {nm[host][proto][port]['state']}")
                                    print(f"  Service: {nm[host][proto][port]['name']}")
                                    print(f"  Version: {nm[host][proto][port]['version']}")
                                    print(f"  Product: {nm[host][proto][port]['product']}")
                                    print(f"  Extra Info: {nm[host][proto][port]['extrainfo']}")
                                    print()
                        print("================================================================")
                        dir_bruteforce(ip_address, wordlist_file)


                        main_while = False
                        op_while = False




            else:
                print("Host is unreachable or offline")

        main_while = False


    elif main_choice == '2':
        break;
    else:
        print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only a number between 1 to 2")
        main_while = True

print(mode.color(34) + '\nThanks for using NANO-ENUM tool wish you a great day <3')
print(mode.color(34) + mode.style(3) + "EXITING....")
exit()




























# import hashlib
# from distutils.dir_util import copy_tree
from datetime import datetime
import sys
import shutil
# from playsound import playsound
import logging
import sys

# list_0 = []
# list_1 = []
# list_2 = []
# l = []
# global web_path
# path_validation_p = True
# flag = True
# path_validation_c = True
# specify = True



#2) Detection and fix
# 3) Scan from an original source code
# 4) Scan and fix from an original source code
# 5) Fix only
# 6) Exit\n""" + mode.color(33) + mode.style(1)))

#     if main_choice == '2':
#          web_path = str(input(mode.style(1) + mode.color(32) + "Please enter the super/sub path directory for your web files: \n " + mode.color(33) + mode.style(1)))
#
#         while path_validation_p:
#             web_path = str(input(mode.style(1) + mode.color(
#                 32) + "Please enter the super/sub path directory for your web files: \n " + mode.color(33) + mode.style(
#                 1)))
#
#             if os.path.isdir(web_path) == True:
#
#                 multi_auth_p = input(
#                     mode.color(32) + "Are you sure that" + str(web_path) + " is your right path? " + mode.style(
#                         3) + "[y/n]: \n" + mode.color(33))
#
#                 if multi_auth_p.lower() == 'y':
#                     print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#                     print(mode.color(34) + "[INFO]: Directory found!")
#                     path_validation_p = False
#
#                 elif multi_auth_p.lower() == 'n':
#                     web_path = str(input(mode.style(1) + mode.color(
#                         32) + "Please enter the super/sub path directory for your web files: \n " + mode.color(
#                         33) + mode.style(1)))
#                     path_validation_p = True
#
#                 else:
#                     print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                     path_validation_p = True
#             else:
#                 print(mode.color(31) + mode.style(
#                     1) + "[ERROR]: The path ( " + web_path + " ) that you have entered for your web files is incorrect please check again and insert it")
#                 path_validation_p = True
#
#         clone_start = str(input(mode.color(32) + "Do you want to specify a path for your Cloned directory" + mode.style(
#             3) + "[y/n] ? [Default] " + os.getcwd() + ' : \n ' + mode.color(33)))
#
#         while specify:
#
#             if clone_start.lower() == 'y':
#                 while path_validation_c:
#                     clone_path = str(input(mode.color(
#                         32) + "Please enter the parent path directory to create the cloned file inside it: " + mode.color(
#                         33)))
#                     if os.path.isdir(clone_path) == True:
#                         multi_auth_c = input(mode.color(32) + "Are you sure that" + str(
#                             clone_path) + " is your right path?" + mode.style(3) + "[y/n]: " + mode.color(33))
#                         if multi_auth_c.lower() == 'y':
#                             print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#                             if (os.path.isdir(clone_path + '/Cloned') == False):
#                                 os.mkdir(clone_path + '/Cloned')
#                                 clone_path = os.getcwd() + '/Cloned'
#                                 print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                                 path_validation_c = False
#                                 specify = False
#                             else:
#                                 os.system('rm ' + clone_path + '/Cloned -rf')
#                                 print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                                 clone_path = os.getcwd() + '/Cloned'
#                                 path_validation_c = False
#                                 specify = False
#                         elif multi_auth_c.lower() == 'n':
#                             path_validation_c = True
#                         else:
#                             print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters", '\n')
#                             path_validation_c = True
#                     else:
#                         print(mode.color(31) + mode.color(
#                             1) + "[ERROR]: The path ( " + clone_path + " ) that you have entered for your web files is incorrect please check again and insert it")
#                         path_validation_c = True
#             elif clone_start.lower() == 'n':
#                 if (os.path.isdir(os.getcwd() + '/Cloned') == False):
#                     os.mkdir(os.getcwd() + '/Cloned')
#                     clone_path = os.getcwd() + '/Cloned'
#                     print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                     specify = False
#                 else:
#                     os.system('rm ' + os.getcwd() + '/Cloned -rf')
#                     print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                     clone_path = os.getcwd() + '/Cloned'
#                     specify = False
#             else:
#                 print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                 clone_start = str(
#                     input(mode.color(32) + "Do you want to specify a path for your Cloned directory" + mode.style(
#                         3) + "[y/n] ? [Default] " + os.getcwd() + ' : \n ' + mode.color(33)))
#                 specify = True
#
#         copy_tree(web_path, clone_path)
#
#         for r, d, f in os.walk(clone_path):
#             for n in f:
#                 F = (os.path.join(r, n))
#                 md5_2 = hashlib.md5()
#                 with open(F, 'rb') as af:
#                     buf = af.read()
#                     md5_2.update(buf)
#                     list_0.append(md5_2.hexdigest())
#
#         print(mode.color(34) + """\n
#                                       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                       $                                                                                                                     $
#                                       $  You will be alerted if there is a web defacement attack occurs to your files, please do not cancel the iteration   $
#                                       $                                                                                                                     $
#                                       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#
#         while flag:
#             for root, direc, files in os.walk(web_path):
#                 for name in files:
#                     # print(os.path.join(root, name))
#                     FILES = (os.path.join(root, name))
#                     md5 = hashlib.md5()
#
#                     with open(str(FILES), 'rb') as afile:
#                         buf = afile.read()
#                         md5.update(buf)
#                         list_1.append(md5.hexdigest())
#             if list_0 == list_1:
#                 flag = True
#                 list_1.clear()
#             else:
#
#                 flag = False
#
#         print(mode.color(37) + mode.style(1) + mode.background(31) + """\n
#         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#         $                                                                                                                                                             $
#         $                                                                        ALERT!                                                                               $
#         $     We detected a web defacement attack on your files, we are fixing the problem please dont close this terminal and contact you admin domain immediatly    $
#         $                                                                                                                                                             $
#         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#
#         shutil.rmtree(web_path, ignore_errors=False, onerror=None)
#         os.mkdir(web_path)
#         os.system('cp ' + clone_path + '/* ' + ' ' + web_path + " -r")
#         # playsound(os.getcwd() + '/alarm.mp3')
#         main_while = False
#
#     elif main_choice == '1':
#         while path_validation_p:
#             web_path = str(input(mode.style(1) + mode.color(
#                 32) + "Please enter the super/sub path directory for your web files: \n " + mode.color(33) + mode.style(
#                 1)))
#
#             if os.path.isdir(web_path) == True:
#                 multi_auth_p = input(
#                     mode.color(32) + "Are you sure that" + str(web_path) + " is your right path? " + mode.style(
#                         3) + "[y/n]: \n" + mode.color(33))
#                 if multi_auth_p.lower() == 'y':
#                     print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#                     print(mode.color(34) + "[INFO]: Directory found!")
#                     path_validation_p = False
#                 elif multi_auth_p.lower() == 'n':
#                     path_validation_p = True
#                 else:
#                     print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                     path_validation_p = True
#             else:
#                 print(mode.color(31) + mode.style(
#                     1) + "[ERROR]: The path ( " + web_path + " ) that you have entered for your web files is incorrect please check again and insert it")
#                 path_validation_p = True
#
#         clone_start = str(input(mode.color(32) + "Do you want to specify a path for your Cloned directory" + mode.style(
#             3) + "[y/n] ? [Default] " + os.getcwd() + ' : \n ' + mode.color(33)))
#
#         while specify:
#
#             if clone_start.lower() == 'y':
#                 while path_validation_c:
#                     clone_path = str(input(mode.color(
#                         32) + "Please enter the parent path directory to create the cloned file inside it: " + mode.color(
#                         33)))
#                     if os.path.isdir(clone_path) == True:
#                         multi_auth_c = input(
#                             mode.color(32) + "Are you sure that" + str(
#                                 clone_path) + " is your right path?" + mode.style(
#                                 3) + "[y/n]: " + mode.color(33))
#                         if multi_auth_c.lower() == 'y':
#                             print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#                             if (os.path.isdir(clone_path + '/Cloned') == False):
#                                 os.mkdir(clone_path + '/Cloned')
#                                 clone_path = os.getcwd() + '/Cloned'
#                                 print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                                 path_validation_c = False
#                                 specify = False
#                             else:
#                                 os.system('rm ' + clone_path + '/Cloned -rf')
#                                 print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                                 clone_path = os.getcwd() + '/Cloned'
#                                 path_validation_c = False
#                                 specify = False
#                         elif multi_auth_c.lower() == 'n':
#                             path_validation_c = True
#                         else:
#                             print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters", '\n')
#                             path_validation_c = True
#                     else:
#                         print(mode.color(31) + mode.color(
#                             1) + "[ERROR]: The path ( " + clone_path + " ) that you have entered for your Cloned path is incorrect please check again and insert it")
#                         path_validation_c = True
#             elif clone_start.lower() == 'n':
#                 if (os.path.isdir(os.getcwd() + '/Cloned') == False):
#                     os.mkdir(os.getcwd() + '/Cloned')
#                     clone_path = os.getcwd() + '/Cloned'
#                     print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                     specify = False
#                 else:
#                     os.system('rm ' + os.getcwd() + '/Cloned -rf')
#                     print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                     clone_path = os.getcwd() + '/Cloned'
#                     specify = False
#             else:
#                 print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                 clone_start = str(
#                     input(mode.color(32) + "Do you want to specify a path for your Cloned directory" + mode.style(
#                         3) + "[y/n] ? [Default] " + os.getcwd() + ' : \n ' + mode.color(33)))
#                 specify = True
#
#         copy_tree(web_path, clone_path)
#
#         for r, d, f in os.walk(clone_path):
#             for n in f:
#                 F = (os.path.join(r, n))
#                 md5_2 = hashlib.md5()
#                 with open(F, 'rb') as af:
#                     buf = af.read()
#                     md5_2.update(buf)
#                     list_0.append(md5_2.hexdigest())
#
#         print(mode.color(34) + """\n
#                                               $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                               $                                                                                                                     $
#                                               $  You will be alerted if there is a web defacement attack occurs to your files, please do not cancel the iteration   $
#                                               $                                                                                                                     $
#                                               $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#         while flag:
#             for root, direc, files in os.walk(web_path):
#                 for name in files:
#                     # print(os.path.join(root, name))
#                     FILES = (os.path.join(root, name))
#                     md5 = hashlib.md5()
#
#                     with open(str(FILES), 'rb') as afile:
#                         buf = afile.read()
#                         md5.update(buf)
#                         list_1.append(md5.hexdigest())
#             if list_0 == list_1:
#                 flag = True
#                 list_1.clear()
#             else:
#                 flag = False
#         main_while = False
#
#         print(mode.color(37) + mode.style(1) + mode.background(31) + """\n
#                                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                             $                                                                                                                             $
#                                             $                                                         ALERT!                                                              $
#                                             $     We detected a web defacement attack on your files, Please rerun the tool and choose Fix only mode to fix the problem    $
#                                             $                                                                                                                             $
#                                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#         # playsound(os.getcwd()+'/alarm.mp3')
#
#     elif main_choice == '3':
#
#         while path_validation_p:
#             web_path = str(input(mode.style(1) + mode.color(
#                 32) + "Please enter the super/sub path directory for your current web files: \n " + mode.color(
#                 33) + mode.style(1)))
#
#             if os.path.isdir(web_path) == True:
#                 multi_auth_p = input(
#                     mode.color(32) + "Are you sure that" + str(web_path) + " is your right path? " + mode.style(
#                         3) + "[y/n]: \n" + mode.color(33))
#                 if multi_auth_p.lower() == 'y':
#                     print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#                     print(mode.color(34) + "[INFO]: Directory found!")
#                     path_validation_p = False
#                 elif multi_auth_p.lower() == 'n':
#                     path_validation_p = True
#                 else:
#                     print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                     path_validation_p = True
#             else:
#                 print(mode.color(31) + mode.style(
#                     1) + "[ERROR]: The path ( " + web_path + " ) that you have entered for your current web files is incorrect please check again and insert it")
#                 path_validation_p = True
#
#         while specify:
#
#             while path_validation_c:
#                 org_path = str(input(mode.color(
#                     32) + "Please enter the parent path directory to your original source code path: " + mode.color(
#                     33)))
#                 if os.path.isdir(org_path) == True:
#                     multi_auth_c = input(
#                         mode.color(32) + "Are you sure that" + str(org_path) + " is your right path?" + mode.style(
#                             3) + "[y/n]: " + mode.color(33))
#                     if multi_auth_c.lower() == 'y':
#                         print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#
#                         print(mode.color(34) + "[INFO]: Direcory for your original source code have been found!")
#                         path_validation_c = False
#                         specify = False
#
#                     elif multi_auth_c.lower() == 'n':
#                         path_validation_c = True
#                     else:
#                         print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters", '\n')
#                         path_validation_c = True
#                 else:
#                     print(mode.color(31) + mode.color(
#                         1) + "[ERROR]: The path ( " + org_path + " ) that you have entered for your orginal source code path is incorrect please check again and insert it")
#                     path_validation_c = True
#
#             if specify:
#                 print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                 org_path = str(input(mode.color(
#                     32) + "Please enter the parent path directory to your original source code path: " + mode.color(
#                     33)))
#             # specify = True
#
#         for r, d, f in os.walk(org_path):
#             for n in f:
#                 F = (os.path.join(r, n))
#                 md5_2 = hashlib.md5()
#                 with open(F, 'rb') as af:
#                     buf = af.read()
#                     md5_2.update(buf)
#                     list_2.append(md5_2.hexdigest())
#
#         for root, direc, files in os.walk(web_path):
#             for name in files:
#                 FILES = (os.path.join(root, name))
#                 md5 = hashlib.md5()
#
#                 with open(str(FILES), 'rb') as afile:
#                     buf = afile.read()
#                     md5.update(buf)
#                     list_1.append(md5.hexdigest())
#
#         if list_2 == list_1:
#
#             print(mode.color(34) + mode.style(3) + """\n
#                          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                          $                                                        $
#                          $     Your files are the same and no need to fix them    $
#                          $                                                        $
#                          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#
#         else:
#
#             playsound(os.getcwd() + '/alarm.mp3')
#             print(mode.color(31) + mode.color(1) + """\n
#
#                          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                          $                                                                                            $
#                          $     Your files have been defaced before please run Scan and fix mode to fix the problem    $
#                          $                                                                                            $
#                          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#
#         main_while = False
#
#     elif main_choice == '4':
#
#         while path_validation_p:
#             web_path = str(input(mode.style(1) + mode.color(
#                 32) + "Please enter the super/sub path directory for your current web files: \n " + mode.color(
#                 33) + mode.style(1)))
#
#             if os.path.isdir(web_path) == True:
#                 multi_auth_p = input(
#                     mode.color(32) + "Are you sure that" + str(web_path) + " is your right path? " + mode.style(
#                         3) + "[y/n]: \n" + mode.color(33))
#                 if multi_auth_p.lower() == 'y':
#                     print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#                     print(mode.color(34) + "[INFO]: Directory found!")
#                     path_validation_p = False
#                 elif multi_auth_p.lower() == 'n':
#                     path_validation_p = True
#                 else:
#                     print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                     path_validation_p = True
#             else:
#                 print(mode.color(31) + mode.style(
#                     1) + "[ERROR]: The path ( " + web_path + " ) that you have entered for your current web files is incorrect please check again and insert it")
#                 path_validation_p = True
#
#         while specify:
#
#             while path_validation_c:
#                 org_path = str(input(mode.color(
#                     32) + "Please enter the parent path directory to your original source code path: " + mode.color(
#                     33)))
#                 if os.path.isdir(org_path) == True:
#                     multi_auth_c = input(
#                         mode.color(32) + "Are you sure that" + str(org_path) + " is your right path?" + mode.style(
#                             3) + "[y/n]: " + mode.color(33))
#                     if multi_auth_c.lower() == 'y':
#                         print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#
#                         print(mode.color(34) + "[INFO]: Directory for your original source code have been found!")
#                         path_validation_c = False
#                         specify = False
#
#                     elif multi_auth_c.lower() == 'n':
#                         path_validation_c = True
#                     else:
#                         print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters", '\n')
#                         path_validation_c = True
#                 else:
#                     print(mode.color(31) + mode.color(
#                         1) + "[ERROR]: The path ( " + org_path + " ) that you have entered for your orginal source code path is incorrect please check again and insert it")
#                     path_validation_c = True
#
#             if specify:
#                 print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                 org_path = str(input(mode.color(
#                     32) + "Please enter the parent path directory to your original source code path: " + mode.color(
#                     33)))
#             # specify = True
#
#         for r, d, f in os.walk(org_path):
#             for n in f:
#                 F = (os.path.join(r, n))
#                 md5_2 = hashlib.md5()
#                 with open(F, 'rb') as af:
#                     buf = af.read()
#                     md5_2.update(buf)
#                     list_2.append(md5_2.hexdigest())
#
#         for root, direc, files in os.walk(web_path):
#             for name in files:
#                 FILES = (os.path.join(root, name))
#                 md5 = hashlib.md5()
#
#                 with open(str(FILES), 'rb') as afile:
#                     buf = afile.read()
#                     md5.update(buf)
#                     list_1.append(md5.hexdigest())
#
#         if list_2 == list_1:
#
#             print(mode.color(34) + mode.style(3) + """\n
#              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#              $                                                        $
#              $     Your files are the same and no need to fix them    $
#              $                                                        $
#              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#         else:
#
#             print(mode.color(31) + mode.color(1) + """\n
#              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#              $                                             $
#              $     Your files have been defaced before     $
#              $                                             $
#              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#
#             shutil.rmtree(web_path, ignore_errors=False, onerror=None)
#             os.mkdir(web_path)
#             os.system('cp ' + org_path + '/* ' + ' ' + web_path + " -r")
#             playsound(os.getcwd() + '/alarm.mp3')
#             print(mode.color(34) + mode.style(
#                 3) + "\n[INFO]: Fixing the problem please stand by and dont close the running terminal...")
#             print(mode.color(34) + mode.style(3) + "[INFO]: The process have been completed")
#             main_while = False
#
#     elif main_choice == '5':
#         while path_validation_p:
#             web_path = str(input(mode.style(1) + mode.color(
#                 32) + "Please enter the super/sub path directory for your web files: \n " + mode.color(33) + mode.style(
#                 1)))
#
#             if os.path.isdir(web_path) == True:
#
#                 multi_auth_p = input(
#                     mode.color(32) + "Are you sure that" + str(web_path) + " is your right path? " + mode.style(
#                         3) + "[y/n]: \n" + mode.color(33))
#
#                 if multi_auth_p.lower() == 'y':
#                     print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#                     print(mode.color(34) + "[INFO]: Directory found!")
#                     path_validation_p = False
#
#                 elif multi_auth_p.lower() == 'n':
#                     web_path = str(input(mode.style(1) + mode.color(
#                         32) + "Please enter the super/sub path directory for your web files: \n " + mode.color(
#                         33) + mode.style(1)))
#                     path_validation_p = True
#
#                 else:
#                     print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                     path_validation_p = True
#             else:
#                 print(mode.color(31) + mode.style(
#                     1) + "[ERROR]: The path ( " + web_path + " ) that you have entered for your web files is incorrect please check again and insert it")
#                 path_validation_p = True
#
#         clone_start = str(input(mode.color(32) + "Do you want to specify a path for your Cloned directory" + mode.style(
#             3) + "[y/n] ? [Default] " + os.getcwd() + ' : \n ' + mode.color(33)))
#
#         while specify:
#
#             if clone_start.lower() == 'y':
#                 while path_validation_c:
#                     clone_path = str(input(mode.color(
#                         32) + "Please enter the parent path directory to create the cloned file inside it: " + mode.color(
#                         33)))
#                     if os.path.isdir(clone_path) == True:
#                         multi_auth_c = input(mode.color(32) + "Are you sure that" + str(
#                             clone_path) + " is your right path?" + mode.style(3) + "[y/n]: " + mode.color(33))
#                         if multi_auth_c.lower() == 'y':
#                             print(mode.color(34) + "[INFO]: Searching for the inserted directory...")
#                             if (os.path.isdir(clone_path + '/Cloned') == False):
#                                 os.mkdir(clone_path + '/Cloned')
#                                 clone_path = os.getcwd() + '/Cloned'
#                                 print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                                 path_validation_c = False
#                                 specify = False
#                             else:
#                                 os.system('rm ' + clone_path + '/Cloned -rf')
#                                 print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                                 clone_path = os.getcwd() + '/Cloned'
#                                 path_validation_c = False
#                                 specify = False
#                         elif multi_auth_c.lower() == 'n':
#                             path_validation_c = True
#                         else:
#                             print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters", '\n')
#                             path_validation_c = True
#                     else:
#                         print(mode.color(31) + mode.color(
#                             1) + "[ERROR]: The path ( " + clone_path + " ) that you have entered for your web files is incorrect please check again and insert it")
#                         path_validation_c = True
#             elif clone_start.lower() == 'n':
#                 if (os.path.isdir(os.getcwd() + '/Cloned') == False):
#                     os.mkdir(os.getcwd() + '/Cloned')
#                     clone_path = os.getcwd() + '/Cloned'
#                     print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                     specify = False
#                 else:
#                     os.system('rm ' + os.getcwd() + '/Cloned -rf')
#                     print(mode.color(34) + "[INFO]: Cloned directory have been created successfully")
#                     clone_path = os.getcwd() + '/Cloned'
#                     specify = False
#             else:
#                 print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only y or n letters")
#                 clone_start = str(
#                     input(mode.color(32) + "Do you want to specify a path for your Cloned directory" + mode.style(
#                         3) + "[y/n] ? [Default] " + os.getcwd() + ' : \n ' + mode.color(33)))
#                 specify = True
#
#         copy_tree(web_path, clone_path)
#
#         for r, d, f in os.walk(clone_path):
#             for n in f:
#                 F = (os.path.join(r, n))
#                 md5_2 = hashlib.md5()
#                 with open(F, 'rb') as af:
#                     buf = af.read()
#                     md5_2.update(buf)
#                     list_0.append(md5_2.hexdigest())
#
#         for root, direc, files in os.walk(web_path):
#             for name in files:
#                 # print(os.path.join(root, name))
#                 FILES = (os.path.join(root, name))
#                 md5 = hashlib.md5()
#
#                 with open(str(FILES), 'rb') as afile:
#                     buf = afile.read()
#                     md5.update(buf)
#                     list_1.append(md5.hexdigest())
#
#         if list_0 == list_1:
#             print(mode.color(34) + mode.color(3) + """\n
#              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#              $                                                        $
#              $     Your files are the same and no need to fix them    $
#              $                                                        $
#              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#         else:
#             print(mode.color(31) + mode.color(1) + """\n
#              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#              $                                                                                            $
#              $     Your files have been defaced before please run Scan and fix mode to fix the problem    $
#              $                                                                                            $
#              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
#
#         print(mode.color(32) + "Fixing the problem....")
#         shutil.rmtree(web_path, ignore_errors=False, onerror=None)
#         os.mkdir(web_path)
#         os.system('cp ' + clone_path + '/* ' + ' ' + web_path + " -r")
#         playsound(os.getcwd() + '/alarm.mp3')
#         print(mode.color(32) + mode.style(3) + "[INFO]: FINISHED")
#         main_while = False
#
#     elif main_choice == '6':
#         break;
#     else:
#         print(mode.color(31) + mode.style(1) + "[ERROR]: Please enter only a number between 1 to 6")
#         main_while = True
#
# print(mode.color(34) + '\nThanks for using Nano_facment tool wish you a great day <3')
# print(mode.color(34) + mode.style(3) + "EXITING....")
# exit()
