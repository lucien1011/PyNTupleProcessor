import os, shutil

def testFunc():
    print("This is a test!")

def make_dir_copy_file(infile, newdir):
    """
    make_dir_copy_file(infile, newdir)
    
    Copy infile into newdir, creating newdir if it doesn't already exist. 
    Especially good for putting an index.php file into newdir to view png plots.
    
    Arguments: 
    infile must be a full path, not relative.
    newdir must be a full path, not relative.
    """
    name_file = os.path.split(infile)[-1]
    
    if not os.path.exists(newdir): 
        os.makedirs(newdir)
        print "New directory made at:", newdir
        
    if not os.path.exists(newdir+name_file): 
        shutil.copyfile(infile, newdir+name_file)
        print infile, "copied to:", newdir