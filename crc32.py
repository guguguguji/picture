import binascii
import string

dic=string.printable     #各种打印字符

crc1 = 0xEA4446B6
crc2 = 0xED7987DE
crc3=0x46FE0943
crc4=0x4BE30989
crc5=0xB31975C0
crc6=0xD6BB1BEF

def CrackCrc(crc):
    for i in dic :
        for j in dic:
            s=i+j
            if crc == (binascii.crc32(s.encode()) & 0xffffffff):
                print(s,end='')
CrackCrc(crc1)
CrackCrc(crc2)
CrackCrc(crc3)
CrackCrc(crc4)
CrackCrc(crc5)
CrackCrc(crc6)

