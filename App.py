# Import the Tkinter library for GUI development
import tkinter as tk
# If you're using Python 2, you would import it as:
# import Tkinter as tk
# Create the main application window
root = tk.Tk()
# Additional libraries can be imported as needed for your specific project
# For example, if you plan to work with dropdown menu options, you might import tkinter.ttk
# import tkinter.ttk as ttk

# Create the main application window
root = tk.Tk()
# Set the window title
root.title("Dropdown Menu Example")
# Set the window dimensions (width x height)
root.geometry("400x300")
# You can also specify a minimum window size (optional)
root.minsize(300, 200)
# You can specify a maximum window size (optional)
root.maxsize(800, 600)
# Create a StringVar to hold the selected option
selected_option = tk.StringVar()
# Create the dropdown menu
dropdown = tk.OptionMenu(root, selected_option, "Option 1", "Option 2", "Option 3", "Option 4")
dropdown.pack()
# Run the main event loop
root.mainloop()