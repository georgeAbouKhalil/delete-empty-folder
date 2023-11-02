import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

for filename in os.listdir(desktop):
    try:
        file_path = os.path.join(desktop, filename)

        if os.path.isdir(file_path):
            if os.listdir(file_path):  # Check if the folder is not empty
                print(f"Folder '{filename}' is not empty.")

                # Check if the folder contains subfolders
                subfolders = [f for f in os.listdir(file_path) if os.path.isdir(os.path.join(file_path, f))]
                if subfolders:
                    print(f"Folder '{filename}' contains subfolders: {subfolders}")

                    # Check and delete empty subfolders
                    for subfolder in subfolders:
                        subfolder_path = os.path.join(file_path, subfolder)
                        if not os.listdir(subfolder_path):
                            os.rmdir(subfolder_path)
                            print(f"Empty subfolder '{subfolder}' Deleted")

                # Check if the main folder is empty
                if not os.listdir(file_path):
                    os.rmdir(file_path)
                    print(f"Empty folder '{filename}' Deleted")
                else:
                    print(f"Folder '{filename}' is not empty after handling subfolders.")
            else:
                os.rmdir(file_path)
                print(f"Folder '{filename}' is empty.")
        elif os.path.isfile(file_path):
            with open(file_path, 'r') as f:  # open in readonly mode
                content = f.read()
                if content:  # Check if file content is not empty
                    print(f"File is not empty: {filename}")
                else:
                    os.remove(file_path)
                    print(f"File '{filename}' Deleted")

    except Exception as e:
        print(f"Error cant read: {filename}")
