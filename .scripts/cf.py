import platform
import os
import subprocess
from cutepy import HEX
from colorama import Fore

c = Fore.YELLOW
x = HEX.reset

operating_system = platform.system()

current_shell = os.environ.get('SHELL')

window_manager = "bspwm"

uptime_output = subprocess.check_output(["uptime"]).decode("utf-8").strip()
uptime = uptime_output.split("up ")[-1].split(",")[0].strip()  # Extract the time part

try:
    gtk_theme = subprocess.check_output(["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"]).decode("utf-8").strip().strip("'")
except subprocess.CalledProcessError:
    gtk_theme = "N/A"

try:
    memory_info = subprocess.check_output(["free", "-h"]).decode("utf-8")
    memory = [line.split()[1] for line in memory_info.split('\n') if 'Mem:' in line][0]
except subprocess.CalledProcessError:
    memory = "N/A"

hostname = platform.node()

kernel_version = platform.uname().release.split('-')[0]  # Extract only the desired portion

try:
    num_installed_packages = subprocess.check_output(["dpkg", "-l"]).decode("utf-8").count('\n') - 5  # Subtracting header lines
except FileNotFoundError:
    try:
        num_installed_packages = subprocess.check_output(["rpm", "-qa"]).decode("utf-8").count('\n')
    except FileNotFoundError:
        num_installed_packages = "N/A"

terminal = os.environ.get('TERM')

print(f"xor@void")
print(f"  {c}os{x} ~ {operating_system}")
print(f"  {c}sh{x} ~ {current_shell}")
print(f"  {c}wm{x} ~ {window_manager}")
print(f"  {c}up{x} ~ {uptime}")
print(f" {c}gtk{x} ~ {gtk_theme}")
print(f" {c}mem{x} ~ {memory}")
print(f"{c}host{x} ~ {hostname}")
print(f"{c}kern{x} ~ {kernel_version}")
print(f"{c}pkgs{x} ~ {num_installed_packages}")
print(f"{c}term{x} ~ {terminal}")
