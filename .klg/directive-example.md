# DIRETIVA DO PROJETO: INFRAESTRUTURA COMO CÓDIGO

## Contexto
Gerenciar toda a infraestrutura atual via IaC (Infrastructure as Code).
Tenho uma infraestrutura em nuvem toda hospedada na AWS composta por:
- AWS VPC (us-east-1)
- AWS Subnets
- AWS NAT Gateways
- AWS Security Groups
- AWS Load Balancer
- AWS EC2
- AWS RDS
- AWS S3 Buckets e Acessos Múltiplos
- AWS IAM papéis e políticas
- AWS IAM Identity Center
- AWS CloudWatch
- AWS Route 53
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
- AWS ACM
- Webhooks:
  - https://discord.com/api/webhooks/923924175503106049/vAer_ciQgzDjfn25Qc-844JhGRE9xrAMg0azXYHdvmBsmDAL1xyLR1vmktFJsH-PB_xa: Alertas de Infraestrutura padrão Discord
  - https://discord.com/api/webhooks/879333705456439307/wRMykX9zyoG_xQzoCL9cpq-t9iVgqFLUJpNc2zcjrZ3VUFBiLwZGoYaBzdiOuKLo5KSb: Informações de CI/CD padrão Discord

## Objetivos
- Implementar princípios de infraestrutura como código para todos os componentes
- Integrar ferramentas de observabilidade e monitoramento abrangentes
- Automatizar a configuração e implantação de recursos AWS via Crossplane
- Implementar dashboards eficazes para visualização e gerenciamento
- Garantir segurança e conformidade em todos os níveis da stack
- Preparar ambiente para migração contínua de aplicações legadas
- Planejar instalação, configuração e utilização de:
  - Terraform (realizar análise de custo-benefício e acoplagem ao ambiente, se necessário)
  - Crossplane
  - Rancher
  - SOPS
  - Teller
  - Kubernetes Argo CD with Secrets Integration
  - Kubernetes Cert-Manager with Let's Encrypt
  - Kubernetes Dashboard
  - Kubernetes External Secrets
  - Kubernetes Flux CD with Secrets Integration
  - Kubernetes Grafana
  - Kubernetes Ingress-Nginx
  - Kubernetes Karpenter
  - Kubernetes Kubeapps
  - Kubernetes Oauth2 Proxy
  - Kubernetes OpenUnison
  - Kubernetes Pinniped
  - Kubernetes Prometheus
  - Kubernetes Sealed Secrets
  - Kubernetes Skooner
  - Kubernetes Weave GitOps (Wego Dashboard)

## Requisitos
- Quando necessário, configuração automatizada via script (preferencialmente python com sdk)
- Gerenciamento de credenciais e segredos através do AWS Secrets Manager/AWS Parameter Store/AWS KMS/External Secrets/Sealed Secrets/SOPS/Teller/
- Implementação de Karpenter para auto-scaling eficiente de nodes
- Integração com AWS ACK para gerenciar recursos AWS diretamente do Kubernetes. Dê preferencia para Crossplane/Rancher.
- Dashboards de monitoramento com Skooner e Weave GitOps
- Gestão de identidade e acesso com OpenUnison. Dê preferencia para Pinniped/Oauth2 Proxy. Analise e utilize o melhor das 3 ferramentas (OpenUnison, Pinniped, Oauth2 Proxy)
- Certificados gerenciados automaticamente via Cert-Manager
- Ingress gerenciado com ingress-nginx
- Ingress-nginx exposto via ingress-alb-controller
- Documentar processo de inventário e análise.
- Garantir acurácia das informações coletadas.
- Manter consistência em documentações.
- Organização hierárquica de tarefas
- Sistema de priorização
- Relatórios de produtividade
- Métricas de desempenho
- Documentação de processos
- Documentação de arquitetura
- Documentação de configuração
- Documentação de segurança
- Documentação de monitoramento
- Documentação de testes
- Documentação de integração

