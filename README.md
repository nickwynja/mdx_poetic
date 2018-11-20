## Usage

```python
import markdown
from mdx_poetic import PoeticExtension

md = """
This is just some normal text that is prose. It might have some _markdown_.

|||:

    this is a
    line of a poem

    and this is _another_
    stanza of a poem that has a really long line which will wrap
    and more **markdown** in it

|||

And then this is some **more** markdown that follows.
"""

print(markdown.markdown(md, extensions=[PoeticExtension()]))
```

Running that will give you an output like this:

```html
<p>This is just some normal text that is prose. It might have some <em>markdown</em>.</p>
<p><div class="mdx-poem"><div class="mdx-peom--stanza">
<div class="mdx-poem--line">this is a</div>
<div class="mdx-poem--line">line of a poem</div>
</div><div class="mdx-poem--stanza">
<div class="mdx-poem--line">and this is <em>another</em></div>
<div class="mdx-poem--line">stanza of a poem that has a really long line which will wrap</div>
<div class="mdx-poem--line">with <strong>markdown</strong> in it</div>
</div></div></p>
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
  margin-left: 40px;
  text-indent: -20px;
}
```

This will give you a nice clean result where `<div class="mdx-poem">` will be indented slightly, you get a line in between stanzas, and any wrapped lines will be indented under the beginning of the line:

![example](https://github.com/nickwynja/mdx_poetic/raw/master/example.png)
