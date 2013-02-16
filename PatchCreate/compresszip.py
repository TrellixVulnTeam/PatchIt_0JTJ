import os, shutil
import PatchIt

#global zipfile, inputfiles
def compressfiles():
    '''Compress PatchIt! patch'''

    print()
    inputfiles = input("Please enter the path to the files you wish to compress: \n\n> ")
    zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)
        # TODO: Move Patch File from app directory
    #newzipfile = os.replace(zipfile, "{0}{1}.zip".format(name, ver))

    if os.system(inputfiles) == 1:
        print("{0} patch for {1} created and saved to {2}.zip".format(PatchIt.app, createname, inputfiles))
        PatchIt.main()
        #return True
    elif os.system(inputfiles) == 0:
        print("Creation of {0} patch for {1} ended with an unknown error. Please try again.".format(PatchIt.app, createname))
        PatchIt.main()
        #return False
    else:
        print("Creation of {0} patch for {1} failed!".format(PatchIt.app, createname))
        PatchIt.main()
        #return "Fail"