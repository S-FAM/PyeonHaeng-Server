import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials


class PushNotificationModule:
    def __init__(self) -> None:

        # 초기화되면 Admin SDK를 사용하여 다음 유형의 작업을 수행
        __cred = credentials.Certificate("keys/serviceAccountKey.json")
        firebase_admin.initialize_app(__cred)

    def send_push(self, *, title: str, body: str, verbose=False) -> bool:
        try:
            # 사용자에게 푸시알림을 전송하기 위해 topic을 이용
            topic = "PyeonHaeng"

            # See documentation on defining a message payload.
            message = messaging.Message(
                notification=messaging.Notification(title=title, body=body),
                topic=topic,
            )

            # Send a message to devices subscribed to the combination of topics
            # specified by the provided condition.
            response = messaging.send(message)
            # Response is a message ID string.
            if verbose:
                print("Successfully sent message:", response)
        except Exception as error:
            if verbose:
                print(error)
            return False
        return True


if __name__ == "__main__":
    PushNotificationModule().send_push(
        title="3월 제품 업데이트 두 번째 :)!", body="3월 제품 업데이트가 완료되었습니다!"
    )
