# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
import os
import uuid
import json
from pkg_resources import resource_filename
from IPython.display import display, Javascript, clear_output
from ipywidgets import Output

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def display_notification(message='None', url='https://quantum-computing.ibm.com/'):
        options = {}
        options["body"] = message.lstrip("\'\"").rstrip("\'\"")
        options["icon"] = "/static/base/images/favicon.ico"
        notification_uuid = uuid.uuid4()

        # display our browser notification using javascript
        with open(resource_filename("ipyhi", "js/notify.js")) as jsFile:
            jsString = jsFile.read()
        out = Output()
        with out:
            display(Javascript(jsString % {
                "notification_uuid": notification_uuid,
                "url": url,
                "options": json.dumps(options),
            }))
            clear_output(wait=False)