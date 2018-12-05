## Install

```
pip install mdx_poetic
```

## Usage

````python
import markdown
from mdx_poetic import PoeticExtension

md = """
This is just some normal text that is prose. It might have some _markdown_.

```poem

    this is a
    line of a poem

    and this is _another_
    stanza of a poem that has a really long line which will wrap
    and more **markdown** in it

```

And then this is some **more** markdown that follows.
"""

print(markdown.markdown(md, extensions=[PoeticExtension()]))
````

Running that will give you an output like this:

```html
<p>This is just some normal text that is prose. It might have some <em>markdown</em>.</p>
<p><blockquote class="mdx-poem"><p class="mdx-peom--stanza">
<span class="mdx-poem--line">this is a<br></span>
<span class="mdx-poem--line">line of a poem<br></span>
</p><p class="mdx-poem--stanza">
<span class="mdx-poem--line">and this is <em>another</em><br></span>
<span class="mdx-poem--line">stanza of a poem that has a really long line which will wrap<br></span>
<span class="mdx-poem--line">and more <strong>markdown</strong> in it<br></span>
</p></blockquote></p>
<p>And then this is some <strong>more</strong> markdown that follows.</p>
```

But that won't be too useful without the help of some CSS:

```css
.mdx-poem {
  margin-top: 1rem;
}

.mdx-poem--stanza {
  margin-top: 1rem;
}

.mdx-poem .mdx-poem--line {
  margin: 0 0 0 40px;
  text-indent: -20px;
  padding: 0;
  display: block;
}
```

This will give you a nice clean result where `<blockquote class="mdx-poem">` will be indented slightly, you get a line in between stanzas, and any wrapped lines will be indented under the beginning of the line:


![example](https://github.com/nickwynja/mdx_poetic/raw/master/example.png)

Using `<blockquote>` and `<p>` tags with `<span><br></span>` was chosen intentionally to properly format in console RSS readers like [`newsboat`](https://newsboat.org/). Further testing might be necessary for visual compatibility with other readers as well the above is most accurate syntactically to the intended output.

### Developent

For pushlishing to PyPi:

```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
