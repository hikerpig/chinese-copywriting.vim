"""
vim 与文字处理功能的胶水模块，调用 pangu.py 进行格式化
"""
import vim

from copywriting.pangu import spacing_text
from copywriting.debug import debug


def copywriting_format(line_start, line_end):
    """replace  current buffer range with pangu.spacing_text
    """
    buffer = vim.current.buffer
    max_end = len(buffer) - 1

    debug("echo '{0}'".format(line_start))
    if line_start == -1:
        start = 0
        end = max_end
    else:
        start = max(int(line_start) - 1, 0)
        end = min(max_end, max(int(line_end) - 1, 0))

    end = max(end, start)

    buffer_range = buffer[start:end+1]
    text = "\n".join(str(line) for line in buffer_range)
    result_text = spacing_text(text)
    result_lines = result_text.splitlines()

    vim.current.buffer[start:end+1] = result_lines

