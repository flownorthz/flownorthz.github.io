import os
import sys
import re
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import yt_dlp
import ffmpeg
import platform
from datetime import datetime

# ตัวแปรสถานะการยกเลิก
cancel_flag = threading.Event()
process_ref = None

def get_video_duration(filename):
    try:
        probe = ffmpeg.probe(filename)
        return float(probe['format']['duration'])
    except ffmpeg.Error as e:
        log(f"ไม่สามารถอ่านความยาววิดีโอได้: {e}")
        return 0

def delete_file(file_path):
    try:
        os.remove(file_path)
        log(f"ลบไฟล์: {file_path}")
    except Exception as e:
        log(f"ไม่สามารถลบไฟล์ {file_path}: {e}")

def delete_webm_files(output_dir, title):
    for file in os.listdir(output_dir):
        if file.endswith(".webm") and title in file:
            delete_file(os.path.join(output_dir, file))

def convert_webm_to_mp3(input_path, output_path):
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vn',
        '-acodec', 'libmp3lame',
        '-y',
        output_path
    ]
    creation_flags = subprocess.CREATE_NO_WINDOW if platform.system() == "Windows" else 0

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=creation_flags
    )
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        log(f"แปลงเสร็จสิ้น: {output_path}")
        delete_file(input_path)
    else:
        log(f"เกิดข้อผิดพลาดในการแปลง: {stderr.decode()}")

def convert_vp9_to_h264_with_progress(input_file, output_file):
    global process_ref, cancel_flag
    duration = get_video_duration(input_file)
    if duration == 0:
        log("ไม่สามารถแปลงไฟล์ได้เพราะไม่สามารถอ่านความยาววิดีโอ")
        return

    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',
        '-y',
        output_file
    ]

    creation_flags = subprocess.CREATE_NO_WINDOW if platform.system() == "Windows" else 0

    process = subprocess.Popen(
        command,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        encoding='utf-8',
        creationflags=creation_flags
    )
    process_ref = process

    time_pattern = re.compile(r'time=(\d+):(\d+):(\d+).(\d+)')

    for line in process.stderr:
        if cancel_flag.is_set():
            process.terminate()
            log("ยกเลิกการแปลงไฟล์")
            return

        match = time_pattern.search(line)
        if match:
            h, m, s, ms = map(int, match.groups())
            current_time = h * 3600 + m * 60 + s + ms / 100
            progress = (current_time / duration) * 100
            progress_var.set(progress)
            root.update_idletasks()

    process.wait()
    process_ref = None
    if not cancel_flag.is_set():
        log("การแปลงเสร็จสิ้น.")
        delete_file(input_file)

def download_media(url, output_dir, mode='audio'):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    
    # ตั้งค่า format ให้ยืดหยุ่นมากขึ้น
    if mode == 'audio':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, f'%(title)s_{timestamp}.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {
            'format': 'bv*+ba/best',  # ใช้ bestvideo+bestaudio ถ้ามี, ตกลงมาใช้ best
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(output_dir, f'%(title)s_{timestamp}.%(ext)s'),
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            log("กำลังตรวจสอบฟอร์แมตที่มี...")
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

            # สำหรับ video ที่บางครั้งชื่อเป็น .webm แม้ตั้ง merge_output_format แล้ว
            if mode == 'video' and not filename.endswith('.mp4'):
                filename = os.path.splitext(filename)[0] + '.mp4'

            return filename

    except yt_dlp.utils.DownloadError as e:
        log(f"เกิดข้อผิดพลาดในการดาวน์โหลด: {e}")
        raise


def browse_folder():
    path = filedialog.askdirectory()
    if path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, path)

