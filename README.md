Version
-------
ECMWF Data Downloader 0.8.3

!!! NOT SUITED FOR PRODUCTION ENVIRONMENT !!! ONLY FOR TESTING PURPOSES !!!


Project Overview:
-----------------
ECMWF Data Downloader is an open-source tool to help users to download data from the different ECMWF reanalysis datasets, selecting datasets and parameters from the GUI and downloading the data using the official web API.


Compatibility:
--------------
    - sources : linux, windows, macos
    - binaries : linux, windows


Install instructions for binaries:
---------------------------------------
Download and install the last binary file in the Release directory. Actually, the binary file is only compatible with Windows (from Windows 7 32) and Linux (from Ubuntu 14.04). The software should be installed in the Home directory for Linux, and outside the Program Files directory for Windows to avoid issues with Windows admin protections.


Install instructions for sources:
--------------------------------------
Download sources and uncompress them somewhere on your hard drive. Open a terminal in the new directory and launch ECMWF Data Downloader by typing: python ecmwf_data_downloader.py. Do not forget to install dependencies.


External libraries:
-------------------
* PyQt5 v5.10+
* hurry.filesize v0.9+
* requests v2.18+
* selenium v3.11.0+ (only for database creation, not needed to launch ECMWF Data Downloader)
