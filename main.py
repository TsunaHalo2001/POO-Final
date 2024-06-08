import pygame
import threading
from constants import bluetoothUUID
from btconnection import *
from game import *


windowOpen = True

btController = False
btinput = "" 

def notification_handler(sender: int, data: bytearray):
    global btinput

    print(f"Received data from {sender}: {data}")
    print(data.decode())
    btinput = data.decode()

async def main():
    global windowOpen, btController

    device = BluetoothDevice()
    await device.scan()
    await device.connect()
    await device.start_notify(bluetoothUUID, notification_handler)
    while windowOpen:
        btController = device.client.is_connected
        await device.ensure_connected(notification_handler)
        await asyncio.sleep(2)  # check connection status every second

def run_pygame():
    global windowOpen

    pygame.init()
    pygame.mixer.init()

    icon = pygame.image.load('img/icon.png')
    pygame.display.set_icon(icon)

    sizeScreen = (1280, 720)
    screen = pygame.display.set_mode(sizeScreen)

    pygame.display.set_caption("Kirby Starship")

    clock = pygame.time.Clock()
    running = True
    dt = 0

    game = Game(screen)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                windowOpen = False

        game.draw(btController)
        
        game.update(dt, btinput)
        game.checkCollisions()
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        game.conts(btController)

    if main_task:
        main_task.cancel()

    pygame.quit()

def run(loop):
    global main_task
    pygame_thread = threading.Thread(target=run_pygame)
    pygame_thread.start()

    main_task = loop.create_task(main())

    try:
        loop.run_until_complete(main_task)
    except asyncio.CancelledError:
        pass

    pygame_thread.join()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    run(loop)