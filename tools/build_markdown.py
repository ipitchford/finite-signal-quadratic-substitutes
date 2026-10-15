"""Format the unchanged LaTeX manuscript as Markdown using Pandoc."""
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
source = (root / 'paper.tex').read_text()
title = re.search(r'\\title\{([^}]+)\}', source).group(1)
abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', source, re.S).group(1).strip()

def citation(match):
    locator = match.group(1)
    return r'\texttt{[' + match.group(2) + (': ' + locator if locator else '') + ']}'

converted_source = re.sub(r'\\cite(?:\[([^]]*)\])?\{([^}]+)\}', citation, source)
converted_source = re.sub(r'\\begin\{thebibliography\}\{[^}]+\}', r'\\section*{References}', converted_source)
converted_source = converted_source.replace(r'\end{thebibliography}', '')
converted_source = re.sub(r'\\bibitem\{([^}]+)\}', lambda m: '\n' + r'\subsection*{[' + m.group(1) + ']}\n', converted_source)
result = subprocess.run(['pandoc', '--from=latex', '--to=markdown+tex_math_dollars', '--wrap=none'], input=converted_source, text=True, capture_output=True, check=True)
header = '# ' + title + '\n\nAnonymous — unpublished candidate, manuscript version 3; package 0.1.0-candidate. Qualified simulated academic assessment completed; not externally peer reviewed; publication pending.\n\n## Abstract\n\n' + abstract + '\n\n'
(root / 'paper.md').write_text(header + result.stdout)
print('Generated paper.md; named citations and bibliography entries preserved.')
