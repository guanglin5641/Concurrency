import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta

import HaoPingKa

# 创建窗口
window = tk.Tk()

# 添加城市标签和下拉框
# 添加城市标签
city_label = tk.Label(window, text="城市：")
city_label.pack()

# 创建城市列表框
city_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, exportselection=False)
city_listbox.pack()

# 添加城市选项
city_choices = ["杭州", "长沙", "上海"]
for city in city_choices:
    city_listbox.insert(tk.END, city)

# 添加开始时间标签和时间选择器
start_time_label = tk.Label(window, text="开始时间：")
start_time_label.pack()
start_time_var = tk.StringVar()
start_time_picker = ttk.Combobox(window, textvariable=start_time_var,
                                 values=[(datetime(2023, 7, 1) + timedelta(days=i)).strftime("%Y-%m-%d 00:00:00") for i
                                         in range(365)])
start_time_picker.pack()

# 添加结束时间标签和时间选择器
end_time_label = tk.Label(window, text="结束时间：")
end_time_label.pack()
end_time_var = tk.StringVar()
end_time_picker = ttk.Combobox(window, textvariable=end_time_var,
                               values=[(datetime(2023, 7, 1) + timedelta(days=i)).strftime("%Y-%m-%d 00:00:00") for i in
                                       range(365)])
end_time_picker.pack()


# 创建提交按钮
def submit():
    city = [city_listbox.get(idx) for idx in city_listbox.curselection()]  # 获取选中的城市
    start_time = start_time_var.get()
    end_time = end_time_var.get()
    print(city, start_time, end_time)
    result = HaoPingKa.mysql(city, start_time, end_time)
    messagebox.showinfo("查询结果", str(result))


submit_button = tk.Button(window, text="提交", command=submit)
submit_button.pack()

# 运行窗口主循环
window.mainloop()
if __name__ == '__main__':
    window.mainloop()