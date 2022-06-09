from flask import*
from patient1 import patient1
import numpy as np
app=Flask(__name__)
app.register_blueprint(patient1)

app.run(debug=True,port="5001")
