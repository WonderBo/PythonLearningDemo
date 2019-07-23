#!/usr/bin/env python
#coding:utf-8

from lxml import etree

html_1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
</body>
</html>
'''

html_2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test3">
        我左青龙，
        <span id="tiger">
            右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>
            老牛在当中，
        </span>
        龙头在胸口。
    </div>
</body>
</html>
'''

selector_1 = etree.HTML(html_1)
selector_2 = etree.HTML(html_2)

#starts-with()获取相同字符开头属性的标签的相关内容
content_1 = selector_1.xpath("//div[starts-with(@id, 'test')]/text()")
for each in content_1:
    print each

# content_2 = selector_2.xpath("//div[@id='test3']/text()")
# for each in content_2:
#     print each

#string(.)获取嵌套标签里的全部文本内容
node = selector_2.xpath("//div[@id='test3']")[0]
content_3 = node.xpath("string(.)")
content_3 = content_3.replace("\n", "").replace(" ", "")
print content_3