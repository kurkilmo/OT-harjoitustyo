from tkinter import Tk, ttk, StringVar, filedialog # pylint: disable=import-error
from services.metadata_tool import MetadataTool # pylint: disable=import-error
from services.metadata_info import MetadataInfo # pylint: disable=import-error

class UI:
    def __init__(self, root):
        self._root = root
        self.metadatatool = MetadataTool()
        self.metadatainfo = MetadataInfo()
        self.filename = StringVar()
        self.metadata = None
        self.metadata_list = None
        self.edited_metadata = {}


    def start(self):
        top_bar = ttk.Frame(
            master=self._root
        )

        self.metadata_list = ttk.Frame(
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

        top_bar.pack()
        self.metadata_list.pack()

        import_button.grid(row=1, column=0)
        save_button.grid(row=1, column=2)
        file_label.grid(row=0, column=1)
        self._open_file()

    def _open_file(self):
        self.filename.set(filedialog.askopenfilename())
        self.metadata = self.metadatatool.get_metadata(self.filename.get())
        self.display_metadata()

    def _detect_edit(self, entry:ttk.Entry, key):
        if self.metadata[key] != self.edited_metadata[key].get():
            entry.config(
                {"background": "Red"}
            )

    def display_metadata(self):
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
                validate="focusout",
                validatecommand=lambda: self._detect_edit(mtd_entry, key)
            )

            mtd_entry.config(background="green")
            mtd_label.grid(row=line, column=0)
            mtd_entry.grid(row=line, column=1)
            line += 1

    def _save_metadata(self):
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
