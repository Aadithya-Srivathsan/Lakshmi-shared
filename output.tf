utput "function_app_name" {
  description = "Name of the Function App"
  value       = azurerm_linux_function_app.func.name
}

output "function_url_base" {
  description = "Base URL of the Function App"
  value       = "https://${azurerm_linux_function_app.func.default_hostname}"
}

output "key_vault_name" {
  description = "Key Vault name"
  value       = azurerm_key_vault.kv.name
}

output "subscription_id" {
  value = data.azurerm_client_config.current.subscription_id
}
output "tenant_id" {
  value = data.azurerm_client_config.current.tenant_id
}
output "client_id" {
  value = data.azurerm_client_config.current.client_id
}
 
