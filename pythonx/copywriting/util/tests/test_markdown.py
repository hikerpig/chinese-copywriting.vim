# coding: utf-8

from . import PanguTest, format, pangu

outdent = format.outdent


class SpacingMarkdownTest(PanguTest):
    def test_chinese_after_code_block(self):
        text = outdent('''
        ``` text
        block
        ```

        中文word

        ''')

        expected_text = outdent('''
        ``` text
        block
        ```

        中文 word

        ''')

        result = format.format_markdown(text)

        self.assertEqual(len(text.splitlines()), len(result.splitlines()))
        self.assertEqual(result, expected_text)

    def test_should_not_remove_tail_empty_lines(self):
        text = outdent('''中文 word


        ''')
        self.assertEqual(format.format_markdown(text), text)

    def test_should_not_remove_top_empty_lines(self):
        text = outdent('''
        - [Pangu.vim](https://github.com/hotoo/pangu.vim)

        ''')

        result = format.format_markdown(text)
        self.assertEqual(result, text)
