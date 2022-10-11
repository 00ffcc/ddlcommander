import math
import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QTextEdit,QSpinBox,QMessageBox,QLabel
from PyQt5.QtCore import Qt
import json
from datetime import date, datetime
import math
from functools import partial
from PyQt5.QtCore import pyqtSignal, QThread
import os
t=[]
class Child(QWidget):
    signal=pyqtSignal()
    def __init__(self, parent=None,tp={},id=0):
        super(Child, self).__init__()
        self.setWindowTitle("ddl战士:修改")
        self.setWindowIcon(QIcon(__file__[:-12]+'qwq.ico'))
        self.name=QTextEdit(self)
        self.name.setPlaceholderText('在此修改名字')
        self.name.setText(tp['name'])
        self.name.resize(300,30)

        self.detail=QTextEdit(self)
        self.detail.setPlaceholderText('在此修改备注')
        self.detail.setText(tp['detail'])
        self.detail.resize(300,30)
        self.detail.move(0,30)

        self.year=QSpinBox(self)
        self.year.setRange(1970,2038)
        self.year.setSingleStep(1)
        self.year.setValue(tp['ddl'].year)
        self.year.move(0,60)
        self.year.resize(60,30)

        self.month=QSpinBox(self)
        self.month.setRange(1,12)
        self.month.setSingleStep(1)
        self.month.setValue(tp['ddl'].month)
        self.month.move(60,60)
        self.month.resize(60,30)

        self.day=QSpinBox(self)
        self.day.setRange(1,31)
        self.day.setSingleStep(1)
        self.day.setValue(tp['ddl'].day)
        self.day.move(120,60)
        self.day.resize(60,30)

        self.last_label=QLabel(self)
        self.last_label.setText('在此填写预计完成所需时间')
        self.last_label.setGeometry(0,90,180,30)

        self.last=QSpinBox(self)
        self.last.setRange(0,10000)
        self.last.setSingleStep(1)
        self.last.setValue(1)
        self.last.move(180,90)
        self.last.resize(60,30)

        self.loc=QTextEdit(self)
        self.loc.setPlaceholderText('在此填写文件地址')
        self.loc.setText(tp['loc'])
        self.loc.resize(300,30)
        self.loc.move(0,120)

        self.submit=QPushButton('确定',self)
        self.submit.move(0,150)
        self.submit.clicked.connect(partial(self.record,id))

        self.eraser=QPushButton('删除',self)
        self.eraser.move(90,150)
        self.eraser.clicked.connect(partial(self.erase,id))

        self.eraser=QPushButton('打开文件',self)
        self.eraser.move(180,150)
        self.eraser.clicked.connect(partial(self.open_file,id))
    def record(self,id):
        data={'name':self.name.toPlainText(),'detail':self.detail.toPlainText(),'ddl':date(self.year.value(),self.month.value(),self.day.value()),'last':self.last.value(),'loc':self.loc.toPlainText()}
        data['time']=(data['ddl']-date.today()).days+1
        global t
        t[id]=data
        self.signal.emit()
        print(t)
        self.close()
    def erase(self,id):
        global t
        t=t[:id]+t[id+1:]
        self.signal.emit()
        self.close()
    def open_file(self,id):
        data={'name':self.name.toPlainText(),'detail':self.detail.toPlainText(),'ddl':date(self.year.value(),self.month.value(),self.day.value()),'last':self.last.value(),'loc':self.loc.toPlainText()}
        data['time']=(data['ddl']-date.today()).days+1
        global t
        t[id]=data
        self.signal.emit()
        print(t)
        try:
            a=os.startfile(t[id]['loc'])
        except:
            QMessageBox.critical(self,'error','未找到指定文件或文件夹')
