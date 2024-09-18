# ccsrch-python3
ccsrch-python是一个信用卡数据扫描识别工具，参考（https://github.com/roganartu/ccsrch）<br>
原作者使用c写的，我用python3重写了ccsrch，实现了原作者写的那些基本功能<br>
使用python3重写后可扩展性更强一些,但性能比c要弱很多(主要是我c太菜😭)<br>
ccsrch_regex.py是正则版本，替换正则表达式再改改判断方式可用来搜索别的敏感信息
#PCI DSS #card scan #信用卡数据扫描


## 用法
```bash
pip3 install textract
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
[
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 3,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "Valid Dummy Pan Numbers\n \nDiscover, 6011########3105\nDiscover, 6011963280099774\n "
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 4,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": " \nDiscover, 6011186767363105\nDiscover, 6011########9774\n \nMasterCard, 5173582815239055"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 6,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "Discover, 6011963280099774\n \nMasterCard, 5173########9055\nMasterCard, 5135299256640694\nMasterCard, 5263067393947775"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": " \nMasterCard, 5173582815239055\nMasterCard, 5135########0694\nMasterCard, 5263067393947775\nMasterCard, 5173582815239055"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 8,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "MasterCard, 5173582815239055\nMasterCard, 5135299256640694\nMasterCard, 5263########7775\nMasterCard, 5173582815239055\n "
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 9,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "MasterCard, 5135299256640694\nMasterCard, 5263067393947775\nMasterCard, 5173########9055\n \nVISA, 4012888888881881"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 11,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "MasterCard, 5173582815239055\n \nVISA, 4012########1881\nVISA, 4485983356242217\nVISA, 4716204638950696"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": " \nVISA, 4012888888881881\nVISA, 4485########2217\nVISA, 4716204638950696\nVISA, 4485########2217"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 13,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4012888888881881\nVISA, 4485983356242217\nVISA, 4716########0696\nVISA, 4485983356242217\nVISA, 4716########0696"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 14,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "VISA, 4485########2217\nVISA, 4716204638950696\nVISA, 4485########2217\nVISA, 4716204638950696\nVISA, 4024007135532710"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 15,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4716########0696\nVISA, 4485983356242217\nVISA, 4716########0696\nVISA, 4024007135532710\nVISA, 4556474670906442"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 16,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "VISA, 4485983356242217\nVISA, 4716204638950696\nVISA, 4024########2710\nVISA, 4556474670906442\nVISA, 4929391046267988"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 17,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "VISA, 4716204638950696\nVISA, 4024007135532710\nVISA, 4556########6442\nVISA, 4929391046267988\n "
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 18,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "VISA, 4024007135532710\nVISA, 4556474670906442\nVISA, 4929########7988\n \nAmerican Express, 378734493671000"
    },
    {
        "filename": "/root/ccsrch/tests/pdf.pdf",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "VISA, 4929391046267988\n \nAmerican Express, 3787#######1000\n \n "
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 3,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "\nFile Name Format Platform PAN, CC company Valid Pan? Track Data included Track Number\nBBQ.doc MS Word doc Any MasterCard, 5173########9055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 4,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "File Name Format Platform PAN, CC company Valid Pan? Track Data included Track Number\nBBQ.doc MS Word doc Any MasterCard, 5173582815239055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012########1881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 5,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "BBQ.doc MS Word doc Any MasterCard, 5173582815239055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 3787#######1000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 6,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "The Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485########2217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "MIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135########0694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 8,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "MIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716########0696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 9,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "DrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 3876######5160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 10,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "bridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485########2217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485########2217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 11,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "WmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173########9055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "restaurant.xml XML ANY VISA, 4485########2217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485########2217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 13,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "Pen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 3787#######1000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 14,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "control-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135########0694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 16,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "linux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929########7988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 17,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "ubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 17,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "ubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 18,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "diving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 18,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "diving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 19,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "archive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 19,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "archive.zip zip ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485########2217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "stuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 3787#######1000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO\nCPU.xlsx MS Excel xlsx Any MasterCard, 5173452815239055 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 25,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "diffie.pdf pdf ANY Diners 30249963624666 NO NO\nmslogfile.xml XML MS Log American Express, 388734498671000 NO NO\nLocalizable.strings strings MAC OS VISA, 4024########2710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 26,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "mslogfile.xml XML MS Log American Express, 388734498671000 NO NO\nLocalizable.strings strings MAC OS VISA, 4024007135532710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263########7775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 27,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "Localizable.strings strings MAC OS VISA, 4024007135532710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485########2217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 28,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "CocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556########6442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 29,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "StartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024########2710 YES YES (Track 1) %B4024########2710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "build-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 3787#######1000 YES YES (Track 2) ;3787#######1000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "build-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 3787#######1000 YES YES (Track 2) ;3787#######1000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 31,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "coms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135########0694 YES YES (Track 1) %B5135########0694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 32,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "parse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 32,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "parse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 33,
        "card_number": "3024######2904",
        "card_type": "Diners Club",
        "context": "cissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\naircraft.pdf pdf ANY Diners 3024######2904 YES YES (Track 1) %B3024######2904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 34,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "iecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 34,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "iecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 35,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "aircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 35,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "aircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/WmsServerList.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/The Defence Signals Directorate.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/stuff.tar -> /tmp/tmp6t1qz_oq/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/stuff.tar -> /tmp/tmp6t1qz_oq/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/StartupParameters.plist",
        "line_number": 11,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "        start   = \"Starting Cisco Systems VPN Client Kernel Extension\";\n\n        stop    = \"Stopping Cisco Systems VPN Client Kernel Extension\";\n\n\tcredit_card = \"VISA, 4485########2217\";\n\n    };\n\n}\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/restaurant.xml",
        "line_number": 25,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\t<restaurant name=\"Buffalo Grill\">\n\n\t\t<address>12 Chapel Street, Edinburgh, EH8 9AY</address>\n\n\t\t<cuisine>VISA, 4485########2217</cuisine>\n\n\t\t<phoneno>01316677427</phoneno>\n\n\t</restaurant>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/Pen_Tablet.dat",
        "line_number": 31,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "\"<TabletAwareApplicationInterface\",\"type=map>\"\n\n\"<NormalizedMaxPressure\",\"type=integer>1023</NormalizedMaxPressure>\"\n\n\"</TabletAwareApplicationInterface>\",\"MasterCard, 5173########9055\"\n\n\"</root>\"\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/MIPS.xlsx",
        "line_number": 27,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "Reg[IR[20-16]]=MDLR 3 0x23 X X 0 (false) (false) (false) (false) (false)\nsw alu=A_reg+sign-extend(IR[15-0]) , MAR = alu 1 0x2b X X 2 (false) (false) (false) (false) true\nMEM[MAR] = MDSR 2 0x2b X VISA, 4485########2217 0 (false) (false) true (false) (false)\nbeq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false)"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/MIPS.xls",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "beq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false) (false) (false) (false) (false) (false) (false) PC_ALU X A_PC B_IR_16x4 X (ADD)\nAmerican Express, 3787#######1000\nDo nothing 2 0x4 X False 0 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X X X X X\nbne Alu = A_reg \u2013 B_reg 1 0x5 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/linux_download.gpg",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "BesAoJgvzMplr6vwRdZJKRMkHqlDYVzf\n\n=V77a\n\nMasterCard, 5135########0694\n\n-----END PGP SIGNATURE-----\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/DrRoss.txt",
        "line_number": 40,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "Unix System Administration\n\nProfessional Affiliations:\n\nCredit Card Number : MasterCard, 5135########0694, expiry 15/05/13 ,CVV 747 Knock yourselves out !\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/coreutils_7.deb",
        "line_number": 1,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "American Express, 3787#######1000"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/CocoaStandard.sdef",
        "line_number": 22,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "\t\t\t<enumerator name=\"yes\" code=\"yes \" description=\"Save the file.\"/>\n\n\t\t\t<enumerator name=\"no\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator credit_card=\"MasterCard, 5263########7775\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator name=\"ask\" code=\"ask \" description=\"Ask the user whether or not to save the file.\"/>\n\n\t\t</enumeration>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/build-crt-0.log",
        "line_number": 19,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "\n\n\n\nVISA, 4556########6442\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/bridgepoint.rtf",
        "line_number": 19,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "\n\n\n\nVISA, 4716########0696\n\n\n\nIn the mid-1980s a need arose for a standardized, vendor-neutral, certification program that provided structure and demonstrated competence. In November 1988, the Special Interest Group for Computer Security (SIG-CS), a member of the Data Processing Management Association (DPMA), brought together several organizations interested in this. The International Information Systems Security Certification Consortium or \"(ISC)\" formed in mid-1989 as a non-profit organization with this goal.[5][6][7]\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/archive.zip -> /tmp/tmpsh9hwu1k/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/archive.zip -> /tmp/tmpsh9hwu1k/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/ValidPAN/aircraft.pdf",
        "line_number": 64,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "\nAmerican Express, \n3787#######1000 \n\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/Track Data/trackExample.zip -> /tmp/tmpzi2yrvop/zipzip.xml",
        "line_number": 7,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "    <domain>104.com.tw</domain>\n\n    <domain docMode=\"EmulateIE8\">10jqka.com.cn</domain>\n\n    <domain>;4485########2217=121212054321999876?1</domain>\n\n    <domain docMode=\"EmulateIE8\">115.com</domain>\n\n    <domain>118114.cn</domain>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/Track Data/parse table.xlsx",
        "line_number": 18,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "Exp3 Exp4 Ops3 Exp4 Ops3 Exp4 Ops3 Exp4 Ops3\nOps3 Track2\n;3787#######1000=121212054321999876?1 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 * Exp4 Ops3\nExp4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4\nOps4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4 \u03b5 \u03b5 Exp5 Ops4 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/Track Data/iecompatdata.xml",
        "line_number": 7,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "    <domain>104.com.tw</domain>\n\n    <domain docMode=\"EmulateIE8\">10jqka.com.cn</domain>\n\n    <domain>;4485########2217=121212054321999876?1</domain>\n\n    <domain docMode=\"EmulateIE8\">115.com</domain>\n\n    <domain>118114.cn</domain>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/Track Data/archive.zip -> /tmp/tmpb39uwoh4/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/Dummy.zip -> /tmp/tmppzgb9esz/Dummy/ContaminatedData/Track Data/archive.zip -> /tmp/tmpb39uwoh4/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/ignore_space.txt",
        "line_number": 2,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "These should work:\n\nDiscover, 6011########3105\n\nDiscover, 6011    9632    8009    9774\n\nMasterCard, 5173                                                                5 8 2 8 1  5                  2 3  9  0 5    5\n"
    },
    {
        "filename": "/root/ccsrch/tests/ignore_space.txt",
        "line_number": 3,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": "These should work:\n\nDiscover, 6011 1867 6736 3105\n\nDiscover, 6011########9774\n\nMasterCard, 5173                                                                5 8 2 8 1  5                  2 3  9  0 5    5\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 3,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "Valid Dummy Pan Numbers\n\n\n\nDiscover, 6011########3105\n\nDiscover, 6011963280099774\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 4,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": "\n\nDiscover, 6011186767363105\n\nDiscover, 6011########9774\n\n\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 6,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "Discover, 6011963280099774\n\n\n\nMasterCard, 5173########9055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "\n\nMasterCard, 5173582815239055\n\nMasterCard, 5135########0694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 8,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "MasterCard, 5173582815239055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263########7775\n\nMasterCard, 5173582815239055\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 9,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "MasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173########9055\n\n\n\nVISA, 4012888888881881\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 11,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "MasterCard, 5173582815239055\n\n\n\nVISA, 4012########1881\n\nVISA, 4485983356242217\n\nVISA, 4716204638950696\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012888888881881\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 13,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4012888888881881\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 14,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "VISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4024007135532710\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 15,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4024007135532710\n\nVISA, 4556474670906442\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 16,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "VISA, 4485983356242217\n\nVISA, 4716204638950696\n\nVISA, 4024########2710\n\nVISA, 4556474670906442\n\nVISA, 4929391046267988\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 17,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "VISA, 4716204638950696\n\nVISA, 4024007135532710\n\nVISA, 4556########6442\n\nVISA, 4929391046267988\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 18,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "VISA, 4024007135532710\n\nVISA, 4556474670906442\n\nVISA, 4929########7988\n\n\n\nAmerican Express, 378734493671000\n"
    },
    {
        "filename": "/root/ccsrch/tests/basic.txt",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "VISA, 4929391046267988\n\n\n\nAmerican Express, 3787#######1000\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 3,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "Valid Dummy Pan Numbers\n\n\n\nDiscover, 6011########3105\n\nDiscover, 6011963280099774\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 4,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": "\n\nDiscover, 6011186767363105\n\nDiscover, 6011########9774\n\n\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 6,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "Discover, 6011963280099774\n\n\n\nMasterCard, 5173########9055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "\n\nMasterCard, 5173582815239055\n\nMasterCard, 5135########0694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 8,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "MasterCard, 5173582815239055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263########7775\n\nMasterCard, 5173582815239055\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 9,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "MasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173########9055\n\n\n\nVISA, 4012888888881881\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 11,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "MasterCard, 5173582815239055\n\n\n\nVISA, 4012########1881\n\nVISA, 4485983356242217\n\nVISA, 4716204638950696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012888888881881\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 13,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4012888888881881\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 14,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "VISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4024007135532710\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 15,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4024007135532710\n\nVISA, 4556474670906442\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 16,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "VISA, 4485983356242217\n\nVISA, 4716204638950696\n\nVISA, 4024########2710\n\nVISA, 4556474670906442\n\nVISA, 4929391046267988\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 17,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "VISA, 4716204638950696\n\nVISA, 4024007135532710\n\nVISA, 4556########6442\n\nVISA, 4929391046267988\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 18,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "VISA, 4024007135532710\n\nVISA, 4556474670906442\n\nVISA, 4929########7988\n\n\n\nAmerican Express, 378734493671000\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/test2.zip -> /tmp/tmp7z207sui/basic.txt",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "VISA, 4929391046267988\n\n\n\nAmerican Express, 3787#######1000\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 3,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "Valid Dummy Pan Numbers\n\n\n\nDiscover, 6011########3105\n\nDiscover, 6011963280099774\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 4,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": "\n\nDiscover, 6011186767363105\n\nDiscover, 6011########9774\n\n\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 6,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "Discover, 6011963280099774\n\n\n\nMasterCard, 5173########9055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "\n\nMasterCard, 5173582815239055\n\nMasterCard, 5135########0694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 8,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "MasterCard, 5173582815239055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263########7775\n\nMasterCard, 5173582815239055\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 9,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "MasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173########9055\n\n\n\nVISA, 4012888888881881\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 11,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "MasterCard, 5173582815239055\n\n\n\nVISA, 4012########1881\n\nVISA, 4485983356242217\n\nVISA, 4716204638950696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012888888881881\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 13,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4012888888881881\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 14,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "VISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4024007135532710\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 15,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4024007135532710\n\nVISA, 4556474670906442\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 16,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "VISA, 4485983356242217\n\nVISA, 4716204638950696\n\nVISA, 4024########2710\n\nVISA, 4556474670906442\n\nVISA, 4929391046267988\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 17,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "VISA, 4716204638950696\n\nVISA, 4024007135532710\n\nVISA, 4556########6442\n\nVISA, 4929391046267988\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 18,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "VISA, 4024007135532710\n\nVISA, 4556474670906442\n\nVISA, 4929########7988\n\n\n\nAmerican Express, 378734493671000\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.mac.zip -> /tmp/tmpffpi1034/test/basic.txt",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "VISA, 4929391046267988\n\n\n\nAmerican Express, 3787#######1000\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 3,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "Valid Dummy Pan Numbers\n\n\n\nDiscover, 6011########3105\n\nDiscover, 6011963280099774\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 4,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": "\n\nDiscover, 6011186767363105\n\nDiscover, 6011########9774\n\n\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 6,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "Discover, 6011963280099774\n\n\n\nMasterCard, 5173########9055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "\n\nMasterCard, 5173582815239055\n\nMasterCard, 5135########0694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 8,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "MasterCard, 5173582815239055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263########7775\n\nMasterCard, 5173582815239055\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 9,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "MasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173########9055\n\n\n\nVISA, 4012888888881881\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 11,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "MasterCard, 5173582815239055\n\n\n\nVISA, 4012########1881\n\nVISA, 4485983356242217\n\nVISA, 4716204638950696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012888888881881\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 13,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4012888888881881\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 14,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "VISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4024007135532710\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 15,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4024007135532710\n\nVISA, 4556474670906442\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 16,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "VISA, 4485983356242217\n\nVISA, 4716204638950696\n\nVISA, 4024########2710\n\nVISA, 4556474670906442\n\nVISA, 4929391046267988\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 17,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "VISA, 4716204638950696\n\nVISA, 4024007135532710\n\nVISA, 4556########6442\n\nVISA, 4929391046267988\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 18,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "VISA, 4024007135532710\n\nVISA, 4556474670906442\n\nVISA, 4929########7988\n\n\n\nAmerican Express, 378734493671000\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/test2.zip -> /tmp/tmp2ejr25e2/basic.txt",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "VISA, 4929391046267988\n\n\n\nAmerican Express, 3787#######1000\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 3,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "Valid Dummy Pan Numbers\n\n\n\nDiscover, 6011########3105\n\nDiscover, 6011963280099774\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 4,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": "\n\nDiscover, 6011186767363105\n\nDiscover, 6011########9774\n\n\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 6,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "Discover, 6011963280099774\n\n\n\nMasterCard, 5173########9055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "\n\nMasterCard, 5173582815239055\n\nMasterCard, 5135########0694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 8,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "MasterCard, 5173582815239055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263########7775\n\nMasterCard, 5173582815239055\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 9,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "MasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173########9055\n\n\n\nVISA, 4012888888881881\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 11,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "MasterCard, 5173582815239055\n\n\n\nVISA, 4012########1881\n\nVISA, 4485983356242217\n\nVISA, 4716204638950696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012888888881881\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 13,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4012888888881881\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 14,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "VISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4024007135532710\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 15,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4024007135532710\n\nVISA, 4556474670906442\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 16,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "VISA, 4485983356242217\n\nVISA, 4716204638950696\n\nVISA, 4024########2710\n\nVISA, 4556474670906442\n\nVISA, 4929391046267988\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 17,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "VISA, 4716204638950696\n\nVISA, 4024007135532710\n\nVISA, 4556########6442\n\nVISA, 4929391046267988\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 18,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "VISA, 4024007135532710\n\nVISA, 4556474670906442\n\nVISA, 4929########7988\n\n\n\nAmerican Express, 378734493671000\n"
    },
    {
        "filename": "/root/ccsrch/tests/test.zip -> /tmp/tmpzhxs2b55/basic.txt",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "VISA, 4929391046267988\n\n\n\nAmerican Express, 3787#######1000\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/ignore_dash.txt",
        "line_number": 2,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "These should work:\n\nDiscover, 6011########3105\n\nDiscover, 6011----9632----8009----9774\n\nMasterCard, 5173----------------------------------------------------------------5-8-2-8-1--5------------------2-3--9--0-5----5\n"
    },
    {
        "filename": "/root/ccsrch/tests/ignore_dash.txt",
        "line_number": 3,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": "These should work:\n\nDiscover, 6011-1867-6736-3105\n\nDiscover, 6011########9774\n\nMasterCard, 5173----------------------------------------------------------------5-8-2-8-1--5------------------2-3--9--0-5----5\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/xlsx.xlsx",
        "line_number": 19,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "add Alu = A_reg + B_reg, ALUout = alu 1 0x0 0x20 X 2 (false) (false) (false) (false) (false)\nStore ALUout to Register File\nReg[IR[20-16]]=ALUout 2 0x0 0x20 X 0 (false) (false) (false) (false) (false) 6011########3105\nsub Alu = A_reg - B_reg, ALUout = alu 1 0x0 0x22 X 2 (false) (false) (false) (false) (false) 4929391046267988\nStore ALUout to Register File"
    },
    {
        "filename": "/root/ccsrch/tests/xlsx.xlsx",
        "line_number": 20,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "Store ALUout to Register File\nReg[IR[20-16]]=ALUout 2 0x0 0x20 X 0 (false) (false) (false) (false) (false) 6011 1867 6736 3105\nsub Alu = A_reg - B_reg, ALUout = alu 1 0x0 0x22 X 2 (false) (false) (false) (false) (false) 4929########7988\nStore ALUout to Register File\nReg[IR[20-16]]=ALUout 2 0x0 0x22 X 0 (false) (false) (false) (false) (false)"
    },
    {
        "filename": "/root/ccsrch/tests/xlsx.xlsx",
        "line_number": 27,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "Reg[IR[20-16]]=MDLR 3 0x23 X X 0 (false) (false) (false) (false) (false) 4939394046267988\nsw alu=A_reg+sign-extend(IR[15-0]) , MAR = alu 1 0x2b X X 2 (false) (false) (false) (false) true 388734498671000\nMEM[MAR] = MDSR 2 0x2b X VISA, 4485########2217 0 (false) (false) true (false) (false)\nbeq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false)"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 3,
        "card_number": "6011########3105",
        "card_type": "Discover",
        "context": "Valid Dummy Pan Numbers\n\n\n\nDiscover, 6011########3105\n\nDiscover, 6011963280099774\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 4,
        "card_number": "6011########9774",
        "card_type": "Discover",
        "context": "\n\nDiscover, 6011186767363105\n\nDiscover, 6011########9774\n\n\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 6,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "Discover, 6011963280099774\n\n\n\nMasterCard, 5173########9055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "\n\nMasterCard, 5173582815239055\n\nMasterCard, 5135########0694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173582815239055\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 8,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "MasterCard, 5173582815239055\n\nMasterCard, 5135299256640694\n\nMasterCard, 5263########7775\n\nMasterCard, 5173582815239055\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 9,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "MasterCard, 5135299256640694\n\nMasterCard, 5263067393947775\n\nMasterCard, 5173########9055\n\n\n\nVISA, 4012888888881881\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 11,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "MasterCard, 5173582815239055\n\n\n\nVISA, 4012########1881\n\nVISA, 4485983356242217\n\nVISA, 4716204638950696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012888888881881\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 13,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4012888888881881\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 14,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "VISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4485########2217\n\nVISA, 4716204638950696\n\nVISA, 4024007135532710\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 15,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "VISA, 4716########0696\n\nVISA, 4485983356242217\n\nVISA, 4716########0696\n\nVISA, 4024007135532710\n\nVISA, 4556474670906442\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 16,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "VISA, 4485983356242217\n\nVISA, 4716204638950696\n\nVISA, 4024########2710\n\nVISA, 4556474670906442\n\nVISA, 4929391046267988\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 17,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "VISA, 4716204638950696\n\nVISA, 4024007135532710\n\nVISA, 4556########6442\n\nVISA, 4929391046267988\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 18,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "VISA, 4024007135532710\n\nVISA, 4556474670906442\n\nVISA, 4929########7988\n\n\n\nAmerican Express, 378734493671000\n"
    },
    {
        "filename": "/root/ccsrch/tests/test2.zip -> /tmp/tmp4n5demwe/basic.txt",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "VISA, 4929391046267988\n\n\n\nAmerican Express, 3787#######1000\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/docx.docx -> /tmp/tmp9pwq1nhl/word/document.xml",
        "line_number": 2,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n\n<w:document xmlns:o=\"urn:schemas-microsoft-com:office:office\" xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" xmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" xmlns:w10=\"urn:schemas-microsoft-com:office:word\" xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\"><w:body><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>The Defence Signals Directorate\u2019s (DSD) information security function is outlined in the</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId2\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Intelligence Services Act\u00a02001</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. As the Commonwealth authority on the security of information, DSD provides advice and other assistance to federal and state authorities on matters relating to the security and integrity of information.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD is responsible for producing ICT security policy and standards for government and publishes these in the Australian Government</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId3\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Information Security Manual (ISM, formerly ACSI\u00a033)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. DSD is heavily involved in specialised information security traininVISA, 4716204852950696g, policy guidance and professional forums in support of government information security. We draw widely on the expertise within DSD, and aim to add unique value to the practice of ICT security in government.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD facilitates the evaluation of ICT security products for the Australian Government. The</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId4\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Evaluated Products List (EPL)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>lists ICT security products certified by the DSD-managed</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId5\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Australasian Information Security Evaluation Program (AISEP)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>for use in Australian and New Zealand government agencies. AISEP allows the security claims of ICT products to be independently assessed against internationally recognised</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId6\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Common Criteria (CC)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. Our evaluation programs include cryptographic, high assurance and cross-domain solutions.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>The</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId7\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Emanation Security Program</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>sets out the</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"000000\"/><w:sz w:val=\"23\"/><w:szCs w:val=\"23\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"000000\"/><w:sz w:val=\"23\"/><w:szCs w:val=\"23\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>VISA, 4012########1881</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:bookmarkStart w:id=\"0\" w:name=\"_GoBack\"/><w:bookmarkStart w:id=\"1\" w:name=\"_GoBack\"/><w:bookmarkEnd w:id=\"1\"/><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t xml:space=\"preserve\"> </w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>requirements for government and industry agencies to be formally recognised by the national authority, the Defence Signals Directorate (DSD), to conduct emanation security practices to national standards.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD advises the Australian Government on high-grade cryptographic equipment and cryptographic modernisation. We make sure Australia is at the forefront of cryptology by keeping abreast of emerging equipment and technologies.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Countering the threat to the security of government information requires DSD to work closely with the ICT industry to deliver threat and vulnerability information and help DSD build capability and expand its capacity to secure government ICT.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>MasterCard, 5173582815239055</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Our</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId8\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Cyber Security Operations Centre (CSOC)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>has two main roles. It provides government with a comprehensive understanding of sophisticated cyber threats against Australian interests, in addition to coordinating and assisting operational responses to cyber events of national importance across government and systems of national importance. Its services revolve around ICT security incident response, ICT systMasterCard, 5263067493947775em forensics and specialist assistance, vulnerability assessments, education and awareness. DSD\u2019s expertise is used to identify and help mitigate vulnerabilities within Australian government systems and the National Information Infrastructure.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Finally, DSD participates in whole-of-government efforts to promote</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId9\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>cyber security</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>to all Australians. Our</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId10\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Top 35 Mitigation Strategies</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>emphasises the importance of keeping software up to date to minimise the opportunities for criminals to steal or misuse your information. TAmerican Express, 378734493671000</w:t><w:t>he</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId11\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>CyberSense video</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>shows some of these threats.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style0\"/></w:pPr><w:hyperlink r:id=\"rId12\"><w:r><w:rPr><w:rStyle w:val=\"style17\"/></w:rPr><w:t>http://www.dsd.gov.au/infosec/</w:t></w:r></w:hyperlink></w:p><w:sectPr><w:formProt w:val=\"false\"/><w:pgSz w:h=\"16838\" w:w=\"11906\"/><w:docGrid w:charSpace=\"0\" w:linePitch=\"360\" w:type=\"default\"/><w:textDirection w:val=\"lrTb\"/><w:pgNumType w:fmt=\"decimal\"/><w:type w:val=\"nextPage\"/><w:pgMar w:bottom=\"1440\" w:left=\"1440\" w:right=\"1440\" w:top=\"1440\"/></w:sectPr></w:body></w:document>"
    },
    {
        "filename": "/root/ccsrch/tests/docx.docx -> /tmp/tmp9pwq1nhl/word/document.xml",
        "line_number": 2,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n\n<w:document xmlns:o=\"urn:schemas-microsoft-com:office:office\" xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" xmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" xmlns:w10=\"urn:schemas-microsoft-com:office:word\" xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\"><w:body><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>The Defence Signals Directorate\u2019s (DSD) information security function is outlined in the</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId2\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Intelligence Services Act\u00a02001</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. As the Commonwealth authority on the security of information, DSD provides advice and other assistance to federal and state authorities on matters relating to the security and integrity of information.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD is responsible for producing ICT security policy and standards for government and publishes these in the Australian Government</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId3\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Information Security Manual (ISM, formerly ACSI\u00a033)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. DSD is heavily involved in specialised information security traininVISA, 4716204852950696g, policy guidance and professional forums in support of government information security. We draw widely on the expertise within DSD, and aim to add unique value to the practice of ICT security in government.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD facilitates the evaluation of ICT security products for the Australian Government. The</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId4\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Evaluated Products List (EPL)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>lists ICT security products certified by the DSD-managed</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId5\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Australasian Information Security Evaluation Program (AISEP)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>for use in Australian and New Zealand government agencies. AISEP allows the security claims of ICT products to be independently assessed against internationally recognised</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId6\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Common Criteria (CC)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. Our evaluation programs include cryptographic, high assurance and cross-domain solutions.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>The</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId7\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Emanation Security Program</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>sets out the</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"000000\"/><w:sz w:val=\"23\"/><w:szCs w:val=\"23\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"000000\"/><w:sz w:val=\"23\"/><w:szCs w:val=\"23\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>VISA, 4012888888881881</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:bookmarkStart w:id=\"0\" w:name=\"_GoBack\"/><w:bookmarkStart w:id=\"1\" w:name=\"_GoBack\"/><w:bookmarkEnd w:id=\"1\"/><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t xml:space=\"preserve\"> </w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>requirements for government and industry agencies to be formally recognised by the national authority, the Defence Signals Directorate (DSD), to conduct emanation security practices to national standards.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD advises the Australian Government on high-grade cryptographic equipment and cryptographic modernisation. We make sure Australia is at the forefront of cryptology by keeping abreast of emerging equipment and technologies.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Countering the threat to the security of government information requires DSD to work closely with the ICT industry to deliver threat and vulnerability information and help DSD build capability and expand its capacity to secure government ICT.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>MasterCard, 5173########9055</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Our</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId8\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Cyber Security Operations Centre (CSOC)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>has two main roles. It provides government with a comprehensive understanding of sophisticated cyber threats against Australian interests, in addition to coordinating and assisting operational responses to cyber events of national importance across government and systems of national importance. Its services revolve around ICT security incident response, ICT systMasterCard, 5263067493947775em forensics and specialist assistance, vulnerability assessments, education and awareness. DSD\u2019s expertise is used to identify and help mitigate vulnerabilities within Australian government systems and the National Information Infrastructure.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Finally, DSD participates in whole-of-government efforts to promote</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId9\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>cyber security</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>to all Australians. Our</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId10\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Top 35 Mitigation Strategies</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>emphasises the importance of keeping software up to date to minimise the opportunities for criminals to steal or misuse your information. TAmerican Express, 378734493671000</w:t><w:t>he</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId11\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>CyberSense video</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>shows some of these threats.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style0\"/></w:pPr><w:hyperlink r:id=\"rId12\"><w:r><w:rPr><w:rStyle w:val=\"style17\"/></w:rPr><w:t>http://www.dsd.gov.au/infosec/</w:t></w:r></w:hyperlink></w:p><w:sectPr><w:formProt w:val=\"false\"/><w:pgSz w:h=\"16838\" w:w=\"11906\"/><w:docGrid w:charSpace=\"0\" w:linePitch=\"360\" w:type=\"default\"/><w:textDirection w:val=\"lrTb\"/><w:pgNumType w:fmt=\"decimal\"/><w:type w:val=\"nextPage\"/><w:pgMar w:bottom=\"1440\" w:left=\"1440\" w:right=\"1440\" w:top=\"1440\"/></w:sectPr></w:body></w:document>"
    },
    {
        "filename": "/root/ccsrch/tests/docx.docx -> /tmp/tmp9pwq1nhl/word/document.xml",
        "line_number": 2,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n\n<w:document xmlns:o=\"urn:schemas-microsoft-com:office:office\" xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" xmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" xmlns:w10=\"urn:schemas-microsoft-com:office:word\" xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\"><w:body><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>The Defence Signals Directorate\u2019s (DSD) information security function is outlined in the</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId2\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Intelligence Services Act\u00a02001</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. As the Commonwealth authority on the security of information, DSD provides advice and other assistance to federal and state authorities on matters relating to the security and integrity of information.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD is responsible for producing ICT security policy and standards for government and publishes these in the Australian Government</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId3\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Information Security Manual (ISM, formerly ACSI\u00a033)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. DSD is heavily involved in specialised information security traininVISA, 4716204852950696g, policy guidance and professional forums in support of government information security. We draw widely on the expertise within DSD, and aim to add unique value to the practice of ICT security in government.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD facilitates the evaluation of ICT security products for the Australian Government. The</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId4\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Evaluated Products List (EPL)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>lists ICT security products certified by the DSD-managed</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId5\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Australasian Information Security Evaluation Program (AISEP)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>for use in Australian and New Zealand government agencies. AISEP allows the security claims of ICT products to be independently assessed against internationally recognised</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId6\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Common Criteria (CC)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>. Our evaluation programs include cryptographic, high assurance and cross-domain solutions.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>The</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId7\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Emanation Security Program</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>sets out the</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"000000\"/><w:sz w:val=\"23\"/><w:szCs w:val=\"23\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"000000\"/><w:sz w:val=\"23\"/><w:szCs w:val=\"23\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>VISA, 4012888888881881</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:bookmarkStart w:id=\"0\" w:name=\"_GoBack\"/><w:bookmarkStart w:id=\"1\" w:name=\"_GoBack\"/><w:bookmarkEnd w:id=\"1\"/><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t xml:space=\"preserve\"> </w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>requirements for government and industry agencies to be formally recognised by the national authority, the Defence Signals Directorate (DSD), to conduct emanation security practices to national standards.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>DSD advises the Australian Government on high-grade cryptographic equipment and cryptographic modernisation. We make sure Australia is at the forefront of cryptology by keeping abreast of emerging equipment and technologies.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Countering the threat to the security of government information requires DSD to work closely with the ICT industry to deliver threat and vulnerability information and help DSD build capability and expand its capacity to secure government ICT.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>MasterCard, 5173582815239055</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Our</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId8\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Cyber Security Operations Centre (CSOC)</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>has two main roles. It provides government with a comprehensive understanding of sophisticated cyber threats against Australian interests, in addition to coordinating and assisting operational responses to cyber events of national importance across government and systems of national importance. Its services revolve around ICT security incident response, ICT systMasterCard, 5263067493947775em forensics and specialist assistance, vulnerability assessments, education and awareness. DSD\u2019s expertise is used to identify and help mitigate vulnerabilities within Australian government systems and the National Information Infrastructure.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style23\"/><w:ind w:hanging=\"0\" w:left=\"225\" w:right=\"225\"/><w:spacing w:after=\"28\" w:before=\"28\"/></w:pPr><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Finally, DSD participates in whole-of-government efforts to promote</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId9\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>cyber security</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>to all Australians. Our</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId10\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>Top 35 Mitigation Strategies</w:t></w:r></w:hyperlink><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>emphasises the importance of keeping software up to date to minimise the opportunities for criminals to steal or misuse your information. TAmerican Express, 3787#######1000</w:t><w:t>he</w:t></w:r><w:r><w:rPr><w:rStyle w:val=\"style16\"/><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>\u00a0</w:t></w:r><w:hyperlink r:id=\"rId11\"><w:r><w:rPr><w:color w:val=\"6699CC\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rStyle w:val=\"style17\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>CyberSense video</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val=\"333333\"/><w:sz w:val=\"21\"/><w:szCs w:val=\"21\"/><w:rFonts w:ascii=\"Arial\" w:cs=\"Arial\" w:hAnsi=\"Arial\"/></w:rPr><w:t>shows some of these threats.</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"style0\"/></w:pPr><w:hyperlink r:id=\"rId12\"><w:r><w:rPr><w:rStyle w:val=\"style17\"/></w:rPr><w:t>http://www.dsd.gov.au/infosec/</w:t></w:r></w:hyperlink></w:p><w:sectPr><w:formProt w:val=\"false\"/><w:pgSz w:h=\"16838\" w:w=\"11906\"/><w:docGrid w:charSpace=\"0\" w:linePitch=\"360\" w:type=\"default\"/><w:textDirection w:val=\"lrTb\"/><w:pgNumType w:fmt=\"decimal\"/><w:type w:val=\"nextPage\"/><w:pgMar w:bottom=\"1440\" w:left=\"1440\" w:right=\"1440\" w:top=\"1440\"/></w:sectPr></w:body></w:document>"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 3,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "\nFile Name Format Platform PAN, CC company Valid Pan? Track Data included Track Number\nBBQ.doc MS Word doc Any MasterCard, 5173########9055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 4,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "File Name Format Platform PAN, CC company Valid Pan? Track Data included Track Number\nBBQ.doc MS Word doc Any MasterCard, 5173582815239055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012########1881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 5,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "BBQ.doc MS Word doc Any MasterCard, 5173582815239055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 3787#######1000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 6,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "The Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485########2217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "MIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135########0694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 8,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "MIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716########0696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 9,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "DrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 3876######5160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 10,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "bridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485########2217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485########2217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 11,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "WmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173########9055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "restaurant.xml XML ANY VISA, 4485########2217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485########2217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 13,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "Pen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 3787#######1000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 14,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "control-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135########0694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 16,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "linux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929########7988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 17,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "ubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 17,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "ubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 18,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "diving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 18,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "diving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 19,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "archive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 19,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "archive.zip zip ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485########2217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "stuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 3787#######1000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO\nCPU.xlsx MS Excel xlsx Any MasterCard, 5173452815239055 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 25,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "diffie.pdf pdf ANY Diners 30249963624666 NO NO\nmslogfile.xml XML MS Log American Express, 388734498671000 NO NO\nLocalizable.strings strings MAC OS VISA, 4024########2710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 26,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "mslogfile.xml XML MS Log American Express, 388734498671000 NO NO\nLocalizable.strings strings MAC OS VISA, 4024007135532710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263########7775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 27,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "Localizable.strings strings MAC OS VISA, 4024007135532710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485########2217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 28,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "CocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556########6442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 29,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "StartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024########2710 YES YES (Track 1) %B4024########2710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "build-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 3787#######1000 YES YES (Track 2) ;3787#######1000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "build-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 3787#######1000 YES YES (Track 2) ;3787#######1000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 31,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "coms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135########0694 YES YES (Track 1) %B5135########0694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 32,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "parse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 32,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "parse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 33,
        "card_number": "3024######2904",
        "card_type": "Diners Club",
        "context": "cissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\naircraft.pdf pdf ANY Diners 3024######2904 YES YES (Track 1) %B3024######2904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 34,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "iecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 34,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "iecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 35,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "aircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 35,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "aircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/WmsServerList.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/The Defence Signals Directorate.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/stuff.tar -> /tmp/tmpkfu_717t/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/stuff.tar -> /tmp/tmpkfu_717t/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/StartupParameters.plist",
        "line_number": 11,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "        start   = \"Starting Cisco Systems VPN Client Kernel Extension\";\n\n        stop    = \"Stopping Cisco Systems VPN Client Kernel Extension\";\n\n\tcredit_card = \"VISA, 4485########2217\";\n\n    };\n\n}\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/restaurant.xml",
        "line_number": 25,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\t<restaurant name=\"Buffalo Grill\">\n\n\t\t<address>12 Chapel Street, Edinburgh, EH8 9AY</address>\n\n\t\t<cuisine>VISA, 4485########2217</cuisine>\n\n\t\t<phoneno>01316677427</phoneno>\n\n\t</restaurant>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/Pen_Tablet.dat",
        "line_number": 31,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "\"<TabletAwareApplicationInterface\",\"type=map>\"\n\n\"<NormalizedMaxPressure\",\"type=integer>1023</NormalizedMaxPressure>\"\n\n\"</TabletAwareApplicationInterface>\",\"MasterCard, 5173########9055\"\n\n\"</root>\"\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/MIPS.xlsx",
        "line_number": 27,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "Reg[IR[20-16]]=MDLR 3 0x23 X X 0 (false) (false) (false) (false) (false)\nsw alu=A_reg+sign-extend(IR[15-0]) , MAR = alu 1 0x2b X X 2 (false) (false) (false) (false) true\nMEM[MAR] = MDSR 2 0x2b X VISA, 4485########2217 0 (false) (false) true (false) (false)\nbeq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false)"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/MIPS.xls",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "beq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false) (false) (false) (false) (false) (false) (false) PC_ALU X A_PC B_IR_16x4 X (ADD)\nAmerican Express, 3787#######1000\nDo nothing 2 0x4 X False 0 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X X X X X\nbne Alu = A_reg \u2013 B_reg 1 0x5 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/linux_download.gpg",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "BesAoJgvzMplr6vwRdZJKRMkHqlDYVzf\n\n=V77a\n\nMasterCard, 5135########0694\n\n-----END PGP SIGNATURE-----\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/DrRoss.txt",
        "line_number": 40,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "Unix System Administration\n\nProfessional Affiliations:\n\nCredit Card Number : MasterCard, 5135########0694, expiry 15/05/13 ,CVV 747 Knock yourselves out !\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/coreutils_7.deb",
        "line_number": 1,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "American Express, 3787#######1000"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/CocoaStandard.sdef",
        "line_number": 22,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "\t\t\t<enumerator name=\"yes\" code=\"yes \" description=\"Save the file.\"/>\n\n\t\t\t<enumerator name=\"no\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator credit_card=\"MasterCard, 5263########7775\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator name=\"ask\" code=\"ask \" description=\"Ask the user whether or not to save the file.\"/>\n\n\t\t</enumeration>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/build-crt-0.log",
        "line_number": 19,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "\n\n\n\nVISA, 4556########6442\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/bridgepoint.rtf",
        "line_number": 19,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "\n\n\n\nVISA, 4716########0696\n\n\n\nIn the mid-1980s a need arose for a standardized, vendor-neutral, certification program that provided structure and demonstrated competence. In November 1988, the Special Interest Group for Computer Security (SIG-CS), a member of the Data Processing Management Association (DPMA), brought together several organizations interested in this. The International Information Systems Security Certification Consortium or \"(ISC)\" formed in mid-1989 as a non-profit organization with this goal.[5][6][7]\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/archive.zip -> /tmp/tmpmehbgrh7/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/archive.zip -> /tmp/tmpmehbgrh7/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/ValidPAN/aircraft.pdf",
        "line_number": 64,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "\nAmerican Express, \n3787#######1000 \n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/Track Data/trackExample.zip -> /tmp/tmp9laf41xz/zipzip.xml",
        "line_number": 7,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "    <domain>104.com.tw</domain>\n\n    <domain docMode=\"EmulateIE8\">10jqka.com.cn</domain>\n\n    <domain>;4485########2217=121212054321999876?1</domain>\n\n    <domain docMode=\"EmulateIE8\">115.com</domain>\n\n    <domain>118114.cn</domain>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/Track Data/parse table.xlsx",
        "line_number": 18,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "Exp3 Exp4 Ops3 Exp4 Ops3 Exp4 Ops3 Exp4 Ops3\nOps3 Track2\n;3787#######1000=121212054321999876?1 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 * Exp4 Ops3\nExp4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4\nOps4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4 \u03b5 \u03b5 Exp5 Ops4 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/Track Data/iecompatdata.xml",
        "line_number": 7,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "    <domain>104.com.tw</domain>\n\n    <domain docMode=\"EmulateIE8\">10jqka.com.cn</domain>\n\n    <domain>;4485########2217=121212054321999876?1</domain>\n\n    <domain docMode=\"EmulateIE8\">115.com</domain>\n\n    <domain>118114.cn</domain>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/Track Data/archive.zip -> /tmp/tmpfvy8tgdl/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy.zip -> /tmp/tmpvzlipt7n/Dummy/ContaminatedData/Track Data/archive.zip -> /tmp/tmpfvy8tgdl/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 3,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "\nFile Name Format Platform PAN, CC company Valid Pan? Track Data included Track Number\nBBQ.doc MS Word doc Any MasterCard, 5173########9055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 4,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "File Name Format Platform PAN, CC company Valid Pan? Track Data included Track Number\nBBQ.doc MS Word doc Any MasterCard, 5173582815239055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012########1881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 5,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "BBQ.doc MS Word doc Any MasterCard, 5173582815239055 YES NO\nThe Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 3787#######1000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 6,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "The Defence Signals Directorate.docx MS Word docx Any VISA, 4012888888881881 YES NO\nMIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485########2217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "MIPS.xls MS Excel xls Any American Express, 378734493671000 YES NO\nMIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135########0694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 8,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "MIPS.xlsx MS Excel xlsX Any VISA, 4485983356242217 YES NO\nDrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716########0696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 9,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "DrRoss.txt TXT ANY MasterCard, 5135299256640694 YES NO\nbridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 3876######5160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 10,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "bridgepoint.rtf RTF ANY VISA, 4716204638950696 YES NO\nWmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485########2217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485########2217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 11,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "WmsServerList.xml XML MS Log Diners 38767186195160 YES NO\nrestaurant.xml XML ANY VISA, 4485983356242217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173########9055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 12,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "restaurant.xml XML ANY VISA, 4485########2217 YES NO\nPen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485########2217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 13,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "Pen_Tablet.dat dat ANY MasterCard, 5173582815239055 YES NO\ncontrol-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 3787#######1000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 14,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "control-unit-table.ods Open Office ods ANY VISA, 4485983356242217 YES NO\ncoreutils_7.deb deb Linux American Express, 378734493671000 YES NO\nlinux_download.gpg gpg Linux MasterCard, 5135########0694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 16,
        "card_number": "4929########7988",
        "card_type": "VISA",
        "context": "linux_download.gpg gpg Linux MasterCard, 5135299256640694 YES NO\nubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929########7988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 17,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "ubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 17,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "ubuntuFiles.list list Linux Diners 30249963624666 YES NO\ndiving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 18,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "diving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 18,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "diving_center.accdb MS Access ANY VISA, 4929391046267988 YES NO\narchive.zip zip ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 3876######5160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 19,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "archive.zip zip ANY VISA, 4012########1881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012########1881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012########1881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 19,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "archive.zip zip ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\nstuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485########2217 YES NO\naircraft.pdf pdf ANY American Express, 378734493671000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 20,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "stuff.tar tar ANY VISA, 4012888888881881, Diners 38767186195160 YES NO\notherStuff.wim wim ANY VISA, 4012888888881881 ,VISA, 4485983356242217 YES NO\naircraft.pdf pdf ANY American Express, 3787#######1000 YES NO\ndefcon.docx MS Word docx Any VISA, 4585983356242217 NO NO\nCPU.xlsx MS Excel xlsx Any MasterCard, 5173452815239055 NO NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 25,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "diffie.pdf pdf ANY Diners 30249963624666 NO NO\nmslogfile.xml XML MS Log American Express, 388734498671000 NO NO\nLocalizable.strings strings MAC OS VISA, 4024########2710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 26,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "mslogfile.xml XML MS Log American Express, 388734498671000 NO NO\nLocalizable.strings strings MAC OS VISA, 4024007135532710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263########7775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 27,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "Localizable.strings strings MAC OS VISA, 4024007135532710 YES NO\nCocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485########2217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 28,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "CocoaStandard.sdef sdef MAC OS MasterCard, 5263067393947775 YES NO\nStartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556########6442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 29,
        "card_number": "4024########2710",
        "card_type": "VISA",
        "context": "StartupParameters.plist plist MAC OS VISA, 4485983356242217 YES NO\nbuild-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024########2710 YES YES (Track 1) %B4024########2710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "build-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 3787#######1000 YES YES (Track 2) ;3787#######1000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "build-crt-0.log log MS Log VISA, 4556474670906442 YES NO\ncoms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 3787#######1000 YES YES (Track 2) ;3787#######1000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 31,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "coms3000.docx MS Word docx Any VISA, 4024007135532710 YES YES (Track 1) %B4024007135532710^ROSS/DAVID^121210100896000000?1\nparse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135########0694 YES YES (Track 1) %B5135########0694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 32,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "parse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 32,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "parse table.xlsx MS Excel xlsx Any American Express, 378734493671000 YES YES (Track 2) ;378734493671000=121212054321999876?1\ncissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 33,
        "card_number": "3024######2904",
        "card_type": "Diners Club",
        "context": "cissp.txt TXT ANY MasterCard, 5135299256640694 YES YES (Track 1) %B5135299256640694^BARAK/OBAMA^121210100896000000?1\niecompatdata.xml XML ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\naircraft.pdf pdf ANY Diners 3024######2904 YES YES (Track 1) %B3024######2904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485983356242217 YES YES (Track 2) ;4485983356242217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 34,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "iecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 34,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "iecompatdata.xml XML ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\naircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 35,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "aircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/Dummy_Data_Info.xlsx",
        "line_number": 35,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "aircraft.pdf pdf ANY Diners 30249963622904 YES YES (Track 1) %B30249963622904^MONTGOMERY/JAMES^121210100896000000?1\ntrackExample.zip zip ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1\nasis_top_secret.ods Open Office ods ANY VISA, 4485########2217 YES YES (Track 2) ;4485########2217=121212054321999876?1"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/Track Data/trackExample.zip -> /tmp/tmpsbo2v5oi/zipzip.xml",
        "line_number": 7,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "    <domain>104.com.tw</domain>\n\n    <domain docMode=\"EmulateIE8\">10jqka.com.cn</domain>\n\n    <domain>;4485########2217=121212054321999876?1</domain>\n\n    <domain docMode=\"EmulateIE8\">115.com</domain>\n\n    <domain>118114.cn</domain>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/Track Data/iecompatdata.xml",
        "line_number": 7,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "    <domain>104.com.tw</domain>\n\n    <domain docMode=\"EmulateIE8\">10jqka.com.cn</domain>\n\n    <domain>;4485########2217=121212054321999876?1</domain>\n\n    <domain docMode=\"EmulateIE8\">115.com</domain>\n\n    <domain>118114.cn</domain>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/Track Data/parse table.xlsx",
        "line_number": 18,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "Exp3 Exp4 Ops3 Exp4 Ops3 Exp4 Ops3 Exp4 Ops3\nOps3 Track2\n;3787#######1000=121212054321999876?1 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 * Exp4 Ops3\nExp4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4\nOps4 Exp5 Ops4 Exp5 Ops4 Exp5 Ops4 \u03b5 \u03b5 Exp5 Ops4 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5 \u03b5"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/Track Data/archive.zip -> /tmp/tmpfrphurbr/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/Track Data/archive.zip -> /tmp/tmpfrphurbr/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/MIPS.xls",
        "line_number": 30,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "beq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false) (false) (false) (false) (false) (false) (false) PC_ALU X A_PC B_IR_16x4 X (ADD)\nAmerican Express, 3787#######1000\nDo nothing 2 0x4 X False 0 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X X X X X\nbne Alu = A_reg \u2013 B_reg 1 0x5 X X 2 (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) (false) X X A_REG B_REG X (SUB)"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/archive.zip -> /tmp/tmpq14kgwmj/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/archive.zip -> /tmp/tmpq14kgwmj/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/StartupParameters.plist",
        "line_number": 11,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "        start   = \"Starting Cisco Systems VPN Client Kernel Extension\";\n\n        stop    = \"Stopping Cisco Systems VPN Client Kernel Extension\";\n\n\tcredit_card = \"VISA, 4485########2217\";\n\n    };\n\n}\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/coreutils_7.deb",
        "line_number": 1,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "American Express, 3787#######1000"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/stuff.tar -> /tmp/tmp1naug1f0/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/stuff.tar -> /tmp/tmp1naug1f0/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/build-crt-0.log",
        "line_number": 19,
        "card_number": "4556########6442",
        "card_type": "VISA",
        "context": "\n\n\n\nVISA, 4556########6442\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/Pen_Tablet.dat",
        "line_number": 31,
        "card_number": "5173########9055",
        "card_type": "MasterCard",
        "context": "\"<TabletAwareApplicationInterface\",\"type=map>\"\n\n\"<NormalizedMaxPressure\",\"type=integer>1023</NormalizedMaxPressure>\"\n\n\"</TabletAwareApplicationInterface>\",\"MasterCard, 5173########9055\"\n\n\"</root>\"\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/DrRoss.txt",
        "line_number": 40,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "Unix System Administration\n\nProfessional Affiliations:\n\nCredit Card Number : MasterCard, 5135########0694, expiry 15/05/13 ,CVV 747 Knock yourselves out !\n\n\n\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/The Defence Signals Directorate.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/CocoaStandard.sdef",
        "line_number": 22,
        "card_number": "5263########7775",
        "card_type": "MasterCard",
        "context": "\t\t\t<enumerator name=\"yes\" code=\"yes \" description=\"Save the file.\"/>\n\n\t\t\t<enumerator name=\"no\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator credit_card=\"MasterCard, 5263########7775\" code=\"no  \" description=\"Do not save the file.\"/>\n\n\t\t\t<enumerator name=\"ask\" code=\"ask \" description=\"Ask the user whether or not to save the file.\"/>\n\n\t\t</enumeration>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/linux_download.gpg",
        "line_number": 7,
        "card_number": "5135########0694",
        "card_type": "MasterCard",
        "context": "BesAoJgvzMplr6vwRdZJKRMkHqlDYVzf\n\n=V77a\n\nMasterCard, 5135########0694\n\n-----END PGP SIGNATURE-----\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/MIPS.xlsx",
        "line_number": 27,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "Reg[IR[20-16]]=MDLR 3 0x23 X X 0 (false) (false) (false) (false) (false)\nsw alu=A_reg+sign-extend(IR[15-0]) , MAR = alu 1 0x2b X X 2 (false) (false) (false) (false) true\nMEM[MAR] = MDSR 2 0x2b X VISA, 4485########2217 0 (false) (false) true (false) (false)\nbeq Alu = A_reg \u2013 B_reg 1 0x4 X X 2 (false) (false) (false) (false) (false)\nPC = ALU (A_PC,B_IR_16X4 ) 2 0x4 X True 0 (false) (false) (false) true (false)"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/defense.docx",
        "line_number": 15,
        "card_number": "4012########1881",
        "card_type": "VISA",
        "context": "\n\nVISA, 4012########1881\n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/WmsServerList.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/bridgepoint.rtf",
        "line_number": 19,
        "card_number": "4716########0696",
        "card_type": "VISA",
        "context": "\n\n\n\nVISA, 4716########0696\n\n\n\nIn the mid-1980s a need arose for a standardized, vendor-neutral, certification program that provided structure and demonstrated competence. In November 1988, the Special Interest Group for Computer Security (SIG-CS), a member of the Data Processing Management Association (DPMA), brought together several organizations interested in this. The International Information Systems Security Certification Consortium or \"(ISC)\" formed in mid-1989 as a non-profit organization with this goal.[5][6][7]\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/list.xml",
        "line_number": 25,
        "card_number": "3876######5160",
        "card_type": "Diners Club",
        "context": "  </Server>\n\n  <Server>\n\n    <GetCapabilitiesUrl>Diners 3876######5160</GetCapabilitiesUrl>\n\n  </Server>\n\n  <Server>\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/aircraft.pdf",
        "line_number": 64,
        "card_number": "3787#######1000",
        "card_type": "American Express",
        "context": "\nAmerican Express, \n3787#######1000 \n\n"
    },
    {
        "filename": "/root/ccsrch/tests/tmp/Dummy/ContaminatedData/ValidPAN/restaurant.xml",
        "line_number": 25,
        "card_number": "4485########2217",
        "card_type": "VISA",
        "context": "\t<restaurant name=\"Buffalo Grill\">\n\n\t\t<address>12 Chapel Street, Edinburgh, EH8 9AY</address>\n\n\t\t<cuisine>VISA, 4485########2217</cuisine>\n\n\t\t<phoneno>01316677427</phoneno>\n\n\t</restaurant>\n"
    }
]
```


