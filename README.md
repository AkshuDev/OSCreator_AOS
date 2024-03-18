OS Creator (Under Development)
Made By - Pheonix Community



This is an OS creator project developed using Python. It is still under development and requires the following dependencies:

tarfile: Used for handling tar files.
lzma: Required for LZMA compression and decompression.
pyvmomi: Provides Python bindings for the VMware vSphere API.
configparser: Used for parsing configuration files.
pyvbox: Python API for interacting with Oracle VM VirtualBox.
vboxapi: API for VirtualBox automation.
virtualbox: Virtualization software required for using the API.
datetime: Provides classes for manipulating dates and times.
Setup Instructions
1. Installing VirtualBox and vboxapi
Go to VirtualBox Downloads and download VirtualBox for your operating system.
After installing VirtualBox, navigate to the VirtualBox installation folder.
Inside the VirtualBox folder, locate the sdk folder.
Open a command prompt (cmd) in the sdk folder.
Run the following command to install the vboxapi package:


python vboxapisetup.py install


2. Installing Other Dependencies
To install the other required Python modules (except virtualbox related modules), you can run the Dependency.py file provided in this repository. Make sure you have Python installed on your system.


python Dependency.py


This command will install the necessary Python dependencies using pip.

Usage
Once you have all the dependencies installed, you can start using the OS Creator project. Follow the instructions provided in the project documentation or source code to create and manage your custom operating systems.

Notes
This project is currently under development and may have incomplete features or bugs.
Make sure to check the official documentation of each dependency for detailed usage and troubleshooting information.
Feel free to contribute to this project or report any issues by creating a pull request or raising an issue on GitHub.

Happy coding! 😊🚀
