import usb.core
import usb.util
import sys

dev = usb.core.find(idVendor=0x09da, idProduct=0x9090)

if dev is None:
    raise ValueError('Device not found')

for cfg in dev:
    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
    for intf in cfg:
        sys.stdout.write('\t' + \
                         str(intf.bInterfaceNumber) + \
                         ',' + \
                         str(intf.bAlternateSetting) + \
                         '\n')
        for ep in intf:
            sys.stdout.write('\t\t' + \
                             str(ep.bEndpointAddress) + \
                             '\n')
print hex(usb.util.CTRL_IN)
ret = dev.ctrl_transfer(0x80, 0x06, 0xb600,0x0002, 8)
print [hex(x) for x in ret]

#dev.attach_kernel_driver(0)
