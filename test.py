import usb.core
import usb.util
import sys

dev = usb.core.find(idVendor=0x09da, idProduct=0x9090)

if dev is None:
    raise ValueError('Device not found')

ret = dev.ctrl_transfer(0x80, 0x06, 0xb504,0x1800, 1)
ret = dev.ctrl_transfer(0x80, 0x06, 0xb500,0x9a00, 1)
ret = dev.ctrl_transfer(0x80, 0x06, 0xb504,0xfe00, 1)
#print [hex(x) for x in ret]
ret = dev.ctrl_transfer(0x80, 0x06, 0xb501,0x1a00, 2)
print [hex(x) for x in ret]
ret = dev.ctrl_transfer(0x80, 0x06, 0xb600,0x0002, 8)
print [hex(x) for x in ret]

#dev.attach_kernel_driver(0)
