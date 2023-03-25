import os

'''
add:
- check the path exists - if so print to screen and ask for confirmation
- at the first file show the current filename and the name it will be changed to and ask for conf
- regex to find pattern in a string of text and change filename to that text
'''


path = 'D:\\AGAIN\\NEW\\rename'
#path = 'C:\\Users\\matth\\Desktop\\New folder'

for filename in os.listdir(path):
    current = path + '\\' + filename
    #remove first 16 chars
    #newpath = path + '\\' + (filename[16:len(filename)])
    #remove first 11 chars
    newpath = path + '\\' + (filename[11:len(filename)])
    #remove first 8 chars
    #newpath = path + '\\' + (filename[8:len(filename)])
    
    #newpath = path + '\\' + (filename + ".mp4")
    os.rename(current, newpath)