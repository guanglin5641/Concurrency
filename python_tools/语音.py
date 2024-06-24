from gtts import gTTS
import tkinter as tk
from tkinter import filedialog
import os
def convert_to_speech():
    text = text_entry.get("1.0", "end-1c")
    tts = gTTS(text=text, lang='zh-cn')
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
    if save_path:
        tts.save(save_path)
        os.system(f'open {save_path}')  # 打开生成的语音文件
 # 创建GUI窗口
window = tk.Tk()
window.title("文字转语音")
window.geometry("400x200")
 # 创建文本输入框
text_entry = tk.Text(window, height=5, width=40)
text_entry.pack()
 # 创建生成语音按钮
convert_button = tk.Button(window, text="生成语音", command=convert_to_speech)
convert_button.pack()
 # 运行GUI窗口
window.mainloop()
