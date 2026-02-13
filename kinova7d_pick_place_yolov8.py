import subprocess
import tkinter as tk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VENV_PYTHON_EXE = r"C:\Users\sadhil\Documents\VS CODE\Machine Learning\ml_env\Scripts\python.exe"
PYTHON_SCRIPT = os.path.join(BASE_DIR, r"bottle_tracking_and_saving\homography_main.py")
CPP_EXE = os.path.join(BASE_DIR, r"move_to_point_angular_input\main.exe")


def run_python_opencv():
    subprocess.Popen(
        [VENV_PYTHON_EXE, PYTHON_SCRIPT],
        cwd=BASE_DIR,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    
def run_cpp():
    subprocess.Popen(
        [CPP_EXE],
        cwd=BASE_DIR,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


# ---- GUI ----
root = tk.Tk()
root.title("Program Launcher")
root.geometry("300x150")

tk.Button(
    root,
    text="Calibrate Camera / Start Tracking",
    command=run_python_opencv,
    height=2
).pack(pady=10)

tk.Button(
    root,
    text="Pick and Place Object",
    command=run_cpp,
    height=2
).pack(pady=5)

root.mainloop()