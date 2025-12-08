PS C:\Users\lakshmig2\Desktop\project-root\infra> terraform plan
data.archive_file.function_zip: Reading...
data.archive_file.function_zip: Still reading... [00m10s elapsed]
data.archive_file.function_zip: Still reading... [00m20s elapsed]

Planning failed. Terraform encountered an error while generating this plan.

╷
│ Error: Archive creation error
│
│   with data.archive_file.function_zip,
│   on main.tf line 102, in data "archive_file" "function_zip":
│  102: data "archive_file" "function_zip" {
│
│ error creating archive: error archiving directory: could not archive missing directory: ./../gpt-function
╵
╷
│ Error: Terraform does not have the necessary permissions to register Resource Providers.
│
│ Terraform automatically attempts to register the Azure Resource Providers it supports, to
│ ensure it is able to provision resources.
│
│ If you don't have permission to register Resource Providers you may wish to disable this
│ functionality by adding the following to the Provider block:
│
│ provider "azurerm" {
│   "resource_provider_registrations = "none"
│ }
│
│ Please note that if you opt out of Resource Provider Registration and Terraform tries
│ to provision a resource from a Resource Provider which is unregistered, then the errors
│ may appear misleading - for example:
│
│ > API version 2019-XX-XX was not found for Microsoft.Foo
│
│ Could suggest that the Resource Provider "Microsoft.Foo" requires registration, but
│ this could also indicate that this Azure Region doesn't support this API version.
│
│ More information on the "resource_provider_registrations" property can be found here:
│ https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs#resource_provider_registrations
│
│ Encountered the following errors:
│
│ authorization failed: registering resource provider "Microsoft.EventHub": unexpected status 403 (403 Forbidden) with error: AuthorizationFailed: The client 'lakshmig2@godevsuite200.onmicrosoft.com' with object id '5204b986-997a-45b2-8a1a-5322d77fa86b' does not have authorization to perform action 'Microsoft.EventHub/register/action' over scope '/subscriptions/08b45153-8a8b-4480-88e4-0c0406cdee1b' or the scope is invalid. If access was recently granted, please refresh your credentials.
│
│   with provider["registry.terraform.io/hashicorp/azurerm"],
│   on provider.tf line 10, in provider "azurerm":
│   10: provider "azurerm" {
│
╵
PS C:\Users\lakshmig2\Desktop\project-root\infra> 
