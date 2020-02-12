" if exists("b:did_plugin_copywriting")
"   finish
" endif

let b:did_plugin_copywriting=1

py3 import vim
py3 from copywriting.vim_entry import copywriting_format

function copywriting#format(...) range
  let filetype = &filetype
  if a:0 > 0
    let filetype = a:1
  endif
  let is_visual_mode = a:firstline == line("'<") && a:lastline == line("'>")
  if is_visual_mode == 1
    py3 copywriting_format(vim.eval("a:firstline"), vim.eval("a:lastline"), filetype=vim.eval('l:filetype'))
  else
    py3 copywriting_format(-1, -1, filetype=vim.eval('l:filetype'))
  endif
  echo "chinese-copywriting format done"
endfunction

command! -range -nargs=* CopywritingFormat <line1>,<line2>call copywriting#format(<f-args>)

" ---------------- debugging ----------------------
" vmap <F6> :'<,'>call copywriting#format()<cr>
" vmap <F6> :CopywritingFormat<cr>
" ----------------end debugging -------------------
