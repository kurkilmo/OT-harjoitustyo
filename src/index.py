from tkinter import Tk # pylint: disable=import-error
from ui.ui import UI # pylint: disable=import-error


def main():
    window = Tk()
    window.title("Metadata Editor")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
