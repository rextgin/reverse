# Filenames : <Sazxt>
# python bytecode : 2.7
# Time Succses Parser : Mon Jul  6 13:34:59 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import marshal, os, time
#os.system('termux-setup-storage')
h = '\x1b[1;92m'
bi = '\x1b[1;96m'
k = '\x1b[1;93m'
u = '\x1b[1;95m'
pu = '\x1b[1;97m'
b = '\x1b[1;94m'
m = '\x1b[1;91m'
hi = '\x1b[1;30m'
hg = '\x1b[4;92m'
p = '\x1b[0m'

def logo():
    os.system('clear')
    print u + '\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x90\xe2\x94\x8c  \xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\xac  \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\n\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\xac\xe2\x94\x98 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x82  \xe2\x94\x82  \xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x98\xe2\x94\x82\xe2\x94\x82  \xe2\x94\x9c\xe2\x94\xa4 \xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\n\xe2\x94\xb4   \xe2\x94\xb4  \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x98\xe2\x94\x94\xe2\x94\x98  \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4  \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80'
    print hi + '------------------------------------------'
    print p + '[' + h + '\xe2\x80\xa2' + p + '] ' + pu + 'Author ' + m + ': ' + bi + 'Sanz'
    print p + '[' + h + '\xe2\x80\xa2' + p + '] ' + pu + 'Youtube' + m + ': ' + bi + 'SANZ SOEKAMTI'
    print p + '[' + h + '\xe2\x80\xa2' + p + '] ' + pu + 'Github' + m + ': ' + hg + 'https://github.com/B4N954N2-ID' + p
    print hi + '------------------------------------------'
    print p + '[' + h + '+' + p + '] ' + k + 'Simple Marshal Compiler Python Script'
    print p + '[' + h + '+' + p + '] ' + k + 'Choose Your Python Version?'
    print hi + '------------------------------------------'


def log():
    os.system('clear')
    print u + '\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x90\xe2\x94\x8c  \xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\xac  \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\n\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\xac\xe2\x94\x98 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x82  \xe2\x94\x82  \xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x98\xe2\x94\x82\xe2\x94\x82  \xe2\x94\x9c\xe2\x94\xa4 \xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\n\xe2\x94\xb4   \xe2\x94\xb4  \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x98\xe2\x94\x94\xe2\x94\x98  \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4  \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80'
    print hi + '------------------------------------------'
    print p + '[' + h + '\xe2\x80\xa2' + p + '] ' + pu + 'Author ' + m + ': ' + bi + 'Sanz'
    print p + '[' + h + '\xe2\x80\xa2' + p + '] ' + pu + 'Youtube' + m + ': ' + bi + 'SANZ SOEKAMTI'
    print p + '[' + h + '\xe2\x80\xa2' + p + '] ' + pu + 'Github' + m + ': ' + hg + 'https://github.com/B4N954N2-ID' + p
    print hi + '------------------------------------------'


def main():
    time.sleep(0.5)
    logo()
    time.sleep(0.1)
    print p + '[' + h + '01' + p + ']. ' + pu + 'Encrypt Python2 ' + p + '(' + h + 'Marshal' + p + ')'
    time.sleep(0.1)
    print p + '[' + h + '02' + p + ']. ' + pu + 'Encrypt Python3 ' + p + '(' + h + 'Marshal' + p + ')'
    time.sleep(0.1)
    print p + '[' + h + '03' + p + ']. ' + pu + 'Exit Program'
    time.sleep(0.1)
    print hi + '------------------------------------------'
    time.sleep(0.1)
    sanz = raw_input(p + '[' + h + '\xe2\x80\xa2' + p + '] ' + p + 'Choose ' + m + '>> ' + h)
    if sanz == '2' or sanz == '02':
        os.system('python .py3')
    elif sanz == '1' or sanz == '01':
        py2()
    elif sanz == '3' or sanz == '03':
        out()
    else:
        print p + '[' + m + '!' + p + '] ' + pu + 'Wrong Input' + m + '!!'
        time.sleep(1)
        main()


def out():
    time.sleep(0.1)
    print p + '[' + h + '+' + p + '] ' + p + 'Thanks For Using This My Tools'
#    os.system('xdg-open https://youtube.com/SanzSoekamti')
    time.sleep(1)
    exit(p + '[' + m + '!' + p + '] ' + p + 'Exit')


def py2():
    try:
        log()
        print p + '[' + h + '+' + p + '] ' + k + 'Ex ' + m + ': ' + p + '/sdcard/file.py'
        a = raw_input(p + '[' + h + '+' + p + '] ' + pu + 'File ' + m + ': ' + h)
        x = open(a).read()
        b = compile(x, '<Sanz>', 'x = ')
        c = a.replace('.py', '_enc.py')
        d = marshal.dumps(b)
        e = open(c, 'w')
        e.write('# Compile by Sanz\n# Youtube : SANZ SOEKAMTI\n# Github  : https://github.com/B4N954N2-ID\n')
        e.write('import marshal\n')
        e.write('x =  marshal.loads(' + repr(d) + ')')
        e.close()
        time.sleep(2)
        print p + '[' + h + '+' + p + '] ' + pu + 'Files Encrypted ' + m + ': ' + h + c
        os.system('xdg-open https://youtube.com/SanzSoekamti')
        time.sleep(0.1)
    except IOError:
        print p + '[' + m + 'x' + p + '] ' + pu + 'File Not Found'
        time.sleep(1)
        py2()
    except KeyboardInterrupt:
        out()


try:
    main()
except KeyboardInterrupt:
    out()
