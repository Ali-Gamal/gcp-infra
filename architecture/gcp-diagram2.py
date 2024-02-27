from diagrams import Diagram
from diagrams.gcp.compute import ComputeEngine, KubernetesEngine, GKE
from diagrams.gcp.database import SQL, Spanner
from diagrams.gcp.network import LoadBalancing, CDN, VPN, DedicatedInterconnect, Armor
from diagrams.gcp.security import IAP
from diagrams.gcp.storage import Storage, Filestore
from diagrams.gcp.devtools import SourceRepositories, Build, ContainerRegistry

with Diagram("Complete GCP Cloud Architecture Workflow", show=True):
    # Development and version control
    source_repos = SourceRepositories("Source Repos")

    # CI/CD Pipeline
    cloud_build = Build("Cloud Build")
    container_registry = ContainerRegistry("Container Registry")

    # Connection from source code to build and deploy process
    source_repos >> cloud_build >> container_registry

    # Global Load Balancer and CDN for traffic management and content delivery
    ingress = LoadBalancing("Global Load Balancing")
    cdn = CDN("Cloud CDN")

    # Compute resources for running applications
    compute_engine = ComputeEngine("VM Instances")
    kubernetes_engine = GKE("GKE for Containerized App")

    # Container images deployed to GKE or VMs
    container_registry >> kubernetes_engine
    container_registry >> compute_engine

    # Databases for application data
    cloud_sql = SQL("Cloud SQL")
    spanner = Spanner("Spanner for Global Scale")

    # Storage for application and user data
    cloud_storage = Storage("Cloud Storage")
    filestore = Filestore("Filestore for Shared Content")

    # Security features for protecting applications and data
    iap = IAP("Identity-Aware Proxy")
    cloud_armor = Armor("Cloud Armor")

    # Networking for on-premises and cloud integration
    vpn = VPN("Cloud VPN")
    dedicated_interconnect = DedicatedInterconnect("Cloud Interconnect")

    # Connecting components to reflect the workflow
    ingress >> cdn >> cloud_storage  # Traffic flow for static content
    ingress >> [compute_engine, kubernetes_engine]  # Traffic flow for dynamic content

    compute_engine >> [cloud_sql, filestore]  # VM interaction with databases and shared storage
    kubernetes_engine >> [spanner, filestore]  # Container interaction with databases and shared storage

    [cloud_sql, spanner] >> cloud_storage  # Database backup and interaction with cloud storage

    kubernetes_engine >> cloud_armor >> iap  # Enhanced security for containerized applications

    vpn >> dedicated_interconnect >> ingress  # Secure hybrid cloud connectivity

