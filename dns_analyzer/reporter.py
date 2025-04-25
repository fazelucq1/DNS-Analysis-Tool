import os
from pathlib import Path
import datetime
from jinja2 import Environment, FileSystemLoader
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

def get_template_dir():
    """Get the absolute path to templates directory"""
    current_dir = Path(__file__).parent
    template_dir = current_dir / 'templates'
    
    if not template_dir.exists():
        raise FileNotFoundError(
            f"Template directory not found at: {template_dir}\n"
            f"Please ensure the 'templates' folder exists in {current_dir}"
        )
    return str(template_dir)

def generate_html_report(domain, analysis, risks, output_path, comparison=None):
    env = Environment(loader=FileSystemLoader(get_template_dir()))
    template = env.get_template('report_template.html')
    
    html_content = template.render(
        domain=domain,
        analysis=analysis,
        risks=risks,
        comparison=comparison,
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    
    with open(output_path, 'w') as f:
        f.write(html_content)

def generate_pdf_report(domain, analysis, risks, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    # Title
    elements.append(Paragraph(f"DNS Analysis Report: {domain}", styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Analysis Results
    elements.append(Paragraph("Analysis Results", styles['Heading2']))
    analysis_data = [
        ["Record Type", "Value"],
        *[[k, str(v)] for k, v in analysis.items()]
    ]
    analysis_table = Table(analysis_data, colWidths=[200, 300])
    elements.append(analysis_table)
    
    # Security Risks
    if risks:
        elements.append(Spacer(1, 12))
        elements.append(Paragraph("Security Risks", styles['Heading2']))
        for risk in risks:
            elements.append(Paragraph(f"• {risk}", styles['Normal']))
    
    doc.build(elements)

def generate_report(domain, analysis, risks, format, output_path, **kwargs):
    try:
        if format == 'html':
            generate_html_report(
                domain,
                analysis,
                risks,
                output_path,
                comparison=kwargs.get('comparison')
            )
        elif format == 'pdf':
            generate_pdf_report(domain, analysis, risks, output_path)
        else:
            raise ValueError(f"Unsupported format: {format}")
            
        print(f"Successfully generated {format.upper()} report at: {output_path}")
    except Exception as e:
        raise Exception(f"Failed to generate report: {str(e)}")
