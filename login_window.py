import tkinter as tk
from tkinter import messagebox
import subprocess

# 全局变量声明
register_username_entry = None
register_password_entry = None
register_window = None  # 在这里声明全局变量

# 读取员工信息
def read_employee_info():
    employee_info = {}
    with open("employee_info.txt", 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 添加此行代码，跳过空行
                fields = line.strip().split(',')
                if len(fields) == 2:
                    username, password = fields
                    employee_info[username] = password
    return employee_info

# 员工登录
def employee_login():
    username = employee_username_entry.get()
    password = employee_password_entry.get()
    employee_info = read_employee_info()
    if username in employee_info and employee_info[username] == password:
        messagebox.showinfo("登录成功", "员工登录成功")
        subprocess.run(['python', 'employee.py'])
    else:
        messagebox.showerror("登录失败", "用户名或密码错误")

# 读取顾客信息
def read_customer_info():
    customer_info = {}
    with open("customer_info.txt", 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 添加此行代码，跳过空行
                fields = line.strip().split(',')
                if len(fields) == 2:
                    username, password = fields
                    customer_info[username] = password
    return customer_info

# 顾客登录
def customer_login():
    username = customer_username_entry.get()
    password = customer_password_entry.get()
    customer_info = read_customer_info()
    if username in customer_info and customer_info[username] == password:
        messagebox.showinfo("登录成功", "顾客登录成功")
        subprocess.run(['python', 'customer.py'])
    else:
        register = messagebox.askyesno("账户不存在", "是否注册新账户？")
        if register:
            create_register_window(username)
        else:
            messagebox.showerror("登录失败", "用户名或密码错误")

# 创建注册窗口
def create_register_window(username):
    global register_username_entry, register_password_entry, register_window  # 声明为全局变量
    register_window = tk.Toplevel(window)
    register_window.title("注册窗口")
    register_window.geometry("400x300")

    username_label = tk.Label(register_window, text="用户名:", font=("Arial", 14))
    username_label.pack()
    register_username_entry = tk.Entry(register_window, font=("Arial", 14))
    register_username_entry.pack()

    password_label = tk.Label(register_window, text="密码:", font=("Arial", 14))
    password_label.pack()
    register_password_entry = tk.Entry(register_window, show="*", font=("Arial", 14))
    register_password_entry.pack()

    register_button = tk.Button(register_window, text="注册", command=lambda: register_customer(username), font=("Arial", 14))
    register_button.pack(pady=10)

    # 设置默认用户名
    register_username_entry.insert(0, username)

# 注册顾客账户
def register_customer(username):
    global register_username_entry, register_password_entry, register_window  # 声明为全局变量
    register_username = register_username_entry.get()
    register_password = register_password_entry.get()

    if not register_username or not register_password:
        messagebox.showerror("注册失败", "请输入有效的用户名和密码")
        return

    customer_info = read_customer_info()
    if register_username in customer_info:
        messagebox.showerror("注册失败", "该用户名已被注册")
    else:
        with open("customer_info.txt", 'a', encoding='utf-8') as f:
            f.write(f"{register_username},{register_password}\n")
        messagebox.showinfo("注册成功", "顾客账户注册成功")
        register_window.destroy()  # 关闭注册窗口
# 创建窗口
window = tk.Tk()
window.title("选择员工或顾客登录")
window.geometry("400x200")

# 创建单选按钮
login_type = tk.StringVar()
employee_radio_button = tk.Radiobutton(window, text="员工登录", variable=login_type, value="employee", font=("Arial", 16))
employee_radio_button.pack(pady=10)

customer_radio_button = tk.Radiobutton(window, text="顾客登录", variable=login_type, value="customer", font=("Arial", 16))
customer_radio_button.pack(pady=10)

# 登录窗口
def create_login_window():
    login_window = tk.Toplevel(window)
    login_window.title("登录窗口")
    login_window.geometry("400x300")

    if login_type.get() == "employee":
        # 创建员工登录界面
        employee_label = tk.Label(login_window, text="员工登录", font=("Arial", 24))
        employee_label.pack(pady=10)

        employee_username_label = tk.Label(login_window, text="用户名:", font=("Arial", 14))
        employee_username_label.pack()
        global employee_username_entry
        employee_username_entry = tk.Entry(login_window, font=("Arial", 14))
        employee_username_entry.pack()

        employee_password_label = tk.Label(login_window, text="密码:", font=("Arial", 14))
        employee_password_label.pack()
        global employee_password_entry
        employee_password_entry = tk.Entry(login_window, show="*", font=("Arial", 14))
        employee_password_entry.pack()

        employee_login_button = tk.Button(login_window, text="登录", command=employee_login, font=("Arial", 14))
        employee_login_button.pack(pady=10)
    elif login_type.get() == "customer":
        # 创建顾客登录界面
        customer_label = tk.Label(login_window, text="顾客登录", font=("Arial", 24))
        customer_label.pack(pady=10)

        customer_username_label = tk.Label(login_window, text="用户名:", font=("Arial", 14))
        customer_username_label.pack()
        global customer_username_entry
        customer_username_entry = tk.Entry(login_window, font=("Arial", 14))
        customer_username_entry.pack()

        customer_password_label = tk.Label(login_window, text="密码:", font=("Arial", 14))
        customer_password_label.pack()
        global customer_password_entry
        customer_password_entry = tk.Entry(login_window, show="*", font=("Arial", 14))
        customer_password_entry.pack()

        customer_login_button = tk.Button(login_window, text="登录", command=customer_login, font=("Arial", 14))
        customer_login_button.pack(pady=10)

# 创建登录按钮
login_button = tk.Button(window, text="登录", command=create_login_window, font=("Arial", 16))
login_button.pack(pady=20)

# 运行窗口
window.mainloop()