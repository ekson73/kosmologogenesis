# Exemplo 1: Engenharia de Prompts para Migração de Infraestrutura

**Contexto:** Migração de um sistema legado para uma arquitetura baseada em microserviços em Kubernetes.

**Aplicação do Framework:**

1. **Fase Kosmos:**
   - Mapeamento holístico de todos os componentes do sistema e suas interdependências
   - Identificação de padrões de comunicação e fluxos de dados entre serviços
   - Visualização do ecossistema completo incluindo sistemas externos

2. **Fase Logos:**
   ```markdown
   # Prompt para Migração de Sistema Legado para Kubernetes
   
   ## Contexto Sistêmico
   - Sistema atual: Monolítico Java EE em servidor físico
   - Destino: Arquitetura de microserviços em Kubernetes EKS
   - Dependências críticas: 3 sistemas externos, 2 bancos de dados
   
   ## Objetivos
   1. Decompor aplicação monolítica em microserviços
   2. Estabelecer pipeline CI/CD
   3. Implementar monitoramento e observabilidade
   4. Garantir zero downtime durante migração
   ```

3. **Fase Genesis:**
   - Geração de documentos detalhados para cada microserviço
   - Criação de manifestos Kubernetes e configurações de rede
   - Desenvolvimento de scripts de migração de dados
   - Implementação de testes de integração automatizados
