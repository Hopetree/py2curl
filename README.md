# py2curl

将 python 的 requests 代码转换成 curl 命令

## 安装

```bash
pip install py2curl
```

## 使用

```python
import requests
import py2curl

req = requests.get('https://tendcode.com')
result = py2curl.render(req.request)
print(result)
### curl -k -v -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate" -H "Connection: keep-alive" -H "User-Agent: python-requests/2.19.1" https://tendcode.com/
```
