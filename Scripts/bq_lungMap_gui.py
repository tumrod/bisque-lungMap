import Tkinter
import Tkinter.filedialog
import getpass
# Need this for the `os.path.split` function
import os
gui = Tkinter.Tk()
user = getpass.getuser()
def click():
    # Get the file
    file = Tkinter.filedialog.askopenfilename(initialdir='C:/Users/%s' % user)
    # Split the filepath to get the directory
    directory = os.path.split(file)[0]
    print(directory)
button = Tkinter.Button(gui, command=click)
button.grid()
gui.mainloop()