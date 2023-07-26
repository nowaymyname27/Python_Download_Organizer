# File Sorter

## Description
The `File Sorter` is a Python script that monitors a specific folder and automatically sorts files by their extensions. When a new file appears in the watched folder, it is moved to a corresponding subfolder named after the file's extension. If this subfolder does not exist, it's created. 

## How to Use
1. Clone the repository or download the Python script file.

2. Open the Python script and replace the paths in these lines with your desired paths:
   ```python
   folder_to_track = "/Users/Galock/Downloads"  # This is the directory you are monitoring
   folder_destination = "/Users/Galock/Desktop/File Sorter"  # This is where new folders for each file type will be created
   ```
   Here, `folder_to_track` is the directory that the script will monitor for new files, and `folder_destination` is the directory where new folders will be created for each file type.

3. Run the script. It will continue running and monitoring the specified directory until you stop it. 

   You can run the script using this command in the terminal:
   ```bash
   python3 file_sorter.py
   ```
   Replace `file_sorter.py` with the actual name of your script.

## Stopping the Script
The script will continue to run until you stop it. If you're running the script in the terminal, you can stop it by pressing `Ctrl+C`. This sends an interrupt signal to the script, which causes it to stop. 

If the script is running in the background, you'll need to manually kill the process. Find the process ID (PID) with the `ps` command, and then use the `kill` command:
```bash
ps aux | grep python3  # Finds PIDs for all running python3 processes
kill -9 <PID>  # Replace <PID> with the actual process ID
```

## Dependencies
The `File Sorter` script depends on the [Watchdog](https://pypi.org/project/watchdog/) Python library. To install Watchdog, run this command in your terminal:
```bash
pip install watchdog
```

## Note
This script was designed and tested on a system running Python 3. Ensure you have the correct version of Python installed before running.

---

Hopefully, this README provides clear instructions for how to use your script!
