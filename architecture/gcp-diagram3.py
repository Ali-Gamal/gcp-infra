from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import GKE, ComputeEngine
from diagrams.gcp.network import LoadBalancing, CDN, DNS, VPN, PartnerInterconnect, Armor
from diagrams.gcp.security import IAP
from diagrams.gcp.storage import GCS, Filestore
from diagrams.gcp.database import SQL, Spanner
from diagrams.gcp.devtools import SourceRepositories, Build, ContainerRegistry
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.operations import Logging, Monitoring
from diagrams.onprem.network import Internet
from diagrams.onprem.client import User

with Diagram("GCP Cloud Architecture for Global Application", show=True, direction="TB"):
    # User's journey starts here
    user = User("Visitor")
    internet = Internet("Internet")
    dns = DNS("Cloud DNS")

    with Cluster("Google Cloud Platform"):
        # Define the Load Balancer for distributing traffic
        lb = LoadBalancing("Global Load Balancing")
        # CDN for delivering content globally at low latency
        cdn = CDN("Cloud CDN")
        # Cloud Armor for security and IAP for secure application access
        armor = Armor("Cloud Armor")
        iap = IAP("Identity-Aware Proxy")

        # Define the GKE cluster for container management
        with Cluster("Containerized Application"):
            gke = GKE("GKE Cluster")
            with Cluster("Kubernetes Workloads"):
                frontend = ComputeEngine("Frontend Service")
                backend = ComputeEngine("Backend Service")
        
        # Use Cloud SQL and Spanner for databases
        cloud_sql = SQL("Cloud SQL")
        spanner = Spanner("Spanner")
        
        # Cloud Storage and Filestore for object and file storage
        gcs = GCS("Cloud Storage")
        filestore = Filestore("Filestore")

        # CI/CD pipeline with Source Repos, Build, and Container Registry
        source_repos = SourceRepositories("Source Repos")
        cloud_build = Build("Cloud Build")
        container_registry = ContainerRegistry("Container Registry")

        # Logging and Monitoring for operations
        logging = Logging("Cloud Logging")
        monitoring = Monitoring("Cloud Monitoring")

        # Hybrid connectivity with on-prem data center
        vpn = VPN("Cloud VPN")
        Partner_interconnect = PartnerInterconnect("Partner Interconnect")

    # Connections and flows
    user >> internet >> dns >> lb >> cdn >> gcs
    lb >> armor >> iap >> gke
    gke >> frontend >> backend
    backend >> [cloud_sql, spanner]
    frontend >> filestore
    source_repos >> cloud_build >> container_registry >> gke
    gke >> [logging, monitoring]
    [vpn, Partner_interconnect] >> lb
