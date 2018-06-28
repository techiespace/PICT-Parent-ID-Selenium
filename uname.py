myfile = open('username.txt', 'w')
for uname in range(10100,11000):
    myfile.write("P%s\n" % uname)
myfile.close()
