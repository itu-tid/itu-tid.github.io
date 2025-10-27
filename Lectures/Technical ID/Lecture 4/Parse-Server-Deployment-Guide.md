# Parse Server Deployment Guide - Ubuntu on DigitalOcean

This guide documents the successful deployment of Parse Server 8.2.5 on an Ubuntu DigitalOcean droplet. 

## Prerequisites
- Ubuntu server on DigitalOcean (tested on 1GB droplet)
- Root or sudo access

## Step 1: Update System and Install Node.js

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Node.js (via NodeSource)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Install npm separately
sudo apt install -y npm

# Verify installation
node --version
npm --version
```

## Step 2: Install and Configure MongoDB

```bash
# Add MongoDB GPG key
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/mongodb-server-7.0.gpg

# Add MongoDB repository
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# Update package list and install MongoDB
sudo apt update
sudo apt install -y mongodb-org

# Start and enable MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod
```

## Step 3: Add Swap Space (Important for 512MB droplets)

```bash
# Create 2GB swap file
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make swap permanent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

## Step 4: Install Parse Server

```bash
# Create project directory
mkdir ~/parse-server && cd ~/parse-server

# Initialize npm project
npm init -y

# Install Parse Server and Express
npm install parse-server express
```

## Step 5: Create Parse Server Configuration

Create `index.js` file with the following content (replace `YOUR_DROPLET_IP` with your actual IP):

```bash
cat > ~/parse-server/index.js << 'EOF'
const express = require('express');
const ParseServer = require('parse-server').ParseServer;

const app = express();

const parseServer = new ParseServer({
  databaseURI: 'mongodb://localhost:27017/parse',
  appId: 'myAppId',
  masterKey: 'myMasterKey',
  serverURL: 'http://YOUR_DROPLET_IP:1337/parse'
});

async function startServer() {
  await parseServer.start();
  
  app.use('/parse', parseServer.app);
  
  app.listen(1337, '0.0.0.0', () => {
    console.log('Parse Server running on http://0.0.0.0:1337/parse');
  });
}

startServer();
EOF
```

**Important:** Change `YOUR_DROPLET_IP` to your actual DigitalOcean droplet IP address.

## Step 6: Install and Configure PM2

```bash
# Install PM2 globally
sudo npm install -g pm2

# Start Parse Server with PM2
cd ~/parse-server
pm2 start index.js --name parse-server

# Configure PM2 to start on system boot
pm2 startup
pm2 save

# Check status
pm2 status
pm2 logs parse-server
```

## Step 7: Configure Firewall

```bash
# Allow Parse Server port
sudo ufw allow 1337/tcp

# Allow SSH (if not already allowed)
sudo ufw allow 22/tcp

# Enable firewall
sudo ufw enable

# Check status
sudo ufw status
```

## Step 8: Test Your Parse Server

### From the server itself:
```bash
curl -X POST \
  -H "X-Parse-Application-Id: myAppId" \
  -H "Content-Type: application/json" \
  -d '{}' \
  http://localhost:1337/parse/health
```

### From your local machine:
```bash
curl -X POST \
  -H "X-Parse-Application-Id: myAppId" \
  -H "Content-Type: application/json" \
  -d '{}' \
  http://YOUR_DROPLET_IP:1337/parse/health
```

Expected response: `{"status":"ok"}`

### Test creating an object:
```bash
curl -X POST \
  -H "X-Parse-Application-Id: myAppId" \
  -H "Content-Type: application/json" \
  -d '{"score":1337,"playerName":"Test"}' \
  http://YOUR_DROPLET_IP:1337/parse/classes/GameScore
```

## Step 9: Install Parse Dashboard (Optional)

Parse Dashboard provides a web interface to manage your Parse Server data.

```bash
# Install Parse Dashboard globally
sudo npm install -g parse-dashboard

# Create dashboard configuration directory
mkdir -p ~/parse-dashboard
cd ~/parse-dashboard

# Create dashboard config file
cat > parse-dashboard-config.json << 'EOF'
{
  "apps": [
    {
      "serverURL": "http://YOUR_DROPLET_IP:1337/parse",
      "appId": "myAppId",
      "masterKey": "myMasterKey",
      "appName": "MyParseApp"
    }
  ],
  "users": [
    {
      "user": "admin",
      "pass": "password"
    }
  ],
  "useEncryptedPasswords": false
}
EOF
```

**Important:** Replace `YOUR_DROPLET_IP` with your actual IP, and change the username/password for production.

### Start Dashboard with PM2

```bash
# Start Parse Dashboard
pm2 start parse-dashboard -- --dev --config parse-dashboard-config.json --allowInsecureHTTP

# Save PM2 configuration
pm2 save

# Check status
pm2 status
```

### Configure Firewall for Dashboard

```bash
# Allow Dashboard port (default is 4040)
sudo ufw allow 4040/tcp
```

### Access the Dashboard

Open your browser and navigate to:
```
http://YOUR_DROPLET_IP:4040
```

Login with:
- Username: `admin`
- Password: `password`

**Security Note:** For production, you should:
1. Use encrypted passwords (`useEncryptedPasswords: true`)
2. Set up HTTPS with SSL certificate
3. Use strong passwords
4. Consider restricting dashboard access by IP

## Useful PM2 Commands

```bash
# View logs
pm2 logs parse-server

# Restart Parse Server
pm2 restart parse-server

# Stop Parse Server
pm2 stop parse-server

# Check status
pm2 status

# Monitor resources
pm2 monit
```

## Important Notes

1. **Change default credentials**: Replace `myAppId` and `myMasterKey` with secure random strings in production
2. **DigitalOcean Cloud Firewall**: If you still can't connect, check DigitalOcean's Cloud Firewall settings in your control panel
3. **SSL/HTTPS**: For production, set up Nginx as a reverse proxy with Let's Encrypt SSL certificate
4. **Warnings**: The deprecation warnings shown in logs are normal and can be ignored for now

## Next Steps (Recommended for Production)

1. Set up Nginx as a reverse proxy
2. Install SSL certificate with Let's Encrypt
3. Configure a domain name
4. Change default appId and masterKey to secure values
5. Set up MongoDB authentication
6. Configure regular backups

## Your Parse Server is now running at:
```
http://YOUR_DROPLET_IP:1337/parse
```

## Troubleshooting

### Parse Server won't start
- Check logs: `pm2 logs parse-server`
- Verify MongoDB is running: `sudo systemctl status mongod`
- Check if port 1337 is in use: `sudo ss -tlnp | grep 1337`

### Can't connect from external machine
- Verify firewall: `sudo ufw status`
- Check DigitalOcean Cloud Firewall in control panel
- Verify Parse Server is listening on 0.0.0.0: `sudo ss -tlnp | grep 1337`

### Out of memory errors
- Increase swap space
- Consider upgrading to a droplet with more RAM
