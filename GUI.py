import tkinter.filedialog
import tkinter as tk
from tkinter import ttk


def StartApplication():
    master = tk.Tk()
    master.title("Test")

    # using x button actually ends program instead of just closing window
    master.protocol("WM_DELETE_WINDOW", master.quit())

    # place window in middle of screen according to upper left point of window
    window_width = 1280
    window_height = 720
    screen_width = master.winfo_screenwidth()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = 30

    master.geometry("{}x{}+{}+{}".format(window_width,
                                         window_height,
                                         x_coordinate,
                                         y_coordinate))

    # a non-zero weight causes a row or column to grow if there's extra space
    # https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
    master.grid_columnconfigure(1, weight=1)

    MainApplication(master)

    master.mainloop()


class MainApplication():
    def __init__(self, master):
        self.master = master

        menu_bar = MenuBar(self.master)

        widgets = Widgets(self.master)
        notebook = Notebook(self.master)

        options = Options(self.master)


class MenuBar:
    def __init__(self, master):
        self.master = master

        menu_bar = tk.Menu(self.master)


        bar_file = tk.Menu(menu_bar,
                           tearoff=False)
        bar_file.add_command(label="Open",
                             command=self.file_open)
        bar_file.add_separator()
        bar_file.add_command(label="Exit",
                             command=lambda : self.master.quit())
        menu_bar.add_cascade(label="File",
                             menu=bar_file)

        bar_about = tk.Menu(menu_bar,
                            tearoff=False)
        bar_about.add_command(label="Info",
                              command=self.about_info)
        menu_bar.add_cascade(label="About",
                             menu=bar_about)

        self.master.config(menu=menu_bar)

    def file_open(self):
        file_path = tk.filedialog.askopenfilename(title="Select file")
        # add this to only show certain file types
        # filetypes=[("Text", "*.txt")]

        print(file_path + " opened")

    def about_info(self):
        window_about = make_toplevel(self.master,
                                     "About",
                                     [480, 640])

        lines = "aaa " * 1000

        scrollbar = tk.Scrollbar(window_about,
                                 orient=tk.VERTICAL)

        text = tk.Text(window_about,
                       wrap=tk.WORD,
                       yscrollcommand=scrollbar.set,
                       font=("TKDefault", 10))
        text.insert(tk.END,
                    lines)
        text.config(state=tk.DISABLED)

        scrollbar.pack(side=tk.RIGHT,
                       fill=tk.Y)
        text.pack(side=tk.LEFT,
                  fill=tk.Y)

        scrollbar.config(command=text.yview)



class Widgets:
    def __init__(self, master):
        self.master = master

        frame_widgets = tk.Frame(self.master)
        frame_widgets.grid(row=0,
                           column=0,
                           sticky=tk.NSEW,
                           padx=5,
                           pady=5)

        labelframe_options = tk.LabelFrame(frame_widgets,
                                           text="Widgets",
                                           relief="ridge",
                                           padx=5,
                                           pady=5,
                                           font="bold")
        labelframe_options.pack(fill=tk.BOTH,
                                expand=True)

        # Label
        self.label_combobox = tk.Label(labelframe_options,
                                       text="Label")
        self.label_combobox.grid(row=0,
                                 column=0,
                                 columnspan=3,
                                 sticky=tk.W)

        # Combobox
        values = ["Combobox Option " + str(idx+1) for idx in range(5)]
        self.combobox_t = ttk.Combobox(labelframe_options,
                                       values=values)
        self.combobox_t.set(values[0])
        self.combobox_t.bind("<<ComboboxSelected>>",
                             self.command_combobox)
        self.combobox_t.grid(row=1,
                             column=0,
                             columnspan=3,
                             sticky=tk.NSEW,
                             padx=5,
                             pady=(0,5)) # pads the top 0 and the bottom 5

        # Button
        # also showing how widgets can be created in a loop
        self.buttons = []
        for idx in range(3):
            button = tk.Button(labelframe_options,
                               text="Button " + str(idx+1),
                               command=lambda idx=idx : self.command_button(idx)) # https://www.geeksforgeeks.org/how-to-check-which-button-was-clicked-in-tkinter/
            button.grid(row=2,
                        column=idx,
                        sticky=tk.NSEW,
                        padx=2,
                        pady=2)
            self.buttons.append(button)

        # Checkbox
        checkbox_variable = tk.IntVar(value=0)
        checkbox_t = tk.Checkbutton(labelframe_options,
                                    text="Checkbox",
                                    variable=checkbox_variable,
                                    command=lambda : self.command_checkbox(checkbox_variable))
        checkbox_t.grid(row=3,
                        column=0,
                        columnspan=3,
                        sticky=tk.W,
                        padx=2,
                        pady=2)

        # Radiobutton
        titles = ["Radiobutton 1",
                 "Radiobutton 2",
                 "Radiobutton 3"]
        variable = tk.IntVar()
        radiobutton_start_row = 4
        for idx, title in enumerate(titles):
            value = tk.IntVar(value=idx+1)
            radiobutton_t = ttk.Radiobutton(labelframe_options,
                                            text=title,
                                            variable=variable,
                                            value=value,
                                            command=lambda value=value : self.command_radiobutton(value))

            radiobutton_t.grid(row=radiobutton_start_row + idx,
                               column=0,
                               columnspan=3,
                               sticky=tk.W,
                               padx=2,
                               pady=2)

    def command_combobox(self, event): # event is needed but unused
        print(self.combobox_t.get() + " clicked")

    def command_button(self, button_num):
        print(self.buttons[button_num].cget("text") + " clicked")

    def command_checkbox(self, variable):
        if variable.get() == 1:
            print("Checkbox Checked")
        elif variable.get() == 0:
            print("Checkbox Unchecked")

    def command_radiobutton(self, variable):
        print("Radiobutton " + str(variable.get()) + " clicked")


