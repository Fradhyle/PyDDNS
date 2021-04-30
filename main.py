import requests
import time
import tkinter as tk
import tkinter.ttk as ttk


def get_external_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    return response.json()['ip']

root = tk.Tk()

treeview = ttk.Treeview(root, columns=['type', 'name', 'content', 'ttl', 'proxied'])

treeview.column('#0', width=50, anchor='center', stretch=tk.NO)
treeview.heading('#0', text='순번', anchor='center')

treeview.column('type', width=50, anchor='center', stretch=tk.NO)
treeview.heading('type', text='형식', anchor='center')

treeview.column('name', width=100, anchor='center', stretch=tk.NO)
treeview.heading('name', text='이름', anchor='center')

treeview.column('content', width=100, anchor='center', stretch=tk.NO)
treeview.heading('content', text='콘텐츠', anchor='center')

treeview.column('ttl', width=50, anchor='center', stretch=tk.NO)
treeview.heading('ttl', text='TTL', anchor='center')

treeview.column('proxied', width=100, anchor='center', stretch=tk.NO)
treeview.heading('proxied', text='프록시 상태', anchor='center')

treeview.insert('', 'end', text='1', values=['AAAA', 'long_string', '255.255.255.255', 'auto', 'false'], open=True)

ip_label = tk.Label(root, text='IP 주소', anchor='center', justify='center')

ip_entry = tk.Entry(root, justify='center')
ip_entry.insert(0, get_external_ip())

time_label = tk.Label(root, text='최종 업데이트 시간', anchor='center', justify='center')

time_entry = tk.Entry(root, justify='center')
time_entry.insert(0, time.strftime('%Y-%m-%d %p %X', time.localtime()))

treeview.grid(row=0, column=0, columnspan=5, sticky='news')
ip_label.grid(row=1, column=1)
ip_entry.grid(row=1, column=2)
time_label.grid(row=1, column=3)
time_entry.grid(row=1, column=4)

root.title('PyDDNS')
root_pos_right = int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2)
root_pos_down = int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2)
root.geometry(f'+{root_pos_right}+{root_pos_down}')
root.resizable(False, False)

root.mainloop()