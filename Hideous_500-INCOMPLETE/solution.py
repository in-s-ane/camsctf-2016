mappings = {
    0x04:"A",
    0x05:"B",
    0x06:"C",
    0x07:"D",
    0x08:"E",
    0x09:"F",
    0x0A:"G",
    0x0B:"H",
    0x0C:"I",
    0x0D:"J",
    0x0E:"K",
    0x0F:"L",
    0x10:"M",
    0x11:"N",
    0x12:"O",
    0x13:"P",
    0x14:"Q",
    0x15:"R",
    0x16:"S",
    0x17:"T",
    0x18:"U",
    0x19:"V",
    0x1A:"W",
    0x1B:"X",
    0x1C:"Y",
    0x1D:"Z",
    0x1E:"1",
    0x1F:"2",
    0x20:"3",
    0x21:"4",
    0x22:"5",
    0x23:"6",
    0x24:"7",
    0x25:"8",
    0x26:"9",
    0x27:"0",
    0x28:"\n",
    0x2C:" ",
    0x2D:"_",
    0x2E:"=",
    0x2F:"{",
    0x30:"}",
    0x31:"|",
    0x33:";",
    0x34:"'",
    0x36:",",
    0x37:".",
    0x38:"?",
    0x55:"*",
    0x56:"-",
    0x57:"+",
    0xCC:"#"
}

nums = []
keys = open('data.txt')
for line in keys:
    split = line.split(":")
    # Only keep the packets that are valid
    if split[2] != "00" and split[3] == "00":
        nums.append(int(split[2], 16))

keys.close()

caps = False

output = ""
for n in nums:
    if n in mappings:
        if caps:
            output += mappings[n]
        else:
            output += mappings[n].lower()
    elif n == 0x2A:
        # Backspace
        output = output[:-1]
    elif n == 0x39:
        # Caps lock
        caps = not caps

print output

# $ tshark -r hideous.pcap -T fields -e usb.capdata -Y 'usb.endpoint_number == 0x81 && frame.cap_len == 35' > data.txt
