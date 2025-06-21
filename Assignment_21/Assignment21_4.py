import psutil
import os
import time
import schedule
import sys
import yagmail

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)  # Convert to MB
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def CreateLog(FolderName, email):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, f"Marvellous_{timestamp}.log")

    with open(FileName, "w") as fobj:
        border = "-" * 80
        fobj.write(border + "\n")
        fobj.write("\t\tMarvellous Infosystems Process Log\n")
        fobj.write(f"\t\tLog file created at : {time.ctime()}\n")
        fobj.write(border + "\n\n")

        Data = ProcessScan()
        for value in Data:
            fobj.write(f"{value}\n\n")

        fobj.write(border)

    print(f"Log file created: {FileName}")

    # Send the email with the log
    SendEmail(email, FileName)

def SendEmail(recipient_email, log_path):
    try:
        # Replace these with your actual Gmail credentials
        sender_email = "your_email@gmail.com"
        sender_password = "your_app_password"

        yag = yagmail.SMTP(sender_email, sender_password)
        subject = "Marvellous Process Log"
        contents = "Please find attached the latest process log file."
        yag.send(to=recipient_email, subject=subject, contents=contents, attachments=log_path)
        print(f"Email sent successfully to {recipient_email}\n")

    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <FolderName> <RecipientEmail>")
        sys.exit()

    folder = sys.argv[1]
    email = sys.argv[2]

    # Schedule the task every 1 minute
    schedule.every(1).minutes.do(CreateLog, folder, email)

    print("Scheduling started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
