#!/usr/bin/env python
#coding:utf-8

from lxml import etree

html = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li>这是第一条信息</li>
        <li>这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id="useless">
        <li>不需要的信息1</li>
        <li>不需要的信息2</li>
        <li>不需要的信息3</li>
    </ul>

    <div id="url">
        <a href="http://jikexueyuan.com">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
</div>

</body>
</html>
'''

selector = etree.HTML(html)

# //表示根节点，/表示下级节点，@表示属性，text()表示内容
#提取内容
content = selector.xpath("//ul[@id='useful']/li/text()")
for each in content:
    print each

#提取属性
attribute = selector.xpath("//a/@href")
for each in attribute:
    print each

title = selector.xpath("//a/@title")
print title[0]