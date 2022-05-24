"""
This code ouput the file size of each folder for selected directory.
All the size of files that is inside sub-directories(sub-folders) are also outputed.
Returned size is bytes size.
It is recommanded to specify folder path more exactly in order not to get very huge amount of datas. 
"""

import os

files_name_and_size_dict = dict()

chg_path = r'C:/' # this need to be much more specific path. For example like this : C:/Riot Games/League of Legends

# Check current working directory.
Folderpath = os.getcwd()

# Now change the directory
os.chdir( chg_path )

# Check current working directory.
Folderpath = os.getcwd()

# Get size
for path, dirs, files in os.walk(Folderpath):
    for f in files:
        file_name = os.path.join(path, f)

        """
        If file or foler name exceed 260 characters, then you can encounter this error : 
        'FileNotFoundError: [WinError 3] The system cannot find the path specified'
        To fix this error, I found this stackoverflow answer, and here is the link : 
        'https://stackoverflow.com/questions/33604543/python-filenotfounderror-winerror-3-for-getsizefilepath'
        """
        file_name = u"\\\\?\\" + file_name # this single line is added to fix the "FileNotFoundError: [WinError 3]". 

        files_name_and_size_dict[file_name] = os.path.getsize(file_name)

"""
When there is a mismatch between the returned values and the number of variables declared to store these values, this error could occurs :
'ValueError: too many values to unpack (expected 2)'
If we have more objects to assign and fewer variables to hold, we get a ValueError.
To fix this error, I referencing this link : 
'https://itsmycode.com/valueerror-too-many-values-to-unpack-expected-2/'
In the case of dictionary, we should not consider the keys and values in the dictionary as two separate entities in Python.
"""
for name, size in files_name_and_size_dict.items(): # just use items mehtod of dictionary. The items() function returns a view object which contains both key-value pairs stored as tuples.
    print(f"{name} : {str(size)}")
