if exists("b:did_plugin_copywriting")
  finish
endif

let b:did_plugin_copywriting=1

py3 import vim
py3 from copywriting.vim_entry import copywriting_format

function copywriting#format() range
  let is_visual_mode = a:firstline == line("'<") && a:lastline == line("'>")
  if is_visual_mode == 1
    py3 copywriting_format(vim.eval("a:firstline"), vim.eval("a:lastline"))
  else
    py3 copywriting_format(-1, -1)
  endif
  echo "chinese-copywriting format done"
endfunction

command! -bang -range -nargs=? CopywritingFormat <line1>,<line2>call copywriting#format()

" ---------------- debugging ----------------------
" vmap <F6> :'<,'>call copywriting#format()<cr>
" vmap <F6> :CopywritingFormat<cr>
" ----------------end debugging -------------------
