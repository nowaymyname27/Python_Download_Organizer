# Importing required libraries
import os  # Used for operating system related operations like listing directories, paths etc.
import shutil  # Used for operations related to files like moving files etc.
import time  # Used for time related operations like delaying the execution of the script.
from watchdog.observers import Observer  # The Observer watches for any changes in the file system.
from watchdog.events import FileSystemEventHandler  # The event handler responds to changes in the file system.

# Defining the event handler class that responds to changes in the file system.
class MyHandler(FileSystemEventHandler):

    # This method gets called when a file in the watched folder is modified.
    def on_modified(self, event):
        # Loop through all files in the tracked folder.
        for filename in os.listdir(folder_to_track):
            # Separate file name and file extension
            file, file_extension = os.path.splitext(filename)
            # If there is a file extension (this ignores directories).
            if file_extension:
                # Define a new folder for each file type based on its extension.
                new_folder = os.path.join(folder_destination, file_extension.replace('.', '').upper())
                # Define the source path.
                src = os.path.join(folder_to_track, filename)
                # Define the destination path.
                new_destination = os.path.join(new_folder, filename)
                # If the folder doesn't exist, create it.
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                # Move the file to the new destination.
                shutil.move(src, new_destination)

folder_to_track = "/Users/Galock/Downloads"  # This is the directory you are monitoring
folder_destination = "/Users/Galock/Downloads"  # This is where new folders for each file type will be created


# Create an event handler object
event_handler = MyHandler()
# Create an observer object
observer = Observer()
# Tell the observer to use the event handler to watch the folder to track
observer.schedule(event_handler, folder_to_track, recursive=True)
# Start the observer
observer.start()

# Keep the script running and watch for changes.
try:
    while True:
        time.sleep(10)  # Sleep for 10 seconds before the next check
except KeyboardInterrupt:  # If user hits Ctrl+C (or Cmd+C), then exit the loop
    observer.stop()  # Stop the observer

observer.join()  # Wait until the observer thread finishes, i.e., until the script is stopped.
