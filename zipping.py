import os,shutil,zipfile

def backupZip(folder):
    fold=os.path.abspath(folder)
    number=1
    while True:
        zipFilename="F:\\" +os.path.basename(folder)+'_'+str(number)+'.zip'
        print(os.path.basename(folder))
        if not os.path.exists(zipFilename):
            break
        number+=1
    print("Creating  "+zipFilename)
    backupZipfol = zipfile.ZipFile(zipFilename, 'w')

    for foldername,subfolder,filename in os.walk(folder):
        print("Adding file {0} to backup".format(filename,zipFilename))
        backupZipfol.write(foldername)
        for filenames in filename:
            newBase=os.path.basename(folder)+'_'
            print('folder '+foldername)
            print('Filename '+filenames)
            if filenames.startswith(newBase) and filenames.endswith('.zip'):
                continue
            backupZipfol.write(os.path.join(foldername,filenames))
        backupZipfol.close()


backupZip("F:\\program_create")