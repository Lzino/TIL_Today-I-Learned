```json

{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::accountA:oidc-provider/oidc.eks.region.amazonaws.com/id/xxxx"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "oidc.eks.region.amazonaws.com/id/xxxx:sub": "system:serviceaccount:namespace:serviceaccountname"
    }
  }
}

