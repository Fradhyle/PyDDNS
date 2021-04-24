import requests
import tkinter as tk
import tkinter.ttk as ttk


def get_external_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    return response.json()['ip']

root = tk.Tk()

treeview = ttk.Treeview(root, columns=['type', 'name', 'content'])
treeview.pack()

treeview.column('#0', width=50)
treeview.heading('#0', text='순번')

treeview.column('type', width=50)
treeview.heading('type', text='형식')

treeview.column('name', width=50)
treeview.heading('name', text='이름')

treeview.column('content', width=50)
treeview.heading('content', text='콘텐츠')

treeview.insert('', 'end', text='1', values=['test1', 'test2', 'test3'], open=True)

root.title('PyDDNS')
root_pos_right = int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2)
root_pos_down = int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2)
root.geometry(f'+{root_pos_right}+{root_pos_down}')
root.resizable(False, False)

root.mainloop()