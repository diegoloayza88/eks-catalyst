# EKS Catalyst - Terraform Cloud Complete Project

## Instrucciones de Instalación

1. Descarga y extrae este archivo
2. Actualiza el nombre de tu organización en Terraform Cloud
3. Configura GitHub Secrets
4. Deploy!

## Estructura del Proyecto

```
eks-catalyst/
├── README.md
├── .gitignore
├── LICENSE
│
├── terraform/
│   ├── modules/
│   │   ├── vpc/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   └── outputs.tf
│   │   └── eks/
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       └── outputs.tf
│   └── environments/
│       ├── dev/
│       │   ├── main.tf (con TF Cloud backend)
│       │   ├── variables.tf
│       │   └── outputs.tf
│       ├── staging/
│       │   ├── main.tf (con TF Cloud backend)
│       │   ├── variables.tf
│       │   └── outputs.tf
│       └── prod/
│           ├── main.tf (con TF Cloud backend)
│           ├── variables.tf
│           └── outputs.tf
│
├── gitops/
│   ├── argocd/
│   │   ├── bootstrap/
│   │   │   ├── kustomization.yaml
│   │   │   └── install.yaml
│   │   └── applications/
│   │       └── demo-app.yaml
│   └── apps/
│       └── demo-app/
│
├── demo-app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src/
│   │   └── app.py
│   └── k8s/
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── ingress.yaml
│       └── hpa.yaml
│
├── .github/
│   └── workflows/
│       ├── terraform-cloud.yml (NUEVO - triggers TF Cloud)
│       └── app-deploy.yml (app CI/CD)
│
├── docs/
│   ├── terraform-cloud-setup.md
│   ├── architecture.md
│   ├── getting-started.md
│   └── deployment-guide.md
│
└── scripts/
    └── setup.sh
```

## Cambios Clave vs Versión Anterior

### 1. Terraform Cloud Integration
- Backend cambiado de S3 a Terraform Cloud
- State management automático
- Remote execution
- No más conflictos de state

### 2. CI/CD Simplificado
- GitHub Actions solo trigger runs en TF Cloud
- Plans y applies se ejecutan en TF Cloud
- Mejor UI para revisar cambios
- Cost estimation integrada

### 3. Workflow Optimizado
- PR → Plan automático en TF Cloud
- Merge develop → Auto-apply en dev
- Merge main → Manual approval en staging/prod

## Próximos Pasos

1. Descarga los archivos
2. Actualiza `organization = "your-organization-name"` en:
   - terraform/environments/dev/main.tf
   - terraform/environments/staging/main.tf
   - terraform/environments/prod/main.tf

3. Configura Terraform Cloud workspaces:
   - eks-catalyst-dev
   - eks-catalyst-staging
   - eks-catalyst-prod

4. Añade GitHub Secrets:
   - TF_API_TOKEN
   - AWS_ROLE_ARN (para OIDC)

5. Deploy!

Ver `docs/terraform-cloud-setup.md` para guía completa.
