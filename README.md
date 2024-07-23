Please add you db configuration into the yaml file.
Then add a file named $(YourDbName).yaml, containing the queries to perform on that db.
As an example in config.yaml you may have a db called gaia_test, then add a file called gaia_test.yaml inside the queries folder.

```yaml
databases:
    gaia_test: # gaia_test is the db name
        ENGINE: "mssql"
        NAME: "GAIA"
        USER: $(Your user)
        SECRET_KEY: $(Your password)
        HOST: $(Your host)
        PORT: $(Your port)
        OPTIONS:
            connect_timeout: 10
            TrustServerCertificate: "yes"
            driver: "ODBC Driver 11 for SQL Server"
            # Add as many other optional parameters

    # Add as many other db here
```