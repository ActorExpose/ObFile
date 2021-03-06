try:
    import pyfiglet
    import subprocess
    import os
    import re
    from colorama import *
    import platform
    import time
    from os import system, name
    import sys
    from pyarmor.pyarmor import main as call_pyarmor
    from progress.spinner import Spinner
    import tkinter
    from tkinter import messagebox

except ImportError:
    print(Fore.RED + 'Error occured.. please try again')



root = tkinter.Tk()
root.withdraw()

os.system('cls')

banner = pyfiglet.figlet_format('ObFile')
print(banner)
init()
print(Fore.GREEN + "[=] Instant Devs Corp. 2020")
print(Fore.GREEN + '[=] Obfile is a python obfuscator and compiler')
print(Fore.RED +   '----------------------------------------------')
print(Fore.GREEN + '[=] App Version : 1.1.1')
print(Fore.RED +   'Info')
print(Fore.GREEN + 'User OS            : ' + platform.system())
print(Fore.GREEN + 'OS Version         : ' + platform.release())
print(Fore.GREEN + 'ObFile Released    :   5/09/2020    ')
print(Fore.GREEN + 'Last Updated       :   10/09/2020')

print(Fore.RED + '------------------------------------------------')
print(Fore.GREEN + 'Developer : Kavin Jindal')
print(Fore.GREEN + 'Dev Contact : kavinsjindal@gmail.com')
print(Style.RESET_ALL)
print(' ')
print(' ')
input(Fore.RED + "Press enter to start Menu")



subprocess.call('cls', shell=True)

ascii_banner = pyfiglet.figlet_format("ObFile Menu")
print(ascii_banner)
 
