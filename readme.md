# pdfSplitter
pdf词频统计解决方案

初衷是为了解决一位朋友大规模 CNKI 中文文献内容词频统计的需求

作者使用此方法处理了数百篇 pdf 文件且达到了预期效果

在项目内包含了两个 pdf 文件用于示例（其中一篇内容不正常）

--------

### 依赖

pdfminer.six

jieba分词

pandas

--------

### 步骤

1. 将pdf文件通过批量命名工具，命名成数字序号的形式方便处理，放入 pdfs 目录

2. 安装 pdfminer.six

``` 
pip install pdfminer.six
```

3. 在 windows cmd 中将 pdfs 目录下的 pdf 文件批量转为 txts 目录下的 txt 文件

```
for /r %i in (*.pdf) do pdf2txt.py %~ni.pdf -o ..\txts\%~ni.txt
```

4. 运行 splitter

```
python splitter.py
```

5. 每篇 txt 都会在 outputs 目录下生成对应的词频统计结果

6. 汇总结果生成在根目录的 outputAll.txt 文件中


