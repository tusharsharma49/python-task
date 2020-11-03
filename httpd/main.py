import os
os.system('systemctl stop firewalld')
os.system('chmod +x newfile.sh')
check = os.system('rpm -q httpd')

while True:
    choice = int(input('Enter your choice\n1. Start Server\n2. Stop Server\n3. Modify Web file\n4. Modify httpd service5. To exit\nEnter your choice:'))
    if choice == 1:
        os.system('systemctl start httpd')
    elif choice == 2:
        os.system('systemctl stop httpd')
    elif choice == 3:
        ch = input('Press Y/y to modify Or create a file\nAny other charachter to exit\nEnter your choice:')
        if ch==1:
            print('Enter your site code')
            os.system('./newfile.sh')
        else:
            exit()
    elif choice==4:
        ch2 = int(input('Press 1. to install httpd\nPress 2. for remove httpd\nEnter your choice: '))
        if ch2==1:
            print('Installing httpd.....')
            os.system('yum install httpd')
        elif ch2==2:
            print('Uninstalling httpd.....')
            os.system('yum remove httpd')
    elif choice==5:
        exit()
else:
    print('Enter correct number')