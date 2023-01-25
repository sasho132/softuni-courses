class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()
while command != "Stop":
    command_line = command.split(" ")
    current_sender = command_line[0]
    current_receiver = command_line[1]
    current_content = command_line[2]
    email = Email(current_sender, current_receiver, current_content)
    emails.append(email)
    command = input()


send_emails = [int(x) for x in input().split(", ")]

for current_email in send_emails:
    emails[current_email].send()

for temp_email in emails:
    print(temp_email.get_info())
