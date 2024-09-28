import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(smtp_server, sender_email, receiver_email, subject, body):
    try:
        # Create the message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f"Email sent successfully to {receiver_email}!")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {e}")

def send_multiple_emails(sender_email, sender_password, receivers, subject, body):
    # Connect to the SMTP server
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()  # Start TLS encryption
        smtp_server.login(sender_email, sender_password)

        # Create threads for each email
        threads = []
        for receiver_email in receivers:
            thread = threading.Thread(target=send_email, args=(smtp_server, sender_email, receiver_email, subject, body))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        print("All emails sent successfully!")
    except Exception as e:
        print(f"Failed to send emails. Error: {e}")
    finally:
        # Close the SMTP connection
        smtp_server.quit()

if __name__ == '__main__':
    # Replace these variables with actual information
    sender_email = 'nikhil22540@gmail.com'
    sender_password = 'kpxu pjvn tupc zcaz'  # Use App Password if 2FA is enabled
    receivers = ['nikhil22540@gmail.com', 'nikhil22540@gmail.com', 'nikhil22540@gmail.com']  # List of recipient emails
    subject = 'Test Email'
    body = 'This is a test email sent from Python.'

    # Send multiple emails concurrently
    send_multiple_emails(sender_email, sender_password, receivers, subject, body)
