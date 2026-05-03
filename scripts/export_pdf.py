"""
PDF exporter: Markdown -> styled HTML -> Chrome headless PDF.
No watermarks, no external branding, clean metadata.
Usage: python scripts/export_pdf.py
"""
import os, sys, subprocess, tempfile, re
import markdown

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
REPO   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT    = os.path.join(REPO, "case-study", "pdf")

REPORT_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600&display=swap');
@page { size: letter; margin: 1in 1.1in 1in 1.1in; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', system-ui, sans-serif; font-size: 10.5pt;
       line-height: 1.65; color: #1a1a1a; }
.header-block { border-bottom: 2pt solid #0A2240; padding-bottom: 10pt;
                margin-bottom: 18pt; }
.header-block .title { font-family: 'Playfair Display', Georgia, serif;
                       font-size: 16pt; color: #0A2240; font-weight: 600; }
.header-block .subtitle { font-size: 9pt; color: #555; margin-top: 4pt; }
.header-block .meta { font-size: 8.5pt; color: #444; margin-top: 6pt;
                      display: flex; gap: 24pt; flex-wrap: wrap; }
.header-block .meta span { display: inline-block; }
h2 { font-family: 'Playfair Display', Georgia, serif; font-size: 11.5pt;
     color: #0A2240; font-weight: 600; margin-top: 18pt; margin-bottom: 6pt;
     border-bottom: 0.5pt solid #C8102E; padding-bottom: 3pt; }
p { margin-bottom: 8pt; }
strong { font-weight: 600; color: #1a1a1a; }
em { font-style: italic; }
hr { border: none; border-top: 0.5pt solid #ddd; margin: 12pt 0; }
a { color: #0A2240; text-decoration: none; }
.footer-note { font-size: 7.5pt; color: #888; margin-top: 20pt;
               border-top: 0.5pt solid #ddd; padding-top: 6pt; font-style: italic; }
ul { padding-left: 16pt; margin-bottom: 8pt; }
li { margin-bottom: 4pt; }
"""

CASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');
@page { size: letter; margin: 0.9in 1.1in 0.9in 1.1in; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', Georgia, serif; font-size: 10pt;
       line-height: 1.7; color: #1a1a1a; }
.case-title { font-family: 'Playfair Display', Georgia, serif;
              font-size: 22pt; font-weight: 700; color: #0A2240;
              line-height: 1.25; margin-bottom: 6pt; }
.case-meta { font-size: 8pt; color: #666; margin-bottom: 4pt; }
.case-disclaimer { font-size: 8pt; color: #777; border-left: 2pt solid #C8102E;
                   padding: 6pt 10pt; margin: 14pt 0; background: #fafaf8;
                   font-style: italic; line-height: 1.5; }
h2 { font-family: 'Playfair Display', Georgia, serif; font-size: 13pt;
     font-weight: 700; color: #0A2240; margin-top: 22pt; margin-bottom: 8pt; }
h3 { font-size: 10.5pt; font-weight: 600; color: #0A2240;
     margin-top: 14pt; margin-bottom: 5pt; }
p { margin-bottom: 9pt; }
blockquote { border-left: 2.5pt solid #C8102E; padding: 8pt 14pt;
             margin: 14pt 0; background: #f8f6f2; font-style: italic;
             font-size: 10pt; color: #333; line-height: 1.6; }
blockquote p { margin-bottom: 4pt; }
blockquote p:last-child { font-size: 8.5pt; font-style: normal;
                           color: #666; margin-bottom: 0; }
strong { font-weight: 600; }
hr { border: none; border-top: 0.75pt solid #ddd; margin: 16pt 0; }
ol, ul { padding-left: 18pt; margin-bottom: 9pt; }
li { margin-bottom: 5pt; }
a { color: #0A2240; }
.prepared-by { font-size: 7.5pt; color: #888; border-top: 0.5pt solid #ccc;
               margin-top: 24pt; padding-top: 8pt; font-style: italic; }
"""

REPORT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="author" content="Akshay Kumar">
<meta name="title" content="Two-Page Submission Report — Mayo Clinic">
<style>{css}</style>
</head>
<body>
<div class="header-block">
  <div class="title">Mayo Clinic: AI Platform Transformation in Healthcare</div>
  <div class="subtitle">Two-Page Submission Report &nbsp;·&nbsp; ITEC-617 Individual Assignment</div>
  <div class="meta">
    <span><strong>Student:</strong> Akshay Kumar</span>
    <span><strong>Course:</strong> ITEC-617</span>
    <span><strong>Institution:</strong> Kogod School of Business, American University</span>
    <span><strong>Date:</strong> May 3, 2026</span>
  </div>
  <div class="meta" style="margin-top:4pt;">
    <span><strong>Repository:</strong> github.com/akbknight/mayo-clinic-dt-case-study</span>
  </div>
</div>
{body}
<div class="footer-note">Prepared for ITEC-617, Spring 2026 · Kogod School of Business, American University · For academic submission only.</div>
</body>
</html>"""

CASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="author" content="Akshay Kumar">
<meta name="title" content="Mayo Clinic: Building the Platform for the Future of Medicine">
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>"""

def md_to_html_body(md_text):
    md_text = re.sub(r'^---\s*$', '<hr>', md_text, flags=re.MULTILINE)
    html = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    return html

def fix_report_body(html):
    # Remove the H1 (we replace with styled header block)
    html = re.sub(r'<h1>.*?</h1>', '', html, count=1, flags=re.DOTALL)
    # Remove H2 that's the subtitle line
    html = re.sub(r'<h2>Mayo Clinic: AI Platform Transformation.*?</h2>', '', html, count=1)
    # Remove the header metadata paragraph (Akshay Kumar | ITEC-617...)
    html = re.sub(r'<p><strong>Akshay Kumar.*?</p>', '', html, count=1, flags=re.DOTALL)
    # Remove word count footnote
    html = re.sub(r'<p><em>Word count.*?</em></p>', '', html)
    return html.strip()

def fix_case_body(html):
    # Style the H1 as case title
    html = re.sub(
        r'<h1>(.*?)</h1>',
        r'<div class="case-title">\1</div>',
        html, count=1
    )
    # Style the H2 course line as meta
    html = re.sub(
        r'<h2>(ITEC-617.*?)</h2>',
        r'<div class="case-meta">\1</div>',
        html, count=1
    )
    # Style blockquote disclaimer (the first blockquote)
    html = re.sub(
        r'<blockquote>\s*<p>(This case was developed.*?)</p>\s*</blockquote>',
        r'<div class="case-disclaimer">\1</div>',
        html, count=1, flags=re.DOTALL
    )
    # Wrap "prepared by" footer
    html = re.sub(
        r'<p><em>(Case prepared by:.*?)</em></p>',
        r'<div class="prepared-by">\1</div>',
        html, flags=re.DOTALL
    )
    return html.strip()

def export_pdf(md_path, pdf_path, template, css, body_fixer, label):
    print(f"  Reading {os.path.basename(md_path)}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html_body = md_to_html_body(md_text)
    html_body = body_fixer(html_body)
    full_html = template.format(css=css, body=html_body)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.html',
                                      encoding='utf-8', delete=False) as tmp:
        tmp.write(full_html)
        tmp_path = tmp.name

    file_url = "file:///" + tmp_path.replace("\\", "/")
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        file_url
    ]
    print(f"  Exporting {label} -> {os.path.basename(pdf_path)}...")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    os.unlink(tmp_path)

    if result.returncode == 0 and os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) // 1024
        print(f"  OK: {pdf_path} ({size_kb} KB)")
        return True
    else:
        print(f"  FAILED: {result.stderr[:200]}")
        return False

def main():
    os.makedirs(OUT, exist_ok=True)

    jobs = [
        {
            "md":      os.path.join(REPO, "case-study", "MayoClinic_TwoPage_Report.md"),
            "pdf":     os.path.join(OUT,  "MayoClinic_TwoPage_Report_Final.pdf"),
            "template": REPORT_TEMPLATE,
            "css":     REPORT_CSS,
            "fixer":   fix_report_body,
            "label":   "Two-Page Report",
        },
        {
            "md":      os.path.join(REPO, "case-study", "MayoClinic_Case.md"),
            "pdf":     os.path.join(OUT,  "MayoClinic_Case_Final.pdf"),
            "template": CASE_TEMPLATE,
            "css":     CASE_CSS,
            "fixer":   fix_case_body,
            "label":   "Main Case",
        },
    ]

    ok = 0
    for j in jobs:
        if export_pdf(j["md"], j["pdf"], j["template"], j["css"], j["fixer"], j["label"]):
            ok += 1

    print(f"\nDone: {ok}/{len(jobs)} exports successful.")

if __name__ == "__main__":
    main()
