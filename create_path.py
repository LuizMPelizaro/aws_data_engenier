import os

# Diretório base
base_dir = "AWS-Data-Engineer-Certificacao"

# Estrutura fornecida
estrutura_bruta = """
ANALYTICS
Amazon EMR
Amazon Kinesis
Amazon OpenSearch Service
AWS Lake Formation
AWS Glue
Amazon QuickSight
Amazon Managed Streaming for Apache Kafka
Amazon Redshift

APP INTEGRATION
Amazon EventBridge
AWS Step Functions
Amazon AppFlow
Amazon Managed Workflows for Apache Airflow
Amazon Simple Notification Service (Amazon SNS)
Amazon Simple Queue Service (Amazon SQS)

CLOUD FINANCIAL MANAGEMENT
AWS Budgets
AWS Cost Explorer

COMPUTE
AWS Batch
Amazon Elastic Compute Cloud (Amazon EC2)
AWS Lambda
AWS Serverless Application Repository

CONTAINERS
Amazon Elastic Container Registry (Amazon ECR)
Amazon Elastic Container Service (Amazon ECS)
Amazon Elastic Kubernetes Service (Amazon EKS)

DATABASE
Amazon DocumentDB (with MongoDB compatibility)
Amazon DynamoDB
Amazon Keyspaces (for Apache Cassandra)
Amazon MemoryDB for Redis
Amazon Neptune
Amazon Relational Database Service (Amazon RDS)

DEVELOPER TOOLS
AWS Command Line Interface (AWS CLI)
AWS Cloud9
AWS Cloud Development Kit (AWS CDK)
AWS CodeBuild
AWS CodeCommit
AWS CodeDeploy
AWS CodePipeline

FRONTEND WEB
Amazon API Gateway

MACHINE LEARNING
Amazon SageMaker

MANAGEMENT AND GOVERNANCE
AWS CloudFormation
AWS CloudTrail
Amazon CloudWatch
AWS Config
Amazon Managed Grafana
AWS Well-Architected Tool
AWS Systems Manager

MIGRATION AND TRANSFER
AWS Application Discovery Service
AWS Application Migration Service
AWS Database Migration Service (AWS DMS)
AWS DataSync
AWS Transfer Family
AWS Snow Family

NETWORKING AND CONTENT DELIVERY
Amazon CloudFront
AWS PrivateLink
Amazon Route 53
Amazon Virtual Private Cloud (Amazon VPC)

SECURITY, IDENTITY, AND COMPLIANCE
AWS Identity and Access Management (IAM)
AWS Key Management Service (AWS KMS)
Amazon Macie
AWS Secrets Manager
AWS Shield
AWS WAF

STORAGE
AWS Backup
Amazon Elastic Block Store (Amazon EBS)
Amazon Elastic File System (Amazon EFS)
Amazon Simple Storage Service (Amazon S3)
"""

# Processar e montar estrutura
estrutura = {}
pasta_atual = ""

for linha in estrutura_bruta.strip().split("\n"):
    linha = linha.strip()
    if not linha:
        continue
    if linha.isupper():
        pasta_atual = linha.title().replace(" ", "-")
        estrutura[pasta_atual] = []
    else:
        estrutura[pasta_atual].append(linha)

# Criar diretórios e arquivos
for pasta, arquivos in estrutura.items():
    dir_path = os.path.join(base_dir, pasta)
    os.makedirs(dir_path, exist_ok=True)

    for arquivo in arquivos:
        nome_arquivo = f"{arquivo}.md".replace("/", "-")
        file_path = os.path.join(dir_path, nome_arquivo)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {arquivo}\n")

print(f"✅ Estrutura criada dentro da pasta: {base_dir}")
