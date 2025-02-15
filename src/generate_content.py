import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(source, template, dest):
    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        dest_path = os.path.join(dest, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template, dest_path)
        else:
            generate_pages_recursive(from_path, template, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest = os.path.dirname(dest_path)
    if dest != "":
        os.makedirs(dest, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")
