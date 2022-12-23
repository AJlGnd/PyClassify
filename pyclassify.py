import os
import shutil
while True:
    # ENTERING YOUR WORKING DIRECTORY
    parent_directory = input("Enter Your Destination: ")
    listall = os.listdir(parent_directory)
    # FILTERING THIS EXTENSIONS TO BE ALL ADDED TO EITHER Images FOLDER OR Videos Folder
    images = ['.JPG','.JPEG','.PNG']
    videos = ['.MOV','.MP4']
    # CREATING DIRECTORIES ACCORDING TO THE CURRENT FILE IN THE LOOP
    for files in listall:
        split_tup = os.path.splitext(files)
        file_extension = split_tup[1]
        #EXCLUDING THE CURRENT WORKING PYTHON FILE AND EXCLUDING ANY OTHER FOLDERS IN THAT DIRECTORY

        if files != 'pyclassify.py' and file_extension != '':

            isIt = file_extension.upper() in images
            isIt2 = file_extension.upper() in videos

            # CREATING THE DIRECTORIES DYNAMIC-LY
            if isIt:
                dynamic_dir = os.path.join(parent_directory, f"Images Files")
            elif isIt2:
                dynamic_dir = os.path.join(parent_directory, f"Videos Files")
            else:
                dynamic_dir = os.path.join(parent_directory, f"{file_extension} Files")
            # HANDLING ERROR
            try:
                os.mkdir(dynamic_dir)
            except OSError:
                print("ERROR:Directory already exists!")

            #os.mkdir(worddir)
            #os.mkdir(pdfdir)
            #os.mkdir(txtdir)
    # THIS LOOP IS FOR MOVING THE FILES TO ITS CORRESPONDING DIRECTORY
    for files2 in listall:
        split_tup = os.path.splitext(files2)
        file_extension = split_tup[1]

        # EXCLUDING THE PYTHON FILE AND ANY FOLDERS
        if files2 != 'pyclassify.py' and file_extension != '':

            itIs = file_extension.upper() in images
            itIs2 = file_extension.upper() in videos

            path2 = os.path.join(parent_directory,files2)
            path3 = os.path.join(parent_directory,"Images Files")
            path4 = os.path.join(parent_directory, "Videos Files")
            path5 = os.path.join(parent_directory, f"{file_extension} Files")

            # ACTUAL MOVING PROCESS AND HANDLING THE ERRORS
            if itIs:
                try:
                    shutil.move(path2, path3)
                except OSError as error:
                    print("ERROR: Error while moving the files ")
                    print(error)
            elif itIs2:
                try:
                    shutil.move(path2, path4)
                except OSError as error:
                    print("ERROR: Error while moving the files ")
                    print(error)
            else:
                try:
                    shutil.move(path2, path5)
                except OSError as error:
                    print("ERROR: Error while moving the files ")
                    print(error)
    # TERMINATION OR REPETITION OF THE PROCESS
    cmd = input("Do you want to continue?(y,n): ")
    if cmd.lower() == 'y':
        pass
    elif cmd.lower() == 'n':
        break



