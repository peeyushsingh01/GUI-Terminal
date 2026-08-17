#imports
import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit
from PySide6.QtGui import QShortcut,QKeySequence
from PySide6.QtCore import QTimer

app = QApplication(sys.argv)
win1 = QWidget()
window = QWidget()
window.setWindowTitle("Terminal")
window.setFixedSize(1500,600)
window.show()
display = QLineEdit(window)
display.setGeometry(350,50,800,100)
display.setText("hello")
display.setReadOnly(True)
display.setStyleSheet("""
                 background-color : grey;
                 color: black;
                 font-size :27px;
                 border: 4px solid black;
""")
display.show()
display1 = QLineEdit(window)
display1.setGeometry(500,170,500,70)
display1.setText("hello")
display1.setReadOnly(True)
display1.setStyleSheet("""
                 background-color : grey;
                 color: black;
                 font-size :23px;
                 border: 4px solid black;
""")
display1.show()

#base program!!

list = []
x = ""
def maxi(x):
    t = x[0]
    t = int(t)
    for i in x:
        i = int(i)
        if i > t:
            t = i
    return t

def mini(x):
    t = x[0]
    t = int(t)
    for i in x:
        i = int(i)
        if i < t:
            t = i
    return t

def su(x):
    t = 0
    for i in x:
        i = int(i)
        t +=i
    return t
def avg(x):
    t = su(x)
    l = len(x)
    t = t /l
    return t

def e(x):
    c = 0
    for i in x:
        i = int(i)
        if i%2 == 0:
            c += 1
    return c

def o(x):
    c = 0
    for i in x:
        i = int(i)
        if i%2 != 0:
            c += 1
    return c

#functions
def add(a):
    global x
    x = x+a
    showe(x)

def show(b):
    display1.setText(b)

def showe(b):
    display1.setText("press [ENTER] to submit this no.==> {}".format(b))

def typingd1(c):
    t=c
    s=""
    b= 50
    for i in t:
        s = s+i
        b=b+50
        QTimer.singleShot(b,lambda text = s:display.setText(text))

def typingd2(c):
    t=c
    s=""
    b= 50
    for i in t:
        s = s+i
        b=b+50
        QTimer.singleShot(b,lambda text = s:show(text))

def yes():
    typingd1("So I will collect some integers from you to analyse :")
    QTimer.singleShot(2700,lambda :typingd2("press [ENTER] to submit this no.==> " ))


def no():
    typingd1("It was nice to meet you !")
    QTimer.singleShot(1500,lambda :typingd2("If you want to restart press 'R'."))

def re():
    typingd1("Hii! welcome back, shall we start ?")
    QTimer.singleShot(1200, lambda: typingd2("press 'Y' to start now or 'N' to abandon !"))

def en():
    global x
    if x != "":
        list.append(x)
        x = ""
        typingd2("Number of integers saved : {}".format(str(len(list))))
        QTimer.singleShot(1700, lambda: typingd1("If you want to finish registering new no. press 'F'"))
        QTimer.singleShot(4400, lambda: typingd2("press [ENTER] to submit this no.==> "))

def bcsp():
    global x
    x = x[:-1]
    showe(x)

def final():
    global win1
    if len(list) == 0:
        typingd1("no number entered yet - add some")
        return
    else:
        win1.setWindowTitle("Data Analysis")
        win1.setFixedSize(500, 700)
        output1 = QLabel(
            "-> In the given set of number: \n-> Maximum value: {} \n->Minimum value: {} \n-> Sum : {} \n-> Average: {} \n->No. of even no.s: {}\n->No. of odd nos: {}".format(
                maxi(list), mini(list), su(list), avg(list), e(list), o(list)), win1)
        output1.move(50, 50)

        win1.show()



#process
typingd1("Hii! shall we start ?")
QTimer.singleShot(1200,lambda :typingd2("press 'Y' to start now or 'N' to abandon !"))

#buttons

sf = QShortcut(QKeySequence("F"),window)
sf.activated.connect(final)

sb = QShortcut(QKeySequence("Backspace"),window)
sb.activated.connect(bcsp)

se = QShortcut(QKeySequence("Enter"),window)
se.activated.connect(en)

sr = QShortcut(QKeySequence("R"),window)
sr.activated.connect(re)

sn = QShortcut(QKeySequence("N"),window)
sn.activated.connect(no)

sy = QShortcut(QKeySequence("Y"),window)
sy.activated.connect(yes)

s1 = QShortcut(QKeySequence("1"),window)
s1.activated.connect(lambda :add("1"))

s2 = QShortcut(QKeySequence("2"),window)
s2.activated.connect(lambda :add("2"))

s3 = QShortcut(QKeySequence("3"),window)
s3.activated.connect(lambda :add("3"))

s4 = QShortcut(QKeySequence("4"),window)
s4.activated.connect(lambda :add("4"))

s5 = QShortcut(QKeySequence("5"),window)
s5.activated.connect(lambda :add("5"))

s6 = QShortcut(QKeySequence("6"),window)
s6.activated.connect(lambda :add("6"))

s7 = QShortcut(QKeySequence("7"),window)
s7.activated.connect(lambda :add("7"))

s8 = QShortcut(QKeySequence("8"),window)
s8.activated.connect(lambda :add("8"))

s9 = QShortcut(QKeySequence("9"),window)
s9.activated.connect(lambda :add("9"))

s0 = QShortcut(QKeySequence("0"),window)
s0.activated.connect(lambda :add("0"))

sys.exit(app.exec())


#will be used later
