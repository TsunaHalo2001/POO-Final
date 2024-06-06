import asyncio
from bleak import BleakScanner, BleakClient
from constants import bluetoothUUID

class BluetoothDevice:
    def __init__(self, device_name="ESP32 Tsuna"):
        self.device_name = device_name
        self.client = None
        self.devices = []
        self.deviceaux = None

    async def scan(self):
        scanner = BleakScanner()
        self.devices = await scanner.discover()
        while self.device_name not in [device.name for device in self.devices]:
            scanner = BleakScanner()
            self.devices = await scanner.discover()
        for device in self.devices:
            print(f"Device: {device.name}, Address: {device.address}")

    async def connect(self):
        for device in self.devices:
            if device.name == self.device_name:
                print(f"Device found: {device}")
                self.deviceaux = device
                self.client = BleakClient(device)
                await self.client.connect()
                print("Connected: ", self.client.is_connected)

    async def start_notify(self, uuid, callback):
        if self.client is not None and self.client.is_connected:
            await self.client.start_notify(uuid, callback)

    async def stop_notify(self, uuid):
        if self.client is not None and self.client.is_connected:
            await self.client.stop_notify(uuid)

    async def print_services(self):
        if self.client is not None and self.client.is_connected:
            services = self.client.services
            for service in services:
                print(f"Service: {service.uuid}")
                for characteristic in service.characteristics:
                    print(f"  Characteristic: {characteristic.uuid}")

    async def ensure_connected(self, notification_handler):
        if self.client is None or not self.client.is_connected:
            print("Reconnecting...")
            try:
                self.client = BleakClient(self.deviceaux)
                await self.client.connect()
                print("Connected: ", self.client.is_connected)
                if self.client.is_connected:
                    await self.start_notify(bluetoothUUID, notification_handler)
            except Exception as e:
                if "Device with address" in str(e) and "was not found" in str(e):
                    print("Device not found")
                else:
                    raise