import receiver as rec
import transmitter as trans

ACCESS_TOKEN = "ACCESS_TOKEN"

def main():
    receiver = rec.Receiver(ACCESS_TOKEN)
    transmitter = trans.Transmitter("localhost", 5555)

    transmitter.send_conversations(
        receiver.conversations()
    )

if __name__ == "__main__":
    main()