class Notebook:
    def __init__(self, master):
        self.master = master

        frame_notebook = tk.Frame(self.master)
        frame_notebook.grid(row=0,
                            column=1,
                            sticky=tk.NSEW,
                            padx=5,
                            pady=5)

        notebook = ttk.Notebook(frame_notebook)
        notebook.pack(fill=tk.BOTH, expand=True)

        tab_1 = tk.Frame(notebook)
        tab_2 = tk.Frame(notebook)

        tab_1.pack(fill=tk.BOTH, expand=True)
        tab_2.pack(fill=tk.BOTH, expand=True)

        tab_1 = self.make_tab1(tab_1)
        tab_2 = self.make_tab2(tab_2)

        notebook.add(tab_1, text="Tab 1")
        notebook.add(tab_2, text="Tab 2")

    def make_tab1(self, tab_1):
        # Label
        label_t = tk.Label(tab_1,
                           text="Entry ")
        label_t.grid(row=0,
                     column=0,
                     sticky=tk.W,
                     padx=(5,0),
                     pady=5)


        label_t = tk.Label(tab_1,
                           text="Password ")
        label_t.grid(row=1,
                     column=0,
                     sticky=tk.W,
                     padx=(5,0),
                     pady=5)

        # Entry
        self.entry_username = tk.Entry(tab_1,
                                       textvariable=tk.StringVar(value=""),
                                       width=50)
        self.entry_username.grid(row=0,
                                 column=1,
                                 padx=5,
                                 pady=5)

        self.entry_password = tk.Entry(tab_1,
                                       textvariable=tk.StringVar(value=""),
                                       width=50)
        self.entry_password.grid(row=1,
                                 column=1,
                                 padx=5,
                                 pady=5)

        # Button - approve Entry
        button = tk.Button(tab_1,
                           text="Enter",
                           command=self.command_button)
        button.grid(row=2,
                    column=1,
                    sticky=tk.W,
                    padx=2,
                    pady=2)


        return tab_1

    def command_button(self):
        print("Info\n"
              + "\tUsername : " + self.entry_username.get() + "\n"
              + "\tPassword : " + self.entry_password.get())
        pass

    def make_tab2(self, tab_2):
        return tab_2

class Options:
    def __init__(self, master):
        self.master = master

        frame_options = tk.Frame(self.master)
        frame_options.grid(row=1,
                           column=0,
                           sticky=tk.NSEW,
                           padx=5,
                           pady=5)

        labelframe_options = tk.LabelFrame(frame_options,
                                           text="Options",
                                           relief="ridge",
                                           padx=5,
                                           pady=5,
                                           font="bold")
        labelframe_options.pack(fill=tk.BOTH,
                                expand=True)

        button_t = tk.Button(labelframe_options,
                             text="Options Test")
        button_t.grid(row=0,
                      column=0,
                      sticky=tk.NSEW)



# makes a toplevel window in center of master window with given title and height
def make_toplevel(master, title, dimensions):
    toplevel_window = tk.Toplevel(master)
    toplevel_window.title(title)

    pos_x = (master.winfo_width() - dimensions[0]) // 2 + master.winfo_x()
    pos_y = (master.winfo_height() - dimensions[1]) // 2 + master.winfo_y()

    toplevel_window.geometry("{}x{}+{}+{}".format(dimensions[0],
                                                  dimensions[1],
                                                  pos_x,
                                                  pos_y))

    return toplevel_window