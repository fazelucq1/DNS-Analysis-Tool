from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from jinja2 import Environment, FileSystemLoader
import os
from pathlib import Path

def generate_report(domain, analysis, risks, format, output, comparison=None, verbose=False):
    env = Environment(loader=FileSystemLoader('templates'))
    
    if format == 'html':
        template = env.get_template('report_template.html')
        html_content = template.render(
            domain=domain,
            analysis=analysis,
            risks=risks,
            comparison=comparison,
            verbose=verbose
        )
        with open(output, 'w') as f:
            f.write(html_content)
            
    elif format == 'pdf':
        doc = SimpleDocTemplate(output, pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []
        
        elements.append(Paragraph(f"DNS Analysis Report: {domain}", styles['Title']))
        elements.append(Spacer(1, 12))
        
        analysis_data = [[k, str(v)] for k, v in analysis.items()]
        analysis_table = Table(analysis_data, colWidths=[200, 300])
        elements.append(analysis_table)
        
        if risks:
            elements.append(Spacer(1, 12))
            elements.append(Paragraph("Security Risks:", styles['Heading2']))
            for risk in risks:
                elements.append(Paragraph(f"• {risk}", styles['Normal']))
        
        doc.build(elements)

def create_output_dir():
    Path("reports").mkdir(exist_ok=True)
