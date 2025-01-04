
# Invoice Processor

This project contains components for processing invoices using Google Cloud services.

## Project Structure

- `/cloud-function/` - Contains the main Cloud Function code
  - `main.py` - Entry point that handles Cloud Storage trigger events
  - `/utils/` - Helper utilities
    - `firestore_helper.py` - Functions for interacting with Firestore
    - `docai_helper.py` - Functions for processing documents with Document AI

## Key Features

- Automatically processes invoices uploaded to Cloud Storage
- Extracts key invoice details using Google Document AI
- Validates service IDs against known configurations in Firestore
- Uses Gemini AI for additional validation checks

## Flow

1. Invoice PDF is uploaded to Cloud Storage bucket
2. Cloud Function is triggered by the upload
3. Document AI processes the invoice to extract text and structure
4. Service IDs and other key fields are extracted
5. Configuration is fetched from Firestore
6. Validation is performed using Gemini AI
7. Results are stored and notifications sent if needed

## Configuration

The system uses Firestore to store configuration data:
- Database: "your-database-name"
- Collection: "your-collection-name"
- Project: "your-project-id"
## Dependencies

- Google Cloud Functions Framework
- PyMuPDF (fitz) for PDF processing
- Google Cloud Document AI
- Google Cloud Firestore
- Vertex AI (Gemini)
