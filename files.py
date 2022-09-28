# below script is about how to read/copy a file

with open('xxx.png', 'rb') as rf:
    with open('xxx_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)