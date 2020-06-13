node {
    def app

    stage('Clone repository') {
        checkout scm
        
    }
    stage('install kub') {
            steps {
                echo '> installing kub cluster...'
                sh 'ansible-playbook playbook.yaml'
            }
        }
     stage('Deploy') {
            steps {
                sh 'kubectl create -f deployapp.yaml'
            }
        }
}