class Child2(QWidget):
    signal=pyqtSignal()
    def __init__(self, parent=None):
        super(Child2, self).__init__()
        self.setWindowTitle("ddl战士:新建")
        self.setWindowIcon(QIcon(__file__[:-12]+'qwq.ico'))
        self.name=QTextEdit(self)
        self.name.setPlaceholderText('在此修改名字')
        self.name.resize(300,30)

        self.detail=QTextEdit(self)
        self.detail.setPlaceholderText('在此修改备注')
        self.detail.resize(300,30)
        self.detail.move(0,30)

        self.year=QSpinBox(self)
        self.year.setRange(1970,2038)
        self.year.setSingleStep(1)
        self.year.setValue(date.today().year)
        self.year.move(0,60)
        self.year.resize(60,30)

        self.month=QSpinBox(self)
        self.month.setRange(1,12)
        self.month.setSingleStep(1)
        self.month.setValue(date.today().month)
        self.month.move(60,60)
        self.month.resize(60,30)

        self.day=QSpinBox(self)
        self.day.setRange(1,31)
        self.day.setSingleStep(1)
        self.day.setValue(date.today().day)
        self.day.move(120,60)
        self.day.resize(60,30)

        self.last_label=QLabel(self)
        self.last_label.setText('在此填写预计完成所需时间')
        self.last_label.setGeometry(0,90,180,30)

        self.last=QSpinBox(self)
        self.last.setRange(0,10000)
        self.last.setSingleStep(1)
        self.last.setValue(1)
        self.last.move(180,90)
        self.last.resize(60,30)

        self.loc=QTextEdit(self)
        self.loc.setPlaceholderText('在此填写文件地址')
        self.loc.resize(300,30)
        self.loc.move(0,120)    

        self.submit=QPushButton('确定',self)
        self.submit.move(0,150)
        self.submit.clicked.connect(partial(self.record,id))
    def record(self,id):
        data={'name':self.name.toPlainText(),'detail':self.detail.toPlainText(),'ddl':date(self.year.value(),self.month.value(),self.day.value()),'last':self.last.value(),'loc':self.loc.toPlainText()}
        data['time']=(data['ddl']-date.today()).days+1
        global t
        t.append(data)
        self.signal.emit()
        print(t)
        self.close()
        '''
        f=open(__file__[:-12]+'todolist.txt','w')
        f.write(json.dumps(t))
        f.close()
        '''

class Demo(QWidget):
    item=[]
    def __init__(self):
        super(Demo,self).__init__()
        global t
        f=open(__file__[:-12]+'todolist.txt')
        re=f.readline()
        if re=='':
            re='[]'
        t=json.loads(re)
        f.close()
        for i in range(len(t)):
            print(t[i])
            t[i]['ddl']=date.fromisoformat(t[i]['ddl'])
            t[i]['time']=(t[i]['ddl']-date.today()).days+1
        self.flash()
    def flash(self):
        self.setWindowTitle("ddl战士")
        self.setWindowIcon(QIcon(__file__[:-12]+'qwq.ico'))
        global t
        global item
        #print(t)
        for i in range(len(self.item)):
            self.item[i].deleteLater()
        self.item=[]
        t.sort(key=lambda x:x['time'])
        tim_mx=0
        for i in t:
            tim_mx=max(tim_mx,i['time'])
        self.resize(500,max(len(t)*100,100))
        sum_time=0
        for i in t:
            self.item.append(QPushButton(i['name']+' 还有'+str(i['time'])+'天', self))
            self.item[-1].resize(max(int(500*math.pow(i['time'],1/3)/math.pow(tim_mx,1/3)),200),100)
            self.item[-1].move(0,100*(len(self.item)-1))
            self.item[-1].clicked.connect(partial(self.showchild,i,len(self.item)-1))
            last_time=i['time']-sum_time
            if last_time<i['last']:
                self.item[-1].setStyleSheet("QPushButton{font-family:微软雅黑;font-size:30px;color:rgb(0,0,0,200);}\
QPushButton{background-color:rgb(255,0,0)}\
QPushButton:hover{background-color:rgb(200,0,0)}")
                sum_time=i['time']
            else:
                tp=int(i['last']/last_time*100)-50
                self.item[-1].setStyleSheet("QPushButton{font-family:'宋体';font-size:30px;color:rgb(255,255,255,255);}\
QPushButton{background-color:rgb("+str(200+tp)+",0,"+str(200-tp)+")}\
QPushButton:hover{background-color:rgb("+str(200-tp)+",0,"+str(200+tp)+")}")
                sum_time+=i['last']
            self.item[-1].show()
        self.creat_new=QPushButton('新建',self)
        self.creat_new.move(400,0)
        self.creat_new.clicked.connect(self.creatnew)
        self.creat_new.show()

        self.png=QLabel(self)
        pix=QPixmap(__file__[:-12]+'qwq.png')
        self.png.setPixmap(pix)
        self.png.move(0,max(len(t)*100,100)-100)
        self.png.raise_()
        self.png.show()

    def creatnew(self):
        child=Child2(self)
        child.signal.connect(self.flash)
        child.show()
    def showchild(self,tp,id):
        child=Child(self,tp,id)
        child.signal.connect(self.flash)
        child.show()
    def closeEvent(self,e):
        f=open(__file__[:-12]+'todolist.txt','w')
        for i in range(len(t)):
            t[i]['ddl']=t[i]['ddl'].isoformat()
        f.write(json.dumps(t))
        f.close()
        self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())