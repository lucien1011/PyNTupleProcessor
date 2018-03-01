import subprocess

def getGitDescribe():
    return subprocess.check_output(["git", "describe", "--tags"])

def getGitDiff():
    return subprocess.check_output(["git", "diff"])

def getGitRevisionHash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'])

def getGitRevisionShortHash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
