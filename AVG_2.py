import tkinter as tk
from tkinter import messagebox

class AverageCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("محاسبه میانگین")
        self.master.geometry('350x200')
        
        self.list1 = []  # لیست برای ذخیره مقادیر

        # ایجاد Entry
        self.entry = tk.Entry(master,font=('Arial',15),bg='#36e0de')
        self.entry.pack(pady=10)

        # دکمه Submit
        self.submit_button = tk.Button(master, text="ثبت", command=self.submit,font=('Arial',18),width=3,height=1)
        self.submit_button.pack(pady=5)

        # دکمه Average
        self.average_button = tk.Button(master, text="میانگین", command=self.calculate_average,font=('Arial',18),width=10,height=1)
        self.average_button.pack(pady=5)

    def submit(self):
        try:
            # دریافت مقدار از Entry
            value = float(self.entry.get())
            self.list1.append(value)  # اضافه کردن مقدار به لیست
            self.entry.delete(0, tk.END)  # پاک کردن Entry
        except ValueError:
            messagebox.showerror("خطا", "لطفاً یک عدد معتبر وارد کنید.")

    def calculate_average(self):
        if self.list1:  # بررسی اینکه لیست خالی نیست
            average = sum(self.list1) / len(self.list1)
            messagebox.showinfo("میانگین", f"میانگین مقادیر: {average}")
        else:
            messagebox.showwarning("هشدار", "لیست خالی است!")

# ایجاد پنجره اصلی و اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = AverageCalculatorApp(root)
    root.mainloop()
