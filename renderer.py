from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import yaml
import pandas as pd

def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)

def render_report(data: pd.DataFrame):
    cfg = load_config()

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    html_content = template.render(
        table=data.to_dict(orient="records"),
        summary={
            "rows": len(data),
            "columns": len(data.columns)
        }
    )

    output_path = cfg["report"]["output_path"]
    HTML(string=html_content).write_pdf(output_path)

    return output_path