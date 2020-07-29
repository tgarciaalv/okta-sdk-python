"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject
from okta.models.policy_rule_auth_context_condition\
    import PolicyRuleAuthContextCondition
from okta.models.policy_network_condition\
    import PolicyNetworkCondition
from okta.models.policy_people_condition\
    import PolicyPeopleCondition


class OktaSignOnPolicyRuleConditions(
    OktaObject
):
    """
    A class for OktaSignOnPolicyRuleConditions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "authContext" in config:
                if isinstance(config["authContext"],
                              PolicyRuleAuthContextCondition):
                    self.auth_context = config["authContext"]
                else:
                    self.auth_context = PolicyRuleAuthContextCondition(
                        config["authContext"]
                    )
            else:
                self.auth_context = None
            if "network" in config:
                if isinstance(config["network"],
                              PolicyNetworkCondition):
                    self.network = config["network"]
                else:
                    self.network = PolicyNetworkCondition(
                        config["network"]
                    )
            else:
                self.network = None
            if "people" in config:
                if isinstance(config["people"],
                              PolicyPeopleCondition):
                    self.people = config["people"]
                else:
                    self.people = PolicyPeopleCondition(
                        config["people"]
                    )
            else:
                self.people = None
        else:
            self.auth_context = None
            self.network = None
            self.people = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "authContext": self.auth_context,
            "network": self.network,
            "people": self.people
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
