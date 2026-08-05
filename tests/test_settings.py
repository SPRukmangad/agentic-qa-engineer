from agentic_qa_engineer.config.settings import Settings

settings = Settings()


print(f"App Name     : {settings.app_name}")
print(f"Environment  : {settings.environment}")
print(f"Debug Mode   : {settings.debug}")