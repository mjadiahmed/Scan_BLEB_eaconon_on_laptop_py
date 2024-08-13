# TO SCAN ALL BEACONS:
import asyncio
from bleak import BleakScanner
from tabulate import tabulate

async def run():
    try:
        # Create a BleakScanner instance
        scanner = BleakScanner()

        # Print a header
        print("Scanning for BLE devices...")

        while True:
            try:
                # Discover BLE devices
                devices = await scanner.discover()
                
                # Prepare data for tabulation
                table_data = []
                for device in devices:
                    name = device.name if device.name else "Unnamed"
                    table_data.append([name, device.address, f"{device.rssi} dBm"])
                
                # Print table
                headers = ["Name", "Address", "RSSI"]
                print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))
            
            except Exception as e:
                print(f"Error during scanning: {e}")
            
            # Wait for a bit before scanning again
            await asyncio.sleep(5)  # Adjust the sleep time as needed

    except Exception as e:
        print(f"Error initializing scanner: {e}")

# Run the event loop
asyncio.run(run())

# SCAN BLE BEACONS while filtering by NAME
# import asyncio
# from bleak import BleakScanner

# # Define the name you're interested in
# TARGET_NAME = "nxtBLERTLS"

# async def run():
#     # Scan for BLE devices
#     scanner = BleakScanner()
    
#     while True:
#         devices = await scanner.discover()  # Rescan
#         for device in devices:
#             # Check if device.name is not None
#             if device.name and TARGET_NAME in device.name:
#                 print(f"Found target device: {device.name} - {device.address}")

#         # Wait for a bit before scanning again
#         await asyncio.sleep(5)  # Adjust the sleep time as needed

# # Run the event loop
# asyncio.run(run())

