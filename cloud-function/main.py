import functions_framework
import json

from utils.invoice_processor import process_invoice



# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def process_document(cloud_event):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """

    data = cloud_event.data
    

    bucket_name = data["data"]["bucket"]
    file_name = data["context"]["resource"]["name"]
    invoice = {
        "bucket_name": bucket_name,
        "file_name": file_name
    }
    print(f"Processing Invoice: {invoice}")

    result = process_invoice(invoice)

    return