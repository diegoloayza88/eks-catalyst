# EKS Catalyst - Enterprise Kubernetes Platform

**Powered by Terraform Cloud** 🚀

Production-ready Amazon EKS platform with Infrastructure as Code, GitOps, and automated workflows.

## ⚡ Quick Start

1. **Setup Terraform Cloud** (5 min)
   - Create account at https://app.terraform.io
   - Create 3 workspaces: `eks-catalyst-{dev,staging,prod}`
   - See [docs/terraform-cloud-setup.md](docs/terraform-cloud-setup.md)

2. **Clone & Configure** (2 min)
   ```bash
   git clone https://github.com/your-org/eks-catalyst.git
   cd eks-catalyst
   # Update organization name in terraform/environments/*/main.tf
   ```

3. **Deploy** (15 min)
   ```bash
   terraform login
   cd terraform/environments/dev
   terraform init
   terraform apply
   ```

4. **Install ArgoCD** (5 min)
   ```bash
   aws eks update-kubeconfig --name eks-catalyst-dev --region us-east-1
   kubectl apply -k gitops/argocd/bootstrap
   ```

## 🎯 Key Features

- ✅ **Terraform Cloud Integration** - Remote state, cost estimates, team collaboration
- ✅ **GitOps with ArgoCD** - Automated application deployments
- ✅ **Multi-Environment** - Dev, Staging, Production ready
- ✅ **Security First** - IRSA, encryption, pod security standards
- ✅ **Auto-Scaling** - Cluster and application level
- ✅ **CI/CD** - GitHub Actions + Terraform Cloud

## 📁 Project Structure

```
eks-catalyst/
├── terraform/
│   ├── modules/          # Reusable modules (VPC, EKS)
│   └── environments/     # Dev, Staging, Prod
├── gitops/
│   └── argocd/          # ArgoCD configs & apps
├── demo-app/            # Sample application
├── .github/workflows/   # CI/CD pipelines
└── docs/                # Documentation
```

## 🔄 Workflow

1. **Pull Request** → Plan runs in Terraform Cloud
2. **Merge to develop** → Auto-deploy to dev
3. **Merge to main** → Manual approval for staging/prod

## 📚 Documentation

- [Terraform Cloud Setup](docs/terraform-cloud-setup.md) ⭐ START HERE
- [Architecture](docs/architecture.md)
- [Deployment Guide](docs/deployment-guide.md)

## 💰 Cost Estimate

- Dev: ~$200/month
- Staging: ~$500/month
- Production: ~$1200/month

## 🆘 Support

- GitHub Issues
- Terraform Cloud Support: https://support.hashicorp.com

---

**Built for Enterprise Kubernetes | Powered by Terraform Cloud**

