from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🙂 [link=https://alihkudeir.com] Ali H. kudeir", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source Projects", guide_style="bright_black")
python_tree.add("[bold link=https://github.com/kalideir/Express-REST-Starter-TypeScript/] Express Template[/]       - [bright_black]Express, REST Starter with TypeScript")

contrib_tree = tree.add("🔬 Experiments", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/koaning/akin]akin[/]           - [bright_black]sort based on zero-shot similarities")

contrib_tree = tree.add("👍 Contributions", guide_style="bright_black")

online_tree = tree.add("⭐ Online Projects", guide_style="bright_black")
online_tree.add("[bold link=https://koaning.io]koaning.io[/]     - [bright_black]personal blog")


console.print(tree)
console.print("")
console.print("[green]Follow me on twitter [bold link=https://twitter.com/kalideir]@kalideir[/]")
console.print("<img src="https://komarev.com/ghpvc/?username=kalideir" alt="https://github.com/kalideir" />")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
