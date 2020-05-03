# Companion Prog by AfreAustin
# Created for Hack at Home 02-03/5/2020
# For easy reference of Python v3 syntax

from tkinter import *
import os

def main():
    root = Tk()
    root.geometry("600x600")
    
    app = Application(root)
    app.configure(bg = '#94d58b')
    
    root.mainloop()

# GUI Interface
class Application(Frame):

    # main window / master widget
    def __init__(self, master = None):              # master = None is default
        Frame.__init__(self, master)

        self.master = master
        
        self.pack()
        self.init_window()
        self.create_labels()
        self.library()

    # creates main frame
    def init_window(self):

        self.master.title(" (◉)ᨎ(◉) Companion Prog ")
        self.pack(fill = BOTH, expand = 1)

       # Menu
        dropdown = Menu(self.master)
        self.master.config(menu = dropdown)

            # File Menu
        file = Menu(dropdown)
        file.add_command(label = "Exit",
                         command = self.master.destroy)
        dropdown.add_cascade(label = 'File', menu = file)

    # adds labels
    def create_labels(self):
        
        # Title
        title = Label(self, text = "(◉)ᨎ(◉)    COMPANION PROG       ",
                     bg = '#9be491', relief = RAISED)
        title.config( font = ('CopperplateGothicLight', '25', 'bold') )
        title.pack(anchor = 'n')

        # Exit Button
        exitButton = Button(self, text = " EXIT ", 
                            bg = '#f44040', fg = 'black',
                            command = self.master.destroy )
        exitButton.place(x = 548, y = 50)

        # Credits
        credits = Label(self, text = ("_" * 115) + "\n created by AfreAustin",
                      bg = '#94d58b')
        credits.place(x = 10, y = 550)
      
     # creates library
    def library(self):
        
        # Library List Menu
        lib_items = [ "Input / Output",
                      "Variables",
                      "Math Operations",
                      "If/Elif/Else",
                      "Loops",
                      "Sequences",
                      "Error Handling",
                      "File Handling", 
                      "---------"]

        library = Listbox(self, bg = '#E4FAD0', 
                          height = 20)
        library.place(x = 10, y = 50)
        for items in lib_items:
            library.insert(END, items)
        
        # Library Content Display
        lib_inout = ''' # \'\'\' Multiline/Block Comments \'\'\' are text literals  \n
                    \n an_input = input('  Enter input: ')      # stored as string 
                    \n print ("  ", an_input) 
                    '''
        lib_vars  = ''' # not typecast
                    \n # cannot have Python key words or spaces, or starts with digits
                    \n
                    \n string = "Variables  :"
                    \n integer = 1
                    \n a_float = 2.3
                    \n var_1, var_2 = 7, 8
                    \n
                    \n # Conversions
                    \n conv_to_string = str(integer)
                    \n conv_to_integer = int(a_float)
                    \n conv_to_float = float(integer) 
                    '''
        lib_math  = ''' addition = 1 + 2
                    \n subtraction = 3 - 4 
                    \n multiplication = 5 * 6
                    \n division_float = 7 / 8     # returns float
                    \n division_floor = 7 // 8   # returns integer
                    \n modulus = 9 % 10          # returns remainder
                    \n power = 2 ** 3
                    \n exponential = 4.5e6
                    '''
        lib_ifels = ''' # Decision / Selection Control Structure
                    \n # can be nested infinitely
                    \n int_1, int_2 = 2 , 3
                    \n
                    \n if int_1 != int_2 and int_2 != int_1 or int_1 == int_2:
                    \n # and = both true , or = one true
                    \n print (" ", int_1, " is not equal to ", int_2)
                    \n
                    \n if int_1 < int_2:         # <= includes 2nd
                    \n print (" ", int_1, " is less than ", int_2)
                    \n elif int_1 > int_2:     # >= includes 2nd
                    \n print (" ", int_1, " is more than ", int_2)
                    \n else:                         # == is equal to
                    \n print (" ", int_1, " is equal to ", int_2)
                    '''
        lib_loops = ''' # Iterative Structure
                    \n
                    \n # While Loop
                    \n condition = 0
                    \n while condition != 3:
                    \n    condition += 1
                    \n    print(" ", condition)

                    \n # For Loop
                    \n for condition in range(1):
                        print("In Progress")    # Set 09 Slide 29'''
        lib_sqnce = ''' # Lists     need: tuples, dictionaries
                    \n a_list = ["string "]            # [] * n = prints lists n times
                    \n b_list = [1, 2, 3, 4]
    
                    \n a_list[0] = "index"             # changes value at index [n]
                    \n b_list.append(5)                # adds (item) to list
                    \n b_list.index(5)                 # checks what index (item) is
                    \n del b_list[4]                   # deletes [index] in list
    
                    \n _list  = a_list + b_list        # + here is called concatenation operator
                    \n if "index" in _list:            # in = checks if in list
                    \n    print(" ", _list)            # print(*a_list, sep = " " ) # = print without []
                    \n    print("  Length: ", len(_list) )'''
        lib_errh  = ''' lib_label.configure(text = lib_errh)
                    \n # Executed Code
                    \n # Errors
                    \n # syntax, runtime, and logic
                    \n
                    \n # try/except block
                    \n try:
                    \n    number = float(input("\n Enter only a number: "))
                    \n    print("  ", number)
                    \n except ValueError:
                    \n    print("  Error: Must be a number! ")      # need: raise, more error types
                    '''
        lib_files = ''' # opens/creates file for writing
                    \n file = open("example file.txt", "w")    # "a" = appends instead of overwrites
                    \n file.write(" This is the example file for File")
                    \n file.close()
                    \n 
                    \n # opens file for reading
                    \n file = open("example file.txt", "r")
                    \n file_contents = file.read()
                    \n print(file_contents)
                    \n file.close()'''

            # Title
        def get_title(event):
            # get selected line index
            index = library.curselection()
            # get the line's text
            seltext = library.get(index)
            # show selected text in label
            lib_title.configure(text = seltext)

        lib_title = Label(self, text = " Select a Category ",
                          justify = CENTER,
                          relief = GROOVE, width = 50)
        lib_title.place(x = 150, y = 50)
        library.bind('<<ListboxSelect>>', get_title)
        
            # Contents
        def get_contents(event):
            # get selected line index
            index = library.curselection()
            # get the line's text
            seltext = library.get(index)
            
            if seltext == "Input / Output":
                lib_label.configure(text = lib_inout)
                # Executed Code
                an_input = input("  Enter input: ")
                print ("  ", an_input)
            elif seltext == "Variables":
                lib_label.configure(text = lib_vars)
                # Executed Code
                string   = "Variables  :"
                integer  = 1
                a_float  = 2.3
                var_1, var_2 = 7, 8

                print ("\n ", string, integer, a_float, var_1, var_2 )

                # Conversions
                conv_to_string  = str(integer)
                conv_to_integer = int(a_float)
                conv_to_float = float(integer)

                print ("\n  Conversions:", conv_to_string, conv_to_integer, conv_to_float)
            elif seltext == "Math Operations":
                lib_label.configure(text = lib_math)
                # Executed Code
                addition       = 1 + 2
                subtraction    = 3 - 4 
                multiplication = 5 * 6
                division_float = 7 / 8    # returns float
                division_floor = 7 // 8   # returns integer
                modulus        = 9 % 10   # returns remainder
                power          = 2 ** 3
                lg_float = 4.5e6

                print ("\n  Operations: ", addition, subtraction, 
                       multiplication, division_float, division_floor, 
                       modulus, power)
            elif seltext == "If/Elif/Else":
                lib_label.configure(text = lib_ifels)
                # Executed Code
                int_1, int_2 = 2 , 3

                if int_1 != int_2 and int_2 != int_1 or int_1 == int_2:
                    # and = both true , or = one true
                    print (" ", int_1, " is not equal to ", int_2)
        
                    if int_1 < int_2:       # <= includes 2nd
                        print (" ", int_1, " is less than ", int_2)
                    elif int_1 > int_2:     # >= includes 2nd
                        print (" ", int_1, " is more than ", int_2)
                    else:                   # == is equal to
                        print (" ", int_1, " is equal to ", int_2)
            elif seltext == "Loops":
                lib_label.configure(text = lib_loops)
                # Executed Code
                # Iterative Structure

                # While Loop
                condition = 0
                while condition != 3:
                    condition += 1
                    print(" ", condition)

                # For Loop
                for condition in range(1):
                    print("In Progress")    # Set 09 Slide 29
            elif seltext == "Sequences":
                lib_label.configure(text = lib_sqnce)
                # Executed Code
                # Lists     need: tuples, dictionaries
                a_list = ["string "]            # [] * n = prints lists n times
                b_list = [1, 2, 3, 4]
    
                a_list[0] = "index"             # changes value at index [n]
                b_list.append(5)                # adds (item) to list
                b_list.index(5)                 # checks what index (item) is
                del b_list[4]                   # deletes [index] in list
    
                _list  = a_list + b_list        # + here is called concatenation operator
                if "index" in _list:            # in = checks if in list
                    print(" ", _list)            # print(*a_list, sep = " " ) # = print without []
                    print("  Length: ", len(_list) )
            elif seltext == "Error Handling":
                lib_label.configure(text = lib_errh)
                # Executed Code
                # Errors
                # syntax, runtime, and logic

                # try/except block
                try:
                    number = float(input("\n Enter only a number: "))
                    print("  ", number)
                except ValueError:
                    print("  Error: Must be a number! ")      # need: raise, more error types
            elif seltext == "File Handling":
                lib_label.configure(text = lib_files)
                # Executed Code
                # opens/creates file for writing
                file = open("example file.txt", "w")    # "a" = appends instead of overwrites
                file.write(" This is the example file for File")
                file.close()

                # opens file for reading
                file = open("example file.txt", "r")
                file_contents = file.read()
                print(file_contents)
                file.close()
            else:
                lib_label.configure(text = "Coming Soon")
        
        lib_label = Label(self, text = "",
                          justify = LEFT, pady = 0.2,
                          width = 50, relief = RAISED)
        lib_label.place(x = 150, y = 80)
        library.bind('<ButtonRelease-1>', get_contents)

main()
