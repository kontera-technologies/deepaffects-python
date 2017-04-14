# coding: utf-8

"""
    SeerNet Audio APIs

    OpenAPI Specification of SeerNet audio APIs

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.audio import Audio
from .models.diarize_audio import DiarizeAudio
from .models.emotion_score import EmotionScore

# import apis into sdk package
from .apis.denoise_api import DenoiseApi
from .apis.diarize_api import DiarizeApi
from .apis.ellipsis_api import EllipsisApi
from .apis.emotion_api import EmotionApi
from .apis.featurize_api import FeaturizeApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
