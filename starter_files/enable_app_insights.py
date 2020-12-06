from azureml.core import Workspace
from azureml.core.webservice import Webservice
ws = Workspace.from_config()
aci_service= Webservice(ws, "bank-mark-vote-ensemble-model")
aci_service.update(enable_app_insights=True)