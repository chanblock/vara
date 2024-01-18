# context_processors.py
from . import assetsUtil

def assets_context(request):
    return {'assets': assetsUtil.get_assets()}
