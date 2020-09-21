from tkinter import *
root = Tk()
#root['bg']='white'
root.title("tkinter.Text sample")
canv = Canvas(root, width=600, height=400,defilregion=(0, 0, 1200, 800))
canv.grid(row=0, column=0)

defilY = Scrollbar(root, orient='vertical',command=canv.yview)
defilY.grid(row=0, column=1, sticky='ns')

defilX = Scrollbar(self, orient='horizontal',command=canv.xview)
defilX.grid(row=1, column=0, sticky='ew')

canv['xscrollcommand'] = defilX.set
canv['yscrollcommand'] = defilY.set
root.loop()
