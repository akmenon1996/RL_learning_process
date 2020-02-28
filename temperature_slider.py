import tkinter
import threading
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg

class Plotter():
    def __init__(self,fig):
        self.root = tkinter.Tk()
        self.root.state("zoomed")

        self.fig = fig
        t = threading.Thread(target=self.PlottingThread,args=(fig,))
        t.start()

    def PlottingThread(self,fig):
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=self.root)
        canvas.show()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        toolbar = matplotlib.backends.backend_tkagg.NavigationToolbar2TkAgg(canvas, self.root)
        toolbar.update()
        canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.root.mainloop()


fig = plt.figure()
Plotter(fig)


fig.gca().clear()
fig.gca().plot([1,2,3],[4,5,6])
fig.canvas.draw()