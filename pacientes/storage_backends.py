from storages.backends.azure_storage import AzureStorage
import os

class ReportesPDFStorage(AzureStorage):
    account_name = os.getenv('AZURE_ACCOUNT_NAME')
    account_key = os.getenv('AZURE_ACCOUNT_KEY')
    azure_container = 'reportes-pdf'
    expiration_secs = None

class ImagenesMedicasStorage(AzureStorage):
    account_name = os.getenv('AZURE_ACCOUNT_NAME')
    account_key = os.getenv('AZURE_ACCOUNT_KEY')
    azure_container = 'imagenes-medicas'
    expiration_secs = None
