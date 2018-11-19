import markdown
from poetic import PoeticExtension

md = """
This is just some normal text that is prose. It might have some _markdown_.

|||:

    this is a
    line of a poem

    and this is _another_
    stanza of a poem
    with **markdown** in it

|||

And then this is some **more** markdown that follows.
"""

print(markdown.markdown(md, extensions=[PoeticExtension()]))
