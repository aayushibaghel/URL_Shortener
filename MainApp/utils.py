import string
import random
from django.conf import settings

SHORTCODE_MIN=getattr(settings,'SHORTCODE_MIN',6)

def code_generator(len=SHORTCODE_MIN,chars= string.ascii_lowercase  + string.digits):

     new_code=''
     for _ in range(len):
         new_code += random.choice(chars)

     new_code = "http://www.shortx.co/{0}".format(new_code)
     print(new_code)
     return new_code
