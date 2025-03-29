import pdfkit

def save_summary_to_pdf(summary, filename="report.pdf"):
    pdfkit.from_string(summary, filename)

