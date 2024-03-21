import os
import sys
import PyQt5 as pyqt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from ctypes import *
from GUI import *
import GUI.OSCgui as oscgui
import LIB

WinDLL("Shell32").SetCurrentProcessExplicitAppUserModelID(LIB.OSCreatorID)

LIBW = LIB.Win

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About @ OSCreator")
        self.setGeometry(100, 100, 1000, 1500)
        self.setWindowIcon(QIcon("OSCreator/Assets/PheonixStudios.png"))
        self.setStyleSheet('background-color: white;color:black')
        content = """OSCreator, short for Operating System Creator,
is a software application designed to facilitate the creation and development of custom
operating systems.
It provides users with a graphical user interface (GUI) to streamline the process of
building an OS from scratch or modifying existing ones.
Here are some key features and components typically found in an OSCreator application:

Graphical User Interface (GUI): OSCreator offers an intuitive interface that allows
users to interact with various tools and functionalities using buttons,
menus, and other visual elements.

Project Management: Users can create, open, save, and manage OS projects within the
OSCreator environment.
This includes organizing files, configuring settings, and tracking project progress.

Customization Tools: OSCreator provides a range of customization options for designing
and configuring different aspects of the operating system,
such as the user interface, system settings, drivers, and installed applications.

Code Editor: For advanced users and developers, OSCreator may include a built-in code
editor with syntax highlighting, code completion,
and other features to facilitate writing and editing system code, scripts, and
configurations.

Resource Management: OSCreator helps manage system resources such as memory, storage,
and CPU usage,
ensuring optimal performance and stability of the operating system.

Testing and Debugging: The application may include tools for testing, debugging, and
troubleshooting operating system components, allowing users to identify and fix
errors and issues efficiently.

Documentation and Tutorials: OSCreator often provides comprehensive documentation,
tutorials, and guides to assist users in understanding the OS development process,
learning new concepts, and troubleshooting common problems.

Community Support: Users can access online forums, communities, and support
channels to seek help, share ideas, collaborate with others, and stay updated
on the latest developments in OS creation and customization.

Overall, OSCreator empowers users, from hobbyists to experienced developers, to
create unique and tailored operating systems suited to their specific requirements,
preferences, and objectives. Whether for educational purposes, research projects,
or commercial ventures, OSCreator serves as a versatile platform for exploring and
experimenting with operating system development."""
        self.label = QLabel(content, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.bold()
        self.label.setFont(font)

class OS_Creator_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("OS Creator @ Pheonix Studios")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(LIBW.PSICO))
        self.setStyleSheet('background-color: white;')

        self.label = QLabel('Welcome to OS Creator', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet('color: black;')
        self.label.adjustSize()

        self.aboutB = QPushButton("About", self)
        self.aboutB.move(150, 100)
        self.aboutB.setStyleSheet('QPushButton{color: gray; border: 2px solid gray;} QPushButton:hover{background-color:#ececec;color:black;border-color: black;}')
        self.aboutB.setFont(QFont('Arial', 20))
        self.aboutB.clicked.connect(self.display_about)

        self.button = QPushButton("New OS", self)
        self.button.move(150, 150)
        self.button.setStyleSheet('QPushButton{color: gray; border: 2px solid gray;} QPushButton:hover{background-color:#ececec;color:black;border-color: black;}')
        self.button.setFont(QFont('Arial', 20))
        self.button.clicked.connect(self.create_os)

        self.seperator = QFrame(self)
        self.seperator.setFrameShape(QFrame.VLine)
        self.seperator.setStyleSheet('color: black')

        self.read_projects()
        print("reading done!")
        self.add_OS_labels()
        print("adding done!")

        font = QFont()
        font.bold()
        font.setPointSize(40)
        self.label.setFont(font)

        self.center()
        print("__init__ completed!")

    def center(self):
        screen_geometry = QApplication.desktop().screenGeometry()
        window_width = int(screen_geometry.width() * 0.8)
        window_height = int(screen_geometry.height() * 0.8)
        center_point = screen_geometry.center()
        self.setGeometry(0, 0, window_width, window_height)

        button_width = 300
        button_height = 100
        button_x = (window_width - button_width) // 2
        button_y = window_height - 150  # Adjust the vertical position of the button
        self.button.setGeometry(button_x, button_y, button_width, button_height)

        button_y = window_height - 300
        self.aboutB.setGeometry(button_x, button_y, button_width, button_height)

        label_y = 100  # Adjust the vertical position of the label
        self.label.setGeometry(0, label_y, self.width(), 80)  # Set the label's width to cover the entire window

        separator_y = 0  # Adjust the vertical position of the separator
        separator_height = window_height - separator_y
        separator_x = 300
        self.seperator.setGeometry(separator_x, separator_y, 2, separator_height)  # Adjust the separator's geometry

        self.move(center_point.x() - self.width() // 2, center_point.y() - self.height() // 2)

    def read_projects(self):
        abs_path = os.path.abspath(LIBW.Projects)
        print(f"Reading... [{abs_path}]")
        try:
            with open(abs_path, "r") as file:
                print("READ STEP 1A-PSS:")
                projects = file.readlines()
                print(projects)
                self.os_names = projects
                print(self.os_names)
        except Exception:
            try:
                with open(abs_path, "w") as file:
                    file.close()
                self.os_names = []
            except Exception:
                raise Exception(f"Sorry no folder named [{abs_path}]. Please Create a folder named [old_projects] in the location where this script is located, and restart this script.")
        print(self.os_names)

    def add_OS_labels(self):
        label_height = 100
        label_width = 200
        label_spacing = 100
        max_labels = 5

        font = QFont()
        font.setPointSize(20)

        print("Creating...")

        for i, os_name in enumerate(self.os_names[:max_labels]):
            print("CREATE STEP 1A-PSS:")
            print(os_name)
            label = QLabel(os_name, self)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("color: black;")
            label.setFont(QFont('Arial', 16))
            label.setGeometry(5, 50 + 20 + 50 + label_height * i + label_spacing * (i + 1), label_width, label_height)
            label.setFont(font)
            print("Label Added:", os_name)

    def clear_view(self):
        for widget in self.findChildren(QWidget):
            widget.deleteLater()

    def name_OS(self):
        name_label = QLabel("Name of OS", self)
        name_label.setStyleSheet("color: black;")
        print("label [__init__] complete")
        font = QFont()
        font.bold()
        font.setPointSize(40)
        name_label.setFont(font)
        print("FONT SET")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setGeometry(0, 100, self.width(), 80)
        self.name = QLineEdit(self)
        self.name.setStyleSheet('QLineEdit{color: gray;background-color: #ececec;border: 2px solid black} QLineEdit:hover{color: black;background-color:gray;border-color:#ececec}')
        self.name.setGeometry(370, 300, int(self.width() / 2), 90)
        font.setPointSize(20)
        self.name.setFont(font)
        self.cancel = QPushButton("Cancel", self)
        self.cancel.setGeometry(370,700,300,100)
        self.cancel.setStyleSheet("QPushButton{color: gray; border: 2px solid gray;} QPushButton:hover{background-color:#ececec;color:black;border-color: black;}")
        self.ok = QPushButton("Ok", self)
        self.ok.setGeometry(870,700,300,100)
        self.ok.setStyleSheet("QPushButton{color: gray; border: 2px solid gray;} QPushButton:hover{background-color:#ececec;color:black;border-color: black;}")
        self.ok.setFont(font)
        self.cancel.setFont(font)
        name_label.show()
        self.ok.show()
        self.cancel.show()
        self.name.show()
        print("SET COMPLETE")


    def create_os(self):
        print("Creating new Project...")
        self.clear_view()
        print("Cleared View!")
        self.name_OS()
        self.cancel.clicked.connect(self.backHOME)
        self.ok.clicked.connect(self.addOS)
        print("OS NAME - []")

    def addOS(self):
        abs_path = LIBW.Projects
        try:
            with open(abs_path, "a") as file:
                file.write(self.name.text()+"\n")
                file.close()
            print("PFILE [written]")
        except Exception:
            try:
                with open(abs_path, "w") as file:
                    file.write(self.name.text()+"\n")
                    file.close()
                print("PFILE [written]")
            except Exception:
                raise Exception(f"Sorry no folder named [{abs_path}]. Please Create a folder named [old_projects] in the location where this script is located, and restart this script.")

        self.clear_view()
        oscG = oscgui.LS(self)
        oscG.show()

    def backHOME(self):
        self.clear_view()
        self.initUI()

    def display_about(self):
        About = AboutDialog()
        About.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ocg = OS_Creator_GUI()
    ocg.show()
    sys.exit(app.exec_())
