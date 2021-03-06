#
# Copyright 2015-2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from flask import Flask
from . import config
from flask_sqlalchemy import SQLAlchemy
import inspect
from flask import request, url_for
from datetime import datetime
from .jinja_filters import timesince, local_datetime_since, basename

app = Flask(__name__, static_folder="static", static_url_path="/telemetryui/static")
app.config.from_object(config.Config)

try:
   #try importing from the local dev configuration if it exists
   from . import config_local
   app.config.from_object(config_local.Config)
except:
   pass

from . import views

def url_for_other_page(page, page_size=None):
    args = request.args.copy()
    if page_size is not None:
        args['page_size'] = page_size
    return url_for(request.endpoint, page=page, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page
app.add_template_filter(timesince)
app.add_template_filter(local_datetime_since)
app.add_template_filter(basename)


# vi: ts=4 et sw=4 sts=4
