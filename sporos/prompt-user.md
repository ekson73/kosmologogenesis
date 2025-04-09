Tenho uma infraestrutura em nuvem toda hospedada na AWS composto por:
- AWS VPC - us-east-1
- AWS Subnets
- AWS NAT Gateways
- AWS Security Groups
- AWS Load Balancer
- AWS EC2
- AWS RDS
- AWS S3 Buckets e Acessos Multiplos
- AWS IAM papéis e políticas
- AWS IAM Identity Center
- AWS CloudWatch
- AWS Route53
- AWS EKS Cluster
- AWS ECS Cluster
- AWS ECR Registry
- AWS Organizações de Contas Múltiplas
- Backup em Multi-Regiões via Veeam Backup for AWS
- Checkmk para monitoramento
- Flux CD v2
- Helm
- External DNS
- Cert-Manager
- Arquivo de configuração eksctl do cluster
- AWS Config
- Logs AWS CloudWatch
- AWS CloudFormation
- AWS Cloudfront
- AWS Secrets Manager
- AWS Parameter Store
- AWS Systems Manager
- AWS KMS
- AWS Certificate Manager

**Objetivo:**
 Gerenciar toda a infraestrutura atual via IaC (Infrastructure as Code)
- Planejar instalação, configuração e utilização de:
  - Terraform (realizar análise de custo-benefício e acoplagem ao ambiente, se necessário)
  - Crossplane
  - Rancher
  - Flux CD
  - Argo CD
  - external-secrets
  - sealed-secrets
  - sops
  - teller

**Tarefas do Agente de IA:**
1. Inventariar diretório/repositório gitops do projeto.
2. Analisar arquivo `./eks--create-cluster--install.sh` (script de instalação detalhado do cluster EKS).
3. Inventariar todo o ambiente.
4. Gerar documentação completa do ambiente (relatórios, diagramas, fluxogramas, etc.).
5. Criar arquitetura, plano estratégico e ação com detalhamento de passos e etapas.
6. Gerar arquivos de configuração do Crossplane, Rancher, Argo CD, Terraform, etc.
7. Importar infraestrutura existente para Crossplane, Rancher e/ou Terraform.
8. Manter o Flux CD e Argo CD em operação.

**Conhecimentos necessários:**
- Conhecimento em Argo CD
- Arquitetura de Soluções
- AWS e seus serviços
- Ferramentas de IaC como Terraform, Helm, etc.
- Soluções de Monitoramento como Checkmk
- Ferramentas de Gestão de Segredos como external-secrets, sealed-secrets, sops, teller
- Ferramentas de Gestão de Clusters Kubernetes como Crossplane, Rancher
- Ferramentas de Gestão de Aplicações no Kubernetes como Argo CD, Flux CD

**Requisitos:**
- Documentar processo de inventário e análise.
- Garantir acurácia das informações coletadas.
- Manter consistência em documentações.

**Artefatos de Saída:**
- Relatórios detalhados do inventário.
- Diagramas e fluxogramas do ambiente.
- Planos estratégicos e de ação.
- Arquivos de configuração para todas as ferramentas necessárias.
