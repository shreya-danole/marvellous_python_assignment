import psutil

def ProcessDisplay(name):
    border = "*" * 50
    print(border)
    print(f"Information of running processes with name: {name}")
    print(border)

    found = False

    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            if proc.info['name'].lower() == name.lower():
                found = True
                # Add VMS in MB
                proc_info = proc.info
                proc_info['vms'] = f"{proc.memory_info().vms / (1024 * 1024):.2f} MB"
                print(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if not found:
        print(f"No running process found with name: {name}")

def main():
    # Example: Replace this with actual process name like "chrome.exe"
    ProcessDisplay("CalculatorApp.exe")

if __name__ == "__main__":
    main()
