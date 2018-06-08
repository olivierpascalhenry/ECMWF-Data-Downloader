=============
Installation
=============
The latest version of ECMWF Data Downloader (EDD) can be obtained from https://github.com/olivierpascalhenry/ECMWF-Data-Downloader. EDD comes in three different versions:

* Sources
* A stand-alone package for Windows (https://github.com/olivierpascalhenry/ECMWF-Data-Downloader/releases, .msi package)
* A stand-alone package for Linux (https://github.com/olivierpascalhenry/ECMWF-Data-Downloader/releases, .tar.gz package)


*******
Sources
*******
Use of EDD from sources requires the following packages:

* Python 3.5.4 or newer. Available at https://www.python.org/
* PyQt5 5.10 or newer. Available at https://www.riverbankcomputing.com/software/pyqt/download5
* hurry.filesize 0.9 or newer. Available at https://pypi.org/project/hurry.filesize/
* requests 2.18 or newer. Available at https://pypi.org/project/requests/
* selenium v3.11 or newer. Available at https://pypi.org/project/selenium/. Not mandatory to run EDD. Only to build a part of the database.

Then, to launch the software, download sources, uncompress the package, navigate into the new directory and run the following command (Windows)::

   PS User> python ecmwf_data_downloader.py
   
Or (Linux)::

    & python ecmwf_data_downloader.py

    
***************************************
Installation of the stand-alone package
***************************************

-----------
For Windows
-----------

The installation of the package for Windows is really simple. Just donwload the .msi file from its repository on GitHub, double click on it to launch the installation and follow the instructions on screen. Once the installation is done, you can launch the software from its icon on Windows desktop, or from its folder in Windows start menu.

To avoid issues with admin rights, EDD should be installed outside of Program Files folder: two files are created when it is launched for the first times, *ecmwf_downloader.ini* which contains all options (by default) of the software, and *ecmwf_downloader_log.out* which contains all log messages of the software. Installing EDD in Program Files could lead to the rejection of the creation of both files.


---------
For Linux
---------

The installation of the package for Linux is also really simple. Just donwload the .tar.gz file from its repository on GitHub, uncompress it somewhere in your HOME folder, navigate to the new folder and launch the executable by double-clicking on it or from the terminal.


*******
Options
*******
A file is creating when the software is executed for the first time. This file, called *ecmwf_downloader.ini* contains the different options of the software. It is possible to modify those options in a dedicated window, detailed in the following chapter. Here is a list of those options:

* *level*: the logging level (``DEBUG``, ``INFO``, ``WARNING``, ``CRITICAL``, ``ERROR``). In beta version, by default it is set on ``DEBUG``. In final version, it will be set on ``INFO``. It can be changed by the user from the Options window.
* *path*: where the logging file should be saved. For those who want to keep all their logging file at the same place. By default the option is empy, which means the logging file is created in the software folder. It can be changed by the user from the Options window. If the path doesn't exist, an error message is added to the log file and the path is reseted to the default path.
* *check_update*: when on ``TRUE``, the software will check automatically for an update at each startup. ``TRUE`` by default, it can be change by the user from the Options window.
* *language*: set on english actually. Probably used in a future version, once translations are available. It can't be changed by the user at this time.
* *display_api_info*: when on ``TRUE``, a window will be displayed at startup to give information about the ECMWF web API. ``TRUE`` by default, it can be change by the user from the Options window.
* *email*: the email registered in the ECMWF account. It is only used when using the ECMWF web API. It can be changed by the user from the Options window.
* *url*: the url of the ECMWF web API. By default it is alreay embedded in the software. It can be changed by the user from the Options window.
* *key*: the key provided by the user ECMWF account. Mandatory to connect to the ECMWF web API. It can be changed by the user from the Options window.
* *folder*: where files are stored once downloaded. It can be changed by the user from the Options window.  EDD check the path at each startup. If the path doesn't exist, an error message is added to the log file and displayed to the user, and the path is reseted to the default path.


***
Log
***
A logging system is available in EDD. By default, the output file is available in the directory of EDD and the logging level has been set to DEBUG until a final release. Both options for logging level and logging location have been set in a config file, those options can be changed by the user in the Options window.

If issues are noticed, the logging file should be attached to the message when reporting the issue.


******
Update
******
An automatic update system is available for EDD, when installed from stand-alone packages. Once an update is available for EDD, the Update icon is enabled. If the user click on it, a warning window about the availability of an update will be displayed, asking him to click on **Update** to start the automatic update procedure.

With sources, the same icon informs about an update and proposes to the user to download the update. Then it is up to the user to install the update or not. 

The checking of an update can be disabled in the Options window.
