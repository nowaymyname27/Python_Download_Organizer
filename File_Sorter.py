import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            file, file_extension = os.path.splitext(filename)
            if file_extension:  # to ignore any folders
                new_folder = os.path.join(folder_destination, file_extension.replace('.', '').upper())
                src = os.path.join(folder_to_track, filename)
                new_destination = os.path.join(new_folder, filename)

                # If the folder doesn't exist, create it
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                
                # Move the file
                shutil.move(src, new_destination)

folder_to_track = "/Users/Galock/Downloads"
folder_destination = "/Users/Galock/Downloads/PDF"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
