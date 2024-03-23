import tkinter as tk
from tkinter import messagebox

class Goods(object):
    def __init__(self, name, num, primecost, sellingprice):
        self.name = name
        self.num = num
        self.primecost = primecost
        self.sellingprice = sellingprice

    def __str__(self):
        state = "已售罄" if self.num == 0 else "有货"
        return '名称：%s, 状态：%s, 数量：%d, 进货价格：%.2f, 售出价格：%.2f' % (
            self.name, state, self.num, self.primecost, self.sellingprice)

class gGoods:
    def __init__(self, name, gnum, gprimecost, gsellingprice):
        self.name = name
        self.gnum = gnum
        self.gprimecost = gprimecost
        self.gsellingprice = gsellingprice

    def __str__(self):
        return '名称：%s, 卖出数量：%d, 进货价格：%.2f, 售出价格：%.2f' % (
            self.name, self.gnum, self.gprimecost, self.gsellingprice)

class GoodsManager(object):
    def __init__(self):
        self.go = []  # 库存列表
        self.js = []  # 已售出列表
        self.init()

    def init(self):
        with open("goods.txt", "r", encoding="utf-8") as file:
            for line in file:
                name, num, primecost, sellingprice = line.strip().split(",")
                num = int(num)
                primecost = float(primecost)
                sellingprice = float(sellingprice)
                self.go.append(Goods(name, num, primecost, sellingprice))

    def showGoods(self):
        if not self.go:
            self.show_info("库存为空！")
        else:
            info = "所有商品：\n\n"
            for goods in self.go:
                info += str(goods) + "\n"
            self.show_info(info)

    def show_info(self, info):
        top = tk.Toplevel()
        top.title("信息")
        tk.Label(top, text=info, font=("Microsoft Yahei", 12)).pack(padx=20, pady=20)
        tk.Button(top, text="关闭", width=15, height=1, command=top.destroy).pack(pady=10)

    def saveGoods(self):
        with open("goods.txt", "w", encoding="utf-8") as file:
            for goods in self.go:
                file.write("%s,%d,%.2f,%.2f\n" % (goods.name, goods.num, goods.primecost, goods.sellingprice))

    def addGoods(self):
        top = tk.Toplevel()
        top.title("添加商品")
        tk.Label(top, text="名称：", font=("Microsoft Yahei", 12)).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        tk.Label(top, text="数量：", font=("Microsoft Yahei", 12)).grid(row=1, column=0, sticky="w", padx=20, pady=10)
        tk.Label(top, text="进货价格：", font=("Microsoft Yahei", 12)).grid(row=2, column=0, sticky="w", padx=20, pady=10)
        tk.Label(top, text="售出价格：", font=("Microsoft Yahei", 12)).grid(row=3, column=0, sticky="w", padx=20, pady=10)

        name_entry = tk.Entry(top, font=("Microsoft Yahei", 12))
        num_entry = tk.Entry(top, font=("Microsoft Yahei", 12))
        primecost_entry = tk.Entry(top, font=("Microsoft Yahei", 12))
        sellingprice_entry = tk.Entry(top, font=("Microsoft Yahei", 12))

        name_entry.grid(row=0, column=1, padx=20, pady=10)
        num_entry.grid(row=1, column=1, padx=20, pady=10)
        primecost_entry.grid(row=2, column=1, padx=20, pady=10)
        sellingprice_entry.grid(row=3, column=1, padx=20, pady=10)

        def add():
            name = name_entry.get()
            num = num_entry.get()
            primecost = primecost_entry.get()
            sellingprice = sellingprice_entry.get()

            if not name or not num or not primecost or not sellingprice:
                messagebox.showerror("错误", "请填写完整的信息！")
                return

            try:
                num = int(num)
                primecost = float(primecost)
                sellingprice = float(sellingprice)
            except ValueError:
                messagebox.showerror("错误", "数量、进货价格和售出价格必须是数字！")
                return

            for goods in self.go:
                if goods.name == name:
                    goods.num += num
                    self.show_info("商品%s已存在，数量增加%d" % (name, num))
                    break
            else:
                self.go.append(Goods(name, num, primecost, sellingprice))
                self.show_info("商品%s添加成功" % name)
            self.saveGoods()  # 调用 saveGoods 方法保存数据
            top.destroy()

        tk.Button(top, text="添加", width=15, height=1, command=add).grid(row=4, column=0, padx=20, pady=10)
        tk.Button(top, text="取消", width=15, height=1, command=top.destroy).grid(row=4, column=1, padx=20, pady=10)

    def delGoods(self):
        top = tk.Toplevel()
        top.title("删除商品")
        tk.Label(top, text="名称：", font=("Microsoft Yahei", 12)).grid(row=0, column=0, sticky="w", padx=20, pady=10)

        name_entry = tk.Entry(top, font=("Microsoft Yahei", 12))
        name_entry.grid(row=0, column=1, padx=20, pady=10)

        def delete():
            name = name_entry.get()

            for goods in self.go:
                if goods.name == name:
                    self.go.remove(goods)
                    self.show_info("商品%s删除成功" % name)
                    break
            else:
                messagebox.showerror("错误", "商品%s不存在！" % name)
            self.saveGoods()
            top.destroy()

        tk.Button(top, text="删除", width=15, height=1, command=delete).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(top, text="取消", width=15, height=1, command=top.destroy).grid(row=1, column=1, padx=20, pady=10)

    def modifyGoods(self):
        top = tk.Toplevel()
        top.title("修改商品信息")
        tk.Label(top, text="名称：", font=("Microsoft Yahei", 12)).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        tk.Label(top, text="数量：", font=("Microsoft Yahei", 12)).grid(row=1, column=0, sticky="w", padx=20, pady=10)
        tk.Label(top, text="进货价格：", font=("Microsoft Yahei", 12)).grid(row=2, column=0, sticky="w", padx=20, pady=10)
        tk.Label(top, text="售出价格：", font=("Microsoft Yahei", 12)).grid(row=3, column=0, sticky="w", padx=20, pady=10)

        name_entry = tk.Entry(top, font=("Microsoft Yahei", 12))
        num_entry = tk.Entry(top, font=("Microsoft Yahei", 12))
        primecost_entry = tk.Entry(top, font=("Microsoft Yahei", 12))
        sellingprice_entry = tk.Entry(top, font=("Microsoft Yahei", 12))

        name_entry.grid(row=0, column=1, padx=20, pady=10)
        num_entry.grid(row=1, column=1, padx=20, pady=10)
        primecost_entry.grid(row=2, column=1, padx=20, pady=10)
        sellingprice_entry.grid(row=3, column=1, padx=20, pady=10)

        def modify():
            name = name_entry.get()
            num = num_entry.get()
            primecost = primecost_entry.get()
            sellingprice = sellingprice_entry.get()

            if not name or not num or not primecost or not sellingprice:
                messagebox.showerror("错误", "请填写完整的信息！")
                return

            try:
                num = int(num)
                primecost = float(primecost)
                sellingprice = float(sellingprice)
            except ValueError:
                messagebox.showerror("错误", "数量、进货价格和售出价格必须是数字！")
                return

            for goods in self.go:
                if goods.name == name:
                    goods.num = num
                    goods.primecost = primecost
                    goods.sellingprice = sellingprice
                    self.show_info("商品%s信息修改成功" % name)
                    break
            else:
                messagebox.showerror("错误", "商品%s不存在！" % name)
            self.saveGoods()
            top.destroy()

        tk.Button(top, text="修改", width=15, height=1, command=modify).grid(row=4, column=0, padx=20, pady=10)
        tk.Button(top, text="取消", width=15, height=1, command=top.destroy).grid(row=4, column=1, padx=20, pady=10)

    def sellGoods(self):
        top = tk.Toplevel()
        top.title("卖出商品")
        tk.Label(top, text="名称：", font=("Microsoft Yahei", 12)).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        tk.Label(top, text="数量：", font=("Microsoft Yahei", 12)).grid(row=1, column=0, sticky="w", padx=20, pady=10)

        name_entry = tk.Entry(top, font=("Microsoft Yahei", 12))
        num_entry = tk.Entry(top, font=("Microsoft Yahei", 12))

        name_entry.grid(row=0, column=1, padx=20, pady=10)
        num_entry.grid(row=1, column=1, padx=20, pady=10)

        def sell():
            name = name_entry.get()
            num = num_entry.get()

            if not name or not num:
                messagebox.showerror("错误", "请填写完整的信息！")
                return

            try:
                num = int(num)
            except ValueError:
                messagebox.showerror("错误", "数量必须是数字！")
                return

            for goods in self.go:
                if goods.name == name:
                    if goods.num >= num:
                        goods.num -= num
                        self.js.append(gGoods(name, num, goods.primecost, goods.sellingprice))
                        self.show_info("商品%s卖出成功%d" % (name, num))
                        break
                    else:
                        messagebox.showerror("错误", "商品%s库存不足！" % name)
                        break
            else:
                messagebox.showerror("错误", "商品%s不存在！" % name)

            top.destroy()

        tk.Button(top, text="卖出", width=15, height=1, command=sell).grid(row=2, column=0, padx=20, pady=10)
        tk.Button(top, text="取消", width=15, height=1, command=top.destroy).grid(row=2, column=1, padx=20, pady=10)


if __name__ == "__main__":
    gm = GoodsManager()

    root = tk.Tk()
    root.title("商品管理系统")
    root.geometry("500x500")

    # 创建一个Frame作为容器，并设置其在窗口中的位置
    frame = tk.Frame(root)
    frame.pack(pady=50)

    # 创建按钮，将其放置在Frame中，并设置居中对齐
    tk.Button(frame, text="显示商品信息", width=20, height=2, command=gm.showGoods).pack(pady=10)
    tk.Button(frame, text="添加商品", width=20, height=2, command=gm.addGoods).pack(pady=10)
    tk.Button(frame, text="删除商品", width=20, height=2, command=gm.delGoods).pack(pady=10)
    tk.Button(frame, text="修改商品信息", width=20, height=2, command=gm.modifyGoods).pack(pady=10)
    tk.Button(frame, text="卖出商品", width=20, height=2, command=gm.sellGoods).pack(pady=10)
    tk.Button(frame, text="退出", width=20, height=2, command=root.quit).pack(pady=10)
    root.mainloop()