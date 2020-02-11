import vim

from copywriting.pangu import spacing_text
from copywriting.debug import debug


def copywriting_format():
    """replace  current buffer range with pangu.spacing_text
    """
    buffer_range = vim.current.range
    text = "\n".join(str(line) for line in buffer_range)
    result_text = spacing_text(text)
    # debug(result_text)

    # vim.eval("echo '{0}'".format(result_text))
    vim.current.range[:] = result_text.split("\n")
