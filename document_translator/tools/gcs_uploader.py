import datetime
from google.cloud import storage
from google.adk.tools import ToolContext

def upload_to_gcs(text: str, original_document_name: str, target_language: str, bucket_name: str, tool_context: ToolContext) -> dict:
    """
    Uploads translated text to a GCS bucket and returns a URL.

    Args:
        text: The translated text to upload.
        original_document_name: The name of the original document.
        target_language: The target language of the translation.
        bucket_name: The GCS bucket name (e.g., 'my-bucket').
        tool_context: The tool context.

    Returns:
        A dictionary containing the GCS URL or an error.
    """
    try:
        # The gcs bucket name can be passed with or without the gs:// prefix.
        if bucket_name.startswith("gs://"):
            bucket_name = bucket_name[5:]

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"translated_{target_language}_{original_document_name}_{timestamp}.txt"

        blob = bucket.blob(file_name)
        blob.upload_from_string(text, content_type="text/plain")

        result = {"gcs_url": blob.public_url}
        tool_context.state["gcs_upload_output"] = result
        return result
    except Exception as e:
        result = {"error": f"Failed to upload to GCS: {e}"}
        tool_context.state["gcs_upload_output"] = result
        return result