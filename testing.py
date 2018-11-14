import markdown
from poetic import PoeticExtension

print(markdown.markdown('Apple\n:   Pomaceous fruit of plants of the genus Malus in\n    the family Rosaceae.', extensions=[PoeticExtension()]))
