# ccsrch-python3
ccsrch-python是一个信用卡数据扫描识别工具，参考（https://github.com/roganartu/ccsrch）<br>
原作者使用c写的，我用python3重写了ccsrch，实现了原作者写的那些基本功能<br>
使用python3重写后可扩展性更强一些,但性能比c要弱很多(主要是我c太菜😭)<br>
ccsrch_regex.py是正则版本，替换正则表达式再改改判断方式可用来搜索别的敏感信息
#PCI DSS #card scan #信用卡数据扫描


## 用法
```bash
python ccsrch.py [options] <start_path>
```

## 例如
```bash
python ccsrch.py --json-output -i ignore_list.txt -n .exe,.dll /path/to/scan

-i 参数是将一些不扫描的文件放在 ignore_list.txt中，相当于是基于文件名的白名单
-n 参数是制定某些后缀名的文件不扫描,比如.dll文件等
--json-output 参数选择json结果输出
--mask 参数是将卡号掩码,默认不掩码
```

## 增加新功能：打印卡号上下文内容,方便人工识别是否是真实的卡号信息以及卡号脱敏
```json
{
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/WmsServerList.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n
    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servl
et19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n",
        "modification_time": "2012-09-20T13:24:12",
        "access_time": "2024-09-15T22:00:30.103991",
        "creation_time": "2024-09-15T22:00:30.030988",
        "byte_offset": 31
    },
    {
        "filename": "/tmp/tmpndx0kc7l/Dummy/ContaminatedData/ValidPAN/stuff.tar/list.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n
    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servl
et19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n",
        "modification_time": "2012-09-20T13:24:12",
        "access_time": "2024-09-15T22:00:30.129992",
        "creation_time": "2024-09-15T22:00:30.128992",
        "byte_offset": 31
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/StartupParameters.plist",
        "line_number": 11,
        "card_number": "4485######2217",
        "card_type": "VISA",
        "context": "    {\n\n        start   = \"Starting Cisco Systems VPN Client Kernel Extension\";\n\n        stop    = \"Stopping Cisco Systems 
VPN Client Kernel Extension\";\n\n\tcredit_card = \"VISA, 4485######2217\";\n\n    };\n\n}\n",
        "modification_time": "2012-10-01T15:52:46",
        "access_time": "2024-09-15T22:00:30.138993",
        "creation_time": "2024-09-15T22:00:30.029988",
        "byte_offset": 22
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/restaurant.xml",
        "line_number": 25,
        "card_number": "4485#########2217",
        "card_type": "VISA",
        "context": "\t</restaurant>\n\n\t<restaurant name=\"Buffalo Grill\">\n\n\t\t<address>12 Chapel Street, Edinburgh, EH8 9AY</address>\n\n\t\t<c
uisine>VISA, 4485#########2217</cuisine>\n\n\t\t<phoneno>01316677427</phoneno>\n\n\t</restaurant>\n\n\t<restaurant name=\"Nile Valley\">\n",
        "modification_time": "2012-09-20T13:25:46",
        "access_time": "2024-09-15T22:00:30.144993",
        "creation_time": "2024-09-15T22:00:30.029988",
        "byte_offset": 17
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/Pen_Tablet.dat",
        "line_number": 31,
        "card_number": "5173######9055",
        "card_type": "MasterCard",
        "context": "\"<TabletArray\",\"type=array/>\"\n\n\"<TabletAwareApplicationInterface\",\"type=map>\"\n\n\"<NormalizedMaxPressure\",\"type=inte
ger>1023</NormalizedMaxPressure>\"\n\n\"</TabletAwareApplicationInterface>\",\"MasterCard, 5173######9055\"\n\n\"</root>\"\n",
        "modification_time": "2012-09-20T13:27:26",
        "access_time": "2024-09-15T22:00:30.146993",
        "creation_time": "2024-09-15T22:00:30.029988",
        "byte_offset": 50
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/otherStuff.wim",
        "line_number": 140,
        "card_number": "4485#########2217",
        "card_type": "VISA",
        "context": "\t</restaurant>\n\n\t<restaurant name=\"Buffalo Grill\">\n\n\t\t<address>12 Chapel Street, Edinburgh, EH8 9AY</address>\n\n\t\t<c
uisine>VISA, 4485#########2217</cuisine>\n\n\t\t<phoneno>01316677427</phoneno>\n\n\t</restaurant>\n\n\t<restaurant name=\"Nile Valley\">\n",
        "modification_time": "2012-09-20T13:34:36",
        "access_time": "2024-09-15T22:00:30.152993",
        "creation_time": "2024-09-15T22:00:30.029988",
        "byte_offset": 17
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/MIPS.xls",
        "line_number": 30,
        "card_number": "3787#####1000",
        "card_type": "American Express",
        "context": "MEM[MAR] = MDSR 2 0x2b X X 0 (false) (false) true (false) (false) (false) (false) (false) (false) (false) X X ADDR_MAR X X X X\nb
eq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SU
B)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false) (false) (false) (false) (false) (false) (false) PC_ALU X A_PC B_IR
_16x4 X (ADD)\nAmerican Express, 3787#####1000\nDo nothing 2 0x4 X False 0 (false) (false) (false) (false) (false) (false) (false) (false) (false) (f
alse) (false) X X X X X X\nbne Alu = A_reg \u2013 B_reg 1 0x5 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (
false) X X A_REG B_REG X (SUB)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x5 X False 0 (false) (false) (false) true (false) (false) (false) (false) (false) (fals
e) (false) PC_ALU X A_PC B_IR_16x4 X (ADD)",
        "modification_time": "2012-09-20T13:14:50",
        "access_time": "2024-09-15T22:00:30.156993",
        "creation_time": "2024-09-15T22:00:30.029988",
        "byte_offset": 18
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/Localizable.strings",
        "line_number": 3,
        "card_number": "4024######2710",
        "card_type": "VISA",
        "context": "bplist00\u0010[\u0001\u0002\u0003\u0004\u0005\u0006\u0007\b\t\n\n\u000b\f\n\n\u000e\u000f\u0010\u0011\u0012\u0013\u0014\u0015\u00
16\u0017\u0018\u0019\u001a\u001b\u001c\u001d\u001e\u001f !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz
{|}~\u007f]VwWprivate_\u0010,Every month on the %@ (list of numeral days)_\u0010\u0014Every year on the %@Tnone\\start date: \\confidential_\u0010\u0
015Every %ld weeks on %@VminuteYimportantUgroup_\u0010\u0016Every year on every %@_\u0010!Every %ld years on every %@ in %@_\u0010\u0016Every %ld mon
ths on %@_\u0010\u001cEvery year on every %@ in %@VpublicYcompleted_\u0010\u0010Every year in %@UchairUevent\\event type: _\u0010\u0013<unnamed organ
izer>]not important_\u0010\"Every %ld years on the %@ %@ of %@_\u0010\u0018Every month on the %@ %@YEvery day_\u0010\u001bEvery %ld years on every %@
Troom_\u00101Every %ld months on the %@ (list of numeral VISA, 4024######2710 days)T, %@[Every month_\u0010\u0017Every year on the %@ %@_\u0010\u0013
<untitled calendar>Wseconds_\u0010\u000fEvery %ld weeks_\u0010\u001cEvery %ld years on the %@ %@Uhours_\u0010\u0011Every month on %@Ytentative_\u0010
\u0011completion date: W and %@Vbefore_\u0010\"unable to determine the recurrence_\u0010\u000f<untitled todo>_\u0010\u0014ends after %ld timesThour_\
u0010\u0019Every %ld years on the %@_\u0010\u001dEvery %ld months on the %@ %@Zindividual^Every %d yearsU%d %@WminutesTdays_\u0010\u0010Every week on
 %@_\u0010\u0010Every %ld monthsZend date: _\u0010\u000fends on date %@\\\n\nin %@ at %@_\u0010\u001aEvery year on the %@ of %@ZEvery yearXaccepted_\
u0010\u000fnon participantX%d %@ %@_\u0010$Every month on the %@ (weekday list)Wunknown\\needs actionZend time: _\u0010\u0013ends after %ld time_\u00
10\u0015Every %ld years in %@]all day eventZEvery weekYdelegated_\u0010\u0012<unnamed attendee>V\n\nin %@Sday\\start time: Xdeclined_\u0010\u001fEver
y %ld years on the %@ of %@_\u0010\u0014required participant^%@ (read-only)^very important_\u0010\u0014optional participantUafter_\u0010\u001dEvery y
ear on the %@ %@ of %@Zin process_\u0010\u0010<untitled event>R, ^Every %ld daysXresourceYcancelledYconfirmed_\u0010)Every %ld months on the %@ (week
day list)e \u000f\u0005\u0005\u0005\u0005k\u0005\u0005\u0000 \u0000%\u0000@\u0000 \u0005\u0005\u0005\u0005\u0005k \u000f\u0005\u0005\u0000 \u0005\u00
05\u0005\u0000 \u0005\u0000%\u0000@d \u000f\u0005\u0005\u0005m\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0005\u0000:\u0000 d\u000
5\u0005\u0005\u0005o\u0010\u0016 \u000f\u0005\u0005\u0000 \u0000%\u00001\u0000$\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0005\u0005\u0000 \u0005
\u0000%\u00002\u0000$\u0000@c\u0005\u0005\u0005d\u0005\u0005\u0005\u0005e\u0005\u0005\u0005\u0005\u0005m\u0005\u0005\u0000 \u0005\u0005\u0005\u0000 \
u0005\u0005\u0005\u0000 \u0000%\u0000@o\u0010\u001d \u000f\u0005\u0005\u0000 \u0000%\u00001\u0000$\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0000
 \u0005\u0005\u0005\u0000 \u0000%\u00002\u0000$\u0000@\u0000 \u0005\u0000%\u00003\u0000$\u0000@o\u0010\u0016 \u000f\u0005\u0005\u0000 \u0000%\u00001\
u0000$\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0000%\u00002\u0000$\u0000@o\u0010\u0016 \u000f\u0005\u0005\u0000 \u0005
\u0005\u0005\u0000 \u0005\u0005\u0005\u0000 \u0000%\u00001\u0000$\u0000@\u0000 \u0005\u0000%\u00002\u0000$\u0000@f\u0005\u0005\u0005\u0005\u0005\u000
5e\u0005\u0005\u0005\u0005\u0005k \u000f\u0005\u0005\u0000 \u0005\u0005\u0005\u0000 \u0005\u0000%\u0000@e \u000f\u0005\u0005\u0000\"\u0005e\u0005\u00
05\u0005\u0005\u0005m \u000f\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0005\u0005\u0000:\u0000 o\u0010\u000f \u000f\u0000<\u0005\u0005\u0005\
u0005\u0005\u0000 \u0005\u0005\u0005\u0000 \u0005\u0005\u0000>g\u0005\u0005\u0000 \u0005\u0005\u0005\u0005o\u0010\" \u000f\u0005\u0005\u0000 \u0000%\
u00001\u0000$\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0000 \u0005\u0000%\u00003\u0000$\u0000@\u0000 \u0005\u0000%\u00002\u0000$\u0000@\u0000 \u
0005\u0005\u0000 \u0000%\u00004\u0000$\u0000@o\u0010\u0014 \u000f\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0000 \u0005\u0000%\u00002\u0000$\u0000@
\u0000 \u0005\u0000%\u00001\u0000$\u0000@f\u0005\u0005\u0000 \u0005\u0005\u0005o\u0010\u0016\u0005\u0005\u0000 \u0000%\u00001\u0000$\u0000l\u0000d\u0
000 \u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0000 \u0000%\u00002\u0000$\u0000@c\u0005\u0005\u0005o\u0010\u001d \u000f\u0005\u0005\u0000 \u0
000%\u00001\u0000$\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0000-\u0000%\u00002\u0000$\u0000@\u0000 \u0005\u0005\u0005\
u0005\u0005e \u000f\u0000,\u0000 \u0000%\u0000@h \u000f\u0005\u0005\u0000 \u0005\u0005\u0005\u0005o\u0010\u0014 \u000f\u0005\u0005\u0000 \u0005\u0005
\u0005\u0000 \u0005\u0000%\u00002\u0000$\u0000@\u0000 \u0005\u0000%\u00001\u0000$\u0000@\u0000 o\u0010\u0010\u0000<\u0005\u0005\u0005\u0000 \u0005\u0
005\u0005\u0000 \u0005\u0005\u0005\u0000 \u0005\u0005\u0000>e\u0005\u0005\u0005\u0005\u0005m\u0005\u0005\u0000 \u0000%\u0000l\u0000d\u0000 \u0005\u00
05\u0005\u0005\u0005\u0005o\u0010\u001a \u000f\u0005\u0005\u0000 \u0000%\u00001\u0000$\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0000 \u0005\u000
0%\u00003\u0000$\u0000@\u0000 \u0005\u0000%\u00002\u0000$\u0000@d\u0005\u0005\u0005\u0005l \u000f\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0000 \u
0005\u0000%\u0000@k \u000f\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0005m\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005
\u0005\u0000:\u0000 e \u000f\u0005\u0000-\u0000%\u0000@e \u000f\u0005\u0005\u0005\u0005o\u0010\u001c \u000f\u0005\u0005\u0000 \u0005\u0005\u0005\u000
5\u0000 \u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0005o\u0010\u000f\u0000<\u00
05\u0005\u0005\u0005\u0005\u0000  \u000f\u0005\u0005\u0005\u0000 \u0005\u0005\u0000>o\u0010\u0015\u0005\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0
005\u0005\u0005\u0000 \u0000%\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0005c\u0005\u0005\u0005o\u0010\u0014 \u000f\u0005\u0005\u0000 \u0000%\u00
001\u0000$\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0000 \u0005\u0000%\u00002\u0000$\u0000@o\u0010\u001c \u000f\u0005\u0005\u0000 \u0000%\u00001
\u0000$\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0000%\u00003\u0000$\u0000@\u0000 \u0005\u0000%\u00002\u0000$\u0000@d\u
0005\u0005\u0005\u0005j\u0005\u0005\u0000 \u0000%\u0000d\u0000 \u0005\u0005\u0005\u0005Y%1$d %2$@d\u0005\u0005\u0005\u0005e \u000f\u0005\u0005\u0005\
u0005i\u0005\u0005\u0000 \u0005\u0005\u0005\u0000 \u0000%\u0000@m\u0005\u0005\u0000 \u0000%\u0000l\u0000d\u0000 \u0005\u0005\u0005\u0005\u0005\u0005l
\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0000:\u0000 o\u0010\u0010\u0005\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005
\u0005\u0005\u0005\u0000 \u0000%\u0000@o\u0010\u0011 \u000f\u0000\n\n\u0005\u0000%\u00001\u0000$\u0000@\u0000 \u0005\u0005\u0005\u0005\u0000 \u0000%\
u00002\u0000$\u0000@o\u0010\u0015 \u000f\u0005\u0005\u0000 \u0005\u0005\u0005\u0000 \u0005\u0000%\u00001\u0000$\u0000@\u0000 \u0005\u0005\u0000 \u000
0%\u00002\u0000$\u0000@g \u000f\u0005\u0005\u0000 \u0005\u0005\u0005e\u0005\u0005\u0005\u0005\u0005h\u0005\u0005\u0000-\u0005\u0005\u0005\u0005\u0005
^%1$d %2$@ %3$@h \u000f\u0005\u0005\u0000 \u0005\u0005\u0005\u0005k\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0005j\u0005\u0005\u
0005\u0000 \u0005\u0005\u0005\u0005\u0000:\u0000 o\u0010\u0014 \u000f\u0005\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0000 \u0005
\u0005\u0005\u0000 \u0000%\u0000l\u0000do\u0010\u0013\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0000 \u0
005\u0005\u0005\u0005h \u000f\u0005\u0005\u0000 \u0005\u0005\u0005\u0005n \u000f\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0005\u0005\u
0005\u0000 n\u0000<\u0005\u0005\u0005\u0005\u0005\u0000 \u0005\u0005\u0005\u0000 \u0005\u0005\u0000>e \u000f\u0000\n",
        "modification_time": "2012-10-01T16:06:34",
        "access_time": "2024-09-15T22:00:30.162993",
        "creation_time": "2024-09-15T22:00:30.028988",
        "byte_offset": 649
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/linux_download.gpg",
        "line_number": 7,
        "card_number": "5135######0694",
        "card_type": "MasterCard",
        "context": "iEYEABECAAYFAlBlja0ACgkQRhgUM/u3VFELXwCfUtlNNWoNCduDGxY/cZLuQDzv\n\nBesAoJgvzMplr6vwRdZJKRMkHqlDYVzf\n\n=V77a\n\nMasterCard, 5135
######0694\n\n-----END PGP SIGNATURE-----\n",
        "modification_time": "2012-10-06T10:19:23",
        "access_time": "2024-09-15T22:00:30.164994",
        "creation_time": "2024-09-15T22:00:30.028988",
        "byte_offset": 12
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/DrRoss.txt",
        "line_number": 40,
        "card_number": "5135######0694",
        "card_type": "MasterCard",
        "context": "IBM ISS products\n\nUnix System Administration\n\nProfessional Affiliations:\n\nCredit Card Number : MasterCard, 5135######0694, 
expiry 15/05/13 ,CVV 747 Knock yourselves out !\n\n\n\n\n\n\n",
        "modification_time": "2012-09-20T13:19:52",
        "access_time": "2024-09-15T22:00:30.165993",
        "creation_time": "2024-09-15T22:00:30.028988",
        "byte_offset": 33
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/coreutils_7.deb",
        "line_number": 1,
        "card_number": "3787########1000",
        "card_type": "American Express",
        "context": "American Express, 3787########1000",
        "modification_time": "2012-10-06T10:18:30",
        "access_time": "2024-09-15T22:00:30.206995",
        "creation_time": "2024-09-15T22:00:30.023988",
        "byte_offset": 18
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/CocoaStandard.sdef",
        "line_number": 22,
        "card_number": "5263######7775",
        "card_type": "MasterCard",
        "context": "\t\t<enumeration name=\"save options\" code=\"savo\">\n\n\t\t\t<enumerator name=\"yes\" code=\"yes \" description=\"Save the file
.\"/>\n\n\t\t\t<enumerator name=\"no\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator credit_card=\"MasterCard, 5263#####
#7775\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator name=\"ask\" code=\"ask \" description=\"Ask the user whether or n
ot to save the file.\"/>\n\n\t\t</enumeration>\n\n\n",
        "modification_time": "2012-10-01T15:57:14",
        "access_time": "2024-09-15T22:00:30.213995",
        "creation_time": "2024-09-15T22:00:30.023988",
        "byte_offset": 40
    },
{
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/bridgepoint.rtf",
        "line_number": 19,
        "card_number": "4716#########0696",
        "card_type": "VISA",
        "context": "[edit]History\n\n\n\n\n\nVISA, 4716#########0696\n\n\n\nIn the mid-1980s a need arose for a standardized, vendor-neutral, certifi
cation program that provided structure and demonstrated competence. In November 1988, the Special Interest Group for Computer Security (SIG-CS), a me
mber of the Data Processing Management Association (DPMA), brought together several organizations interested in this. The International Information S
ystems Security Certification Consortium or \"(ISC)\" formed in mid-1989 as a non-profit organization with this goal.[5][6][7]\n\n[edit]Certification
 subject matter\n",
        "modification_time": "2012-09-20T13:22:06",
        "access_time": "2024-09-15T22:00:30.227996",
        "creation_time": "2024-09-15T22:00:30.023988",
        "byte_offset": 6
    },
    {
        "filename": "/tmp/tmpndx0kc7l/Dummy/ContaminatedData/ValidPAN/archive.zip/list.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n
    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servl
et19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n",
        "modification_time": "2012-09-20T15:24:14",
        "access_time": "2024-09-15T22:00:30.289999",
        "creation_time": "2024-09-15T22:00:30.288998",
        "byte_offset": 31
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/aircraft.pdf",
        "line_number": 64,
        "card_number": "3787#####1000",
        "card_type": "American Express",
        "context": "EMAIL: Sales \n\nAmerican Express, \n3787#####1000 \n\n",
        "modification_time": "2012-09-20T13:42:52",
        "access_time": "2024-09-15T22:00:30.300999",
        "creation_time": "2024-09-15T22:00:30.022988",
        "byte_offset": 0
    },
```


