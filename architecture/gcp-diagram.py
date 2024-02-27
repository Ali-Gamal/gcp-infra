from diagrams import Diagram
from diagrams.gcp.compute import KubernetesEngine
from diagrams.gcp.devtools import Build, SourceRepositories
from diagrams.gcp.database import SQL, Spanner
from diagrams.gcp.network import LoadBalancing, CDN
from diagrams.gcp.security import IAP
from diagrams.gcp.storage import Storage
from diagrams.gcp.network import VPN, DedicatedInterconnect, Armor

with Diagram("GCP Cloud Architecture for Global Application", show=True):
    ingress = LoadBalancing("Global Load Balancer")
    compute = KubernetesEngine("GKE Cluster")
    databases = Spanner("Cloud Spanner")
    storage = Storage("Cloud Storage")
    security = [IAP("Identity-Aware Proxy"), Armor("Cloud Armor")]
    connectivity = [VPN("Cloud VPN"), DedicatedInterconnect("Cloud Interconnect")]
    ci_cd = [Build("Cloud Build"), SourceRepositories("Cloud Source Repositories")]
    cdn = CDN("Cloud CDN")

    ingress >> compute >> databases
    ingress >> cdn >> storage
    compute >> security
    databases >> storage
    connectivity >> ingress
    compute >> ci_cd