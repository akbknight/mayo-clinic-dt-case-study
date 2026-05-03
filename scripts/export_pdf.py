"""
PDF exporter: Markdown -> fpdf2 PDF (pure Python, no browser dependency).
Usage: python scripts/export_pdf.py
"""
import os, re
import markdown
from fpdf import FPDF, HTMLMixin
from fpdf.fonts import FontFace

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(REPO, "case-study", "pdf")

NAVY  = (10, 34, 64)
RED   = (200, 16, 46)
GRAY  = (107, 114, 128)
BLACK = (28, 28, 30)
WHITE = (255, 255, 255)


class ReportPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='pt', format='Letter')
        self.set_margins(72, 72, 72)
        self.set_auto_page_break(auto=True, margin=72)
        self.add_page()

    def header_block(self, title, subtitle, meta_lines):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*NAVY)
        self.multi_cell(0, 22, title, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*GRAY)
        self.cell(0, 14, subtitle, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        for line in meta_lines:
            self.set_font("Helvetica", "", 9)
            self.set_text_color(*BLACK)
            self.cell(0, 12, line, new_x="LMARGIN", new_y="NEXT")
        # Red divider
        self.ln(8)
        self.set_draw_color(*RED)
        self.set_line_width(1)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(14)
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)

    def section_heading(self, text):
        self.ln(10)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*NAVY)
        self.cell(0, 15, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*RED)
        self.set_line_width(0.5)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)

    def body_para(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*BLACK)
        self.multi_cell(0, 14, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def horizontal_rule(self):
        self.ln(6)
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.5)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)

    def sub_heading(self, text):
        self.ln(6)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*NAVY)
        self.cell(0, 14, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def footer(self):
        self.set_y(-50)
        self.set_font("Helvetica", "I", 7.5)
        self.set_text_color(*GRAY)
        self.cell(0, 10,
            "Prepared for ITEC-617, Spring 2026  ·  Kogod School of Business, American University  ·  For academic submission only.",
            align="C")


class CasePDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='pt', format='Letter')
        self.set_margins(72, 65, 72)
        self.set_auto_page_break(auto=True, margin=65)
        self.add_page()

    def case_title(self, text):
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(*NAVY)
        self.multi_cell(0, 30, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def case_meta(self, text):
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*GRAY)
        self.cell(0, 12, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(6)

    def disclaimer_box(self, text):
        self.set_fill_color(250, 250, 248)
        self.set_draw_color(*RED)
        self.set_line_width(2)
        x, y, w = self.l_margin, self.get_y(), self.w - self.l_margin - self.r_margin
        # Draw left border
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(60, 60, 60)
        self.multi_cell(w, 13, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)

    def section_heading(self, text):
        self.ln(16)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*NAVY)
        self.cell(0, 18, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def sub_heading(self, text):
        self.ln(8)
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*NAVY)
        self.cell(0, 14, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def body_para(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*BLACK)
        self.multi_cell(0, 15, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def blockquote(self, text):
        self.ln(8)
        x, y = self.l_margin, self.get_y()
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(50, 50, 50)
        self.set_x(self.l_margin + 20)
        self.multi_cell(self.w - self.l_margin - self.r_margin - 20, 14,
                        text, new_x="LMARGIN", new_y="NEXT")
        # Draw left red bar
        end_y = self.get_y()
        self.set_draw_color(*RED)
        self.set_line_width(2.5)
        self.line(x + 5, y, x + 5, end_y)
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)
        self.ln(6)

    def horizontal_rule(self):
        self.ln(8)
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.5)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(8)
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)

    def footer(self):
        self.set_y(-50)
        self.set_font("Helvetica", "I", 7.5)
        self.set_text_color(*GRAY)
        self.cell(0, 10,
            f"Mayo Clinic: Building the Platform for the Future of Medicine  ·  ITEC-617, Spring 2026  ·  Page {self.page_no()}",
            align="C")


def ascii_safe(text):
    """Replace common Unicode typographic characters with ASCII equivalents."""
    replacements = {
        '—': '--',   # em dash
        '–': '-',    # en dash
        '‘': "'",    # left single quote
        '’': "'",    # right single quote
        '“': '"',    # left double quote
        '”': '"',    # right double quote
        '…': '...',  # ellipsis
        ' ': ' ',    # non-breaking space
        '•': '-',    # bullet
        'é': 'e',    # e acute
        'è': 'e',    # e grave
        'à': 'a',    # a grave
        'ü': 'u',    # u umlaut
    }
    for char, sub in replacements.items():
        text = text.replace(char, sub)
    # Drop any remaining non-latin1 chars
    return text.encode('latin-1', errors='replace').decode('latin-1')


