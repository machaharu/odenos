# -*- coding:utf-8 -*-

# Copyright 2015 NEC Corporation.                                          #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License");          #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#   http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #

from org.o3project.odenos.core.component.network.flow.basic.flow_action\
    import FlowAction
import unittest


class FlowActionTest(unittest.TestCase):
    Type = "FlowActionOutput"

    def setUp(self):
        self.target = FlowAction(self.Type)

    def tearDown(self):
        self.target = None

    def test_constructor(self):
        self.assertEqual(self.target._body[self.target.TYPE], self.Type)

    def test_type(self):
        self.assertEqual(self.target.type, self.Type)

if __name__ == '__main__':
    unittest.main()