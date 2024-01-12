import paramiko
from getpass import getpass
import os

def download_directory(sftp, remote_dir, local_dir):
    for item in sftp.listdir(remote_dir):
        remote_path = f"{remote_dir}/{item}"
        local_path = os.path.join(local_dir, item)

        try:
            if sftp.stat(remote_path).st_mode & 0o100000:
                # If it's a file, download the file
                sftp.get(remote_path, local_path)
                print(f"{remote_path} successfully downloaded to {local_path}.")
            elif sftp.stat(remote_path).st_mode & 0o040000:
                # If it's a directory, create the directory and download its contents
                os.makedirs(local_path, exist_ok=True)
                download_directory(sftp, remote_path, local_path)
        except Exception as e:
            print(f"Error: {e}")

def upload_directory(sftp, local_dir, remote_dir):
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        remote_path = f"{remote_dir}/{item}"

        try:
            if os.path.isfile(local_path):
                # If it's a file, upload the file to the remote server
                sftp.put(local_path, remote_path)
                print(f"{local_path} successfully uploaded to {remote_path}.")
            elif os.path.isdir(local_path):
                # If it's a directory, create the directory on the remote server and upload its contents
                sftp.mkdir(remote_path)
                upload_directory(sftp, local_path, remote_path)
        except Exception as e:
            print(f"Error: {e}")

def ssh_transfer(username, hostname, password, port, operation, local_path, remote_path):
    try:
        # Establish SSH connection
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=password)

        # Establish SFTP connection
        sftp = paramiko.SFTPClient.from_transport(transport)

        if operation == "download":
            # Download directory and its contents
            download_directory(sftp, remote_path, local_path)

        elif operation == "upload":
            # Upload directory and its contents
            upload_directory(sftp, local_path, remote_path)

        else:
            print("Invalid operation choice. Please enter 'download' or 'upload'.")

        # Close connections
        sftp.close()
        transport.close()

    except Exception as e:
        print(f"Error: {e}")

# User input
username = input("Enter your username: ")
hostname = input("Enter the server address: ")
password = getpass("Enter the password: ")
port = int(input("Enter the SSH port (e.g., 1322): "))
operation = input("Choose the operation you want to perform (download/upload): ").lower()

if operation == "download":
    remote_path = input("Enter the remote directory path: ")
    local_path = input("Enter the local target directory: ")
elif operation == "upload":
    local_path = input("Enter the local file or directory path: ")
    remote_path = input("Enter the remote target directory: ")
else:
    print("Invalid operation choice. Please enter 'download' or 'upload'.")

# Perform SSH transfer
ssh_transfer(username, hostname, password, port, operation, local_path, remote_path)
