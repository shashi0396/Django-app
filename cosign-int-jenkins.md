file(credentialsId: 'cosign-private-key', variable: 'COSIGN_KEY')
string(credentialsId: 'cosign-passphrase', variable: 'COSIGN_PASSWORD')

you need to create two Jenkins credentials:

cosign-private-key → the Cosign private key file
cosign-passphrase → the password protecting that key
1. Generate the Cosign key pair

On a secure machine:

cosign generate-key-pair

You'll get:

cosign.key
cosign.pub

It will ask:

Enter password for private key:
Enter password for private key again:

Use a strong passphrase.

Your important files are:

cosign.key    # PRIVATE - never expose
cosign.pub    # PUBLIC - safe to distribute
2. Add the private key to Jenkins

Go to:

Jenkins → Manage Jenkins → Credentials

Then select the credential store used by your pipeline, typically:

(global)
    ↓
Add Credentials

Choose:

Kind: Secret file

Then:

File:        cosign.key
ID:          cosign-private-key
Description: Cosign private signing key

Click Create.

So Jenkins stores the actual cosign.key securely rather than you putting it into your Jenkinsfile.

3. Add the passphrase

Again:

Manage Jenkins → Credentials → Add Credentials

Choose:

Kind: Secret text

Set:

Secret:      <your Cosign key passphrase>
ID:          cosign-passphrase
Description: Cosign private key passphrase

Click Create.

You should now have:

Credentials
├── cosign-private-key   Secret file
└── cosign-passphrase    Secret text