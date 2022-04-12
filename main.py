import time, threading
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from playsound import playsound
class MainTimer:

    def __init__(self):

        # Interface
        
        self.root = tk.Tk()
        self.root.geometry('560x300')
        self.root.title('Pomodoro Timer Cauã')

        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Ubuntu', 16))
        self.style.configure('TButton', font=('Ubuntu', 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill='both', pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=560, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=560, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=560, height=100)

        self.pomodoro_timer_label = ttk.Label(self.tab1, text='25:00', font=('Ubuntu', 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.sb_timer_label = ttk.Label(self.tab2, text='05:00', font=('Ubuntu', 48))
        self.sb_timer_label.pack(pady=20)

        self.lb_timer_label = ttk.Label(self.tab3, text='10:00', font=('Ubuntu', 48))
        self.lb_timer_label.pack(pady=20)
        

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='SB')
        self.tabs.add(self.tab3, text='LB')

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=5)

        self.start_button = ttk.Button(self.grid_layout, text='Start', command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.pause_button = ttk.Button(self.grid_layout, text='Pause', command=self.pause_timer)
        self.pause_button.grid(row=0, column=1)

        self.skip_button = ttk.Button(self.grid_layout, text='Skip', command=self.skip_timer)
        self.skip_button.grid(row=0, column=2)

        self.reset_button = ttk.Button(self.grid_layout, text='Reset', command=self.reset_timer)
        self.reset_button.grid(row=0, column=3)

        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text='Cycles: 0', font=('Ubuntu', 16))
        self.pomodoro_counter_label.grid(row=1, column=0, pady=10)

        self.full_time_label = ttk.Label(self.grid_layout,
         text=f'Total Time: 00:00',
         font=('Ubuntu', 16))
        self.full_time_label.grid(row=1, column=3)

        self.cycles = 0
        self.skipped = False
        self.stopped = False
        self.running = False

        self.count = 1

        self.total = 0
        
        self.root.mainloop()

    #logic

    def start_timer(self):
        self.stopped = False
        self.skipped = False
        self.pause = False
        
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
                full_seconds = 60 * 25
                #full_seconds = 5
 
                while full_seconds > 0 and not self.stopped:

                    if self.pause:
                        self.count = 0
                    elif not self.pause:
                        self.count = 1

                    minutes, seconds = divmod(full_seconds, 60)
                    self.pomodoro_timer_label.config(text=f'{minutes:02d}:{seconds:02d}')
                    self.root.update()
                    time.sleep(1)
                    full_seconds -= self.count

                    self.total += self.count
                    total_min, total_sec = divmod(self.total, 60)
                    total_hour, total_min = divmod(total_min, 60)

                    if self.total < 60 * 60:
                        self.full_time_label.config(text=f'Total Time: {total_min:02d}:{total_sec:02d}')
                    else:
                        self.full_time_label.config(text=f'Total Time: {total_hour:d}:{total_min:02d}:{total_sec:02d}')

                if not self.skipped and not self.stopped or self.skipped and self.stopped:
                    playsound('assets/ring_edited.mp3')
                
                if not self.stopped or self.skipped:
                    self.cycles += 1
                    self.pomodoro_counter_label.config(text=f'Cycles: {self.cycles}')

                    if self.cycles % 4 == 0:
                        self.tabs.select(2)
                    else:
                        self.tabs.select(1)
                    self.start_timer()

        elif timer_id == 2:
                full_seconds = 60 * 5
                #full_seconds = 5
                while full_seconds > 0 and not self.stopped:

                    if self.pause:
                        self.count = 0
                    elif not self.pause:
                        self.count = 1
                    
                    minutes, seconds = divmod(full_seconds, 60)
                    self.sb_timer_label.config(text=f'{minutes:02d}:{seconds:02d}')
                    self.root.update()
                    time.sleep(1)
                    full_seconds -= self.count
                    self.total += self.count
                    total_min, total_sec = divmod(self.total, 60)
                    self.full_time_label.config(text=f'Total Time: {total_min:02d}:{total_sec:02d}')

                if not self.skipped and not self.stopped or self.skipped and self.stopped:
                    playsound('assets/ring_edited.mp3')
                
                if not self.stopped or self.skipped:
                    self.tabs.select(0)
                    self.start_timer()

        elif timer_id == 3:
                full_seconds = 60 * 10
                #full_seconds = 5
                while full_seconds > 0 and not self.stopped:
                    minutes, seconds = divmod(full_seconds, 60)
                    self.lb_timer_label.config(text=f'{minutes:02d}:{seconds:02d}')
                    self.root.update()
                    time.sleep(1)
                    full_seconds -= self.count
                    self.total += self.count
                    total_min, total_sec = divmod(self.total, 60)
                    self.full_time_label.config(text=f'Total Time: {total_min:02d}:{total_sec:02d}')

                if not self.skipped and not self.stopped or self.skipped and self.stopped:
                    playsound('assets/ring_edited.mp3')

                if not self.stopped or self.skipped:
                    self.tabs.select(0)
                    self.start_timer()

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True
        else:
            if messagebox.askyesno('Error', 'To start another timer you need to reset\n\n Do you want to reset now?', ):
                self.reset_timer()
                

    def reset_timer(self):

        self.stopped = True
        self.skipped = False
        self.cycles = 0
        self.pomodoro_timer_label.config(text='25:00')
        self.sb_timer_label.config(text='05:00')
        self.lb_timer_label.config(text='10:00')
        self.pomodoro_counter_label.config(text='Cycles: 0')
        self.running = False
        self.full_time_label.config(text='Total Time: 00:00')
        self.total = 0
    
    def skip_timer(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodoro_timer_label.config(text='25:00')
        elif current_tab == 1:
            self.sb_timer_label.config(text='05:00')
        elif current_tab == 2:
            self.lb_timer_label.config(text='10:00')

        self.skipped = True
        self.stopped = True

    def pause_timer(self):

        #if self.pause_button['text'] == 'Pause':
        #    self.pause_button['text'] = 'Unpause'
        #else:
        #    self.pause_button['text'] = 'Pause'
        
        if not self.pause:
            self.pause_button.config(text='Unpause')
            self.pause = True
            
        elif self.pause:
            self.pause_button.config(text='Pause')
            self.pause = False
            


MainTimer()