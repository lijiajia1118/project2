import tkinter as tk
from tkinter import messagebox
import subprocess

# 定义文件名
employee_info_file = 'employee_info.txt'
customer_info_file = 'customer_info.txt'

# 读取员工信息
def read_employee_info():
    employee_info = {}
    with open(employee_info_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 确保读取的行不为空
                username, password = line.strip().split(',')
                employee_info[username] = password
    return employee_info

# 写入员工信息
def write_employee_info(username, password):
    with open(employee_info_file, 'a', encoding='utf-8') as f:
        f.write(f'{username},{password}\n')

# 读取顾客信息
def read_customer_info():
    customer_info = {}
    with open(customer_info_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 确保读取的行不为空
                username, password = line.strip().split(',')
                customer_info[username] = password
    return customer_info

# 写入顾客信息
def write_customer_info(username, password):
    with open(customer_info_file, 'a', encoding='utf-8') as f:
        f.write(f'{username},{password}\n')

def employee_login():
    username = employee_username_entry.get()
    password = employee_password_entry.get()
    employee_info = read_employee_info()
    if username in employee_info and employee_info[username] == password:
        messagebox.showinfo("登录成功", "员工登录成功")
        subprocess.run(['python', 'employee.py'])  # 运行 employee.py 文件
    else:
        messagebox.showerror("登录失败", "用户名或密码错误")

def customer_register():
    username = customer_username_entry.get()
    password = customer_password_entry.get()
    customer_info = read_customer_info()
    if username in customer_info:
        messagebox.showerror("注册失败", "用户名已存在")
    else:
        write_customer_info(username, password)
        messagebox.showinfo("注册成功", "注册成功")

def customer_login():
    username = customer_username_entry.get()
    password = customer_password_entry.get()
    customer_info = read_customer_info()
    if username in customer_info and customer_info[username] == password:
        messagebox.showinfo("登录成功", "顾客登录成功")
        subprocess.run(['python', 'customer.py'])  # 运行 customer.py 文件
    else:
        messagebox.showerror("登录失败", "用户名或密码错误")

# 创建窗口
window = tk.Tk()
window.title("选择员工或顾客登录")
window.geometry("300x200")

# 创建员工登录界面
employee_label = tk.Label(window, text="员工登录")
employee_label.pack()

employee_username_label = tk.Label(window, text="用户名:")
employee_username_label.pack()
employee_username_entry = tk.Entry(window)
employee_username_entry.pack()

employee_password_label = tk.Label(window, text="密码:")
employee_password_label.pack()
employee_password_entry = tk.Entry(window, show="*")
employee_password_entry.pack()

employee_login_button = tk.Button(window, text="登录", command=employee_login)
employee_login_button.pack()

# 创建顾客登录和注册界面
customer_label = tk.Label(window, text="顾客登录/注册")
customer_label.pack()

customer_username_label = tk.Label(window, text="用户名:")
customer_username_label.pack()
customer_username_entry = tk.Entry(window)
customer_username_entry.pack()

customer_password_label = tk.Label(window, text="密码:")
customer_password_label.pack()
customer_password_entry = tk.Entry(window, show="*")
customer_password_entry.pack()

customer_register_button = tk.Button(window, text="注册", command=customer_register)
customer_register_button.pack()

customer_login_button = tk.Button(window, text="登录", command=customer_login)
customer_login_button.pack()

# 运行窗口