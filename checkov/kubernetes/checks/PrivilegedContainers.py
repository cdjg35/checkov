from checkov.common.models.enums import CheckCategories
from checkov.kubernetes.base_spec_omitted_or_value_check import BaseSpecOmittedOrValueCheck


class PrivilegedContainers(BaseSpecOmittedOrValueCheck):

    def __init__(self):
        # CIS-1.3 1.7.1
        name = "Do not admit privileged containers"
        id = "CKV_K8S_2"
        supported_kind = ['PodSecurityPolicy']
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_kind)

    def get_inspected_key(self):
        return "spec/privileged"

    def get_resource_id(self, conf):
        return 'PodSecurityPolicy.spec.privileged'


check = PrivilegedContainers()