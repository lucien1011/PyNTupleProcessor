import subprocess

def isRootFile(fileName):
    return fileName.endswith(".root")

def listdir_uberftp(path,selection=isRootFile):
    cmd = ["uberftp", "cmsio.rc.ufl.edu", "ls %s"%path]
    output = subprocess.Popen(cmd,stdout=subprocess.PIPE).communicate()[0]
    return [l.split()[-1] for l in output.split('\r\n') if selection(l)]


