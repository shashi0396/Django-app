# SonarQube and Jenkins Integration

1. Generate a Token
   - Log in to SonarQube at http://<your-ec2-ip>:9000.
   - Use the default credentials: admin/admin.
   - Go to My Account > Security and generate a new user token.

2. Install the Plugin
   - In Jenkins, go to Manage Jenkins > Plugins.
   - Install the 'SonarQube Scanner' plugin.
   - Restart Jenkins if prompted.

3. Add Credentials
   - Go to Manage Jenkins > Credentials.
   - Add a new Secret text credential.
   - Paste your SonarQube token and set the ID to 'sonar-token'.

4. Configure the Server
   - Go to Manage Jenkins > System.
   - Scroll down to SonarQube servers.
   - Check Environment variables.
   - Click Add SonarQube.
   - Name it "SonarQubeServer" (this exact name is used in the pipeline).
   - Set the URL to http://<EC2_PRIVATE_IP>:9000.
   - Select your 'sonar-token'.

5. Configure the Scanner
   - Go to Manage Jenkins > Tools.
   - Scroll to SonarQube Scanner.
   - Click Add SonarQube Scanner.
   - Name it 'sonar-scanner'.
   - Check Install automatically.