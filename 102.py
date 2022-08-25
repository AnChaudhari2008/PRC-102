from distutils import extension
import os 
import shutil

source = '/Users/mahen/OneDrive/Desktop/abc'
destination = '/Users/mahen/OneDrive/Desktop'
list_of_files = os.listdir(source)
for i in list_of_files:
    name, extension = os.path.splitext(i)
    if(extension == ''):
        continue 
    if extension in ['.txt', '.pdf', '.doc', '.docx','.jpeg']:
        path1 = source + '/' + i # Example path1 : Downloads/ImageName1.jpg
        path2 = destination + '/' + 'Image_files' # Example path1 : Downloads/ImageName1.jpg
        path3 = destination + '/' + "Image_files" + '/'+i # Example path1 : Downloads/ImageName1.jpg
        
        if os.path.exists(path2):
            print('moving')
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('moving')
            shutil.move(path1, path3)
            


