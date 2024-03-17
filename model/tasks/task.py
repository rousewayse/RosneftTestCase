from . import app
from typing import Union, List
@app.task
def add(args: List[Union[float, int]])->Union[int, float]:
    return sum(args)
