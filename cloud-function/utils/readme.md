
# DocAI Helper Documentation

This module provides helper functions for processing documents using Google Cloud Document AI.

## Functions

### get_document_details(invoice)

Extracts and returns key details from a Lumen invoice document.

#### Parameters:
- invoice: The invoice document to process

#### Returns:
A dictionary containing the following invoice details:
- billing_account_number: The billing account number
- vendor: The vendor name (LUMEN)
- invoice_date: The date of the invoice
- payment_due_date: The payment due date
- vendor_subsidiary: The vendor subsidiary name
- service_ids: List of service IDs found in the invoice


# Firestore Helper Documentation

### get_config_from_firestore(document_id)

Retrieves configuration data from Firestore for a given document ID.

#### Parameters:
- document_id: The ID of the document to fetch configuration for

#### Returns:
A dictionary containing the configuration data stored in Firestore for the specified document ID.

#### Details:
- Connects to the "invoice-config" database in the "chc-corp-data-management" project
- Retrieves document from the "invoice_config" collection
- Returns the document data as a Python dictionary
- Prints status messages during execution for debugging purposes



# Gemini Helper Documentation

### check_if_all_service_ids_exist(service_ids)

Validates that all service IDs are present in an invoice document using Google's Gemini AI model.

#### Parameters:
- service_ids: List of service ID strings to validate

#### Returns:
Boolean indicating whether all service IDs were found in the invoice (True) or not (False)

#### Details:
- Uses Vertex AI's GenerativeModel for validation
- Currently returns True by default (placeholder implementation)


