# Import necessary modules from libqtile library
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
import os

# Import FPDF module for generating a PDF of key bindings
from fpdf import FPDF

# Define the modifier key (mod key) for keybindings
mod = "mod4"

# Guess the terminal to be used (default terminal if not specified)
terminal = guess_terminal()
#The user home path
home = os.path.expanduser('~')
# Function to run at startup once. It is used to run commands specified in the 'autostart.sh'
@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# Define the key bindings
keys = [
    # Launches Zathura with a specific PDF file
    Key([mod,"shift"],"i", lazy.spawn("setsid zathura ~/Mqtile.pdf"),desc="Info system keybindings"),

    # Shutdown or reboot the PC using a custom bash script
    Key([mod, "shift"], "x", lazy.spawn(f'{home}/.config/qtile/bash_scripts/ro_sd.sh'), desc="Shutdown || Reboot"),

    # Switch between US and IL keyboard layouts
    Key(["mod1"],"shift_L",  lazy.widget["keyboardlayout"].next_keyboard(), desc="Keyboard layout (US || IL)"),

    # Terminal emulators
    Key([mod], "t", lazy.spawn("kitty"), desc="Terminal kitty -> bash"),
    Key([mod], "a", lazy.spawn("XTerm"), desc="Terminal XTerm ->fish"),
    Key([mod], "m", lazy.spawn("Terminal"), desc="Terminal terminator ->zsh"),

    # Close the focused window
    Key([mod], "c", lazy.window.kill(), desc="Close focused window"),
