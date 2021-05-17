" 配色方案
colorscheme desert

" 语法高亮
syntax on

" 侦测文件类型
filetype on

" 载入文件插件类型
filetype plugin on

" 不同文件类型使用不同缩进
filetype indent on 

" ==========

" 显示行号
set number

" 去掉输入错误时的提示声音
set noerrorbells

" 右下角显示光标位置
set ruler

" ==========

" 打开自动缩进
set autoindent

" 所用C/C++的缩进方式
set cindent

" 为C程序提供自动缩进
set smartindent

" 将Tab转化为空格
set expandtab

" 设定Tab键长度为四
set tabstop=4

" 设置自动缩进长度为四个空格
set shiftwidth=4

" 设定退格键一次可以删除四个空格
set softtabstop=4

" 详细参考文档 :help smarttab 
"set smarttab

" ==========

" 自定义状态行
set statusline=%F%m%r%h%w[%L][%{&ff}]%y[%p%%][%04l,%04v]
"              | | | | |  |   |      |  |     |    |
"              | | | | |  |   |      |  |     |    +-- 当前列数
"              | | | | |  |   |      |  |     +-- 当前行数
"              | | | | |  |   |      |  +-- 当前光标位置百分比
"              | | | | |  |   |      +-- 使用的语法高亮器
"              | | | | |  |   +-- 文件格式
"              | | | | |  +-- 文件总行数
"              | | | | +-- 预览标志
"              | | | +-- 帮助文件标志
"              | | +-- 只读标志
"              | +-- 已修改标志
"              +-- 当前文件绝对路径
