# modules/invoice_gen.py
from fpdf import FPDF
import pandas as pd
import os

def generate_invoices(csv_path: str, output_dir: str = "invoices"):
    os.makedirs(output_dir, exist_ok=True)
    data = pd.read_csv(csv_path)
    for _, row in data.iterrows():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Invoice", ln=True, align="C")
        pdf.cell(200, 10, txt=f"Customer: {row['name']}", ln=True)
        pdf.cell(200, 10, txt=f"Email: {row['email']}", ln=True)
        pdf.cell(200, 10, txt=f"Product: {row['product']}", ln=True)
        pdf.cell(200, 10, txt=f"Amount: ${row['amount']}", ln=True)
        pdf.output(f"{output_dir}/invoice_{row['name'].replace(' ', '_')}.pdf")