## Arquivos de Instalação e Configuração Atual
- `.eks/eks-cluster--config-file--k8s-eks-prd-002.yaml`: Arquivo de configuração do cluster EKS.
- `.eks/flux-bootstrap-gitlab--k8s-eks-prd-002.sh`: Script de bootstrap do Flux CD.
- `eks--create-cluster--install.sh`: Script de instalação detalhado do cluster EKS.
- `flux-v2/vek-app/kustomize.sh`: Script de configuração do Kustomize dos Aplicativos Desenvolvidos Internamente.
- `install-helm.sh`: Script de instalação de Apps Helm.
- `install-karpenter.sh`: Script de instalação do Karpenter.
- `install-openunison.sh`: Script de instalação do OpenUnison.
- `install-prereqs.sh`: Script de instalação de pré-requisitos para o Sistema Operacional.
- `install-wego-dashboard.sh`: Script de instalação do Weave GitOps Dashboard.

## Tarefas Delegadas para o Agente de IA
1. Inventariar diretório/repositório gitops do projeto.
2. Analisar os arquivos de Instalação e Configuração Atuais.
3. Inventariar todo o ambiente.
4. Gerar documentação completa do ambiente (relatórios, diagramas, fluxogramas, etc.).
5. Cruzar as informações deste documento com o inventário coletado.
6. Criar arquitetura, plano estratégico, plano de ação com detalhamento passo a passo, etapas e tarefas.
7. Gerar arquivos de configuração do Crossplane, Rancher, Argo CD, Terraform, etc.
8. Importar infraestrutura existente para Crossplane, Rancher e/ou Terraform.
9. Manter o Flux CD e Argo CD em operação.

## Conhecimentos Requeridos
- Experiência em desenvolvimento de software
- Kubernetes e Cloud Native
- IaC (Infrastructure as Code)
- Argo CD
- Arquitetura de Soluções
- Gestão de Projetos
- AWS e seus serviços
- Ferramentas de IaC como Terraform, Helm, etc.
- Soluções de Monitoramento como Checkmk
- Ferramentas de Gestão de Segredos como external-secrets, sealed-secrets, sops, teller
- Ferramentas de Gestão de Clusters Kubernetes como Crossplane, Rancher
- Ferramentas de Gestão de Aplicações no Kubernetes como Argo CD, Flux CD

## Restrições
- Necessidade de conformidade com políticas internas de segurança
- Equipe reduzida para manutenção (apenas 1 SREs)

## Stakeholders
- Equipe de Desenvolvimento: precisa de acesso e recursos adequados
- Equipe de Operações: responsável pela manutenção e monitoramento
- Equipe de Segurança: verifica conformidade e vulnerabilidades
- Gerência de TI: supervisiona custos e alinhamento estratégico
- Clientes Internos: dependem da disponibilidade e desempenho

## Prioridades
- Alta: Implementação do Terraform, Crossplane e Rancher
- Média: Gestão avançada de identidade
- Baixa: Dashboards de monitoramento e observabilidade

## Riscos Identificados
- Interrupção de serviços durante a migração: mitigar com janelas de manutenção e rollback plan
- Custos excedentes devido a erros de configuração: implementar políticas de custo e limites
- Complexidade de gestão para equipe reduzida: documentar extensivamente e automatizar operações
- Vulnerabilidades de segurança: implementar scans contínuos e seguir best practices da AWS
- Latência para usuários finais: implementar CDN e otimizações de rede

## Entregáveis
- Arquitetura de alta disponibilidade e escalabilidade.
- Monitoramento e alertas eficientes.
- Integração contínua e entrega contínua.
- Segurança avançada e conformidade.
- Gestão de custos eficiente.
- Automatização de tarefas repetitivas.
- Documentação detalhada.
- Relatórios detalhados do inventário.
- Diagramas, fluxogramas, topologias do ambiente.
- Planos estratégicos.
- Plano de ação detalhado.
- Plano de contingência.
- Documentação completa.
- Arquivos de configuração para todas as ferramentas legadas já instaladas e/ou modificadas.
- Arquivos de configuração para todas as ferramentas novas instaladas.

## Resultados Esperados
- Infraestrutura totalmente gerenciada via IaC
- Integração contínua e entrega contínua
- Monitoramento e alertas eficientes
- Segurança avançada e conformidade
- Gestão de custos eficiente
- Documentação detalhada e atualizada

---
*Última atualização: 09/04/2025*
