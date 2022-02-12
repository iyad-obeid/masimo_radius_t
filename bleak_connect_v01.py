import asyncio
from bleak import BleakScanner, BleakClient

async def demo_scan():
    devices = await BleakScanner.discover()
    for d in devices:
        if "Radius" in d.name:
            print("")
            print(d)

            print("\nNAME: \t", d.name)
            print("ADDR:\t",d.address)
            print("RSSI:\t",d.rssi)
            print("META:")
            print(d.metadata)
            print("")
        
            async with BleakClient(d.address) as client:
                svcs = await client.get_services()
                print("Services:")
                for service in svcs:
                    print(service)



asyncio.run(demo_scan())     

'''
OUTPUT

CB:53:0E:AC:24:34: RadiusT

NAME:    RadiusT
ADDR:    CB:53:0E:AC:24:34
RSSI:    -55
META:
{'uuids': ['5c0e1000-8b06-43fb-9e21-e4261db7d0b2'], 'manufacturer_data': {579: b'\x02\x03\x01\x18\x10\x00\xcbS\x0e\xac$4'}}

Services:
00001800-0000-1000-8000-00805f9b34fb (Handle: 1): Generic Access Profile
00001801-0000-1000-8000-00805f9b34fb (Handle: 10): Generic Attribute Profile
5c0e1000-8b06-43fb-9e21-e4261db7d0b2 (Handle: 11): Unknown

'''