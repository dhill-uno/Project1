from gui import *


def main():
    """
    A window size of 250 length, and 180 height
    the window is not resizable
    """
    window = Tk()
    window.title('Project 1')
    window.geometry('250x180')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
