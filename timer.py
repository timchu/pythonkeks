# This code lets you enter in a time, and then creates a terminal popup window
# when the time is up.
# Very useful for any timed activity. Timchu, 3/16/16.

import time
import os

def print_command(thing_to_print):
    return "printf '" + str(thing_to_print) + "'"

def spawn_terminal(command):
    os.system("gnome-terminal -e 'bash -c \"" + command + "; exec bash \"'")

t = raw_input("Enter time in minutes: ")
time.sleep(60 * float(t))
spawn_terminal(print_command("TIME!"))


# Known error: There's some stupid string escaping business that prevents me from
# printing "TIME IS UP, or anything complex". 
# But I don't have the patience to find it.

# More functions with string escaping errors.
# def multi_print_command(thing_to_print, k):
#     return "printf '" + thing_to_print + "\\n%.0s' {1.." + str(k) + "}"
# Example command:
# command = printf 'HelloWorld\n%.0s' {1..5}
