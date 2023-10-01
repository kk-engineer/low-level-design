
class NotificationUtils:

    @staticmethod
    def send_email(subject: str, content: str):
        # Email sending logic goes here
        print("Sent email with subject: ", subject, " : ", content)

    @staticmethod
    def send_sms(subject: str, content: str):
        # SMS sending logic goes here
        print("Sent SMS with subject: ", subject, " : ", content)

    @staticmethod
    def send_push(subject: str, content: str):
        # Push notification sending logic goes here
        print("Sent push notification with subject: ", subject, " : ", content)