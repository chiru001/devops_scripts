import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess

def get_disk_usage():
    # Run the 'df -h' command and capture its output
    result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')  # Convert bytes to string

def send_email(subject, body, to_email):
    from_email = "xxxx@gmail.com"
    app_password = "xxxx xxxx xxxx xxxx"  # # Direct password not taking so we need to create a app https://myaccount.google.com/apppasswords => create a app it will provide pass and paste that password here

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, app_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

# Get the disk usage
disk_usage = get_disk_usage()

# Send the disk usage output in an email
send_email("Disk Space Usage Report", disk_usage, "xxxx@gmail.com")
