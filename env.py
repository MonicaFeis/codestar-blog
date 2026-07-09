import os

# Pass the key and value normally without using a keyword argument

os.environ.setdefault(
    "DATABASE_URL", 
    "postgresql://neondb_owner:npg_E1ru5tjMoUzc@ep-blue-poetry-ase5mus4.c-4.eu-central-1.aws.neon.tech:6543/drive_lent_fruit_350945?sslmode=require"
)

# Add your secret key here for local use
os.environ.setdefault("SECRET_KEY", "django-insecure-6q)l($0s&72dy-shu95r&p#*j4ye7lz1xhy$^409iut*(lihs%")

