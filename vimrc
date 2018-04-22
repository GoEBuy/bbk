syntax on
"使用vim的键盘模式
set nocompatible
"tab缩进
set tabstop=4 "tab宽为4个空格
"set softtabstop=4 "编辑模式下退格键的时候退回缩进的长度
set shiftwidth=4
"set expandtab "tab替换为空格 缩进用空格表示
"set noexpandtab "空格替换为tab， 制表符表示缩进
"自动对齐
set autoindent
"智能缩进
set smartindent

"高亮查找匹配
set hlsearch
set nu
autocmd InsertLeave * se nocul  " 用浅色高亮当前行  
autocmd InsertEnter * se cul    " 用浅色高亮当前行  
set ruler "显示标尺
set showcmd         " 输入的命令显示出来，看的清楚些
"set cmdheight=1     " 命令行（在状态行下）的高度，设置为1
set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8

set laststatus=2 "总是显示状态行

" 命令行（在状态行下）的高度，默认为1，这里是2
set cmdheight=2

"设置tags  
set tags=tags,/home/yyy/tags/tags_django
"set autochdir 
filetype on

" 高亮显示匹配的括号
set showmatch

"例如：如果是c/c++类型 
":autocmd FileType c,cpp :set foldmethod=syntax 
":autocmd FileType c,cpp :set number 
":autocmd FileType c,cpp :set cindent 
""例如：如果是python类型 
":autocmd FileType python :set number 
":autocmd FileType python : set foldmethod=syntax 
":autocmd FileType python :set smartindent



"新建.c,.h,.sh,.java文件，自动插入文件头 
"autocmd BufNewFile *.cpp,*.[ch],*.sh,*.java exec ":call SetTitle()" 
""定义函数SetTitle，自动插入文件头 



"##############快捷键####################
"开关tag窗口
map <f9> :TlistToggle<CR>
"使用左侧窗口
let Tlist_Use_Left_Window=1
