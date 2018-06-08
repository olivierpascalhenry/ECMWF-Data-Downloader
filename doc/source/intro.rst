=============
Introduction
=============
The ECMWF Data Downloader is a software written in Python 3.5 and PyQt5, and designed with Qt Creator. Its purpose is to download data from ECMWF public datasets using the official Web API.

The idea behind EDD is to have a software with a minimal Graphical User Interface in order to prepare a query for data in all ECMWF public datasets, using the official web API. The idea comes from a discussion I had with my wife, a geophysist, and the use for the first time of the ECMWF web API with Python. Few years ago, it was still possible to use the ECMWF website to download data on a large period of time. Few months ago, I noticed that it was no longer possible: now the user can donwload data only for a month or for a year. That limitation is not present if one uses the official web API. After struggling for a certain amount of time with the web API and the preparation of a simple query, which worked on Linux but failed on Windows, I decided to write a software dedicated to this task, and which could work on Windows and Linux. Even if the software makes use of the official web API, the official ECMWF python library is not used, the query and the download of data rely on a homemade function and on the library ``requests`` to handle HTTPS protocol.

.. NOTE::
  EDD is still in beta state. Few queries can lead to errors. The user should use its account to check the status of the query and why it failed (http://apps.ecmwf.int/webmars/joblist/).
