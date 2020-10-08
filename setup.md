### Tech
- Python (3.6+, recommended)
- Serverless Framework (IaaC framework that organises code as per Cloud/AWS infra)
- Node / NPM (for serverless framework)
- Optional, but recommended: AWS CLI, virtual environment, brew

### Step 1: Install & Configure vendor libraries/packages

**A) Install Python virtual environment**

```
$ [sudo] apt-get install python3
$ [sudo] apt-get install python3-pip
$ python3 -v
# Update ~/.bash_profile or ~/.bashrc or $PATH variable, if required, to set default python version
$ [sudo] pip3 install virtualenv
## OR any virtual environment setup of your choice ##
```

**B) Create project directory of your choice & activate virtual environment
```
$ mkdir serverless-workshop && cd serverless-workshop
serverless-workshop>$  which python3
```
> /usr/local/bin/python3
```
serverless-workshop>$  virtualenv -p /usr/local/bin/python3 serverless-workshop
```
> Running virtualenv with interpreter /usr/local/bin/python3
> Already using interpreter /usr/local/opt/python/bin/python3.7
> Using base prefix '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7'
> New python executable in /Users/sejal/serverless/serverless-workshop/serverless-workshop/bin/python3.7
> Also creating executable in /Users/sejal/serverless/serverless-workshop/serverless-workshop/bin/python
> Installing setuptools, pip, wheel...
> done.
```
serverless-workshop>$  source serverless-workshop/bin/activate
```
> (serverless-workshop) serverless-workshop>$
**C) Install node/npm**

*MAC USERS*

Install `brew`:
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew update
$ brew doctor
```

Install `node`/`npm`:
```
$ brew install node
## OR ##
$ brew install npm
```

Check version (Should be Node.js 6.x or later):
```
$ node -v
## OR ##
$ npm -v
```

**D) Install serverless framework**

```
$ [sudo] npm install -g serverless
$ serverless -v
## OR ##
$ sls -v
```

Update `~/.bash_profile` or `~/.bashrc` and/or `$PATH` env variable, if required


### Step 2: Configure AWS / IAM access on local

**A) Install ** [aws cli](https://github.com/aws/aws-cli#installation) (OPTIONAL)
*MAC USERS*
```
$ pip install awscli --ignore-installed six
$ aws --version
```
Based on the email with the creds you must have received for this workshop, configure your IAM key-pair. 
Contact Administrator/workshop owner for any issues.
**B) Configure awscli **
```
$ aws configure --profile <any-profile-name>
```
> AWS Access Key ID [None]: `<ACCESS-KEY-ID>`
  
> AWS Secret Access Key [None]: `<SECRET-KEY>`
  
> Default region name [None]: `eu-west-1`
> Default output format [None]: `<blank>`
```
$ cat ~/.aws/credentials
>
```
```
[<any profile name>]
AWS_ACCESS_KEY_ID=<ACCESS-KEY-ID>
AWS_SECRET_ACCESS_KEY=<SECRET-KEY>
```
### Step 3: Configure serverless
**A) Configure serverless framework with AWS
```
$ serverless config credentials --provider aws --key <ACCESS-KEY-ID> --secret <SECRET-KEY> --profile <any-profile-name> --o
$ cat ~/.aws/credentials
```
```
[<any-profile-name>]
AWS_ACCESS_KEY_ID=<ACCESS-KEY-ID>
AWS_SECRET_ACCESS_KEY=<SECRET-KEY>
```
**B) Test AWS connection**

To check if your local is connected to *`AWS-Postman-Staging`* account
```
$ aws s3 ls
## OR ##
$ aws s3 ls --profile <any-profile-name>
```
You should see a list of existing buckets present on this *`AWS-account`*. 

### References

For more info:

https://serverless.com/framework/docs/providers/aws/guide/quick-start/
https://serverless.com/framework/docs/providers/aws/guide/installation/
https://serverless.com/framework/docs/providers/aws/guide/credentials/
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
