terraform {
  cloud {
    organization = "catalyst-projects"

    workspaces {
      name = "eks-catalyst-dev"
    }
  }
}

