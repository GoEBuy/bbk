syntax on

"set background=dark
"colorscheme solarized
"使用vim的键盘模式
set nocompatible
"tab缩进
set tabstop=4
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
set cmdheight=2

set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8

set laststatus=2 "总是显示状态行

"设置tags  
set tags=tags,/home/yyy/tags/tags_django
"set autochdir 
filetype on


" 设置包括vundle和初始化相关的runtime path
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" 让vundle管理插件版本,必须
Plugin 'VundleVim/Vundle.vim'

" 以下范例用来支持不同格式的插件安装.
" 请将安装插件的命令放在vundle#begin和vundle#end之间.
" Github上的插件
" 格式为 Plugin '用户名/插件仓库名'
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'


" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'

Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" 安装L9，如果已经安装过这个插件，可利用以下格式避免命名冲突
Plugin 'ascenator/L9', {'name': 'newL9'}

"=======================已安装插件加载=====================
Plugin 'taglist.vim'
Plugin 'NERD_tree-Project'
Plugin 'code-snippet'
Plugin 'compilerpython.vim'
Plugin 'ctags.vim'
Plugin 'ctrlp.vim'
Plugin 'django.vim'
Plugin 'HTML5-Syntax-File'
Plugin 'pythoncomplete'
Plugin 'python_import.vim'
Plugin 'python.vim'
Plugin 'Session-manager'
Plugin 'Syntastic'
Plugin 'Tagbar'
Plugin 'TaskList.vim'
Plugin 'todolist.vim'
Plugin 'UltiSnips'
Plugin 'vim-django-support'
"Plugin 'pyflakes.vim'
Plugin 'Filesearch'
Plugin 'FindInNERDTree'
Plugin 'template.vim'
Plugin 'json.vim'
"Plugin 'javascript.vim'
Plugin 'html_FileCompletion'
Plugin 'html-xml-tag-matcher'
Plugin 'git-diff'
Plugin 'html5.vim'
Plugin 'indenthtml.vim'
Plugin 'The-NERD-tree'
Plugin 'The-NERD-Commenter'
Plugin 'checksyntax'
Plugin 'pydoc.vim'
Plugin 'matchit.zip'
Plugin 'xml.vim'
Plugin 'calendar.vim'
Plugin 'css3'
Plugin 'css.vim'
Plugin 'SQLComplete.vim'
let g:sql_type_default = 'mysql'
Plugin 'bookmarks.vim'


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

"
" 简要帮助文档
" :PluginList       - 列出所有已配置的插件
" :PluginInstall    - 安装插件,追加 `!` 用以更新或使用 :PluginUpdate
" :PluginSearch foo - 搜索 foo ; 追加 `!` 清除本地缓存
" :PluginClean      - 清除未使用插件,需要确认; 追加 `!` 自动批准移除未使用插件
"
" 查阅 :h vundle 获取更多细节和wiki以及FAQ



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
"会话管理
"set sessionoptions=blank,buffers,curdir,folds,tabpages,winsize
map <F7> :call SessionManagerToggle()<CR>


map <F8> :ToggleNERDTree<CR>


"开关tag窗口
"使用左侧窗口
let Tlist_Use_Left_Window=1
map <F9> :TlistToggle<CR>



"map <F5> :call RunPY()<CR>

"=====================自定义函数======================
func! RunPY()
exec "w"
exec "!python %<.py"
endfunc

