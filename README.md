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
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/WmsServerList.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servlet19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n",
        "modification_time": "2012-09-20T13:24:12",
        "access_time": "2024-09-18T21:02:21.085876",
        "creation_time": "2024-09-18T21:02:21.021874",
        "byte_offset": 31
    },
    {
        "filename": "/tmp/tmp_sxs_3i1/Dummy/ContaminatedData/ValidPAN/stuff.tar -> list.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servlet19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n",
        "modification_time": "2012-09-20T13:24:12",
        "access_time": "2024-09-18T21:02:21.111877",
        "creation_time": "2024-09-18T21:02:21.110877",
        "byte_offset": 31
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/StartupParameters.plist",
        "line_number": 11,
        "card_number": "4485######2217",
        "card_type": "VISA",
        "context": "    {\n\n        start   = \"Starting Cisco Systems VPN Client Kernel Extension\";\n\n        stop    = \"Stopping Cisco Systems VPN Client Kernel Extension\";\n\n\tcredit_card = \"VISA, 4485######2217\";\n\n    };\n\n}\n",
        "modification_time": "2012-10-01T15:52:46",
        "access_time": "2024-09-18T21:02:21.120878",
        "creation_time": "2024-09-18T21:02:21.020874",
        "byte_offset": 22
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/restaurant.xml",
        "line_number": 25,
        "card_number": "4485#########2217",
        "card_type": "VISA",
        "context": "\t</restaurant>\n\n\t<restaurant name=\"Buffalo Grill\">\n\n\t\t<address>12 Chapel Street, Edinburgh, EH8 9AY</address>\n\n\t\t<cuisine>VISA, 4485#########2217</cuisine>\n\n\t\t<phoneno>01316677427</phoneno>\n\n\t</restaurant>\n\n\t<restaurant name=\"Nile Valley\">\n",
        "modification_time": "2012-09-20T13:25:46",
        "access_time": "2024-09-18T21:02:21.125878",
        "creation_time": "2024-09-18T21:02:21.019874",
        "byte_offset": 17
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/Pen_Tablet.dat",
        "line_number": 31,
        "card_number": "5173######9055",
        "card_type": "MasterCard",
        "context": "\"<TabletArray\",\"type=array/>\"\n\n\"<TabletAwareApplicationInterface\",\"type=map>\"\n\n\"<NormalizedMaxPressure\",\"type=integer>1023</NormalizedMaxPressure>\"\n\n\"</TabletAwareApplicationInterface>\",\"MasterCard, 5173######9055\"\n\n\"</root>\"\n",
        "modification_time": "2012-09-20T13:27:26",
        "access_time": "2024-09-18T21:02:21.127878",
        "creation_time": "2024-09-18T21:02:21.019874",
        "byte_offset": 50
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/MIPS.xls",
        "line_number": 30,
        "card_number": "3787#####1000",
        "card_type": "American Express",
        "context": "MEM[MAR] = MDSR 2 0x2b X X 0 (false) (false) true (false) (false) (false) (false) (false) (false) (false) X X ADDR_MAR X X X X\nbeq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false) (false) (false) (false) (false) (false) (false) PC_ALU X A_PC B_IR_16x4 X (ADD)\nAmerican Express, 3787#####1000\nDo nothing 2 0x4 X False 0 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X X X X X\nbne Alu = A_reg \u2013 B_reg 1 0x5 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x5 X False 0 (false) (false) (false) true (false) (false) (false) (false) (false) (false) (false) PC_ALU X A_PC B_IR_16x4 X (ADD)",
        "modification_time": "2012-09-20T13:14:50",
        "access_time": "2024-09-18T21:02:21.140878",
        "creation_time": "2024-09-18T21:02:21.019874",
        "byte_offset": 18
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/linux_download.gpg",
        "line_number": 7,
        "card_number": "5135######0694",
        "card_type": "MasterCard",
        "context": "iEYEABECAAYFAlBlja0ACgkQRhgUM/u3VFELXwCfUtlNNWoNCduDGxY/cZLuQDzv\n\nBesAoJgvzMplr6vwRdZJKRMkHqlDYVzf\n\n=V77a\n\nMasterCard, 5135######0694\n\n-----END PGP SIGNATURE-----\n",
        "modification_time": "2012-10-06T10:19:23",
        "access_time": "2024-09-18T21:02:21.147879",
        "creation_time": "2024-09-18T21:02:21.019874",
        "byte_offset": 12
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/DrRoss.txt",
        "line_number": 40,
        "card_number": "5135######0694",
        "card_type": "MasterCard",
        "context": "IBM ISS products\n\nUnix System Administration\n\nProfessional Affiliations:\n\nCredit Card Number : MasterCard, 5135######0694, expiry 15/05/13 ,CVV 747 Knock yourselves out !\n\n\n\n\n\n\n",
        "modification_time": "2012-09-20T13:19:52",
        "access_time": "2024-09-18T21:02:21.148879",
        "creation_time": "2024-09-18T21:02:21.019874",
        "byte_offset": 33
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/coreutils_7.deb",
        "line_number": 1,
        "card_number": "3787########1000",
        "card_type": "American Express",
        "context": "American Express, 3787########1000",
        "modification_time": "2012-10-06T10:18:30",
        "access_time": "2024-09-18T21:02:21.188880",
        "creation_time": "2024-09-18T21:02:21.014874",
        "byte_offset": 18
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/CocoaStandard.sdef",
        "line_number": 22,
        "card_number": "5263######7775",
        "card_type": "MasterCard",
        "context": "\t\t<enumeration name=\"save options\" code=\"savo\">\n\n\t\t\t<enumerator name=\"yes\" code=\"yes \" description=\"Save the file.\"/>\n\n\t\t\t<enumerator name=\"no\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator credit_card=\"MasterCard, 5263######7775\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator name=\"ask\" code=\"ask \" description=\"Ask the user whether or not to save the file.\"/>\n\n\t\t</enumeration>\n\n\n",
        "modification_time": "2012-10-01T15:57:14",
        "access_time": "2024-09-18T21:02:21.195881",
        "creation_time": "2024-09-18T21:02:21.014874",
        "byte_offset": 40
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/build-crt-0.log",
        "line_number": 19,
        "card_number": "4556######6442",
        "card_type": "VISA",
        "context": "\n\n\n\n\n\nVISA, 4556######6442\n\n\n\n\n\n\n",
        "modification_time": "2012-10-05T09:10:08",
        "access_time": "2024-09-18T21:02:21.197881",
        "creation_time": "2024-09-18T21:02:21.013873",
        "byte_offset": 6
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> Dummy/ContaminatedData/ValidPAN/bridgepoint.rtf",
        "line_number": 19,
        "card_number": "4716#########0696",
        "card_type": "VISA",
        "context": "[edit]History\n\n\n\n\n\nVISA, 4716#########0696\n\n\n\nIn the mid-1980s a need arose for a standardized, vendor-neutral, certification program that provided structure and demonstrated competence. In November 1988, the Special Interest Group for Computer Security (SIG-CS), a member of the Data Processing Management Association (DPMA), brought together several organizations interested in this. The International Information Systems Security Certification Consortium or \"(ISC)\" formed in mid-1989 as a non-profit organization with this goal.[5][6][7]\n\n[edit]Certification subject matter\n",
        "modification_time": "2012-09-20T13:22:06",
        "access_time": "2024-09-18T21:02:21.207881",
        "creation_time": "2024-09-18T21:02:21.013873",
        "byte_offset": 6
    },
    {
        "filename": " -> defense.docx",
        "line_number": 30,
        "card_number": "3787#####1000",
        "card_type": "American Express",
        "context": "MEM[MAR] = MDSR 2 0x2b X X 0 (false) (false) true (false) (false) (false) (false) (false) (false) (false) X X ADDR_MAR X X X X\nbeq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false) (false) (false) (false) (false) (false) (false) PC_ALU X A_PC B_IR_16x4 X (ADD)\nAmerican Express, 3787#####1000\nDo nothing 2 0x4 X False 0 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X X X X X\nbne Alu = A_reg \u2013 B_reg 1 0x5 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x5 X False 0 (false) (false) (false) true (false) (false) (false) (false) (false) (false) (false) PC_ALU X A_PC B_IR_16x4 X (ADD)",
        "modification_time": "2012-09-20T13:14:50",
        "access_time": "2024-09-18T18:22:12.982624",
        "creation_time": "2024-09-14T16:15:50.245691",
        "byte_offset": 18
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/archive.zip -> list.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servlet19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n",
        "modification_time": "2012-09-20T15:24:14",
        "access_time": "2024-09-18T21:02:24.596015",
        "creation_time": "2024-09-18T21:02:24.595015",
        "byte_offset": 31
    },
```


