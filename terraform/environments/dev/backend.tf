terraform {
  cloud {
    organization = "catalyst-projects"

    workspaces {
      name = "notifications-system-dev"
    }
  }
}

