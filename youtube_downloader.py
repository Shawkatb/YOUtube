import tkinter as tk
from pytube import YouTube

def download_video():
    url = url_entry.get()
    output_path = r"C:\Users\user\Downloads"  # مسار الحفظ الثابت
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        status_label.config(text="جارٍ تحميل الفيديو...")
        video.download(output_path)
        status_label.config(text="تم تحميل الفيديو بنجاح إلى: " + output_path)
    except Exception as e:
        status_label.config(text="حدث خطأ أثناء عملية التحميل: " + str(e))

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("تنزيل فيديو من YouTube")

# إنشاء وتخطيط العناصر داخل النافذة
url_label = tk.Label(root, text="رابط الفيديو:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

output_label = tk.Label(root, text="مسار الحفظ:")
output_label.pack()

output_entry = tk.Entry(root, width=50)
output_entry.insert(0, r"C:\Users\user\Downloads")  # تعيين قيمة افتراضية لمربع النص
output_entry.pack()

download_button = tk.Button(root, text="تنزيل الفيديو", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# تشغيل النافذة
root.mainloop()
