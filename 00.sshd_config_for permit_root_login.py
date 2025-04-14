import subprocess
def permit_root_login (filepath,key,value,service_name):
    with open(filepath, "r") as file:
        lines = file.readlines()
    with open (filepath, "w") as file:
        for line in lines:
            if key in line:
                file.write(f'{key} {value}\n')
            else:
                file.write(line)
    verify_changes(filepath,key)
    restart_service(service_name)

def verify_changes(filepath, key):
    with open(filepath, "r") as file:
        lines = file.readlines()
    print("\n##### Updated sshd_config File #####")
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith(key):
            # Only color the updated key line
            print(f"\033[93m{stripped_line}\033[0m")
        else:
            print(stripped_line)
    print("####################################\n")



def restart_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "restart", service_name], check=True)
        print(f'{service_name} restarted successfully')
    except subprocess.CalledProcessError as e:
        print(f'found error kind check this {e}')



permit_root_login("/etc/ssh/sshd_config", "PermitRootLogin", "yes", "sshd")
