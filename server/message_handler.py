from iso8583 import Iso8583


class ISO8583MessageHandler:
    def __init__(self):
        # Any initialization if needed
        pass

    def message_handler(self, message):
        iso_msg = Iso8583()
        iso_msg.setIsoContent(message)

        # Log the incoming message (optional)
        print("Incoming ISO 8583 Message:")
        print(iso_msg.getIsoContent())

        # Handle the ISO 8583 message here
        # For now, just sending back a simple response

        response = Iso8583()
        response.setMTI('0210')  # Transaction response MTI
        response.setBit(39, '00')  # Success response code

        # Pack the message and return it
        return response.getRawIso()