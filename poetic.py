import re
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension

class PoeticExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        md.preprocessors.add(
            "poem_formatter", PoemFormatter(md), ">html_block")

class PoemFormatter(Preprocessor):
    def run(self, lines):
        open_syntax = "|||:"
        close_syntax = "|||"
        out = []
        inside_poem = False
        for idx, line in enumerate(lines):
            if line == open_syntax:
                inside_poem = True
                # Remove blank opening line
                if lines[idx + 1] == '':
                    del lines[idx + 1]
                out.append('<div class="mdx-poem"><div class="mdx-peom--stanza">')
            elif inside_poem == True and line != close_syntax:
                if line == '':
                    if lines[idx + 1] != close_syntax:
                        out.append('</div><div class="mdx-poem--stanza">')
                else:
                    out.append('<div class="mdx-poem--line">%s</div>' % line.strip())
            elif inside_poem == True and line == close_syntax:
                inside_poem = False
                out.append('</div></div>')
            else:
                # Return line untouched
                out.append(line)
        return out

def makeExtension(configs={}):
    return PoeticExtension(configs=configs)
