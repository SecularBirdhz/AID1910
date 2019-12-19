from tkinter import *
from tkinter.messagebox import *


class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        # self.importPrice = StringVar()
        # self.sellPrice = StringVar()
        # self.deductPrice = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='音乐界面').pack()
        Label(self).pack()
        Label(self).pack()
        Label(self, text='音乐界面').pack()
        # Label(self).grid(row=0, stick=W, pady=10)
        # Label(self, text='药品名称: ').grid(row=1, stick=W, pady=10)
        # Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        # Label(self, text='进价 /元: ').grid(row=2, stick=W, pady=10)
        # Entry(self, textvariable=self.importPrice).grid(row=2, column=1, stick=E)
        # Label(self, text='售价 /元: ').grid(row=3, stick=W, pady=10)
        # Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E)
        # Label(self, text='优惠 /元: ').grid(row=4, stick=W, pady=10)
        # Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E)
        # Button(self, text='录入').grid(row=6, column=1, stick=E, pady=10)


class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='音乐列表').pack()


# class CountFrame(Frame):  # 继承Frame类
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.root = master  # 定义内部变量root
#         self.createPage()
#
#     def createPage(self):
#         Label(self, text='音乐路径').pack()
#
#     def callback(self):
#         fileName = self.root.filedialog.askopenfilename()
#         print(fileName)


class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()


    def createPage(self):
        Label(self, text='关于界面').pack()
        Label(self).pack()
        Label(self).pack()
        Label(self).pack()
        Label(self).pack()
        about_text = """
                   起初只是想做一个音乐播放器,但
                当完成基础功能后又觉得很low,所以
                我们也在不断的添加新的功能,提高产
                品的健壮性和可用性.
                """
        Label(self, text=about_text).pack()
