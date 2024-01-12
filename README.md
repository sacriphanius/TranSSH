# TranSSH
It is used to send files and folders to the target device and receive files and folders from the target device using an SSH connection.


# SSH File Transfer Script

This Python script allows you to perform secure file transfers using SSH/SFTP. You can either download files from a remote server to your local machine or upload files from your local machine to a remote server.

## Prerequisites

- Python 3
- paramiko library

Install the required packages using the following command:

pip install -r requirements.txt

Usage

Clone the repository:
Copy code
git clone https://github.com/sacriphanius/TranSSH.git
Navigate to the project directory:
cd TranSSH
Run the script:
TranSSH.py
Follow the on-screen instructions to enter your credentials and choose the operation (download/upload).
Download
If you choose the 'download' operation, you will be prompted to enter the remote directory path on the server and the local target directory where you want to save the files.

Upload
If you choose the 'upload' operation, you will be prompted to enter the local file or directory path and the remote target directory on the server.

Contributing
If you have suggestions or found a bug, feel free to open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.





 