def open_folder(path):
    if os.path.isdir(path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

def log(message):
    output_text.insert(tk.END, message + "\n")
    output_text.see(tk.END)

def start_download():
    global cancel_flag
    cancel_flag.clear()
    url = url_entry.get()
    output_dir = output_entry.get()
    mode = mode_var.get()

    if not url or not output_dir:
        messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ลิงก์และโฟลเดอร์บันทึก")
        return

    progress_var.set(0)
    output_text.delete(1.0, tk.END)

    threading.Thread(target=run_process, args=(url, output_dir, mode), daemon=True).start()

def run_process(url, output_dir, mode):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log("สร้างโฟลเดอร์ใหม่แล้ว")

        log("กำลังดาวน์โหลด...")
        if cancel_flag.is_set():
            log("ยกเลิกก่อนดาวน์โหลด")
            progress_var.set(0)
            return

        file_path = download_media(url, output_dir, mode)
        log("ดาวน์โหลดเสร็จสิ้น")

        if cancel_flag.is_set():
            log("ยกเลิกหลังดาวน์โหลด")
            progress_var.set(0)
            return

        basename = os.path.splitext(os.path.basename(file_path))[0]

        if mode == 'audio':
            if file_path.endswith(".webm"):
                mp3_path = os.path.join(output_dir, f"{basename}.mp3")
                convert_webm_to_mp3(file_path, mp3_path)
            else:
                log("ไฟล์ไม่ใช่ .webm")
        else:
            delete_webm_files(output_dir, basename)
            output_mp4 = os.path.join(output_dir, f"{basename}_h264.mp4")
            convert_vp9_to_h264_with_progress(file_path, output_mp4)

        log("กระบวนการเสร็จสมบูรณ์")
        progress_var.set(0)
    except Exception as e:
        log(f"เกิดข้อผิดพลาด: {e}")
        progress_var.set(0)

def cancel_download():
    cancel_flag.set()
    progress_var.set(0)
    log("กำลังยกเลิก...")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------- GUI ------------

font = ('Arial', 12)
bg_color = "#f7f7f7"
button_bg = "#4CAF50"
button_fg = "white"
entry_bg = "#e1e1e1"
entry_fg = "#333"
label_fg = "#333"

root = tk.Tk()
root.title("Overflow YouTube Downloader")
root.geometry("400x600")
root.config(bg=bg_color)
root.iconbitmap(resource_path("ytdl-1.ico"))

logo_image = Image.open(resource_path("ytdl-1.ico"))
logo_image = logo_image.resize((120, 120))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg=bg_color)
logo_label.image = logo_photo
logo_label.pack(pady=10)

tk.Label(root, text="ลิงก์ YouTube: (เปลี่ยนภาษาเป็นอังกฤษก่อน)", font=font, fg=label_fg, bg=bg_color).pack(anchor='w', padx=20, pady=(10, 0))
url_entry = tk.Entry(root, font=font, width=70, bg=entry_bg, fg=entry_fg)
url_entry.pack(padx=20)

tk.Label(root, text="โฟลเดอร์บันทึก:", font=font, fg=label_fg, bg=bg_color).pack(anchor='w', padx=20, pady=(10, 0))
output_frame = tk.Frame(root, bg=bg_color)
output_frame.pack(padx=20, fill='x')
output_entry = tk.Entry(output_frame, font=font, width=20, bg=entry_bg, fg=entry_fg)
output_entry.pack(side='left', fill='x', expand=True)
tk.Button(output_frame, text="เลือก...", font=font, command=browse_folder, bg=button_bg, fg=button_fg).pack(side='right')

tk.Label(root, text="โหมด:", font=font, fg=label_fg, bg=bg_color).pack(anchor='w', padx=20, pady=(10, 0))
mode_var = tk.StringVar(value='audio')
tk.Radiobutton(root, text="Audio (Mp3)", variable=mode_var, value='audio', font=font, bg=bg_color).pack(anchor='w', padx=40)
tk.Radiobutton(root, text="Video (Mp4)", variable=mode_var, value='video', font=font, bg=bg_color).pack(anchor='w', padx=40)

button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)
tk.Button(button_frame, text="เริ่มดาวน์โหลด", font=font, command=start_download, bg=button_bg, fg=button_fg).pack(side='left', padx=5)
tk.Button(button_frame, text="ยกเลิก", font=font, command=cancel_download, bg="#f44336", fg="white").pack(side='left', padx=5)
tk.Button(button_frame, text="เปิดโฟลเดอร์", font=font, command=lambda: open_folder(output_entry.get()), bg="#2196F3", fg="white").pack(side='left', padx=5)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill='x', padx=20, pady=(10, 0))

output_text = tk.Text(root, height=10, font=font, bg=entry_bg, fg=entry_fg)
output_text.pack(fill='both', padx=20, pady=10, expand=True)

root.mainloop()

#pyinstaller --noconsole --onefile --icon=ytdl-1.ico --add-data "ytdl-1.ico;." YTDL_BETA02.py
