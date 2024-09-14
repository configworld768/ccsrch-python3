# ccsrch-python3
ccsrch-python是一个信用卡数据扫描识别工具，参考（https://github.com/roganartu/ccsrch）<br>
原作者使用c写的，我用python3重写了ccsrch，实现了原作者写的那些基本功能<br>
使用python3重写后可扩展性更强一些,但性能比c要弱很多(主要是我c太菜😭)<br>
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
```

## 增加新功能：打印卡号上下文内容,方便人工识别是否是真实的卡号信息以及卡号脱敏
```json
{
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/bridgepoint.rtf",
        "line_number": 19,
        "card_number": "4716######0696",
        "card_type": "VISA",
        "context": "[edit]History\n\n\n\n\n\nVISA, 4716-2046-3895-0696\n\n\n\nIn the mid-1980s a need arose for a standardized, vendor-neutral, certi
fication program that provided structure and demonstrated competence. In November 1988, the Special Interest Group for Computer Security (SIG-CS), a 
member of the Data Processing Management Association (DPMA), brought together several organizations interested in this. The International Information
 Systems Security Certification Consortium or \"(ISC)\" formed in mid-1989 as a non-profit organization with this goal.[5][6][7]\n\n[edit]Certificati
on subject matter\n"
    },
    {
        "filename": "/tmp/tmp3evkjhxg/Dummy/ContaminatedData/ValidPAN/archive.zip/list.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n
    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servl
et19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n"
    },
    {
        "filename": "/tmp/tmp3evkjhxg/Dummy/ContaminatedData/Track Data/trackExample.zip/zipzip.xml",
        "line_number": 7,
        "card_number": "4485######2217",
        "card_type": "VISA",
        "context": "    <ttl>1</ttl>\n\n    <domain>104.com.tw</domain>\n\n    <domain docMode=\"EmulateIE8\">10jqka.com.cn</domain>\n\n    <domain>;
4485######2217=121212054321999876?1</domain>\n\n    <domain docMode=\"EmulateIE8\">115.com</domain>\n\n    <domain>118114.cn</domain>\n\n    <domain 
docMode=\"EmulateIE8\">12306.cn</domain>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip/iecompatdata.xml",
        "line_number": 7,
        "card_number": "4485######2217",
        "card_type": "VISA",
        "context": "    <ttl>1</ttl>\n\n    <domain>104.com.tw</domain>\n\n    <domain docMode=\"EmulateIE8\">10jqka.com.cn</domain>\n\n    <domain>;
4485######2217=121212054321999876?1</domain>\n\n    <domain docMode=\"EmulateIE8\">115.com</domain>\n\n    <domain>118114.cn</domain>\n\n    <domain 
docMode=\"EmulateIE8\">12306.cn</domain>\n"
    },
 {
        "filename": "/root/ccsrch/tests/test2.zip/basic.txt",
        "line_number": 12,
        "card_number": "4485######2217",
        "card_type": "VISA",
        "context": "MasterCard, 5173582815239055\n\n\n\nVISA, 4012888888881881\n\nVISA, 4485######2217\n\nVISA, 4716204638950696\n\nVISA, 4485######2
217\n\nVISA, 4716204638950696\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip/cissp.txt",
        "line_number": 27,
        "card_number": "5135######0694",
        "card_type": "MasterCard",
        "context": "\n\nTrack1\n\n\n\n%B5135######0694^BARAK/OBAMA^121210100896000000?1\n\n\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip/army.pdf",
        "line_number": 103,
        "card_number": "3024####2904",
        "card_type": "Diners Club",
        "context": "\nTrack1 \n\n%B3024####2904^MONTGOMERY/JAMES^121210100896000000?1 \n\n\n "
    },
    {
        "filename": "/tmp/tmpz_3mkufr/Dummy/ContaminatedData/Track Data/archive.zip/list.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n
    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servl
et19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n"
    },
{
        "filename": "/root/ccsrch/tests/Dummy.zip/WmsServerList.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n
    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servl
et19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n"
    },
    {
        "filename": "/tmp/tmpz_3mkufr/Dummy/ContaminatedData/ValidPAN/stuff.tar/list.xml",
        "line_number": 25,
        "card_number": "3876####5160",
        "card_type": "Diners Club",
        "context": "    <GetCapabilitiesUrl>http://demo.cubewerx.com/demo/cubeserv/cubeserv.cgi</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n
    <GetCapabilitiesUrl>Diners 3876####5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>http://ims.cr.usgs.gov/servl
et19/com.esri.wms.Esrimap/USGS_EDC_Elev_NED</GetCapabilitiesUrl>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip/StartupParameters.plist",
        "line_number": 11,
        "card_number": "4485######2217",
        "card_type": "VISA",
        "context": "    {\n\n        start   = \"Starting Cisco Systems VPN Client Kernel Extension\";\n\n        stop    = \"Stopping Cisco Systems 
VPN Client Kernel Extension\";\n\n\tcredit_card = \"VISA, 4485######2217\";\n\n    };\n\n}\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip/restaurant.xml",
        "line_number": 25,
        "card_number": "4485######2217",
        "card_type": "VISA",
        "context": "\t</restaurant>\n\n\t<restaurant name=\"Buffalo Grill\">\n\n\t\t<address>12 Chapel Street, Edinburgh, EH8 9AY</address>\n\n\t\t<c
uisine>VISA, 4485-9833-5624-2217</cuisine>\n\n\t\t<phoneno>01316677427</phoneno>\n\n\t</restaurant>\n\n\t<restaurant name=\"Nile Valley\">\n"
    },
```


