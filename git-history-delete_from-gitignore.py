import commands

f = open('.gitignore')
line = f.readline()

while line:
    name = line.rstrip("\n")
    print commands.getoutput("git filter-branch -f --index-filter 'git rm --ignore-unmatch %s' HEAD" % (name))
    line = f.readline()

f.close
