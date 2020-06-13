node {
    def app

    stage('Clone repository') {
        checkout scm
        
    }

    stage('Build image') {
        sh "pwd"
        app = docker.build("pozos/app", "-f simple_api/Dockerfile .")
    }
    
    stage('run image') {
    
        sh "docker run -d -p 5000:5000 pozos/app"
    }
    
    stage('Test image') {
        app.inside {
           echo"hi"
        }
    }
    
    stage('Push image') {
        docker.withRegistry('http://192.168.48.133:5000', 'dockerhub_id') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
            } 
    }
    
    stage('Deploy') {
            steps {
                echo '> Deploying the app'
                sh 'ansible-playbook playbook.yaml'
            }
        }
}
