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
## 扫描测试文件
![image](https://github.com/configworld768/ccsrch-python3/blob/main/img/WechatIMG333.png)<br>

## 增加新功能：打印卡号上下文内容,方便人工识别是否是真实的卡号信息
