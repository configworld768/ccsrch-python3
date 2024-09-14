# ccsrch-python3
ccsrch-python是一个信用卡数据扫描识别工具，参考（https://github.com/roganartu/ccsrch）<br>
原作者使用c写的，我用python3重写了ccsrch，实现了原作者写的那些基本功能<br>
使用python3重写后可扩展性更强一些,但性能比c要弱很多(主要是我c太菜😭)<br>
#PCI DSS #card scan #信用卡数据扫描

缺点: 无法识别数据库中的信用卡数据,比如mysql的ibd文件扫描
```plaintext
直接扫描 ibd 文件的原理
要理解 Recon Card 如何直接扫描 ibd 文件（MySQL/InnoDB 数据库存储文件）中的信用卡数据，我们需要了解 ibd 文件的结构及其存储数据的方式。

什么是 ibd 文件？
ibd 文件是 InnoDB 存储引擎用来存储表数据和索引的文件。在 MySQL 数据库中，每个使用 InnoDB 引擎的表都有一个对应的 .ibd 文件。
这个文件包含了表的所有行数据、行锁、索引等。由于 InnoDB 使用了行格式存储，所以 ibd 文件中的数据是经过内部格式化和压缩的。
直接扫描 ibd 文件的方式
直接扫描 ibd 文件以查找敏感数据（如信用卡号）是一种非常低层的操作，通常通过以下步骤进行：

文件读取和二进制解析：

工具会以二进制方式打开 ibd 文件并逐字节或逐块读取文件内容。由于 ibd 文件是二进制文件，直接读取文件可能需要解析其特定的存储格式。
模式匹配和数据识别：

在读取的数据中，工具会使用正则表达式或模式匹配算法来搜索类似信用卡号的模式。通常会使用正则表达式来匹配符合 Luhn 算法的 16 位数字（信用卡号的常见格式）。
这种扫描会在文件的任意位置寻找与信用卡号格式相似的数据，而不需要了解数据在数据库表中的逻辑结构。
解析 InnoDB 存储结构（可选）：

高级扫描工具可能会尝试解析 InnoDB 页的存储结构，以准确地查找表数据。InnoDB 数据库页是逻辑存储单元，每个页包含多个记录。
工具可能会试图解析页头、槽数组、记录头信息等，以更准确地找到数据行和字段，进行更具针对性的扫描。
识别并提取可能的数据：

一旦匹配到可能的信用卡号格式的数据，工具会将这些数据提取出来，进行进一步分析和验证（例如使用 Luhn 算法进行验证），以确认这些数据是否真的包含有效的信用卡号。
直接扫描的挑战和风险
直接扫描 ibd 文件面临着一些挑战和风险：

性能问题：

直接读取和解析大型数据库文件可能会对服务器性能产生重大影响，特别是在生产环境中运行扫描时，这种操作可能会导致服务器负载增大、IO 性能下降，甚至可能会导致数据库崩溃。
数据完整性风险：

在数据库文件被直接读取时，如果文件被写入操作修改，可能会导致数据不一致甚至损坏。因此，不建议直接扫描生产环境的数据库文件。
格式复杂性：

InnoDB 的文件格式较为复杂，直接解析二进制文件需要对 MySQL 的内部数据存储格式（如行格式、页格式）有深入的了解。这种操作比较复杂，稍有不慎可能会得到错误的数据结果。
合规性和隐私问题：

在某些情况下，直接访问数据库文件可能会违反数据安全和隐私规定，因为它可能涉及到未授权的数据访问。
更安全和推荐的替代方法
使用 SQL 查询扫描数据：

通过 SQL 查询对表中的数据进行扫描，而不是直接访问 ibd 文件。可以编写 SQL 脚本来查找数据库表中的敏感数据，并使用数据库的内置功能来限制对数据的访问和修改。
使用数据库管理工具的内置功能：

许多数据库管理工具（如 MySQL Enterprise Edition）提供了安全审计和数据加密等功能，可以帮助识别和保护数据库中的敏感数据，而不需要直接扫描数据文件。
采用数据库级别的加密：

使用数据库提供的加密功能（如 InnoDB 表空间加密）来保护数据，这样即使文件被访问，数据仍然是加密的，不容易被解析。
```

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

## 增加新功能：打印卡号上下文内容,方便人工识别是否是真实的卡号信息
![image](https://github.com/configworld768/ccsrch-python3/blob/main/img/%E6%88%AA%E5%B1%8F2020-09-14%2017.05.44.png)<br>

## 卡号脱敏
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