def clean_inline(text):
    """Strip basic markdown inline syntax to plain text, then make ASCII-safe."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*',     r'\1', text)
    text = re.sub(r'`(.+?)`',       r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    return ascii_safe(text)


def render_report(md_path, pdf_path):
    print(f"  Reading {os.path.basename(md_path)}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    pdf = ReportPDF()
    pdf.header_block(
        "Mayo Clinic: AI Platform Transformation in Healthcare",
        "Two-Page Submission Report  ·  ITEC-617 Individual Assignment",
        [
            "Student: Akshay Kumar   |   Course: ITEC-617   |   Kogod School of Business, American University",
            "Date: May 3, 2026   |   Repository: github.com/akbknight/mayo-clinic-dt-case-study",
        ]
    )

    # Parse and render body (skip the H1/H2 doc header lines)
    in_header = True
    para_buf = []

    def flush_para():
        if para_buf:
            text = clean_inline(" ".join(para_buf).strip())
            if text:
                pdf.body_para(text)
            para_buf.clear()

    for raw in lines:
        line = raw.rstrip('\n')

        # Skip the document title / metadata block at the top
        if in_header:
            if line.startswith('# ') or line.startswith('## ') or \
               line.startswith('**') or line.startswith('**Date') or \
               line.startswith('**Company') or line.startswith('**Repository'):
                continue
            if line.strip() == '---':
                in_header = False
                continue
            continue

        if line.strip() == '---':
            flush_para()
            pdf.horizontal_rule()
        elif line.startswith('## '):
            flush_para()
            pdf.section_heading(clean_inline(line[3:].strip()))
        elif line.startswith('### '):
            flush_para()
            pdf.sub_heading(clean_inline(line[4:].strip()))
        elif line.strip() == '':
            flush_para()
        elif line.startswith('*Word count'):
            flush_para()  # skip word count footnote
        else:
            para_buf.append(line.strip())

    flush_para()

    print(f"  Writing {os.path.basename(pdf_path)}...")
    pdf.output(pdf_path)
    return True


def render_case(md_path, pdf_path):
    print(f"  Reading {os.path.basename(md_path)}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    pdf = CasePDF()
    para_buf = []
    in_blockquote = False
    bq_buf = []
    first_h1_done = False
    first_h2_done = False
    disclaimer_done = False

    def flush_para():
        if para_buf:
            text = clean_inline(" ".join(para_buf).strip())
            if text:
                pdf.body_para(text)
            para_buf.clear()

    def flush_bq():
        if bq_buf:
            text = clean_inline(" ".join(bq_buf).strip())
            if text:
                pdf.blockquote(text)
            bq_buf.clear()

    for raw in lines:
        line = raw.rstrip('\n')

        if line.startswith('> '):
            flush_para()
            in_blockquote = True
            bq_buf.append(line[2:].strip())
            continue
        elif in_blockquote and line.strip() == '':
            flush_bq()
            in_blockquote = False
            continue
        elif in_blockquote:
            flush_bq()
            in_blockquote = False

        if line.startswith('# ') and not first_h1_done:
            first_h1_done = True
            pdf.case_title(clean_inline(line[2:].strip()))
        elif line.startswith('## ITEC-617') and not first_h2_done:
            first_h2_done = True
            pdf.case_meta(clean_inline(line[3:].strip()))
        elif line.startswith('## '):
            flush_para()
            pdf.section_heading(clean_inline(line[3:].strip()))
        elif line.startswith('### '):
            flush_para()
            pdf.sub_heading(clean_inline(line[4:].strip()))
        elif line.strip() == '---':
            flush_para()
            pdf.horizontal_rule()
        elif line.strip() == '':
            flush_para()
        elif re.match(r'^\*Case prepared by:', line):
            flush_para()
            pdf.set_font("Helvetica", "I", 7.5)
            pdf.set_text_color(*GRAY)
            pdf.ln(10)
            pdf.set_draw_color(200, 200, 200)
            pdf.set_line_width(0.5)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(6)
            pdf.cell(0, 12, clean_inline(line.strip('*').strip()), new_x="LMARGIN", new_y="NEXT")
        else:
            para_buf.append(line.strip())

    flush_para()
    flush_bq()

    print(f"  Writing {os.path.basename(pdf_path)}...")
    pdf.output(pdf_path)
    return True


def validate_pdf(pdf_path, label):
    """Return (ok, size_kb, page_count, first_words)."""
    if not os.path.exists(pdf_path):
        return False, 0, 0, "FILE MISSING"
    size_kb = os.path.getsize(pdf_path) // 1024
    if size_kb < 3:
        return False, size_kb, 0, "TOO SMALL"
    # Quick page count via byte scan
    with open(pdf_path, 'rb') as f:
        data = f.read()
    pages = data.count(b'/Type /Page') - data.count(b'/Type /Pages')
    return True, size_kb, max(pages, 1), "OK"


def main():
    os.makedirs(OUT, exist_ok=True)
    jobs = [
        {
            "md":     os.path.join(REPO, "case-study", "MayoClinic_TwoPage_Report.md"),
            "pdf":    os.path.join(OUT,  "MayoClinic_TwoPage_Report_Final.pdf"),
            "render": render_report,
            "label":  "Two-Page Report",
        },
        {
            "md":     os.path.join(REPO, "case-study", "MayoClinic_Case.md"),
            "pdf":    os.path.join(OUT,  "MayoClinic_Case_Final.pdf"),
            "render": render_case,
            "label":  "Main Case",
        },
    ]

    ok = 0
    for j in jobs:
        print(f"\n--- {j['label']} ---")
        try:
            j["render"](j["md"], j["pdf"])
            valid, size_kb, pages, note = validate_pdf(j["pdf"], j["label"])
            if valid:
                print(f"  VALIDATION: {size_kb} KB  |  ~{pages} page(s)  |  {note}")
                ok += 1
            else:
                print(f"  VALIDATION FAILED: {size_kb} KB  |  {note}")
        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\nDone: {ok}/{len(jobs)} exports successful.")
    if ok < len(jobs):
        print("ACTION REQUIRED: At least one export failed. Do not submit until resolved.")


if __name__ == "__main__":
    main()
