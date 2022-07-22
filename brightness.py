def set(x):
    with open("/sys/class/backlight/amdgpu_bl1/brightness", "w") as f:
        f.write(str(x))
    f.close()

def view():
    with open("/sys/class/backlight/amdgpu_bl1/brightness", "r") as f:
        return f.read()