while True:

    def user_choice_menu():
        while True:
            init()
            print(Fore.GREEN + ' >> Main Menu ')
            print(' ')
            print(Fore.CYAN + '    [=] Compile into exe = Type use 1')
            print(' ')
            print(Fore.CYAN + '    [=] Obfuscate File = Type use 2')
            print(' ')
            print(Fore.CYAN + '    [=] Obfuscate and compile together = Type use 3')
            print(' ')
            print(Fore.CYAN + '    [=] Help = Type use 4')
            print(' ')
            print(Fore.CYAN + '    [=] Quit Program = Type use 5')
            print(' ')
            user_input = input('>>> : ')
            
                      
                        
            if 'use 1' in user_input:
                print(Fore.GREEN + "Opening Compiler please wait")
                subprocess.call('cls', shell = True)
                banner = pyfiglet.figlet_format('ObFile Compiler')
                print(banner)
                print(Fore.WHITE + '---------------------------------------------------') 
                print(Fore.RED +   'ObFile Python to EXE compiler')
                print(Fore.WHITE + '---------------------------------------------------') 
                print(Fore.RED +   'You can compile your .py file into .exe with icon')
                print(Fore.RED +   'You can even compile the file without icon')
                print(Fore.RED +   'Only .ico files are allowed for icons')
                print(Fore.WHITE + '---------------------------------------------------') 
                
                             
                input(Fore.YELLOW + 'Press Enter to continue >>')
                dir_input = input(Fore.YELLOW + "\n Enter correct directory of file >>")
                print(' ')

                print(Fore.CYAN + 'File Directory >> ' + dir_input)
                print(' ')

                user_option = input(Fore.RED + 'Do you want to add icon to your file?'
                '\n' 'Type yes or no >> '
                                               '')


                if 'yes' in user_option:
                    print(Fore.RED + '\nThe file will be compiled into exe with an icon')
                    icon_input = input(Fore.YELLOW + 'Enter icon directory (only .ico) >>> ')
                    print(' ')

                    print(Fore.CYAN + 'Icon Directory >> ' + icon_input)
                    print(' ')
                    print(Fore.YELLOW + 'Starting compiling process')

                    os.system(f'pyinstaller -F -i   {icon_input}   {dir_input}')
                    
                    subprocess.call('cls', shell=True)
                    #os.system("Msgbox\MsgBox.vbs")
                    messagebox.showinfo('ObFile', 'The file has been compiled. ')

                    input(Fore.RED + "Press to continue")


                if 'no' in user_option:
                    print(Fore.CYAN + '\n\n The file will compile into exe without a custom icon')
                    subprocess.call(f'pyinstaller -F {dir_input}', shell=True)
                    subprocess.call('cls', shell=True)
                    print(Fore.RED + '\n\tCompiling process finished')
                    #os.system('Msgbox\MsgBox.vbs')
                    messagebox.showinfo('ObFile', 'The file has been compiled. ')

                    input(Fore.RED + "Press to continue")

                else:
                    input(Fore.CYAN + 'Press enter to continue')
                    subprocess.call('cls', shell=True)
             
    
            
            if 'use 2' in user_input:
                print(Fore.GREEN + "Opening Obfuscator")

                subprocess.call('cls', shell=True)
                banner1 = pyfiglet.figlet_format('ObFile Obfuscator')
                print(banner1)

                print(Fore.WHITE + '--------------------------------------------------------') 
                print(Fore.RED +   'ObFile Obfuscator')
                print(Fore.WHITE + '--------------------------------------------------------') 
                print(Fore.RED +   'You can only "Obfuscate your python file with this tool"')
                print(Fore.RED +   'Make sure to enter the correct file path')
                print(Fore.WHITE + '--------------------------------------------------------') 
                input(Fore.RED +   "Press to Continue >>")


                ob_dir = input(Fore.RED + "\n [=] Enter the file directory>> ")
                print(Fore.WHITE + '\n Starting Compiling....')
                subprocess.call(f'pyarmor obfuscate {ob_dir}', shell=True)
                print(Fore.WHITE + "Obfuscation Complete")
                messagebox.showinfo('ObFile', 'The file has been obfuscated successfully. ')

                input(Fore.RED + "Press to continue")
                
            
            
            if 'use 3' in user_input:
                print('Running program, please wait...')

                subprocess.call('cls', shell=True)
                banner2 = pyfiglet.figlet_format('Obfile')
                print(banner2)

                print(Fore.WHITE + '--------------------------------------------------------') 
                print(Fore.RED +   'ObFile Obfuscator and Compiler')
                print(Fore.WHITE + '--------------------------------------------------------') 
                print(Fore.RED +   'You can obfuscate your python file and also compile it to exe with this tool')
                print(Fore.RED +   'You can also add icons to your file (only .ico files are allowed)')
                print(Fore.RED +   'Make sure to enter the correct file path and icon path')
                print(Fore.WHITE + '--------------------------------------------------------') 
                input(Fore.RED +   "Press to Continue >>") 
                                       
                             
                com_dir = input(Fore.RED + '\n [=] Enter File directory >>')
                print(Fore.WHITE + f'\n\t File directory >> {com_dir}')
                icon_option = input(Fore.RED + 'Do you want to add icon to your file??'
                    '\n' 'Type yes or no >> ')
                if 'yes' in icon_option:
                    print(Fore.YELLOW + 'The file will be compiled with a custom user choice icon')
                    icon_dir = input(Fore.RED + '\n [=] Enter icon directory >>')
                    print(Fore.WHITE + f'\n\t Icon Directory >> {icon_dir}')
                    print(Fore.YELLOW + "Processing.....")

                    print(Fore.YELLOW + "Process started")
                    subprocess.call(f'pyarmor pack -e "--onefile --noconsole --icon {icon_dir}" {com_dir}', shell=True )
                    print(Fore.RED + 'Processing done.....')
                    messagebox.showinfo('ObFile', 'The file has been Processed successfully. ')
                    input(Fore.RED + "Press to continue")

                    #os.system("Msgbox\msgbox3.vbs")

                if 'no' in icon_option:
                    print(Fore.YELLOW + "\n\nThe file will compile without icon")
                   # com_dir1 = input(Fore.RED + "\n [=] enter file directory >>")
                    print(Fore.WHITE + f'\n\t File directory >> {com_dir}')
                    print(Fore.YELLOW + 'Processing.....')
                    subprocess.call(f'pyarmor pack -e " --onefile --noconsole" {com_dir}', shell=True)
                    print(Fore.RED + "Processed.....")
                    messagebox.showinfo('ObFile', 'The file has been Processed successfully. ')
                    input(Fore.RED + "Press to continue")

                    #os.system("Msgbox\msgbox3.vbs")

                
             
               

            if 'use 4' in user_input:
                subprocess.call('HELP.txt', shell=True)
            
            if 'use 5' in user_input:
                print("Quitting")

                sys.exit(2)
            
            else:
                input(Fore.CYAN + 'Press enter to continue')
                subprocess.call('cls', shell=True) 
    user_choice_menu()






#os.system(f'pyarmor obfuscate {directory}')
#os.system(f'pyinstaller -F -i "{icon}" {directory}')
