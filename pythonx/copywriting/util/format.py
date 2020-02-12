# coding: utf-8
from enum import Enum
from typing import List

from . import spacing, spacing_text


def outdent(text):
    lines = text.splitlines()
    if not lines:
        return text

    first_line_chars = list(lines[0])
    line_prefix = ''
    for i in range(len(first_line_chars)):
        if first_line_chars[i] is ' ':
            line_prefix += ' '
        else:
            break
    if not line_prefix:
        return text

    return "\n".join([line_prefix | line.strip() for line in lines])


class BlockType(Enum):
    """
    parser 当前处于的 block type
    """
    NORMAL = 'normal'
    BLOCK_CODE = 'block_code'


class Block:
    """
    一块内容，最小单位是一行
    """
    lines: List[str] = []
    block_type: BlockType

    def __init__(self, block_type, lines=[]):
        self.block_type = block_type
        self.lines = lines

    def append_line(self, line):
        self.lines.append(line)

    @property
    def content(self):
        return "\n".join(self.lines)

    @property
    def formatted_content(self):
        content = self.content
        if self.block_type is not BlockType.BLOCK_CODE:
            content = spacing_text(content)
        return content


def format_markdown(text):
    """
    Perform paranoid text spacing on markdown text
    """
    blocks: List[Block] = []
    lines: List[str] = text.splitlines()

    status: BlockType = BlockType.NORMAL

    cur_block: Block = None

    for line in lines:
        if status is BlockType.BLOCK_CODE:
            cur_block.append_line(line)
            if line[0:3] == '```':
                status = BlockType.NORMAL
                cur_block = None
        else:
            if line[0:3] == '```':
                status = BlockType.BLOCK_CODE
                cur_block = Block(BlockType.BLOCK_CODE, [line])
                blocks.append(cur_block)
            else:
                if cur_block and cur_block.block_type is BlockType.NORMAL:
                    cur_block.append_line(line)
                else:
                    cur_block = Block('normal', [line])
                    blocks.append(cur_block)

    result_contents = []
    for block in blocks:
        # print(block, len(block.lines))
        # print(block.formatted_content)
        result_contents.append(block.formatted_content)
    result = "\n".join(result_contents)
    # print('======= result ==========')
    # print(result)
    return result
