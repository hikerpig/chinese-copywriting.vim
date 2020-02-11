chinese-copywriting.vim 中文排版助手
---

用于格式化中文排版。

## 功能

- 中英文字符间增加一个半角空格
- 中文前后半角标点转成全角标点
- 全角英文、数字转成半角字符。

## 安装

使用 vim-plug:

```viml
Plug "hikerpig/chinese-copywriting.vim"
```

## 使用方式

### `:CopywritingFormat` command

手动执行该命令，将当前文件进行格式化。如果处于 visual 模式，将只格式化选中部分。

## 参考

- [中文文案排版指北](https://github.com/mzlogin/chinese-copywriting-guidelines)
- [pangu.py](https://github.com/vinta/pangu.py)
- [Pangu.vim](https://github.com/hotoo/pangu.vim)
