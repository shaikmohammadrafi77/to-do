pipeline{
    agent any
    environment{
        EC2-USER ='ec2-user'
        EC2-HOST ='13.232.181.168'
        APP-NAME ='to-do-app'
        SHH_CRENDENTIALS ='jenkins-id'
        REPO ='https://github.com/shaikmohammadrafi77/to-do.git'
        BRANCH ='main'
    }
    stages{
        stage('checkout'){
            stepts{
                git branch:"${main}",url:"${REPO}"
            }

        }
        stage('Build'){
            steps{
                sh 'echo Build started'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'

            }
        }
        stage('test'){
            steps{
                sh 'echo test started'
                sh 'pytest'

            }
        }
        stage('deploy to ec2'){
            steps{
                sh 'echo deploy started'
                sh 'scp -o StrictHostKeyChecking=no -i /var/lib/jenkins/keys/jenkins-key.pem -r * ${EC2-USER}@${EC2-HOST}:/home/ec2-user/${APP-NAME}'
                sh 'ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/keys/jenkins-key.pem ${EC2-USER}@${EC2-HOST} << EOF cd /home/ec2-user/ && exit EOF'
                sh  'ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/keys/jenkins-key.pem ${EC2-USER}@${EC2-HOST} << EOF cd /home/ec2-user/${APP-NAME} && pkill -f run.py && nohup python3 run.py > app.log 2>&1 & exit EOF'
                sh 'echo Deployed successfully'
                sh 'echo Application URL: http://${EC2-HOST}:5000'
                sh 'echo Application logs: ssh -i /var/lib/jenkins/keys/jenkins-key.pem ${EC2-USER}@${EC2-HOST} "tail -f /home/ec2-user/${APP-NAME}/app.log"'
                sh 'echo To stop the application: ssh -i /var/lib/jenkins/keys/jenkins-key.pem ${EC2-USER}@${EC2-HOST} "pkill -f run.py"'
                sh 'echo To start the application: ssh -i /var/lib/jenkins/keys/jenkins-key.pem ${EC2-USER}@${EC2-HOST} "cd /home/ec2-user/${APP-NAME} && nohup python3 run.py > app.log 2>&1 &"'
                sh 'echo To check the application status: ssh -i /var/lib/jenkins/keys/jenkins-key.pem ${EC2-USER}@${EC2-HOST} "pgrep -f run.py"'
                sh 'echo To check the application port: ssh -i /var/lib/jenkins/keys/jenkins-key.pem ${EC2-USER}@${EC2-HOST} "netstat -tuln | grep 5000"'
                
               

            }
        }
        
    }
}
