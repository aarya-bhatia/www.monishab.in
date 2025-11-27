import os
from jinja2 import Environment, FileSystemLoader
import shutil
from data.services import services, testimonials, consultations

TEMPLATE_DIR = "templates"
OUTPUT_DIR = "docs"
STATIC_DIR = "static"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
env.globals["static"] = STATIC_DIR

pages = [
    {
        "template": "index.html",
        "output": "index.html",
        "title": "Home",
        "context": {"services": services, "testimonials": testimonials, "consultations": consultations}
    }
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

for page in pages:
    print(f"Building template {page["template"]}")

    try:
        template = env.get_template(page["template"])
        output_html = template.render(
            title=page["title"],
            **page["context"]
        )

        with open(os.path.join(OUTPUT_DIR, page["output"]), "w") as f:
            f.write(output_html)

    except FileNotFoundError as e:
        print(e)


dirname = OUTPUT_DIR + "/" + STATIC_DIR
if os.path.exists(dirname):
    shutil.rmtree(dirname)
shutil.copytree(STATIC_DIR, dirname)

print("Build complete.")
