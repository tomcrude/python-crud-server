import os
from django.conf import settings


def verification(title,description):
    if(title > 30 or description >  100 or title <= 8 or description <=  19):
                return False

def deleteImg(imageName):
                    
        DIR = settings.MEDIA_ROOT
        FULL_DIR = os.path.join(DIR, 'images',imageName[14:])
                    
        os.remove(FULL_DIR)