"""
Syntax:
    file object = open(file_name [, access_mode][, buffering])
    file_name : name of the file to access
    access_mode: the mode in which the file has to be opened i.e., read, write, append, etc
    buffering: 
        if buffering value is set to 0 then no buffering takes place
        if buffering value is set to 1, line buffering is performed while accessing a file
        if buffering value is greater than 1, then buffering action is performed with the indicated buffer size
        if negative, the buffer size is the system default (default behavior)
    
Modes:
    r   - opens a file for readonly. The pointer is placed at the beginning of the file. This is the default mode
    rb  - opens a file for reading only in binary format. The file pointer is placed at the beginning of the file
    r+  - opens a file for both reading and writing. The file pointer is placed at the beginning of the file
    rb+ - opens a file for both reading and writing in binary format. 
            The file pointer is placed at the beginning of the file
    w   - opens a file for writing only. Overwrites the file if the file exists, if the file does not exists, creates  
            a new file for writing
    wb  - opens a file for writing only in binary format. overwrites the file if the file exists. 
            if the file does not exist, creates a new file for writing
    w+  - opens a file for both writing and reading. overwrites the file if the file exists. 
            if the file does not exist, creates a new file for reading & writing
    wb+ - opnes a file for both writing and reading in binary format. overwrites the file if the file exists. 
            if the file does not exist, creates a new file for reading & writing
    a   - opens a file for appending. The file pointer is at the end of the file if the file exists.
            That is, the file is in the append mode. overwrites the file if the file exists. 
            if the file does not exist, creates a new file for writing
    ab  - opens a file for appending in binary format. The file pointer is at the end of the file if the file exists.
            That is, the file is in the append mode. overwrites the file if the file exists. 
            if the file does not exist, creates a new file for writing
    a+  - opens a file for appending. The file pointer is at the end of the file if the file exists.
            That is, the file is in the append mode. overwrites the file if the file exists. 
            if the file does not exist, creates a new file for reading & writing
    ab+  - opens a file for appending in binary format. The file pointer is at the end of the file if the file exists.
            That is, the file is in the append mode. overwrites the file if the file exists. 
            if the file does not exist, creates a new file for reading & writing

file object attributes
    file.closed     - Returns true if file is closed, false otherwise
    file.mode       - Returns access mode with which file was opened
    file.name       - Returns name of the file
    file.softspace  - Returns false if space explicitly required with print, true otherwise
"""
import os

def file_operation():
    f = open("test_file_operation_foo.txt", "wb+")
    print "### File attributes ###"
    print "name of the file is : {}".format(f.name)
    print "Closed or not : {}".format(f.closed)
    print " Opening mode : {}".format(f.mode)
    print "Softspace flag : {}".format(f.softspace)

    print "### File operations ###"
    f.write("Python is great language.\nYeah its great!!\n")
    print "Read result for 10 : {}".format(f.read(10))
    print "Current position of the file is : {} bytes".format(f.tell())
    f.close()

    print "### Renaming the file ###"
    os.rename("test_file_operation_foo.txt", "test_file_operation_foo_renamed.txt")


if __name__ == '__main__':
    file_operation()
