import os

print(os.getcwd())

path = '/Users/raymond/Desktop/test'
# os.getcwd() 
# or feel free to define the path

for i in range(1, 11):
    os.chdir(path)
    Newfolder = "Tutorial-" + str(i)

    try:
        if not os.path.exists(Newfolder):
            os.makedirs(Newfolder)
        # to make folders insider the other folders
            path2 = path + '/' + Newfolder
            os.chdir(path2)
            for j in range(1, 3):
                Newfolder2 = 'Test' + str(j)
                os.makedirs(Newfolder2)
                # looks like there's a bug here
        
    except OSError:
        print('Error: Directory already exist, try to change name ')
