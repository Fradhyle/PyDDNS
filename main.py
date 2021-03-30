import requests
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title('PyDDNS')
root.geometry("640x400+100+100")
root.resizable(False, False)

def get_content():
    res = requests.get(req_point + '/' + id_ + '/dns_records', headers=headers)
    result = res.json()['result']
    return result

treeview=ttk.Treeview(root, columns=['name', 'type', 'content'], displaycolumns=['name', 'type', 'content'])
treeview.pack()

treeview.column('#0', width=30)
treeview.heading('#0', text='순번')

treeview.column('name', width=100)
treeview.heading('name', text='주소')

treeview.column('type', width=30)
treeview.heading('type', text='타입', anchor='center')

treeview.column('content', width=100)
treeview.heading('content', text='IP 주소', anchor='center')

for i in range(len(result)):
    data = result[i]
    treeview.insert('', 'end', text=i+1, values=[data['name'], data['type'], data['content']], iid=i+1)

root.mainloop()