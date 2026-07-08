import os

os.environ.setdefault(
    "DATABASE_URL", 
    "postgres://neondb_owner:npg_E1ru5tjMoUzc@ep-blue-poetry-ase5mus4-pooler.c-4.eu-central-1.aws.neon.tech/drive_lent_fruit_350945?sslmode=require"
)

# Add your secret key here for local use
os.environ.setdefault("SECRET_KEY", "django-insecure-6q)l($0s&72dy-shu95r&p#*j4ye7lz1xhy$^409iut*(lihs%")

# Keeps your local database active to bypass local network firewalls
os.environ["USE_LOCAL_DB"] = "True"