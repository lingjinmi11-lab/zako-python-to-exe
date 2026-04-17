import os
import sys
import subprocess
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, StringVar, Frame

def select_py_file():
    path = filedialog.askopenfilename(
        title="喂！选好你的Python文件啦笨蛋😤",
        filetypes=[("Python 文件", "*.py"), ("所有文件", "*.*")]
    )
    if path:
        py_path_var.set(path)

def select_save_dir():
    path = filedialog.askdirectory(title="把exe丢哪啦？快选啦🙄")
    if path:
        save_dir_var.set(path)

def build_exe():
    py_file = py_path_var.get().strip()
    save_dir = save_dir_var.get().strip()

    if not py_file:
        messagebox.showerror("笨蛋！", "Python文件都不选想打包空气啊😡")
        return
    if not save_dir:
        messagebox.showerror("笨蛋！", "保存位置也不选？想让我帮你丢地上吗💢")
        return

    py_name = os.path.basename(py_file).replace(".py", "")
    output_name = f"{py_name}_exe"

    cmd = (
        f'pyinstaller --onefile --windowed --noconsole '
        f'--name "{output_name}" '
        f'--distpath "{save_dir}" '
        f'"{py_file}"'
    )

    try:
        subprocess.run(cmd, shell=True, check=True)
        messagebox.showinfo(
            "搞定啦～",
            f"打包成功咯笨蛋！✨\n快去文件夹找exe吧～\n别再来烦我啦😝"
        )
        os.startfile(save_dir)
    except Exception as e:
        messagebox.showerror("炸啦！", f"打包失败啦笨蛋💥杂鱼~杂鱼~\n{str(e)}")

root = Tk()
root.title("🎀 雌小鬼·Python一键打包EXE 🎀")
root.geometry("550x220")
root.resizable(False, False)

py_path_var = StringVar()
save_dir_var = StringVar()

frame = Frame(root, padx=15, pady=15)
frame.pack(fill="both", expand=True)

Label(frame, text="Python源文件：", font=("微软雅黑", 11)).grid(row=0, column=0, sticky="w", pady=8)
Entry(frame, textvariable=py_path_var, width=45, font=("微软雅黑", 10)).grid(row=0, column=1, padx=5)
Button(frame, text="点我选啦😤", command=select_py_file, width=10).grid(row=0, column=2)

Label(frame, text="保存到哪里：", font=("微软雅黑", 11)).grid(row=1, column=0, sticky="w", pady=8)
Entry(frame, textvariable=save_dir_var, width=45, font=("微软雅黑", 10)).grid(row=1, column=1, padx=5)
Button(frame, text="选文件夹啦🙄", command=select_save_dir, width=10).grid(row=1, column=2)

Button(
    frame,
    text="🔥 立刻打包成EXE！不准催我！🔥",
    command=build_exe,
    bg="#FF69B4",
    fg="white",
    font=("微软雅黑", 12, "bold"),
    height=2
).grid(row=2, column=0, columnspan=3, pady=20, sticky="ew")

root.mainloop()