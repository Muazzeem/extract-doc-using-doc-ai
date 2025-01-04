import functions_framework

from utils.invoice_processor import process_invoice

# Cloud Function entrypoint that processes documents uploaded to Cloud Storage
@functions_framework.cloud_event
def process_document(cloud_event):
    """Triggered by a change to a Cloud Storage bucket.
    
    This function is triggered when a new file is uploaded to the specified
    Cloud Storage bucket. It extracts the bucket and file information from
    the event and passes it to the invoice processor.
    
    Args:
        cloud_event (CloudEvent): The event object containing information about the
            Cloud Storage change. Contains metadata about the file and bucket.
    
    Returns:
        None
    
    Event data structure:
        cloud_event.data["data"]["bucket"]: Name of the bucket where file was uploaded
        cloud_event.data["context"]["resource"]["name"]: Name/path of the uploaded file
    """

    # Extract storage event data
    data = cloud_event.data
    
    # Get bucket and file information from the event
    bucket_name = data["data"]["bucket"]
    file_name = data["context"]["resource"]["name"]
    
    # Create invoice object with file location details
    invoice = {
        "bucket_name": bucket_name,
        "file_name": file_name
    }
    print(f"Processing Invoice: {invoice}")

    # Process the invoice using the invoice processor utility
    result = process_invoice(invoice)

    return result