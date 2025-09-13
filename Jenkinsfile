pipeline{
    agent any
    environment{
        EC2_USER='ec2-user'
        EC2_HOST='65.0.85.146'
        APP_NAME='to-do-app'
        SSH_CREDENTIALS= 'jenkins-id'
        
    }
    stages{
        stage('checkout'){
            steps{
                git branch:'main' , url: 'https://github.com/shaikmohammadrafi77/to-do.git'
            }

        }
        stage('Build'){
            steps{
                sh '''
                echo Build started
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''

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
                sshagent([env.SSH_CREDENTIALS]) {
                     sh '''
                    echo Deploy started
                    scp -o StrictHostKeyChecking=no -r * ${EC2_USER}@${EC2_HOST}:/home/ec2-user/${APP_NAME}
                    ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} "cd /home/ec2-user/${APP_NAME} && pkill -f run.py || true && nohup python3 run.py > app.log 2>&1 &"
                    echo Deployed successfully
                    echo "Application URL: http://${EC2_HOST}:5000"
                    '''
                }
            }
        }
    }
               
               

            
