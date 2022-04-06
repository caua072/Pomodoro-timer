import time, threading
import tkinter as tk
from tkinter import ttk, font


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

        self.pomodoro_timer_label = ttk.Label(self.tab1, text='25:00', font=('Ubuntu', 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.pomodoro_timer_label = ttk.Label(self.tab2, text='05:00', font=('Ubuntu', 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.pomodoro_timer_label = ttk.Label(self.tab3, text='10:00', font=('Ubuntu', 48))
        self.pomodoro_timer_label.pack(pady=20)
        

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='SB')
        self.tabs.add(self.tab3, text='LB')

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_button = ttk.Button(self.grid_layout, text='Start', command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layout, text='Skip', command=self.skip_timer)
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.grid_layout, text='Reset', command=self.reset_timer)
        self.reset_button.grid(row=0, column=2)

        
        
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