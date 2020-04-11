from markdown import markdown
from unittest import TestCase

from markdown_vimwiki.extension import VimwikiExtension


class TestExtension(TestCase):
    def test_default_config(self):
        source = """
Hello World
===========

* [-] rejected
* [ ] done0
    * [.] done1
    * [o] done2
    * [O] done3
    * [X] done4

:lorem:ipsum:
        """.strip()

        expected = """
<h1>Hello World</h1>
<ul>
<li class="rejected"> rejected</li>
<li class="done0"> done0<ul>
<li class="done1"> done1</li>
<li class="done2"> done2</li>
<li class="done3"> done3</li>
<li class="done4"> done4</li>
</ul>
</li>
</ul>
<p><span class="tag">lorem</span> <span class="tag">ipsum</span></p>
        """.strip()

        html = markdown(source, extensions=[VimwikiExtension()])
        self.assertEqual(html, expected)

        html = markdown(source, extensions=['markdown_vimwiki'])
        self.assertEqual(html, expected)

    def test_custom_config(self):
        source = """
Hello World
===========

* [i] yip
* [a] yap
* [o] yop

:lorem:ipsum:
        """.strip()

        expected = """
<h1>Hello World</h1>
<ul>
<li class="yip"> yip</li>
<li class="yap"> yap</li>
<li class="yop"> yop</li>
</ul>
<p><span class="bark">lorem</span> <span class="bark">ipsum</span></p>
        """.strip()

        html = markdown(source, extensions=[VimwikiExtension(
            list_levels='iao',
            list_classes=['yip', 'yap', 'yop'],
            tag_class='bark')])
        self.assertEqual(html, expected)
