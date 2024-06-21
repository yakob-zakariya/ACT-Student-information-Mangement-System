import tempfile
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from accounts.models import StudentUser

def export_students_to_pdf(department_name, batch, section):
    # Filter students based on section
    section_name = section.name
    students = StudentUser.students.filter(student__section=section).values('username', 'first_name', 'last_name')

    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    file_path = temp_file.name

    # Create a PDF document with small margins
    doc = SimpleDocTemplate(file_path, pagesize=letter, leftMargin=20, rightMargin=20, topMargin=30, bottomMargin=30)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    
    # Heading 1 style
    heading1_style = ParagraphStyle(
        'heading1',
        parent=styles['Heading1'],
        fontSize=20,  # Increased font size for heading 1
        leading=24,
        alignment=1,
        spaceAfter=14
    )

    # Heading 2 style
    heading2_style = ParagraphStyle(
        'heading2',
        parent=styles['Heading2'],
        fontSize=16,  # Font size for heading 2
        leading=20,
        alignment=1,
        spaceAfter=10
    )

    # Add Heading 1
    heading1 = Paragraph("American College of Technology (ACT)", heading1_style)
    elements.append(heading1)
    
    # Spacer to add some space after Heading 1
    elements.append(Spacer(1, 12))

    # Add Heading 2 with department name, batch, section
    heading2_text = f"Department: {department_name} | Batch: {batch} | Section: {section_name}"
    heading2 = Paragraph(heading2_text, heading2_style)
    elements.append(heading2)
    
    # Spacer to add some space after Heading 2
    elements.append(Spacer(1, 12))

    # Create table data with numbering
    data = [['#', 'Username', 'First Name', 'Last Name']]
    for i, student in enumerate(students, start=1):
        data.append([str(i), student['username'], student['first_name'], student['last_name']])

    # Create a table
    table = Table(data, colWidths=[30, 150, 150, 150])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),  # Increased font size for table headers
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),  # Increased font size for table content
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),  # Increased top padding
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),  # Increased bottom padding
    ]))

    elements.append(table)

    # Build the PDF
    doc.build(elements)

    return file_path
