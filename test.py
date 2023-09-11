import os

xdo_window_id = os.popen('xdotool getactivewindow').read()
print('xdo_window_id:', xdo_window_id)
