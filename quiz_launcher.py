#!/usr/bin/env python3
import subprocess
import os

def launch_quiz():
    # Get the path to the quiz script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    quiz_script = os.path.join(current_dir, 'quiz.py')
    
    # Create a shell script that will run the quiz and wait for input before closing
    shell_script = os.path.join(current_dir, 'run_quiz.sh')
    with open(shell_script, 'w') as f:
        f.write(f'''#!/bin/bash
python3 "{quiz_script}"
echo "Press Enter to close this window..."
read''')
    
    # Make the shell script executable
    os.chmod(shell_script, 0o755)
    
    # Try to open in a new terminal window
    try:
        # For GNOME Terminal (Ubuntu default)
        subprocess.Popen(['gnome-terminal', '--', shell_script])
    except FileNotFoundError:
        try:
            # For KDE's Konsole
            subprocess.Popen(['konsole', '-e', shell_script])
        except FileNotFoundError:
            try:
                # For xterm
                subprocess.Popen(['xterm', '-e', shell_script])
            except FileNotFoundError:
                print("No supported terminal found. Running in current window...")
                subprocess.run(['python3', quiz_script])
                input("Press Enter to close...")

if __name__ == "__main__":
    launch_quiz()