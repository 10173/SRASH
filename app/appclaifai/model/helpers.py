import clarifai

def get_model(app_obj:object , model_name: str) -> object:
    " Returns a clarifai model."
    if isinstance(model_name, str):
        return app_obj.models.get(model_name)
    return None

def predict(model_obj: object, image_file: str) -> list:
    " Predict the images and returns all the class"
    image_bin = open(image_file, 'rb').read()
    json_obj = model_obj.predict_by_bytes(image_bin)
    data = [value for item in json_obj['outputs'][0]['data']['concepts']
        for key, value in item.items() if key in ('name', 'value')]
    return zip(data[::2], data[1::2])
