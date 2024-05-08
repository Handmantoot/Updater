from logging import root
import subprocess

def update_packages(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            package = line.strip()
            update_command = f'yum update -y {package}'
            subprocess.run(update_command, shell=True)

if __name__ == '__main__':
    file_path = /root/my_scripts/applicationlist #Seperate text file named packages.txt 
    update_packages(file_path)
