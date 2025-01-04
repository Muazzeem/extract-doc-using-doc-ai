import fitz


def highlight_text(pdf_path, output_path, search_terms, highlight_color=(0, 1, 0)):
    """
    Highlights specified text in a PDF document.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_path (str): Path to save the modified PDF.
        search_terms (list): List of strings to search for and highlight.
        highlight_color (tuple): RGB color for highlighting - (1, 1, 0).
    """

    # Open the PDF document
    doc = fitz.open(pdf_path)

    # Process each page in the PDF
    for page_num in range(len(doc)):
        page = doc[page_num]

        # Search and highlight each term on the current page
        for term in search_terms:
            # Find all instances of the search term
            text_instances = page.search_for(term)

            # Add highlight annotation for each instance found
            for inst in text_instances:
                highlight = page.add_highlight_annot(inst)
                highlight.set_colors(stroke=highlight_color)
                highlight.update()

    # Save the modified PDF
    doc.save(output_path)


# List of invoice IDs to search for in the PDF
ids = ["332772020", "332772067", "332772075", # ... many more IDs
       "FRO2006996789", "FRO2007000806", "FRO2007013994"]

# Convert list to set to remove any duplicates
unique_ids = set(ids)

# Print the count of total and unique IDs
print(len(ids), "Unique IDs:", len(unique_ids))

# Process the PDF file with the unique IDs
highlight_text(
    "your-pdf-path", "your-output-path", list(unique_ids)
)
