from pony import orm 
from .db import db
from .pony_cfg import generate_mapping_config
from .entities import *

db.generate_mapping(**generate_mapping_config)

