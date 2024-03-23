from tkinter import *
import tkinter.messagebox as messagebox

# 创建购物车列表
shopping_cart = []

# 读取商品信息
def read_goods_info():
    goods = []
    try:
        with open('goods.txt', 'r',encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                goods_info = {
                    'name': data[0],
                    'quantity': int(data[1]),
                    'cost_price': float(data[2]),
                    'selling_price': float(data[3])
                }
                goods.append(goods_info)
    except FileNotFoundError:
        messagebox.showerror('错误', '商品信息文件不存在！')
    return goods

# 更新商品信息文件
def update_goods_info(goods):
    with open('goods.txt', 'w', encoding="utf-8") as file:
        for item in goods:
            line = f"{item['name']},{item['quantity']},{item['cost_price']},{item['selling_price']}\n"
            file.write(line)

# 显示商品信息
def show_goods_info(root, goods):
    row_num = 0
    for item in goods:
        name_label = Label(root, text=item['name'])
        name_label.grid(row=row_num, column=0, sticky=W)
        quantity_label = Label(root, text=f"库存数量: {item['quantity']}")
        quantity_label.grid(row=row_num, column=1, padx=10, pady=5, sticky=W)
        selling_price_label = Label(root, text=f"售价: {item['selling_price']}元")
        selling_price_label.grid(row=row_num, column=2, padx=10, pady=5, sticky=W)
        add_button = Button(root, text="加入购物车", command=lambda item=item: add_to_cart(item))
        add_button.grid(row=row_num, column=3, padx=10, pady=5, sticky=W)
        remove_button = Button(root, text="从购物车中删除", command=lambda item=item: remove_from_cart(item))
        remove_button.grid(row=row_num, column=4, padx=10, pady=5, sticky=W)
        # 将name_label和quantity_label保存到item字典中
        item['name_label'] = name_label
        item['quantity_label'] = quantity_label
        row_num += 1

# 加入购物车
def add_to_cart(item):
    if item['quantity'] > 0:
        shopping_cart.append(item)
        item['quantity'] -= 1
        update_goods_info(goods)  # 更新商品信息文件
        update_shopping_cart()
        calculate_total_price()
        messagebox.showinfo('成功', f"{item['name']}已加入购物车！")
        # 修改对应商品库存数量的标签
        item['quantity_label'].config(text=f"库存数量: {item['quantity']}")
    else:
        messagebox.showwarning('警告', f"{item['name']}库存不足！")


# 从购物车中删除商品
def remove_from_cart(item):
    if item in shopping_cart:
        shopping_cart.remove(item)
        item['quantity'] += 1  # 商品数量恢复
        update_goods_info(goods)  # 更新商品信息文件
        update_shopping_cart()
        calculate_total_price()
        messagebox.showinfo('成功', f"{item['name']}已从购物车中移除！")
        # 修改对应商品库存数量的标签
        item['quantity_label'].config(text=f"库存数量: {item['quantity']}")

# 更新购物车
def update_shopping_cart():
    shopping_cart_listbox.delete(0, END)
    for item in shopping_cart:
        shopping_cart_listbox.insert(END, f"{item['name']} - {item['selling_price']}元")

# 计算总价
def calculate_total_price():
    total_cost = sum(item['selling_price'] for item in shopping_cart)
    total_price_label.config(text=f"总价：{total_cost}元")

# 结算
def checkout():
    total_cost = sum(item['selling_price'] for item in shopping_cart)  # 计算总价
    calculate_total_price()
    messagebox.showinfo('结算', f"您共消费{total_cost}元！")
    shopping_cart.clear()
    update_shopping_cart()
    calculate_total_price()

# 创建主窗口
root = Tk()
root.title("商品列表")

# 获取商品信息
goods = read_goods_info()

# 显示商品信息
show_goods_info(root, goods)

# 创建购物车列表
shopping_cart_label = Label(root, text="购物车")
shopping_cart_label.grid(row=len(goods)+1, column=0, sticky=W)
shopping_cart_listbox = Listbox(root)
shopping_cart_listbox.grid(row=len(goods)+2, column=0, padx=10, pady=5, sticky=W)

# 创建总价格标签
total_price_label = Label(root, text="总价：0元")
total_price_label.grid(row=len(goods)+3, column=0, padx=10, pady=5, sticky=W)

# 创建结算按钮
checkout_button = Button(root, text="结算", command=checkout)
checkout_button.grid(row=len(goods)+4, column=0, padx=10, pady=5, sticky=W)

root.mainloop()