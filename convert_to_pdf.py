import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension

# Read the markdown file
with open('base_paper_recommendation.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(md_content, extensions=[TableExtension(), TocExtension()])

# Create a complete HTML document with basic styling
html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Base Paper Recommendation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
        h1 { color: #333; border-bottom: 3px solid #007bff; padding-bottom: 10px; }
        h2 { color: #555; margin-top: 30px; }
        h3 { color: #666; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        table td, table th { border: 1px solid #ddd; padding: 12px; text-align: left; }
        table th { background-color: #f9f9f9; font-weight: bold; }
        table tr:nth-child(even) { background-color: #f9f9f9; }
        code { background-color: #f4f4f4; padding: 2px 6px; border-radius: 3px; }
        ul, ol { margin: 15px 0; padding-left: 30px; }
        p { margin: 15px 0; }
        page-break-after { page-break-after: always; }
    </style>
</head>
<body>
""" + html_content + """
</body>
</html>
"""

# Save HTML file
with open('base_paper_recommendation.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('HTML file created: base_paper_recommendation.html')

# Try to convert HTML to PDF using weasyprint if available
try:
    from weasyprint import HTML
    HTML('base_paper_recommendation.html').write_pdf('base_paper_recommendation.pdf')
    print('PDF created successfully: base_paper_recommendation.pdf')
except ImportError:
    print('weasyprint not installed. Installing...')
    import subprocess
    subprocess.run(['pip', 'install', 'weasyprint'], check=True)
    from weasyprint import HTML
    HTML('base_paper_recommendation.html').write_pdf('base_paper_recommendation.pdf')
    print('PDF created successfully: base_paper_recommendation.pdf')
except Exception as e:
    print(f'Could not create PDF with weasyprint: {e}')
    print('HTML file is ready for manual PDF conversion in a browser.')
