from typing import Protocol

class Drawable(Protocol):
    def draw(self):
        ...


class Circle:
    def draw(self):
        print("Drawing Circle")


class Square:
    def draw(self):
        print("Drawing Square")


def render(obj: Drawable):
    obj.draw()


circle = Circle()
square = Square()

render(circle)
render(square)


from typing import Protocol


class NotificationService(Protocol):

    def send(self, message: str) -> None:
        ...


class EmailService:

    def send(self, message: str) -> None:
        print("Sending email:", message)


class SMSService:

    def send(self, message: str) -> None:
        print("Sending SMS:", message)


class PushService:

    def send(self, message: str) -> None:
        print("Sending push notification:", message)


def notify(service: NotificationService, message: str) -> None:
    service.send(message)


email = EmailService()
sms = SMSService()
push = PushService()

notify(email, "Hello!")
notify(sms, "Hello!")
notify(push, "Hello!")

