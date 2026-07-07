import os

os.environ.setdefault(
    "DATABASE_URL", 
    "postgres://neondb_owner:npg_E1ru5tjMoUzc@ep-blue-poetry-ase5mus4-pooler.c-4.eu-central-1.aws.neon.tech/drive_lent_fruit_350945?sslmode=require"
)

os.environ["USE_LOCAL_DB"] = "True"