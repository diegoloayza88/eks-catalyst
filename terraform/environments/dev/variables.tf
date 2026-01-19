variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "project_name" {
  description = "Project name"
  type        = string
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
}

variable "private_subnets" {
  description = "Private subnet CIDR blocks"
  type        = list(string)
}

variable "public_subnets" {
  description = "Public subnet CIDR blocks"
  type        = list(string)
}

variable "cluster_version" {
  description = "Kubernetes version"
  type        = string
}

variable "cluster_endpoint_public_access_cidrs" {
  description = "CIDR blocks that can access the public endpoint"
  type        = list(string)
}

variable "vpc_cni_version" {
  description = "VPC CNI add-on version"
  type        = string
}

variable "coredns_version" {
  description = "CoreDNS add-on version"
  type        = string
}

variable "kube_proxy_version" {
  description = "kube-proxy add-on version"
  type        = string
}

variable "ebs_csi_driver_version" {
  description = "EBS CSI driver add-on version"
  type        = string
}
