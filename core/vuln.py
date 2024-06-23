from kubernetes import config, dynamic, client
from kubernetes.dynamic.exceptions import ResourceNotFoundError
from kubernetes.client import api_client

class TrivyInfo():
    def __init__(self, **kwargs):
        self.client = dynamic.DynamicClient(
            api_client.ApiClient(configuration=config.load_kube_config(**kwargs)))
    @property
    def get_all_configAuditReport(self):
        try:
            config_audits = self.client.resources.get(api_version="aquasecurity.github.io/v1alpha1",
                                                      kind="ConfigAuditReport").get()["items"]
            # returner = [
            #     [{
            #        "audit_name" : config_audits[x]["metadata"]["name"],
            #        "namespace"  : config_audits[x]["metadata"]["namespace"],
            #        "checks_summary"  : dict(config_audits[x]["report"]["summary"]),
            #         "checks" : [dict(x) for x in config_audits[x]["report"]["checks"]],
            #     }]
            #   for x in range(len(config_audits))]

            returner = {
                config_audits[x]["metadata"]["name"]:
                { 
                    "namespace" : config_audits[x]["metadata"]["namespace"],
                    "checks_data" : {   
                        "checks_summary"  : dict(config_audits[x]["report"]["summary"]),
                        "checks" : [dict(x) for x in config_audits[x]["report"]["checks"]],
                    }
                }
                for x in range(len(config_audits))
            }

            return returner
        except ResourceNotFoundError:
            pass   # implement


if __name__ == "__main__":
    tri = TrivyInfo()
    print(tri.get_all_configAuditReport)

