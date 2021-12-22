from tkinter import Tk, constants, ttk, StringVar, filedialog, Canvas, Scrollbar # pylint: disable=import-error
from services.metadata_tool import MetadataTool # pylint: disable=import-error
from services.metadata_info import MetadataInfo # pylint: disable=import-error

class UI:
    def __init__(self, root):
        """Create a new UI class

        Args:
            root (Tk): Tkinter root for the interface
        """

        self._root = root
        self.metadatatool = MetadataTool()
        self.metadatainfo = MetadataInfo()
        self.filename = StringVar()
        self.metadata = None
        self.metadata_list = None
        self.edited_metadata = {}

    def start(self):
        """Start the interface
        """

        top_bar = ttk.Frame(
            master=self._root
        )

        import_button = ttk.Button(
            master=top_bar,
            text="Open file",
            command=self._open_file
        )

        save_button = ttk.Button(
            master=top_bar,
            text="Save edited metadata",
            command=self._save_metadata
        )

        file_label = ttk.Label(
            master=top_bar,
            textvariable=self.filename
        )

        canvas = Canvas(
            master=self._root,
            width=500,
            height=500
        )

        self.metadata_list = ttk.Frame(
            master=canvas
        )

        scrollbar = Scrollbar(
            master=self._root,
            orient="vertical",
            command=canvas.yview
        )
        canvas.configure(yscrollcommand=scrollbar.set)

        top_bar.pack()
        scrollbar.pack(
            side="right",
            fill="y"
        )
        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )
        canvas.create_window((4,4), window=self.metadata_list, anchor="nw")
        self.metadata_list.bind(
            "<Configure>",
            lambda event,
            canv=canvas: canv.configure(scrollregion=canv.bbox("all"))
        )

        import_button.grid(row=1, column=0)
        save_button.grid(row=1, column=2)
        file_label.grid(row=0, column=0, columnspan=3)
        self._open_file()

    def _open_file(self):
        """Open a file dialog for selecting a file to edit
        """

        self.filename.set(filedialog.askopenfilename())
        self.metadata = self.metadatatool.get_metadata(self.filename.get())
        self.display_metadata()

    def display_metadata(self):
        """Display selected file's metadata
        """

        for widget in self.metadata_list.winfo_children():
            widget.destroy()

        line = 0

        for key, item in self.metadata.items():
            if not self.metadatainfo.check_writable(key):
                continue

            self.edited_metadata[key] = StringVar()
            self.edited_metadata[key].set(item)

            mtd_label = ttk.Label(
                master=self.metadata_list,
                text=key
            )

            mtd_entry = ttk.Entry(
                master=self.metadata_list,
                textvariable=self.edited_metadata[key],
                width=700
            )

            mtd_entry.config(background="green")
            mtd_label.grid(row=line, column=0, sticky=constants.W)
            mtd_entry.grid(row=line, column=1, sticky=constants.E)
            line += 1

    def _save_metadata(self):
        """Save changed metadata to original file
        """

        completed = 0
        failed = 0

        for key, item in self.edited_metadata.items():
            item = item.get()

            if self.metadata[key] != item:
                success = self.metadatatool.set_metadata(
                    self.filename.get(),
                    key,
                    item
                )
                if success:
                    completed += 1
                    self.metadata[key] = item
                else:
                    failed += 1


        win = Tk()
        message = f'{completed} entries changed\n{failed} entries failed'
        ok_button = ttk.Button(
            master=win,
            text="OK",
            command=win.destroy
        )
        message_label = ttk.Label(
            master=win,
            text=message
        )
        message_label.pack()
        ok_button.pack()
        win.mainloop()
