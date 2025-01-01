from utils.docai_helper import get_document_details
from utils.firestore_helper import get_config_from_firestore
from utils import gemini_helper


def process_invoice(invoice):

    # get Invoice details from Document AI
    document_details = get_document_details(invoice=invoice)

    # extract Invoice config from Firestore based on billing account number
    invoice_config = get_config_from_firestore(document_details["billing_account_number"])

    # process Invoice based on Invoice Type
    # if document_details["billing_account_number"] == "0205332642":
    #     print("Processing LUMEN Invoice..")
        # gemini_helper.check_if_all_service_ids_exist(document_details["service_ids"])



    return document_details