if exists("b:did_plugin_copywriting")
  finish
endif

let b:did_plugin_copywriting=1

py3 import vim
py3 from copywriting import copywriting_format

function copywriting#format()
  py3 copywriting_format()
  echo "chinese_copywriting format done"
endfunction

command! -bang -range -nargs=? CopywritingFormat
      \ :call copywriting#format()
