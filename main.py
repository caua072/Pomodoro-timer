import time, threading
import tkinter as tk
from tkinter import ttk

class MainTimer:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry('600x300')
        self.root.title('Pomodoro Timer Cauã')

        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Ubuntu', 16))
        self.style.configure('TButton', font=('Ubuntu', 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill='both', pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='SB')
        self.tabs.add(self.tab3, text='LB')
        
        self.root.mainloop()

    def start_timer_thread(self):
        pass
    
    def start_timer(self):
        pass

    def reset_timer(self):
        pass
    
    def skip_timer(self):
        pass
MainTimer()