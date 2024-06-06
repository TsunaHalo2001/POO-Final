import pygame
import threading
from btconnection import *
from player import Player
from constants import bluetoothUUID, ratio05

windowOpen = True

btinput = ""

def notification_handler(sender: int, data: bytearray):
    global btinput

    print(f"Received data from {sender}: {data}")
    print(data.decode())
    btinput = data.decode()

async def main():
    global windowOpen

    device = BluetoothDevice()
    await device.scan()
    await device.connect()
    await device.start_notify(bluetoothUUID, notification_handler)
    while windowOpen:
        await device.ensure_connected(notification_handler)
        await asyncio.sleep(2)  # check connection status every second

def run_pygame():
    global windowOpen

    pygame.init()
    sizeScreen = (1280, 720)
    screen = pygame.display.set_mode(sizeScreen)
    doubleScreen = (screen.get_width() * 2, screen.get_height() * 2)
    twoThirdsScreen = (int(screen.get_width() * 2 / 3), int(screen.get_height() * 2 / 3))
    bgSpeed = screen.get_width() * ratio05
    clock = pygame.time.Clock()
    running = True
    dt = 0
    tcount = 0

    score = 0

    # Load the background image (replace 'background.jpg' with your image file)
    background = []
    background.append(pygame.image.load('img/bg1.jpg'))
    background.append(pygame.image.load('img/bg2.jpg'))
    background.append(pygame.image.load('img/bg3.jpg'))
    background.append(pygame.image.load('img/bg4.jpg'))
    background.append(pygame.image.load('img/bg4.jpg'))
    for i in range(len(background)):
        background[i] = pygame.transform.scale(background[i], (doubleScreen[0], doubleScreen[0]))

    background_x = []
    for i in range(len(background)):
        background_x.append(0)
    background_x[4] = doubleScreen[0] + 1

    player1 = Player(screen)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                windowOpen = False

        if score < 40:
            background_x[0] -= bgSpeed

            screen.blit(background[0], (int(background_x[0]), -screen.get_width()))

        elif score >= 40 and score < 80:
            background_x[1] -= bgSpeed

            screen.blit(background[1], (int(background_x[1]), -screen.get_width()))

        elif score >= 80 and score < 120:
            background_x[2] -= bgSpeed

            screen.blit(background[2], (int(background_x[2]), -twoThirdsScreen[1]))

        elif score >= 120:
            background_x[3] -= bgSpeed
            background_x[4] -= bgSpeed

            if background_x[3] < -doubleScreen[0]:
                background_x[3] = doubleScreen[0]

            if background_x[4] < -doubleScreen[0]:
                background_x[4] = doubleScreen[0]

            screen.blit(background[3], (int(background_x[3]), -twoThirdsScreen[1]))
            screen.blit(background[4], (int(background_x[4]), -twoThirdsScreen[1]))

        player1.draw()
        player1.oldPos = [player1.pos.x, player1.pos.y]
        keys = pygame.key.get_pressed()
        player1.move(dt, keys)
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        tcount += 1

        if tcount % 30 == 0:
            player1.tstate += 1

        if tcount % 60 == 0:
            print("Score: ", score)
            score += 1
            tcount = 0

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