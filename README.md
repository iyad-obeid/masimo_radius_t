# masimo_radius_t

The two log files can be opened in Wireshark. Notes on how they were acquired are in the [log_notes.txt](log_notes.txt) file.

Briefly:
* 00.log captures the complete pairing and data acquisition process
* 01.log starts with the Pixel and Radius-T already paired, so they just need to connect, trigger, and then data-stream

Connections are between Google Pixel and a [Masimo Radius-T](https://www.masimo.com/products/sensors/radius-t/)

### Helpful downloads
* [Android Studio](https://developer.android.com/studio/)
* [Wireshark Packet Analyzer](https://www.wireshark.org/)
* [Getting Started with Bluetooth Low Energy](https://vdoc.pub/documents/getting-started-with-bluetooth-low-energy-tools-and-techniques-for-low-power-networking-32o2gep4g4vg)

### How to snoop bluetooth packets on Android
* on Android phone, enable bluetooth HCI snoop log in developer options on phone - restart bluetooth
* connect phone to PC with USB cable. if phone requests permission to accept usb connection, click Accept
* on PC, open a windows command line and create a bugreport file by typing `adb.exe bugreport bugreport` Note that `adb.exe` is installed as part of Android Studio and should be located in `C:\Users\[user]\AppData\Local\Android\sdk\platform-tools`
* move `bugreport.zip` to a dedicated folder and unzip the bugreport.zip file: `unzip bugreport.zip` (you might need to do a unix unzip vs a windows unzip)
* in the unzipped files, look for `/FS/data/misc/bluetooth/logs/btsnoop_hci.log`
* open log with wireshark
* be sure to turn off HCI snoop log in the developer options when you're done

### Decoding the data packet
* The transmitted data packets have 76-byte data frames
* Bytes 0-2 are a packet header
* Bytes 3-4 are a timestamp
* Bytes 5-6 are an unsigned 16-bit int (`uint16_t`) which give the temp in milli Celsius

Note that if the sensor is not attached to the body, it will transmit temperatures of `0x00`
