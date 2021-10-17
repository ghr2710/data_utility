# data_utility
A python module for reading and writing CSV files

# How to use
## READ
##list_name = data_utility.read("file_name.csv")
reads from the specified CSV file and returns a list containing the results

## WRITE
##data_utility.write(list_name, "file_name.csv")
writes to a CSV file with the specified name using the given list, if a file by that name already exists it will overwrite the file

# Known Issues
On write: If the CSV you are trying to write to is open, the program will throw an error and crash
