from clarifai.rest import ClarifaiApp
from appclaifai.model.helpers import get_model
from appclaifai.model.helpers import predict

app_obj = ClarifaiApp(api_key = 'a28d6ad6382d434a9cae46a67b97364e')

color_model = get_model(app_obj, 'Color')
paper_model = get_model(app_obj, 'general-v1.3')

output = paper_model.predict_by_bytes(open('appclaifai/pics/ColorPaper1.jpeg', 'rb').read())
