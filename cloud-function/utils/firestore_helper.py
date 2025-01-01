from google.cloud import firestore

def get_config_from_firestore(document_id):
    print(f"Fetching config from Firestore for Document ID: {document_id}")
    db = firestore.Client(project="chc-corp-data-management", database="invoice-config")
    print ("1...")
    config = db.collection('invoice_config').document(document_id).get().to_dict()
    print ("2...")
    return config