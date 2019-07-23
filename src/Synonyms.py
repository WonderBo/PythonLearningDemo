#!/usr/bin/env python
#coding:utf-8

import synonyms

# 获取近义词
print synonyms.nearby("计算机科学")

# 输出近义词(display调用了synonyms的nearby方法)
synonyms.display("计算机技术")

# 获取两个词语或句子的相似度
print synonyms.compare("计算机科学", "计算机技术")