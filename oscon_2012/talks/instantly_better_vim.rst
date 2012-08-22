====================
Instantly Better Vim
====================

:Date:
    2012-07-20

:Speaker:
    Damian Conway

:Slides:
    http://tinyurl.com/IBV2012 (also includes vim snippets)


The Gist
========

+ Handy snippets to make vim awesomer

Help
====

+ ``:helpgrep`` - search help for patterns
+ ``:vimgrep /pat/ files...`` - grep results into vim

Navigating
==========

+ ``ctrl-W T`` - turn a window into a tab
+ ``:set ruler`` - shows line num/pos
+ ``:help statusline`` - customize the ruler
+ ``nnoremap <SPACE> <PAGEDOWN>`` - hit space to page down in normal mode

Persistent Undos
================

+ ``ctrl-R`` - redo
+ ``earlier 30s`` - temporal undo (30s)
+ ``later 1m`` - temporal redo (1m)
+ Normally the undo buffer is lost

  + ``set undodir=$HOME/tmp/.VIM_UNDO_FILES`` - set undo dir
  + ``set undolevels=5000`` (default 1000)

+ ``:help undo-persistence``
+ Plugin to warn undo into previous session (see PDF)

Visual block mode
=================

+ Specify area to be affected; then specify command
+ ``ctrl-V``, navigate to select rectangular area
+ ``:set virtualedit=block`` - always stay in block
+ Persistent visual selections (in tarball: ``plugin/persistentvisuals.vim``)

  + ``gv`` - restore previous selection

+ Column highlighting (in tarball: ``plugin/visualguide.vim``)

Searching
=========

+ ``:set ignorecase`` - ignore case
+ ``:set smartcase`` - partial sensitivity: If string has a capital letter,
  search case-sensitive
+ Search highlighting

  + ``:highlight search ctermfg=white ctermbg=red``
  + ``:set hlsearch`` - enable search highlighting
  + ``:nohlsearch`` - disable highlighted results

Regex
=====

+ Metasyntax must be ``\``-escaped, e.g. ``\\t``
+ Start pattern with ``\v`` and all metasyntax will be treated as literals
+ ``nmap / /\v`` - make literal search the default
+ Search folding to fold buffer on search (in tarball: ``plugin/foldsearches.vim``)

Marks
=====

+ When you jump, vim leaves a mark
+ Mark hotness

  + With persistent undos these persist too!
  + `````` - go back to previous mark
  + ```.`` - jump to last place you modified the buffer
  + ```"`` - jump to last place from last session
  + ``ctrl-O`` - walk history of all jumps - backwards
  + ``ctrl-I`` - walk history of all jumps - forwards
  + ``g;`` - backward thru modifications
  + ``g,`` - forwards thru modifications

Advanced editing
================

+ ``y}`` - yank paragraph
+ ``diw`` - delete *surrounding* word
+ ``di(`` - delete between ``(...)``
+ ``di"`` - delete between ``"..."``
+ ``dit`` - delete between (x)html tags ``<...>``
+ ``vipJ`` - select paragraph, join all lines together
