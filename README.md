# AppWeb-Azure
 L’objectif du projet est de concevoir une solution cloud à petite échelle en utilisant Microsoft Azure. Il s’agit de connecter au moins trois services Azure pour démontrer leur intégration et créer une solution cohérente. Dans ce projet, j’ai utilisé une base de données Azure, un Container Registry Azure et une application web Azure.

 L'application web utilise une image Docker provenant du Container Registry Azure et communique avec la base de données pour récupérer les données.
 Cette application suit un scénario très simple et est utilisée comme test. Elle affiche un listing de tous les employés provenant de la table Employes de ma base de données créée sur Azure.


 Pour lancer en local : 
 docker build -t appweb-azure-main .
 docker run -d -p 8080:8080 appweb-azure-main
 http://localhost:8080

