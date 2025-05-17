#!/bin/bash

# Prompt for chown user:group with default
read -p "Enter the chown user:group [default: docker:users]: " OWNER
OWNER=${OWNER:-docker:users}

echo "🔧 Using owner: $OWNER"

# Define URLs
BASE_URL="https://raw.githubusercontent.com/magicdude4eva/docker-gunbot/refs/heads/main"
FILES=(docker-compose.yml Dockerfile .dockerignore)

echo "⬇️ Downloading base files..."
for file in "${FILES[@]}"; do
    echo "  - $file"
    curl -fsSL "$BASE_URL/$file" -o "$file" || {
        echo "❌ Failed to download $file"
        exit 1
    }
done

# Create config folder and download files
echo "📁 Creating config directory..."
mkdir -p config/backups config/json config/logs config/ssl

echo "⬇️ Downloading config.js..."
curl -fsSL "$BASE_URL/config/config.js" -o config/config.js || {
    echo "❌ Failed to download config.js"
    exit 1
}

echo "📝 Creating empty autoconfig.json and err.log..."
touch config/autoconfig.json
touch config/err.log

# Apply ownership
echo "🔐 Applying ownership to $OWNER..."
chown -R "$OWNER" .

# Apply permissions
echo "🔒 Setting file and directory permissions..."
# Top-level files
chmod 664 docker-compose.yml Dockerfile .dockerignore
# config directory
chmod 775 config
chmod 664 config/config.js config/autoconfig.json config/err.log
chmod 700 config/backups config/logs
chmod 775 config/json config/ssl

echo "✅ Setup complete. You can now run:"
echo "   docker-compose up -d"
