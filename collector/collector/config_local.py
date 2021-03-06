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

# This configuration file can be used for a local development debug server
# at localhost:5000. Overrides the config module.

import logging

class Config(object):
    DEBUG = True
    TESTING = False
    LOG_LEVEL = logging.ERROR

    # If your telemdb database password is not 'postgres', update this line.
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost/telemdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    LOG_FILE = 'handler.log'

    # The maximum retention time for records stored in the database, measured
    # from the time received by the `collector` app.
    MAX_WEEK_KEEP_RECORDS = 5


class Testing(Config):
    TESTING = True

    # If your testdb database password is not 'postgres', update this line.
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost/testdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = True


# vi: ts=4 et sw=4 sts=4
