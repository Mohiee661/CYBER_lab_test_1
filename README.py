# config.py — DarkShield Demo Repo 1
# WARNING: This file contains intentionally exposed credentials for demo purposes only.
# These are FAKE keys used to demonstrate the DarkShield secret scanner.

import os

# ── Database ─────────────────────────────────────────────
DB_HOST = "prod-db.internal.acmecorp.com"
DB_PORT = 5432
DB_NAME = "acme_production"
DB_USER = "admin"
DB_PASSWORD = "Sup3rS3cur3Passw0rd!2024"       # EXPOSED: Generic Password

# ── AWS Credentials ──────────────────────────────────────
AWS_ACCESS_KEY_ID     = "AKIAIOSFODNN7EXAMPLE"                          # EXPOSED: AWS Access Key
AWS_SECRET_ACCESS_KEY = "aws_secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'"  # EXPOSED: AWS Secret Key
AWS_REGION = "us-east-1"
S3_BUCKET  = "acme-prod-backups"

# ── OpenAI ───────────────────────────────────────────────
OPENAI_API_KEY = "sk-proj-T3BlbkFJSHAREDKEY1234567890abcdefghijklmnopqrstuvwxyz"   # EXPOSED: OpenAI Key

# ── Stripe ───────────────────────────────────────────────
STRIPE_SECRET_KEY = "sk_live_51AcmeCorpFakeKeyForDemoOnly00000000000"   # EXPOSED: Stripe Secret

# ── GitHub ───────────────────────────────────────────────
GITHUB_TOKEN = "ghp_16C7e42F292c6912E169E2af8CExampleToken00"           # EXPOSED: GitHub Token

# ── Slack ────────────────────────────────────────────────
SLACK_BOT_TOKEN = "xoxb-123456789012-123456789012-FakeSlackTokenDemo00"  # EXPOSED: Slack Token

# ── Google ───────────────────────────────────────────────
GOOGLE_API_KEY = "AIzaSyDemoFakeKeyForDarkShieldScanner1234"             # EXPOSED: Google API Key

# ── App config (safe) ────────────────────────────────────
DEBUG    = False
APP_NAME = "AcmeCorp Backend"
PORT     = int(os.getenv("PORT", 8080))
