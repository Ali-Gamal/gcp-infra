from diagrams import Diagram, Cluster
from diagrams.gcp.compute import GKE, ComputeEngine
from diagrams.gcp.network import LoadBalancing, CDN, DNS, VPN, PartnerInterconnect, Armor
from diagrams.gcp.security import IAP, KeyManagementService
from diagrams.gcp.storage import GCS, Filestore
from diagrams.gcp.database import Spanner
from diagrams.gcp.devtools import SourceRepositories, Build, ContainerRegistry
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.operations import Logging, Monitoring
from diagrams.onprem.iac import Terraform
from diagrams.onprem.client import User
from diagrams.onprem.network import Internet

with Diagram("GCP Cloud Architecture with Modern Requirements", show=True, direction="TB"):
    user = User("End User")
    internet = Internet("Internet")
    dns = DNS("Cloud DNS")

    with Cluster("Google Cloud Platform"):
        with Cluster("Networking Services"):
            lb = LoadBalancing("Global Load Balancer")
            cdn = CDN("Cloud CDN")
            armor = Armor("Cloud Armor")
            iap = IAP("Identity-Aware Proxy")
            vpn = VPN("Cloud VPN")
            partner_interconnect = PartnerInterconnect("Partner Interconnect")

        with Cluster("Compute Services"):
            with Cluster("Auto-Scaling Compute"):
                gke_auto = GKE("Auto-Scaling GKE Cluster")
                compute_auto = ComputeEngine("Auto-Scaling Compute Engine")

        with Cluster("Storage Services"):
            gcs = GCS("Cloud Storage with Backup")
            filestore = Filestore("Filestore for Shared Content")

        with Cluster("Database Services"):
            spanner_auto = Spanner("Auto-Scaling Spanner")

        with Cluster("Security Services"):
            kms = KeyManagementService("Cloud KMS")

        with Cluster("Operations Services"):
            logging = Logging("Cloud Logging")
            monitoring = Monitoring("Cloud Monitoring")

        with Cluster("CI/CD and IaC"):
            source_repos = SourceRepositories("Source Repositories")
            build = Build("Cloud Build")
            container_registry = ContainerRegistry("Container Registry")
            terraform = Terraform("Terraform for IaC")

    # Diagram connections
    user >> internet >> dns >> lb >> cdn >> gcs
    lb >> armor >> iap
    iap >> gke_auto
    iap >> compute_auto
    gke_auto >> spanner_auto
    compute_auto >> spanner_auto
    gke_auto >> filestore
    compute_auto >> filestore
    gke_auto >> logging
    compute_auto >> logging
    gke_auto >> monitoring
    compute_auto >> monitoring
    spanner_auto >> BigQuery
    source_repos >> build >> container_registry >> gke_auto
    terraform >> gke_auto
    terraform >> spanner_auto
    terraform >> filestore
    terraform >> gcs
    terraform >> vpn
    terraform >> partner_interconnect
    vpn >> partner_interconnect
    partner_interconnect >> lb
    gcs >> kms  # Encryption with Cloud KMS
