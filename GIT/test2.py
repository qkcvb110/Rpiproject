import can
import time
# create a bus instance
# many other interfaces are supported as well (see documentation)
bus = can.Bus(interface='socketcan',
              channel='can0',
              receive_own_messages=True)

# send a message
message = can.Message(arbitration_id=0x11, is_extended_id=False,
 
                      data=[0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38])
while 1:
    bus.send(message, timeout=0.2)
    time.sleep(1)
# iterate over received messages
for msg in bus:
    print(f"{msg.arbitration_id:X}: {msg.data}")

# or use an asynchronous notifier
notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])