import os
# folders

basepath = os.path.dirname(os.path.realpath(__file__))

upload_folder = os.path.join(basepath,'static', 'uploads')

detection_model_path = os.path.join(basepath,'models', 'detection_models')

# extenstions
ALLOWED_EXTENSIONS = (['png', 'jpg'])
