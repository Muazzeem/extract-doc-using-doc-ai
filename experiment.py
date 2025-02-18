"""
Document AI Processing Script

This script processes PDF documents using Google Cloud's Document AI service to extract
and classify information, particularly focusing on service IDs. It includes functionality
to highlight extracted service IDs in the original PDF document.

Dependencies:
    - google-cloud-documentai
    - PyMuPDF (fitz)
    - google-api-core
"""

import logging
from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import GoogleAPIError
from google.cloud import documentai
from google.cloud.documentai_v1 import Document

from create_border_box import highlight_text

# Set up logging
logging.basicConfig(level=logging.INFO)

# Constants
LOCATION = "us"  # Google Cloud region
MIME_TYPE = "application/pdf"  # Document type being processed
DOCUMENTATION_CLASSIFIER_PROCESSOR_NAME = (
    "your-project-id/locations/us/processors/your-processor-id"
    "/processorVersions/your-processor-version"
)

# Create a single client instance for reuse
client = documentai.DocumentProcessorServiceClient(
    client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
)


def process_document(content: bytes, processor_name: str, field_mask: str) -> Document:
    """Processes a document using the specified Document AI processor.

    Args:
        content: The GCS path to the document.
        processor_name: The name of the Document AI processor to use.
        field_mask: The field mask to apply to the response.

    Returns:
        The processed document.

    Raises:
        GoogleAPIError: If there's an error processing the document.
    """
    try:
        request = documentai.ProcessRequest(
            name=processor_name,
            raw_document=documentai.RawDocument(content=content, mime_type=MIME_TYPE),
        )

        result = client.process_document(request=request)
        return result.document
    except GoogleAPIError as ex:
        logging.error(f"Error processing document: {ex}")


def get_document_type(file_path: str) -> Document:
    """Classifies the document type using the Document AI classification processor.

    Args:
        file_path: The name of the file in the bucket.

    Returns:
        Document: The processed document with classification information.
    """
    content = open(file_path, "rb").read()
    result = process_document(
        content, DOCUMENTATION_CLASSIFIER_PROCESSOR_NAME, "entities"
    )

    return result


def extract_entity_from_doc(result: Document):
    """Extracts service IDs from a processed Document AI document.

    Args:
        result: The processed Document AI document.

    Returns:
        list: A list of extracted service IDs.
    """
    service_ids = []
    for p in result.entities:
        if p.type_ == "service_ids":
            service_ids.append(p.mention_text)
    return service_ids


if __name__ == "__main__":
    # Example usage of the document processing pipeline
    pdf_path = "5GSFSSCBM_2022.07.01.pdf"
    doc = get_document_type(pdf_path)
    ids = extract_entity_from_doc(doc)
    print(ids)
    print(len(ids))
    output_file = 'highlighted_file.pdf'
    highlight_text(pdf_path, output_file, ids)

