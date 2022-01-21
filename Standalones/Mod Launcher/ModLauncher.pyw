from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup
import os, requests, sys,subprocess,getpass,zipfile,urllib.request,time
from winreg import *
from win32com.client import Dispatch

global DebugInstalled
exeIconByte = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x06\x04\x05\x06\x05\x04\x06\x06\x05\x06\x07\x07\x06\x08\n\x10\n\n\t\t\n\x14\x0e\x0f\x0c\x10\x17\x14\x18\x18\x17\x14\x16\x16\x1a\x1d%\x1f\x1a\x1b#\x1c\x16\x16 , #&\')*)\x19\x1f-0-(0%()(\xff\xdb\x00C\x01\x07\x07\x07\n\x08\n\x13\n\n\x13(\x1a\x16\x1a((((((((((((((((((((((((((((((((((((((((((((((((((\xff\xc0\x00\x11\x08\x00*\x002\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\xf0\x15br\xd1\n\x16$4\xe1%\xf1\x17\x18\x19\x1a&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xfa*%\x9d\xe1V2Y\xa0# 7\x07\x19\xc55\xe1\x90\xf5\xbb\xb2\x1f\xf0<T7W\x02\x18\xe0\x00\xf5\x8f\xff\x00fj\xc9\xba\xbdQ\xf7\x98\x0f\xa9\xae\xaat9\xd5\xeeq\xd5\xc4\xf2;X\xd6h\x0f}B\xd0\x7f\xdbZ\x954\xcb\x97P\xc9w\x13)\xe4\x10\xe4\x83\xfaW!=\xe4g\xa3\x83\xf8\xd7o\xa0\xbet[B\x009R\x7fZ+P\xf6QN\xe1\x87\xc4:\xd2qh\x87\xfb.\xec\x8c\x0b\x88\xbf\x06?\xe1P}\x96`\x8c\xd1\xde[\xc8P\x17*\xaf\xbb\x8cV\xecM\x99\x07\x02\xb8\x0f\t\xde\xbd\xc5\xed\xca\xbc\x85\x80\xb6s\x82k:t\xf9\xe3)_cZ\x95y\'\x18\xa5\xb9\xd8[\xdcK\xf6x\xbes\xf7G\xf2\xa2\xa2\xb7\xff\x00Q\x1e9\x1bF?*+\x13s\x8d\xf1u\xfc\x96\xcb\xa7\xc7\x19\xdb\xba\xdf$\xf7\xfb\xc6\xb9f\xbb,r\xccI\xf5&\xb4\xbe!K\xb6}7\x07\xfe]\xbf\xf6c\\\x81\xba\xc7z\xf70\xab\xf7H\xf1q1\xbdFn}\xab\xde\xbd_\xc2\xf2\x16\xf0\xed\x81_\xee\x7fZ\xf0\x86\xbc\xf7\xafi\xf0m\xc9\xff\x00\x84WN<\xf3\x1f\xf55\x8e`\xad\x05\xeam\x81V\x9b\xf4:\x14v\xde3\x9cW\x95x\x06\xe0\xbe\xa7|\t?\xf1\xea\xff\x00\xccW\xa5\x89\xcb69\xac\xe7\xd3\xec\xad#\x9eK[Xa\x91\x91\x81d@\xa4\x8a\xf3\xe9\xd5Q\x8c\xa3\xdc\xef\x9d>iF]\x8bV?\xf1\xe5o\xff\x00\\\xd7\xf9QE\x8f\xfcx\xdb\xff\x00\xd75\xfeTVF\xa7\x07\xe2\xbd\r\xb5\xb9-%\x86\xf2\x18DQye_9\xce\xe2\x7f\xads\xff\x00\xf0\x83\\7MJ\xd7\xf1\xc8\xfe\x95\xea\x92\xdb\xc2%p!\x8f\x1b\x8f\xf0\x8ao\xd9\xe1\xff\x00\x9eQ\xff\x00\xdf"\xba\xa1\x8a\xa9\x04\xa3\x16s\xca\x84$\xee\xcf+_\x01]H\xc1WR\xb4\xc9\xe9\x9c\xff\x00\x85z_\x87-\x7f\xb34;;)\xa7\x81\xe4\x856\x96\r\xc1\xe6\xac\xfd\x9e\x1f\xf9\xe5\x1f\xfd\xf2(\xfb<?\xf3\xca?\xfb\xe4T\xd5\xc4N\xaa\xb4\x99T\xe9F\x9b\xbcK\x91\xb4[\x812C\xff\x00}\x8aK\xc7\x87\xec\xb3bX\xc9\xd8z0\xf4\xaa\x9fg\x87\xfeyG\xff\x00|\x8a>\xcf\x0f\xfc\xf2\x8f\xfe\xf9\x15\xcfc[\x96\xac\x7f\xe3\xc6\xdf\xfe\xb9\xaf\xf2\xa2\xb4-\xe3A\x04`"\x80\x14\x00\x00\xf6\xa2\x90\xcf\xff\xd9'
eawIconByte = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x002\x00\x00\x002\x08\x06\x00\x00\x00\x1e?\x88\xb1\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x13\x92IDAThC\xbd\x9a\tp\x95U\x96\xc7\xcf{/\xdbK\x02!\x1b\x84,\xacaK\x00\xd9\x17\x05e\x19\x84q\x99Q[\xed\x96B\x8b\xea\xb6\x85\xe9\xc5\x99r\x98\xea\xa9ig\x8a\xae\xd6\xe9i\xa7\xd5\xa1\xadV\xdb\xea\xa1\x1d\x87.GdQiad\x93Uvd\x0bK\x08d\x87$d\xdf\x93\xf7\x92\xcc\xffw\xe1c\xc4\xd6\x16m\xabO\xd5\xadoy\xf7\x9e\xfb\xff\x9f\xed\x9e/\xe0\xeb\xe9\xe9\xf1\xd9\xd7,\xcb\x97/\xf7\xdd{\xef\xbd\x81\xf6\xf6\xf6\x98\xf2\xf2\xf2\xc8p8\xec\xef\xee\xee\xeelmmm{\xe2\x89\'\xc2\xd7\xa6}\xad\xf2\xb5\x10\xd9\xbcys\xacd\xbc\xc6\xad]]]c###s\x02\x81\xc0\x00\xbf\xdf\x1f\xd7\xd2\xd2\x12\xe1\x93466v\xb5\xb5\xb55\xea\xb75G\x8e\x1cYQ]]]\xdc\xbbw\xef\x0e\x91\xee\xb9\xa6\xe6O\x92\xafL\xe4\xb5\xd7^\x8b\xe8\xd3\xa7\xcf\xadZ\xff\x84\xc0\xcd\x8f\x8e\x8eN\xd2p\xbaD\xc0\r\xfdf"b\xf2\x8c\xd5\xd6\xd6ZTT\x94\x15\x17\x17\x9b\xc8v\xf5\xeb\xd7\xaf\xa1\xb0\xb0\xf0hBB\xc2\x8b\xf2\xd4>\xadm\xf8SH}i"O=\xf5T\x8c,y\x7f\\\\\xdc2\x8dq"\xe1\x03`\xaf^\xbd\x1cp=\x03\xd4bbb\x1c\x19\x85\x94EDDXgg\xa7UTTXII\x89\xa5\xa6\xa6\xda\xde\xbd{m\xf0\xe0\xc1\xfc\xde%\xef\xbc\x9e\x9c\x9c|\xfa\xdc\xb9s+\xdfy\xe7\x9d\x86k[})\xb9i"\xc4\xfd\x8a\x15+\xee\x9a0a\xc2\x8b\x83\x06\r\xcaNII\xb1`0\xe8\xac,B&\xcbZSS\x93{\x96u\x1d!\xee\x11<r\xfa\xf4i\xf7{UU\x95\t\xb0\x8d\x181\xc2\x94?\xa6p\xb4\x01\x03\x06\xd8\xb8q\xe3B\xf1\xf1\xf1k^}\xf5\xd5\x9f\xf7\xed\xdb\xf7\xfc\x86\r\x1b\xda\xdc\xe2\x9b\x94\x00\x00\xaf\xdd\x7f\xaedee%\xee\xda\xb5\xeb\x15Y\xf6gzL\xc6\xda\xca\x01gy\x85\xbf\x85B!\xeb\xe8\xe8p\x1e\x80\x04\x9e\x01\xb4\x80Y}}\xbd5448RxE\xb9\xe2t^\xbe|\xd9\xfd\x8e\x01 *B\x01\xe9\x1d\x91\x96\x96\x96\x95\x94\x94\xd42o\xde\xbc\xb3n\xe2M\xca\x17zD\xd6\xca\x11\x90\xb5\x02>\x02\xd0\x00\xca\xce\xce\xb6\xf4\xf4tw\x0f)\xac\xea\xdd\x13Fx\x88\xb9\x02\xe4\x08\x13^\x00F\xf0\x02s*++\xed\x85\x17^\xb0\xf1\xe3\xc7\xe3\r\xbb\xef\xbe\xfb\xdc\xfc\x0b\x17.\x10~\x9b\x95\x83\xdf\xc8\xcb\xcbkq\x8bnB\xfc\xd7\xae\x9f)\x02{\x9b,\xbbS\x96v$\x90p8\xec,K\x880jjj\xdc\xc0\xaaW\xae\\1%\xae\xf3\x0e\xe0y\x0fh\x84g\xbcD8B\x9c<y\xfc\xf1\xc7\x9d7\xc9/\xbc\xa3\\i\xcf\xc8\xc88-C\xfcB\xfa\x02n\xe1M\xca\xe7\x86\xd6\xc0\x81\x03\xe7j\xe3\xdfk\xd3\x04\xe2\x9d\x81\xb0)d\x00\x0e`@\x01\x06K\x97\x95\x95\xb9\xd0\xe1wr\x880\xc3\x00x\x05o\xb1\xd6K|\x85\xab{\x1e>|\xb8577\x9b\xf2\x82k\xfb\xa5K\x97Vn\xdf\xbe\xbdF\xfb\x15]\xbcx\xb1s\xd6\xacYn\xdf/\x92\xcf\x0c-\x81\x9b\x9c\x98\x98\xf8\x81<\xd1\x07\xa0^>x\x15\x08\xe0\xde;\xca*\x02x\xc8\xf2;$U\xd9\xec\x81\x07\x1ep\xa1\x83\x10z\x00G\x1f\xf7\x10$\xa7\x9e{\xee9\xfb\xe8\xa3\x8fl\xf2\xe4\xc9\xb6d\xc9\x12GH^\xebQX\x95i\xce\xbb\xeb\xd7\xaf\xff\xbb\xd5\xabWw;%\x7fD\xfe\x80\x88\x94di\xb3\x03\xb2f\x1a\xee\xc6\x92:\xc8\\\x02#^\x82cUox\xe1\x83xI\xcf<\xc6\xc2\x85\x0b\xed\x8e;\xeepk \x07\x19\xc2\x8bR\xcc\x15\xd2\x18\xe6\x83\x0f>p{\x0c\x1d:\xd4\xe5\x18\x84e\xa4F\x9d;\xbf~\xf9\xe5\x97\x7ftM\xfd\xe7\xca\r9B\x98\xc9Z\xff!%iX\x1c\xc5l\xe4\x85\x15\x80!\x06@\xdeC\x02\x10\x08@y\xcf3\x03\xab\xa3c\xed\xda\xb57x\xcd+\xc1\xdc\xeb@t\xa5\x98u\xcc?z\xf4\xa8\xed\xdc\xb9\xd3^\x7f\xfdu[\xb3f\x8dm\xda\xb4\xa97\xf3g\xcc\x98\x91\xe3\x14\xfc\x11\xb9\xc1#"p\xbf\xaa\xcb\xdb\xba\xf5\x03\xcc\xab4l\xca3\x84\xb0b~~\xfe\xf5w\x0cO\x00\x04x\xe6\x11\x86x\x861u\xeaT\xbb\xff\xfe\xfb\xdd{t\xb2\x169p\xe0\x80\x9d={\xb5\xcaR\x8eu\xda\xdb#\x8f<b\xbbw\xefv\x84uH\xb2\xbeT\x9e\\\xfc\xc6\x1bo\x84d\xbc&\x19\xe1\xb8[\xf0)\xb9ND.O\xd1\xe5\x84\x16\xa5ya\x84\x95<o\x00033\xd3\x95G\x12\x1b\x80\x90\x00\xb0\xf7;sY\xcb\xe0\x19\xe1\x9eR\xfd\xe4\x93O:/\x92\x03\x84\ra\x0b!\x88\xa1\x07\xe0\xe8"\xfc\xf0\xca\xfe\xfd\xfb\xdd3\xa1(\x1c\xa1\x93\'O\xfaT\xd5\xbe\xadP[\xe5\x14\x7fJ\xae\x87\x966\xfc\xbe\x16\xa6yU\x87\r \x822@Q\x81\xa8\xf3l\x08`\xe2\x98P\xe3\x9e+s\x01\x04H\xc0{\x04=\xa0\x1c\x8a\xbc\x83\x0cW*\x15\xdee/\xf4\xf3\x8e\xbd\xf7\xed\xdb\xe7\x9e\xc7\x8c\x19cS\xa6L\xa1\x8d\xe9QY\xefPH\xff\x8d*\xdc6\xa7\xf43\xc4\x11\x91\xc5\x82\x02\xf38\xa0\xb04\xb1\x8f%\xb0\x1aJy\xc7o\xbc\xe3\xd9\xdb\x18\x80\x10`p~\xf0\xec\x01c.\xc4\x11\x9e)\x18\x8cS\xa7N\xb92\xcd|r\x07\xf0\x84$\xb9\xc7\xfc\xdc\xdc\\\xf7\x9e3\x89sH\x06\xa8\x9f>}\xfa\xef\xe7\xce\x9d{n\xcb\x96-\x97\x9d\xc2\xcf\x10GD\xc99GV\xcc\x000J\xb1\xaa\xdcx=)\xd9\x140\xbc\xc7\x8a\xdc\xe3!\xef\x04g\r\xf7\xac\xe77O\x8f\xd7\xf9\xb2\x06O\xf2N\x1d\xb3\xf3 \x86@\x1f\xefIr\xae\x88\xce\x91\xeb{R\x0cJKK\x13>\xfc\xf0\xc3\x94\xa2\xa2\xa2\xf4E\x8b\x16=\xb6l\xd9\xb2T7\xf1S\xe2\x11y\x94\xcdQ\x000\xac\xe3\xddcE6\x85\x14\x02`\x80y\xa4\xd8\x90*E8\xa1\x83\x90Axf t\xb9\x1e\x11\xf4B\x8eu\x10E?yw\xfc\xf8qS\xe7\xeb\xc6\x89\x13\'\\y&\x1c\x953~yd\x8e\x0c0K\xad\xcc\x1a\x15\x8e\x1a\xa7\xf4S\xe2\x93;{Ky\x896M\xc0\xb5X\x14\x00\x1e\x116#A\t\x01\xb9\xd7Ys\xcf\x9e=\x0e\x00\xe0\x98\x03Q\x8f\x08`y&,\x91\xfe\xfd\xfb\xdb\xd8\xb1c]\xb8r\x9a3\x1fo\x92;x]\x9d\xb4[3j\xd4(\xb7\'\xf3Y_WW\xe7\x06\xe5\x1b/*T\xab\xf5\xbcT^:%r\x85:$\xaf\xd6\xfdk\x12\xd0\xe63e\xd1\xef\x92\x03\x80\x03(dP\x86\x00\x00\x0f\xf1\x8c\x15)\xa5\x00\xc1CX\x1f\xcf0\x07\x81\x88\xb7\x0e\xcfa\x00J(@\x11<\xc8={\xa1\x83\xdf1\x1e\xe1D%\xe4LQur8\xd0\xc5o\xc7\x8e\x1ds\xdeR\xa7\x11\xab\xaay\xbb\xbac\xda\xfd\x90\xba\xe3b\xa7\xf4\x9a\x044a\x91\x80\xcef\xa1\xe7\r\x0f8\x9b\x01\x14+\x02\x00\xaf\x90\x80\xb4\x1d4}\x80\x85\x04\xa1Bx\xb1\x06CPB\xd1\x03P\xde3\x0fkS\x14\x10\xf4{\xe5\x97w\xe8 \x94\xbc\xbd\x18\x87\x0f\x1f\xf6\x1aIg4>\x07\xf4{\xfc\xe8\xd1\xa3\xa7\xc9 \xafl\xdc\xb8\xb1\xf2\x93}X@.\xfb\x9e\x14\xe7\xf2\x00\x08\x0f\x08\x9b`\x11\x94\x11\xab^\x82c5\x92\x10"|\x1c\xa9[\xb5!C\x86\xb8\xd6\x82s\x860\x80\x18\xad\x8a\x97\x0b\xace@\x00\x90x\x84+\xc6\x03(d\xf8\x9d\x92\x8bg \xcf^T7\xda}y\xc1\rpI_\xc4\xb0a\xc3\xea\x96.]zC)\xf6\xe94="\xa6\x13\xb0 V\xf7J,\xb9\x01(6C! \x08\r\xef{\xc2\x0b9B\x87\xf9\x84\x03\xa1\x86\x0e<\xc3\x15\x0b\xa3\x17\x82\x00\xe3\xe4\x06\x0c\x9e\x02<\xde\xc5P\xe8\xe1wt\xa3\x07\x03\xa1\x9f{\xa2\x80\xd0\xe3\x9e\xef\x16\xf6\x9b6mZ\xe5\x993g\x96\xa8;>\xabP,R+\xd3\xe9\x93%\xcfI\xc9p@\xb2)\n\xf1\x06\x0b\xbd\xf0\xf2\x1a<6\xc7B\x00\x07(\xbfay\xee?\x19\xff\x00\xf4H0\x14\xbe\xce@x\x0f\xe3@\xc8\xdbG\xa1\xe2\x8c\xc5\xb3W\xc2\xbdp[\xb9r\xa5{\xafO\n\xe7Y>\x899c\xf0&\xbf\xaf[\xb7\xaeR^|Wg\xce2>/\x7f"\x96A\xc2\x80\xc1\x04\\\xebY\t\x0b\x02\x8e\xcd\xb1\x06\xd5\x86o\r\xc0\xb1!@\x01\x04\x08\xee\x01\x82\x11\xf0\x1a\xc4\x10\xbc\xcb3\xe4\x18\xcca.{\xb0\x0e`\x18\x87kAA\xc1ucQ\xc90\xd0\xa1C\x87\x9c\x01\xee\xbc\xf3N\xb7\x06]\x18@$\xe2\'HDrm@\xa0\x97IA\x1c\x96E9\xca\xd8\x182\xdc#\x10\xf2\x88\xe2%\xae\xbc#O\x00\x06YH\x12&\x10\xc5\xfa\xc4tll\xd0m\np\xde{\xfa=\xf0\xe8`\x1d\xc4\t\x9fn_\x8b\xf5J\x88\xb2\x9c\xd1\xc3\xadw\xafX\x19,\xcdB\x9d!\x17\x9a\x18\x0bc2\xf0\x90\x17\xde*\xed>\xe9X\x15\x90\xc2\x1f\x08L\x02\xc0\xb10\x13X\x04X6#\xee\t\x15\x88B\x82y(\x00\x14n&\xae\x93S\x12\x05:Z\x1dl\xa5\xf3\x1e\xe4\xb8\x0e\xcf\x19d\xdf\xf9\xee\xc3\xd2\x1b\xa35\xca\x99`\xac+ \xe8\xf1\xbc\x11\x13\x15a\xc1\xf8(\xebj\xaf\xb1\xfeIq\xd6\xd6\xd3e\xf9\xe7\x0b\xecb\xc19\xcd\x91\x91\x12\xe2D(\xd1\x06\x0e\x18\xe4\xb0`4\x0c\x8dq\xc85y\xac[\x07\xe8s\x01\x01Z\xac\x10H\x03<\x1b`U\x08p\xc5b\x10c\xf0\x1b\x83C\x10\x10\x84\r\xf7\xb8>3+\xcd\xbe\xf1\xd0\x02\xf3G\xfa\xed\xfc\xb9\x0b\xaaD5\xd6\xd5\x1d\xb2\x86\xbaF\xcb\xcb+\xb0\xdb\xe7L\xb5\xc7\x16\xff\xb5eh^SS\x8be\r\xe8oSf\x8c\xb3\xa4\xc8vK\xe9\xd5#p\x11\x16]Un\x97v\xee1\xd5FK\x1e\x94c\xc3\xb3\xc7Zb\x9f\x14\x0b\xc6\x08\x8f\x1a\x90\xb6v\xfe\x0e\x116\x7f\x84OF\xe4\xfb%\xda\xe1\x10\xa1\x0eU\xd2\x7f\x0e\x08\xec\x02Y{$D\xbc\xfc\xc03s\xef\x9c!\x0b\xd0F\\\xfdc\x02\xef\x18\x08\xa1\xe3\xcd\x83\\\xf5\x95\x1akn\xed\x10\x99{\xed\x9b\x0b\xff\xca&N\xc9\xb5aC\xb2d\xc5\x0c\x8b\x89\xd6:\x19\xa4\xb9\xd1\'"\xc9\x96\x19\xef\xb7\xbd\x07\x8eX\x8f>*GN\x1ec\x11\xb2\xf0\x95\xfa6+oS\'=h\x8cE\xa7f\xc9\xa3\xf1N/\x06\xe4\xfc`\xff\x80?\xc2\xe2\xe3\x94\xaf\x11:\xdb\x82\xf1\xf2\xdaY+*\xbe\xa8\xef\x99\xbc\xb2\xf5\xeb\xdf\xfa\x1d\'\xfb\x18y`&\xa0H0\x16\x13\x16\x83\x87\x0c\xb0\x85\x8f\xddcg\xf2\xce[D\x14\x1fT1\x16\x1b\x15\xb0\xde\x8a\xfb\xc4T\xe5C\x82\xf2!1\xde\xe6-\x98a\xf3\xef\xba]\x1e\x08\xcb\x13\x8d.\x84\xfc\xcd\rv\xe4h\x9e\xb5\x87;\xed\xf6YS\xac\xa5\xd1o5W\xc2VZVl\x05\x85\x97\xad\xb5\xb3\xdb.WT\xda\x99\xe3g\xed\xa3]\xc7L\x10es}\nDF\xb9\xf0\xc1\xcb\x94]"\x83\xc4\xa7\xb5\'\xc7\x88\x00Ha\xf0\n\xad\xbfPP\x88\x11wDD\x04\x7f\xeb\x93G\xe6\t\xfcfB\x05+\xf0W\rH\r\x18\x98n\xd9#\xd3-\x10\x15k\xa9\xfe\xb0\xd5\x1e8d4\x1f\xa9\xb7M\xb7\xe8\xc4>\x16\x9b\x94h\xe1P\xd8:\xdaU$\xbap\xb7YqQ\xa1UU\xd6YM\xd9%k\x92\x87"\xe3\x82\xf6\xd2\x8a\xa7\xad\xb4\xe4\xb2\xbd\xb5~\x9f\xa5(Q\xf3O\x1e\xb5\x8ep\x97e\x91\xc0m!\xba[w>\x10\xf3D\x05\xd5\x90s\xcb\xfbb\x04\xfc\x8e\x1d;l\xe6\xcc\x99\x84R\xf5\xe4\xc9\x93\x93E\xd2\xb7u\xeb\xd6\x90\nD\x9b\n\xc1\x0f\xb7o\xdf\xfe\xdf\x01\x95\xb5+"\xb1T\xb9\x12$\x81\xbd\xb2\xda\xd0\xd0d\x97J\xafXGk\xc8\x122\xd2\xedD\xc9\x15\xbb\xdc\x1a\xb6\xa2\x92\n\xabo\tYY\xf1%\xab\xae\xac\xb5\xda\x9az\x9d\xf4EVRTlMu\xf5VW\xdf\xa0\xb5\xcdFGw\xebm\x13m\xcaxJh\x8c\x15\x957\xd8\xe1\xbd\xbbl\xea\xd8\xd1\xd6\xaa*UVVe\xbe\x08\x9d\xf8"@\x04\xb8\xc4W\xcc{\xe5~\xdb\xb6m\xee\x19"999DJ\xc1\xae]\xbb\xfeM\xd7bu\xcbEj.\x17\x89\xf0\x7f\xa9\xb3\xde\xf5\xf0\xc3\x0f\x87\xdd\xa7\xaeb\xfeMY\xe4\x9b\x10!\xfei\xbb\xbdR\x8b\x9b\xdb\xe5\xce[&\x8e\xb2\xe3\x87OYqq\xa9;G(\x99\xb8\x98\x82\x10P\x02\x0e\x1a\x9ci\xd3gNThtX\xfe\x99\x0bn\xfd\xbc\xb9Sll\xeePS\xccYgL_k\x8dM\xb4\xb6\xd2\x12\xab\x08G[c]\xad\x95\x16\x15Y?}\x06\x1f\xda\xb3\xcb\x1a\xeb\xebD\xdd\xe7\xda\x1d\xc2\xe7\xe0\xc1\x83\x8e\x14\xa1\xee\nJf\xe6{\xea\xbf^\x189r\xe4e\x91K\xd78\xad\x051"U\xaa\xeb\xd5ov\x12^\x0b\xde\x97k}\xde\xc9\x8b\x85\x88W\\\xce\x95\x96z\xd6\xdci\xb6{\xe7\x01Y1\xf2\xda\xa1\x19m\x0f~\xebn\x1b?i\x94\xb5\xaa$\x1e?zA\xc5!l:\xcf\xad\xad\xb5\xc9\xa2#\xbam\xc2\xb8Q\x16:\xa9<P\x07\x9b<x\x80\xf5\x9b3\xdb\xa2G\x8f\xb7\x98\xde\xc9\xd6\xda\xa1F\xf4R\x91\xb5J\x7f}c\x83\x9d9]`U\xb5-Vx\x91\xd0\xaa\xe0\x10,\x13\x89\x90\x0e\xc6\xfdJ\xfa\xdf\x96\x94\x94\x94\xa9=y\xe0\xc8\x91#\x93\xd4\xef=\xa5\xbc\xa9\xd77|\xfdu"j\xc2\xa2\x14\xab\xc7\x95\xec\xd7\xff4\xca\xa1\xc3\xe7&\x1e\xe2\\ \xf9h\xf0\xa6\xdd6\xc1.\x95U8K-\xf9\xdeB\xcb\xbd%W\xe7L\x83\xbe\xa4\xba\xec\xb2\xce\x94\x83\x07N\x8b`\x94\rN\x8a\xb7\x1d\x87NYtl\x9ce$\x04,\xb9\xa2\xd4\xd2jj\x95\x1f\xeax\x15j\xfd\x94kq\xb7\xdefA\x9d+~mY_\xa7/D\x19\x8d\xb1y\xf3\x1e[\xf7\xd6F\x88<+C\xfeJ\xf8\xe2\xd4\x017\xed\xdf\xbf\xbf\xea\xd1G\x1f\x8d\x15\xd6Dy"]\x91Q\xf7\xf1\xc7\x1f\x17\\\'\xc2\x8d\xf2\xe2\xdb\x02\xfc\x1bz\x1aB\x8c\xf0\xe1\xe0\xc1\xcd\xb8\x96D$\\\xfa\xa5\xa5\xda\xa2\xc5\x0fZjr\x92e\xf4K6\xbf\xbc\x92\xa1s\xe1\xcc\xe9\xb3\x96w\xfc\x8c\x15](\xb6\xd1\xc3\x06\xdb\xd1c\xe7-.\xb9\x8f\x15\x16\x95YG[\x87\xa5\xf4Q\xd1HI\xb6\xf4\xc6\x1a\xcbh\xad\xb1\n\x91\x8f\rF[\xd2\x84q6\xea\xee\x05\x16\xaf(\xe8T\xf1\xa8\xd5\xd9\x13\xd2u\xf7\x9ecVZ\\y\xac\xf0B\xd1\x01\xe1\xc8R\xbe\xec\x12\xae\x8b\xf2\xcca\xe1\x89\x92Q}\n\xafs`G\xae\x13\xd1\xd7[\x8cN\xeaC\xf2H.dH8\xac\xee\x91joo\xb3\xcc\xf4\x14{\xea\xef\x1f\xb7\x8caC\xac\\\xc9\x9e(\xa0-\xadm\xf6\xe1\xd6\xdd\xb6s\xdb>kok\xd7A\xd9c\xfdEph\xce0\xe5O\x94\xed\xdf{\xd8.\x9c/r\x07h||\x9c\x1a\xbf\x0c\x1b\x96\xad\x10\xebh\xb6\xcc+e*\xdb]\x96\x10CK\xd3\xd7\x12\xfeb\x86\x05\x06\x0f\xb2j\x15\x10\x7fD\x94\x8aH\xe9\xe9\xaa\xfa\xd65\x8a\x94\x82pk\xeb\xfb\xeb\xd6mm\xd5\xb7{\x87<\x94"\\\xc3\xd4\x97\xeds,$\xd7\x89 b}\xa7\xfa\x96\x8d\xca\x07?9\x00\x11*Gn\xceH\x9b2)\xc7&MV\xa7\xda\x15\xb2\xf4\xc1Y\xd6\xae\xba\xbf\xe5\x7fw\xd9\xbbk7Z\xb9B\x8dy\xac!\x14\xf9~\xe9\x9f\xde\xcf|\x8a\x99By\x08\x12\x9cQ\x0c*bl\\\xacB7Ss\x836<\x10\xb2\xd1\xcd5\x16\xd9\xa9\x86\xd3\xa7^\xacw\x94\x05\'\x8c\xb7\xde\x93\'Y8*\xa8\x82\xd2]SQ^\xfe\xec\x956_Ab\xefh\xeb\x15\x95pp\xf9\xf2\x7f\xef\'\x83\x9fW\x88\xb5_\x83~#\x11\x951\xff{\xef\xbd\xf7\xa6\xfa\xa1\x87\x00CU\xfa\xcb{\xe6\xdac\xdfy\xd8\xbai\xcd\xd5\x82\x98,x\xf4l\xb1m\xdcv\xd0j\xaa\xeb]\xeeP]\x00KQ \xc7 \xc5\x89\x8cx\xa1\xca\xc0\xcb\x08\x85\x84\x01iB5::`\xe9\xfeN\x1b\xd9\xd9hm\xe5\x97,+!\xc6\x1aTP\xfa\xaaT\x87G\xe5Z\xa3EZ\xc0\xd7s\xac\xa1\xbe\xe9o\xcbkZzZ\x9a\x9b\xc7\x06"\x02\'\xca\x8aj\x0e\xf2-\x82\xce\x1b\x88 \xca\x93\xfe\xaab\x87\xd5\xd9\xf6\x87\xc8\xb2\x7fZj#r\xb2\xadS\x80\x8e\xee9d\xfb\x0e\x9f\xd3i[\xe3\xea;\x80\x01\x0e\t\xae\x90\xa7\xbaQ\x92)\xe1\x1cj4v4\x96\x10\xf1J:^\x81\x04\xeb!\x94\x91\x91^\x1c\xea\xea\xf8 \x14\xea\xb8+%\xb2;37Z\x1fx\xd5UvE\x05 \xccY\x93\xda\xd7\x02\xc3s\xac\'!\x91\xe5[\x82\xb1q?\xcd;\x97\x1f,\xbb\\]\xd8\xddV_\xb7o_^\x9d\xfbs\xd0\'E\x16\xbc\xac\xc4~D\xd6\xedd\xc3\r\xeb\xb6\xaa\xbd\xa8\xb1_\xbe\xf8\x86\xfdz\xe5z;u\xea\xac\x03\x8cu=/\x00\x90\xb0\xf9d\x1bO\xa5\xe3\xaf&\xde;\x88)\xb6\xdd\xe1F\xce\xb1\x1eT\\\xd5\xcf\xe5\xb74\xb5?\x1f5*.\xbb\xc1\x17\xb5p_G\xf0\xd8\xf9\x01#\xedBd\xac\x15\xe9\\*U\xebS\xa93\'99\xd6\x9f\x10\x17=\xbf\xb1\xaen\xfb\x88\xa1\x83\x86\xef\xdd\xbe\xf7\xe2\xfc\xf9\x0f\xfd\x7f\xf9u\x0c>%\xaa\x0c\x8b\x04\xe8?\x15f\x91\x0b\xee\x99mM\xaa\xf3;\xb6\x1dp\x9bS\xcd\xb0$B\xe8\xe0\r\xfe\x8c\x031\xbcA\xa5\xbb\n\xf0\xea\xbf\x9c\xf1L\xfe@\n\xe3\xd0\xfe\xe3!\x04\x92\xea&\xce(\x02\x9e\xd7o\xaf\xaf^\xbd\xba\x9b\x7f\x158vl\xef\x82\xba\x9a\xf6\x1fEE\x84f\xf6JL\xf0MT\x83\x99\x96\xd4\xcb\x82\xf2Pm}\xb354\xb7\xf5\x04\x02\x91\xcb\xff\xf1\xe9_\xfc\x14=\x7f\xe0\x11Otr\xaf\x92\xe5\xbf\xa5\xfa\xdd\xb6i\xc3v\xeb\xe9\xe6\xd4\x8fs`?)\x84\x9f7(\x0e\x9c\xf8x\x08"<\xe3\x1d\x84\x83\x15/y\xdf6|\x97\xd0\x0e\xf1\xe7%\x91\xea/\x83\xc4\xe9\xf4\x9e?k\xd6,\xfe\x15\xad\xe7\x9dw\xb6l\x9a=w\xee\xec\xba\xa6\xf6\x99\x05\x17\xcb>>x \xcfJ/5X\x8b\x0e\xd1\xb8`\xc0\xe2b\xa3}\x11\x91\x11\xcb\x7f\xf2\xf4\x0f\x16\xa3\xffs=\xe2\x89\x0e\xa5\xd9\n\x9b\xdf\xa9_J\x9b~\xdbx\xdb\xf4\xfe\x87\x02t\xd5\x1b\nA\xf7\x85\x87W\xbcx\xc7c\xbc\xc7\xf2\x0c\x92\x1eBx\x84\x01A\xc2\x91\xe6Tz\x1b\xb3\xb3\xb3\x9fTI\xad\xd6\xbc\x16}\xbe\x1e\x93\xae&\xbc\xe26\xb8&\x90kj\xad\xbf7\x18\x15\xb3$9\xa5\xcf\xacA\x03\xd2\xa3\x93\x12bUw\xba\xac+\x1c\xea\xa8\xacj\x9c\xf6\x85D\x10\x85Y\x96\xc0\xfc\xaao\xbf\x94\xbb\xb2\xb3\x07\xfaO\x9d<\xef\xaa\x15\xde\x01\xb8Wz\x89}\xc0\xf3\x0e\xcb\x03\x1aOp\xe5P\xe5\xca\'0!\'\x8f\xd4\x8a\xc0\xb3"\xff\x92z\xa8\x9b\xfe\xff)\x13\'NL\x8b\x89\t\xcc\xf7\xf9\xfcSSS\x92\xd2S\x12\x82\xe1\xcepx\xc5M\x11A\x88\xdbg\x9eyf\xde\xac9\xd3\xff5\xff\xec\xc5\t\xcd\xcdm\x8e\x08aB\xecs\x0fX\xf2\x05\x0fx\xef!\xc6{\xc2\x8d\xf7\x0c\x88\xca\xd3\xd5\x19\x19\x19\x8bW\xadZ\xb5\xf1\xda\x16n\x8f\xb7\xdf~;"//\xef\x86?\x87\xde\x8c\xdc4\x11Op\xf3\xd4\x19\xb9\xaf\xfc\xf2\xf9\x95\xa3e\xed)\x02\xe6\'\x94h6\t\x19\xaa\x17\t\x0f`\xc8A\xc4\xf3\x18s\xc8\x13\xad\xdb&2?\xd6\xbc\x02\xfd\xd6\xad9\xb3D4\xa8\xfb<}\xb6\x9e\xf9\xb3\x10A~\xb3\xfa\x85\xc4\x86\xaa\xc6\x07\x9f\xfe\x87\x9f\x9f\x12\xa0Ezu\xb7<\x91\xa90q\x1d\x01\xb9\x02\x19@C\x88w\x84\x18\xf7\x02\xdb#\xe0\xf9*\x02\xd1"\xb6G\xe7\xce\x0e\x85\xda\xc69s\xe6T\x92\xe4Ww\xf8\xf2\xf2\x95\x88 ?\xfe\x97\x1f\xde\x95\x9f_\x94\xf0\xf6\xfflxs\xd2\xa4I\x11\xea{r\xa5k\xa6\xbc\x90#\xa0\xc3tM\xd7\xb4x\x11\xe48\xefP\x98U\x89H\x91\xc6\xd9[n\xb9e\xaf~?\xf0U\xff\x03\xcdg\xc9W&\xa2v&2cH\x9f\xef\x7f\xbc?\xff%}\x8a\xdeX\x93\xff\xecb\xf6\x7f_\xdf\x80y4\xde8\xdc\x00\x00\x00\x00IEND\xaeB`\x82'

mod_names = {
    '1129810972': 'Republic at War',
    '1125571106': "Thrawn's Revenge",
    '1976399102': "Fall of the Republic",
    '1770851727': "EaW Remake:GCW",
    '1397421866': "Awakening of the Rebellion 2.9",
    '1463042552': "The New Jedi Order",
    '1235783994': "Phoenix Rising",
    '1126673817': "The Clone Wars 4.0",
    '1125764259': "Battlefront Commander",
    '1130150761': "Old Republic at War",
    '1301047166': "Nojembre's Republic at War Submod",
    '1780988753': "Rise of the Mandalorians",
    '1241979729': "FOC Alliance Rebellion",
    '2519672553': "Yodenmod 2021",
    '1173542306': "Secrets of a fallen Empire",
    '1125611680': "Elite's Conflict Mod",
    '1156943126': "Ultimate Galactic Conquest Custom Edition",
    '1973616046': "Tournament Edition Mod",
    '1548018187': "Unofficial Forces of Corruption Patch",
    '2244298809': "Yuuzhan Vong at War",
    '1453649616': "Darktimes",
    '1382582782': "Absolute Chaos"
}

def install_debug_build():
    global DebugInstalled
    aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
    aKey = OpenKey(aReg, r"SOFTWARE\WOW6432Node\LucasArts\Star Wars Empire at War Forces of Corruption\1.0")
    val=QueryValueEx(aKey, "InstallPath")[0]
    os.chdir(val)
    msg = QMessageBox()
    msg.setWindowTitle("Downloading Debug Build...")
    msg.setText("Downloading The EaW Debug Kit From Petroglyph (It is normal for this app to not respond while this process is occuring)")
    msg.setWindowModality(Qt.WindowModal)
    msg.show()
    msg.setText("Downloading The EaW Debug Kit From Petroglyph (It is normal for this app to not respond while this process is occuring)")

    url = "https://www.petroglyphgames.com/eawmodtool/EAW_FOC_Debug_Kit.zip"

    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    with zipfile.ZipFile('EAW_FOC_Debug_Kit.zip', 'r') as zip_ref:
        zip_ref.extractall(path=val+'\\')
    msg.setWindowTitle("Download Complete!")
    msg.setText("Downloading Complete!")
    msg.close()
    DebugInstalled = True
# with open('tempimage1.jpg', 'wb') as r:
#     r.write(exeIconByte)
with open('tempimage', 'wb') as r:
    r.write(eawIconByte)

class ImageLabel(QLabel):
    def __init__(self, image_dir):
        super().__init__()
        pixmap = QPixmap(image_dir)
        pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.setPixmap(pixmap)

class ModItem():
    def __init__(self, name,mod_dir, image='tempimage', mod_id=None, steammod=False,allMods=[]):
        self.steam = steammod
        self.directory = mod_dir
        self.layout = QVBoxLayout()
        self.icon = image
        self.nameLayout = QHBoxLayout()
        font = QFont()
        font.setPointSize(10)
        self.nameLayout.addWidget(ImageLabel(image))
        self.modButton = QLabel(name)
        self.modButton.setFont(font)
        self.nameLayout.addWidget(self.modButton)
        self.name = name
        self.dataLayout = QHBoxLayout()
        self.runButton = QPushButton("Run Mod")
        self.configureButton = QPushButton("Configure Mod")
        self.configureButton.clicked.connect(self.configure_mod)
        self.dataLayout.addWidget(self.runButton)
        self.dataLayout.addWidget(self.configureButton)
        self.layout.addLayout(self.nameLayout)
        self.layout.addLayout(self.dataLayout)
        self.runButton.clicked.connect(self.run)
        if mod_id == None:
            self.mod_id = name
        else:
            self.mod_id = mod_id
        self.data_dict = {}
        self.data_dict['DEBUG'] = False
        self.data_dict['PARENT_MOD'] = "Do Not Run As Submod"
        self.data_dict['PARENT_INDEX'] = 0
        self.normal_build = 'G'
        self.debug_build = 'I'
        self.build_id = self.normal_build
        if self.steam:
            self.mod_launch =f"STEAMMOD={self.mod_id}"
        else:
            self.mod_launch ="MODPATH=Mods\\"+self.name
        self.launch_options = self.mod_launch
    def run(self):
        if self.steam:
            subprocess.Popen([f"StarWars{self.build_id}.exe",self.mod_launch, self.data_dict['ARGS']])
        else:
            subprocess.Popen([f"StarWars{self.build_id}.exe",self.mod_launch, self.data_dict['ARGS']])
    def configure_mod(self):
        self.configureMenu.exec()
    def construct_configure_menu(self):
        self.configureMenu = QDialog()
        self.layout = QVBoxLayout()
        self.configureMenu.setLayout(self.layout)
        self.configureMenu.setWindowTitle("Configure " + self.name)
        self.nameLayout = QHBoxLayout()


        self.nameLayout.addWidget(QLabel("Mod Name: " +self.name))

        self.launchCode = QLineEdit()
        self.launchCode.setEnabled(False)
        #self.nameLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        if self.steam:
            self.launchCode.setText(f"STEAMMOD={self.mod_id}")
        else:
            self.launchCode.setText("MODPATH=Mods\\"+self.name)

        self.launchLayout = QHBoxLayout()
        self.launchLayout.addWidget(QLabel("Launch Code:"))
        self.launchLayout.addWidget(self.launchCode)


        self.layout.addLayout(self.nameLayout)
        self.layout.addLayout(self.launchLayout)
        self.debugLayout = QHBoxLayout()
        self.debugLayout.addWidget(QLabel("Run Mod With Debug Build? (Will Install Debug Build If Not Already Installed)"))
        self.debugEnabled= QCheckBox()
        self.debugLayout.addWidget(self.debugEnabled)
        if self.data_dict['DEBUG'] == True:
            self.debugEnabled.setChecked(True)
        self.layout.addLayout(self.debugLayout)

        self.submodLayout = QHBoxLayout()
        self.submodLayout.addWidget(QLabel("Run As Submod Of:"))
        self.parentMod = QComboBox()
        self.parentMod.addItem("Do Not Run As Submod")
        if self.data_dict['PARENT_MOD'] != "Do Not Run As Submod":
            self.parentMod.setCurrentIndex(self.data_dict['PARENT_INDEX'])
        for mod in self.mods:
            if mod.name != self.name:
                self.parentMod.addItem(mod.name)
        self.submodLayout.addWidget(self.parentMod)
        self.layout.addLayout(self.submodLayout)

        self.extraOptionsLayout = QHBoxLayout()
        self.extraOptionsLayout.addWidget(QLabel("Run With Extra Command Line Arguments?"))
        self.extraArgs = QLineEdit()
        self.extraOptionsLayout.addWidget(self.extraArgs)

        self.layout.addLayout(self.extraOptionsLayout)

        self.buttonLayout = QHBoxLayout()
        self.save = QPushButton("Save")
        self.save.clicked.connect(self.save_configuration)
        self.cancel = QPushButton("Cancel")
        self.buttonLayout.addWidget(self.save)
        self.buttonLayout.addWidget(self.cancel)
        self.layout.addLayout(self.buttonLayout)
        self.cancel.clicked.connect(self.configureMenu.accept)
        
    def save_configuration(self):
        parent = self.parentMod.currentIndex()
        debug = self.debugEnabled.isChecked()
        extraOptions = self.extraArgs.text()

        if parent == "Do Not Run As Submod":
            self.data_dict['PARENT_MOD'] = ''
        else:
            # if parent in [x.name for x in self.mods]:
            #     mod_index = [x.name for x in self.mods].index(parent) 
            self.data_dict['PARENT_MOD'] = self.mods[parent]
            self.data_dict['PARENT_INDEX'] = parent
            self.launch_options = self.mods[parent].mod_launch + ' ' + self.mod_launch
        self.data_dict['ARGS'] = extraOptions
        if debug == True:
            self.data_dict['DEBUG'] = True
            currentlabelText = self.name + ' (DEBUG)'
            self.modButton.setText(currentlabelText)
            if DebugInstalled == False:
                install_debug_build()
        else:
            self.data_dict['DEBUG'] = False
            self.modButton.setText(self.name)

        self.configureMenu.accept()
    def addModtable(self, mods):
        self.mods = mods
        self.construct_configure_menu()

class ModLauncherWindow:
    def __init__(self):
        global DebugInstalled
        self.app = QApplication(sys.argv)  
        self.mainWindow = QMainWindow()
        self.exeImageLocation = os.getcwd()+'\\tempimage'
        font = QFont()
        font.setPointSize(10)
        scrollARea = QScrollArea()
        widget = QWidget()
        self.layout = QVBoxLayout(widget)
        self.layout.setAlignment(Qt.AlignTop)
        scrollARea.setWidget(widget)
        scrollARea.setWidgetResizable(True)
        scrollARea.setHorizontalScrollBarPolicy( Qt.ScrollBarAlwaysOff )
        self.mainWindow.setCentralWidget(scrollARea)

        self.mainWindow.setWindowTitle("EaW Mod Launcher")
        self.__menuBar: QMenuBar = QMenuBar()
        self.__fileMenu: QMenu = QMenu("File", self.mainWindow)
        self.__menuBar.addMenu(self.__fileMenu)
        self.mainWindow.setMenuWidget(self.__menuBar)

        self.__quitAction: QAction = QAction("Quit", self.mainWindow)
        self.__quitAction.triggered.connect(sys.exit)
        self.__fileMenu.addAction(self.__quitAction)
        self.createShortcutAction = QAction("Create Shortcut", self.mainWindow)
        self.createShortcutAction.triggered.connect(self.create_shortcut_window)
        self.__menuBar.addAction(self.createShortcutAction)
        self.locate_eaw_installation()
        self.eaw_exe = self.install_location + '\\GameData\\StarWarsG.exe'
        self.foc_location = self.install_location + '\\corruption\\'
        self.desktop = f"C:\\Users\\{getpass.getuser()}\\Desktop"
        DebugInstalled= self.checkForDebugBuild()
        print(DebugInstalled)
        os.chdir(self.install_location)

        self.mods = self.grab_all_mods()
        for mod in self.mods:
            self.layout.addLayout(mod.layout)
            mod.addModtable(self.mods)
        os.chdir(self.foc_location)
        
        #self.mainWindow.setWindowFlags(Qt.WindowCloseButtonHint | )
        self.mainWindow.setFixedSize(650, 650)
        self.mainWindow.show()

        sys.exit(self.app.exec_())
    def locate_eaw_installation(self):
        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        aKey = OpenKey(aReg, r"SOFTWARE\WOW6432Node\LucasArts\Star Wars Empire at War Forces of Corruption\1.0")
        val=QueryValueEx(aKey, "InstallPath")[0]
        self.install_location= val
    def grab_all_mods(self):
        localMods = os.listdir(self.install_location+'\\corruption\\Mods')
        modItems = self.grab_steam_mods()
        os.chdir(self.install_location+'\\corruption\\Mods')
        for modpath in localMods:
            if os.path.isdir(modpath):
                items = os.listdir(self.install_location+'\\corruption\\Mods\\'+modpath)
                modImage = self.exeImageLocation
                for i in items:
                    if '.ico' in i:
                        modImage = self.install_location+'\\corruption\\Mods\\'+modpath+'\\'+i
                modItems.append(ModItem(modpath,self.install_location+'\\corruption\\Mods\\'+modpath, modImage))
        
        return modItems
    def get_steam_mod_name(self, mod_id):
        if mod_id in mod_names.keys():
            return mod_names[mod_id]
        try:
            req = requests.get("https://steamcommunity.com/sharedfiles/filedetails/?id="+mod_id)
            soup = BeautifulSoup(req.text, 'lxml')
            val = soup.find('div', {'class':"workshopItemTitle"}).get_text()
            return val
        except Exception as e:
            return mod_id
    def grab_steam_mods(self):
        steam_dir = self.install_location.replace('common\Star Wars Empire at War', '')
        self.workshop_dir = steam_dir + 'workshop\\content\\32470'
        os.chdir(self.workshop_dir)
        mods = []
        for mod in os.listdir(self.workshop_dir):
            fullPath = os.path.abspath(mod)
            items = os.listdir(self.workshop_dir+'\\'+mod)
            name = self.get_steam_mod_name(mod)
            modImage = self.exeImageLocation
            for i in items:
                if '.ico' in i:
                    modImage = fullPath+'\\'+i
            mods.append(ModItem(name, fullPath, modImage,mod,True))
        return mods
    def create_shortcut(self,mod,path):
        #path = os.path.join(self.desktop, mod.name)
        if mod.data_dict['DEBUG'] == True:
            target = self.foc_location + "StarWarsI.exe " + mod.launch_options
        else:
            target = self.foc_location + "StarWarsG.exe " + mod.launch_options
        wDir = self.foc_location
        icon = self.foc_location + "StarWarsG.exe"
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path+'\\'+mod.name+'.lnk')
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = mod.icon or self.exeImageLocation
        shortcut.save()
    def create_shortcut_window(self):
        self.createShortcutWindow = QDialog()
        self.layout = QVBoxLayout()
        self.createShortcutWindow.setLayout(self.layout)
        self.createShortcutWindow.setWindowTitle("Create Shortcut")

        self.modLayout = QHBoxLayout()
        self.modLayout.addWidget(QLabel("Mod:"))
        self.mod = QComboBox()
        self.mod.addItem("Vanilla Forces Of Corruption")
        for i in self.mods:
            self.mod.addItem(i.name)
        self.modLayout.addWidget(self.mod)

        self.layout.addLayout(self.modLayout)

        self.locationLayout = QHBoxLayout()
        self.locationLayout.addWidget(QLabel("Location:"))
        self.location = QLineEdit()
        self.location.setEnabled(False)
        self.location.setText(f"C:\\Users\\{getpass.getuser()}\\Desktop")
        self.locationLayout.addWidget(self.location)
        self.changeLocation = QToolButton()
        self.changeLocation.setText("...")
        self.locationLayout.addWidget(self.changeLocation)
        self.changeLocation.clicked.connect(self.change_location)
        self.layout.addLayout(self.locationLayout)
        self.buttonLayout = QHBoxLayout()
        self.save = QPushButton("Save")
        self.cancel = QPushButton("Cancel")
        self.buttonLayout.addWidget(self.save)
        self.buttonLayout.addWidget(self.cancel)
        self.layout.addLayout(self.buttonLayout)
        self.cancel.clicked.connect(self.createShortcutWindow.accept)
        self.save.clicked.connect(self.shortcutCreator)
        self.createShortcutWindow.exec()
    def change_location(self):
        directory = str(QFileDialog.getExistingDirectory())
        self.location.setText(directory)
    def shortcutCreator(self):
        modName = self.mod.currentText()
        if modName == "Vanilla Forces Of Corruption":
            target = self.foc_location + "StarWarsG.exe"
            wDir = self.foc_location
            icon = self.foc_location + "StarWarsG.exe"
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(self.location.text()+'\\Forces Of Corruption.lnk')
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            shortcut.IconLocation = icon
            shortcut.save()
        else:
            if modName in [x.name for x in self.mods]:
                modIndex = [x.name for x in self.mods].index(modName) 
            mod = self.mods[modIndex]
            self.create_shortcut(mod, self.location.text())
        self.createShortcutWindow.accept()
    def checkForDebugBuild(self):
        os.chdir(self.foc_location)
        if os.path.isfile("StarWarsI.exe"):
            return True
        return False
ModLauncherWindow()
        