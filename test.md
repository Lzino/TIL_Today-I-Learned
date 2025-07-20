```json

{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::accountA:oidc-provider/oidc.eks.ap-northeast-2.amazonaws.com/id/xxxx"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "oidc.eks.region.amazonaws.com/id/xxxx:sub": "system:serviceaccount:default:tmap-sa"
    }
  }
}




{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject", "s3:PutObject", "s3:ListBucket"
  ],
  "Resource": [
    "arn:aws:s3:::tmap_bucket",
    "arn:aws:s3:::tmap_bucket/*"
  ]
}


{
  "Effect": "Allow",
  "Action": [
    "ecr:GetAuthorizationToken",
    "ecr:BatchCheckLayerAvailability",
    "ecr:GetDownloadUrlForLayer",
    "ecr:BatchGetImage"
  ],
  "Resource": "arn:aws:ecr:region:accountB:repository/tmap_repo"
}
