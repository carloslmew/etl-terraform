# Useful commands for terraform

* Initialize Terraform and download required providers
```
terraform init
```

* Check what is going to be created
```
terraform plan
```

* Create resources
```
terraform apply
```

* Create specific resource
```
terraform apply -target RESOURCE.NAME
```

* Check general state
```
terraform show
```

* Check specific resource state
```
terraform state show RESOURCE.NAME
```

* Destroy all resources
```
terraform destroy
```

* Destroy specific resource
```
terraform destroy -target RESOURCE.NAME
```

* List resources within a Terraform state
```
terraform state list 
```

* Review the changes that Terraform has detected from all managed remote objects and updates the Terraform state to match.
```
terraform apply -refresh-only -auto-approve
```

# Resource Lifecycle

* Prevent something to be destroyed
Just add this argument in your resource
```
lifecycle {
    prevent_destroy = true
}
```

* Ese the `create_before_destroy` attribute to create your new resource before destroying the old resource.
```
  lifecycle {
-   prevent_destroy = true
+   create_before_destroy = true
  }
```

* For changes outside the Terraform workflow that should not impact Terraform operations, use the `ignore_changes` argument. (This will update the state)
```
lifecycle {
    create_before_destroy = true
+   ignore_changes        = [tags]
  }
```
