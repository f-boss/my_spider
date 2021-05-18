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

" ==========杂项==========

" 显示行号
set number

" 去掉输入错误时的提示声音
set noerrorbells

" 右下角显示光标位置
set ruler

" 强调匹配的括号
set showmatch

" 光标短暂跳转到匹配括号的时间，单位为十分之一秒
set matchtime=2

" 显示当前正在键入的命令
set showcmd

" 设置自动切换目录为当前文件所在目录，用:sh时候会很方便
set autochdir

" 搜索时忽略大小写
set ignorecase

" 随着键入即时搜索
set incsearch

" 有一个或以上大写字母时仍大小写敏感
set smartcase

" ==========缩进==========

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

" ==========状态行========

" 自定义状态行
set statusline=%1*\%<%.50F\             " 显示当前文件相对路径
set statusline+=%=%2*\%y%m%r%h%w\       " 显示文件类型和文件状态
set statusline+=%3*\%{&ff}\[%{&fenc}]\  " 显示文件编码类型
set statusline+=%4*\ row:%l/%L,col:%c\  " 显示光标所在行与列
set statusline+=%5*\%3p%%\              " 显示当前光标位置百分比
hi User1 cterm=none ctermfg=25 ctermbg=0
hi User2 cterm=bold ctermfg=1 ctermbg=0
hi User3 cterm=bold ctermfg=1 ctermbg=0
hi User4 cterm=bold ctermfg=6 ctermbg=0
hi User5 cterm=bold ctermfg=green ctermbg=0

